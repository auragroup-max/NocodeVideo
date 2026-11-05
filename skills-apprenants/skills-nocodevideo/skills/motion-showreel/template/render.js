// Rendu du showreel : Playwright filme window.seek(t) image par image.
// node render.js --stills            → une image par temps + planche (renders/stills/planche.jpg)
// node render.js                     → 60 i/s, 3 sous-images par image fondues (flou de mouvement) + bande-son → renders/showreel.mp4
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path"), { execFileSync } = require("child_process");

const ROOT = __dirname, OUT = path.join(ROOT, "renders"), DUR = 15, FPS = 60, SUB = 3, WORKERS = 4;
const STILLS = process.argv.includes("--stills");

async function openPage(browser) {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  page.on("pageerror", (e) => console.log("[erreur page]", e.message));
  await page.goto("file://" + path.join(ROOT, "index.html"));
  await page.evaluate(() => window.ready);
  return page;
}
const shot = async (page, t, file) => { await page.evaluate((tt) => window.seek(tt), t); await page.locator("#stage").screenshot({ path: file, type: "jpeg", quality: 92 }); };

(async () => {
  const browser = await chromium.launch();
  if (STILLS) {
    const dir = path.join(OUT, "stills"); fs.mkdirSync(dir, { recursive: true });
    const page = await openPage(browser);
    const times = process.argv.includes("--at") ? process.argv[process.argv.indexOf("--at") + 1].split(",").map(Number) : Array.from({ length: 30 }, (_, k) => +(k * 0.5 + 0.38).toFixed(2));
    for (const [i, t] of times.entries()) await shot(page, t, path.join(dir, `s${String(i).padStart(2, "0")}.jpg`));
    await browser.close();
    const cols = 6;
    execFileSync("ffmpeg", ["-v", "error", "-y", "-i", path.join(dir, "s%02d.jpg"), "-vf", `scale=480:-2,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='%{n}':x=8:y=8:fontsize=22:fontcolor=yellow:box=1:boxcolor=black,tile=${cols}x${Math.ceil(times.length / cols)}`, "-frames:v", "1", path.join(dir, "planche.jpg")]);
    console.log("planche →", path.join(dir, "planche.jpg"));
    return;
  }
  const dir = path.join(OUT, "frames"); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
  const N = DUR * FPS * SUB, t0 = Date.now();
  const pages = await Promise.all(Array.from({ length: WORKERS }, () => openPage(browser)));
  // bande-son rendue par le navigateur (OfflineAudioContext)
  const wav = await pages[0].evaluate(() => window.renderAudio());
  fs.writeFileSync(path.join(OUT, "bande-son.wav"), Buffer.from(wav, "base64"));
  let done = 0;
  await Promise.all(pages.map(async (page, w) => {
    for (let n = w; n < N; n += WORKERS) { await shot(page, n / (FPS * SUB), path.join(dir, `f${String(n).padStart(5, "0")}.jpg`));
      if (++done % 300 === 0) console.log(`${done}/${N} (${((Date.now() - t0) / 1000).toFixed(0)} s)`); }
  }));
  await browser.close();
  // fondu des 3 sous-images de chaque image → flou de mouvement, puis 60 i/s + son
  execFileSync("ffmpeg", ["-v", "error", "-y", "-framerate", String(FPS * SUB), "-i", path.join(dir, "f%05d.jpg"), "-i", path.join(OUT, "bande-son.wav"),
    "-vf", `tmix=frames=${SUB}:weights='1 1 1',select='eq(mod(n\\,${SUB})\\,${SUB - 1})',setpts=N/(${FPS}*TB)`, "-r", String(FPS),
    "-c:v", "libx264", "-preset", "slow", "-crf", "15", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-shortest", path.join(OUT, "showreel.mp4")], { stdio: "inherit" });
  fs.rmSync(dir, { recursive: true, force: true });
  console.log("OK →", path.join(OUT, "showreel.mp4"), `(${((Date.now() - t0) / 1000).toFixed(0)} s)`);
})();
