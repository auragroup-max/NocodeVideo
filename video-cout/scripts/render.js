// Filme index.html image par image dans Chrome (headless), puis encode en MP4 avec FFmpeg.
// Aucun framework vidéo : la page expose window.__seek(t) et window.__duration, c'est tout.
//
//   node tools/render.js --voice tiktok  → renders/foi-business-tiktok.mp4 (30 i/s, voix normalisée à -14 LUFS)
//   node tools/render.js --voice shorts  → renders/foi-business-shorts.mp4
//   node tools/render.js --stills 4,20.5 → renders/stills/*.png + planche contact
//   options : --workers 4  --fps 30  --from 0 --to 197
const puppeteer = require("puppeteer-core");
const { spawn, spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const CHROME = process.env.CHROME || (process.platform === "win32" ? "C:/Program Files/Google/Chrome/Application/chrome.exe" : "/opt/pw-browsers/chromium");
const arg = (n, d) => { const i = process.argv.indexOf("--" + n); return i >= 0 ? process.argv[i + 1] : d; };
const FPS = Number(arg("fps", 30));
const WORKERS = Number(arg("workers", 4));
const W = Number(arg("w", 1920)), H = Number(arg("h", 1080)); // vidéo longue YouTube : 16:9 par défaut
const VOICE = arg("voice", "tiktok");
const url = "file:///" + path.join(ROOT, arg("page", "index.html")).replace(/\\/g, "/") + "?render=1&v=" + VOICE;
const out = path.join(ROOT, "renders");
fs.mkdirSync(out, { recursive: true });

async function openPage(browser) {
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
  page.on("pageerror", (e) => console.error("[page]", e.message));
  await page.goto(url, { waitUntil: "load", timeout: 180000 }); // 4 navigateurs qui démarrent ensemble peuvent dépasser 30 s
  await page.evaluate(() => window.__ready);
  return page;
}
async function frameAt(page, t, type = "jpeg") {
  await page.evaluate((tt) => window.__seek(tt), t);
  return page.screenshot(type === "png" ? { type: "png" } : { type: "jpeg", quality: 94, optimizeForSpeed: true });
}

const launch = () => puppeteer.launch({
    executablePath: CHROME, headless: true, protocolTimeout: 600000,
    args: [...(process.getuid && process.getuid() === 0 ? ["--no-sandbox"] : []), "--allow-file-access-from-files", "--hide-scrollbars", "--force-device-scale-factor=1", "--disable-gpu-vsync", "--autoplay-policy=no-user-gesture-required", "--disable-background-timer-throttling", "--disable-renderer-backgrounding", "--disable-backgrounding-occluded-windows"],
  });

(async () => {
  const browser = await launch();
  const stills = arg("stills");
  if (stills) {
    const dir = path.join(out, "stills"); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
    const page = await openPage(browser);
    const times = stills.split(",").map(Number);
    for (const [i, t] of times.entries()) fs.writeFileSync(path.join(dir, `s${String(i).padStart(3, "0")}.png`), await frameAt(page, t, "png"));
    await browser.close();
    const cols = Math.min(times.length, 6);
    spawnSync("ffmpeg", ["-v", "error", "-y", "-i", path.join(dir, "s%03d.png"), "-vf", `scale=360:-1,tile=${cols}x${Math.ceil(times.length / cols)}:padding=8:color=white`, "-frames:v", "1", path.join(dir, "planche.jpg")], { stdio: "inherit" });
    console.log("stills ->", dir);
    return;
  }

  const [dur, cues] = await (async () => { const p = await openPage(browser); const r = await p.evaluate(() => [window.__duration, window.__sfx || []]); await p.close(); return r; })();
  const from = Number(arg("from", 0)), to = Math.min(Number(arg("to", dur)), dur);
  const f0 = Math.round(from * FPS), f1 = Math.round(to * FPS);
  const per = Math.ceil((f1 - f0) / WORKERS);
  const segs = [];
  const t0 = Date.now();
  let done = 0;
  await Promise.all(Array.from({ length: WORKERS }, async (_, k) => {
    const a = f0 + k * per, b = Math.min(f1, a + per);
    if (a >= b) return;
    const seg = path.join(out, `seg${k}.mp4`); segs[k] = seg;
    const ff = spawn("ffmpeg", ["-v", "error", "-y", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", "-r", String(FPS), seg], { stdio: ["pipe", "inherit", "inherit"] });
    const wb = await launch();
    const page = await openPage(wb);
    for (let f = a; f < b; f++) {
      const buf = await frameAt(page, f / FPS);
      if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
      if (++done % 150 === 0) console.log(`${done}/${f1 - f0} images (${Math.round((Date.now() - t0) / 1000)} s)`);
    }
    ff.stdin.end();
    await new Promise((r) => ff.on("close", r));
    await wb.close();
  }));
  await browser.close();

  const list = path.join(out, "segs.txt");
  fs.writeFileSync(list, segs.filter(Boolean).map((s) => `file '${s.replace(/\\/g, "/")}'`).join("\n"));
  const silent = path.join(out, "video-sans-son.mp4");
  spawnSync("ffmpeg", ["-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", list, "-c", "copy", silent], { stdio: "inherit" });
  const final = path.join(out, arg("out", `video-${VOICE}.mp4`));
  if (process.argv.includes("--mute")) { // aperçu sans son
    fs.renameSync(silent, final); fs.rmSync(list, { force: true }); for (const s of segs.filter(Boolean)) fs.rmSync(s, { force: true });
    console.log(`OK -> ${final} (${Math.round((Date.now() - t0) / 1000)} s)`); return;
  }
  // Bande-son : voix + effets synthétisés (tools/sfx.py) sur les repères de la page.
  const cueFile = path.join(out, `sfx-${VOICE}.json`), mixFile = path.join(out, `mix-${VOICE}.wav`);
  fs.writeFileSync(cueFile, JSON.stringify(cues));
  spawnSync(process.env.PYTHON || (process.platform === "win32" ? "python" : "python3"), [path.join(__dirname, "mix.py"), cueFile, path.join(ROOT, "assets/audio/voix.wav"), String(dur), mixFile], { stdio: "inherit", cwd: ROOT });
  spawnSync("ffmpeg", ["-v", "error", "-y", "-i", silent, "-ss", String(from), "-to", String(to), "-i", mixFile, "-map", "0:v", "-map", "1:a", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.84:level=false,apad", "-ar", "48000", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", final], { stdio: "inherit" });
  for (const s of segs.filter(Boolean)) fs.rmSync(s, { force: true });
  fs.rmSync(list, { force: true }); fs.rmSync(silent, { force: true }); fs.rmSync(cueFile, { force: true }); fs.rmSync(mixFile, { force: true });
  console.log(`OK -> ${final} (${Math.round((Date.now() - t0) / 1000)} s)`);
})();
