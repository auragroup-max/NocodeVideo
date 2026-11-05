// Miniatures v2 (DA papier) : détoure le présentateur de index-v2.html dans une expression choisie, puis photographie les pages de miniature.
//   node scripts/thumbs-v2.js [expression] [pose]  → assets/thumb-v2-perso.png, renders/miniature-v2-tiktok.png, renders/miniature-v2-youtube.png
const puppeteer = require("puppeteer-core");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe";
const url = (f, q = "") => "file:///" + path.join(ROOT, f).replace(/\\/g, "/") + q;
const EXPR = process.argv[2] || "surpris", POSE = process.argv[3] || "pointe";

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ["--allow-file-access-from-files", "--hide-scrollbars", "--force-device-scale-factor=1"] });
  const page = await browser.newPage();
  page.on("pageerror", (e) => console.error("[page]", e.message));
  await page.setViewport({ width: 1080, height: 1920 });
  await page.goto(url("index-v2.html", "?render=1"), { waitUntil: "load" });
  await page.evaluate(() => window.__ready);
  await page.evaluate((expr, pose) => {
    window.__seek(0.5);
    const $ = (id) => document.getElementById(id);
    ["paper", "ui", "prog", "subs", "hud", "k3d", "trail", "fx", "ring"].forEach((id) => ($(id).style.visibility = "hidden"));
    document.documentElement.style.background = document.body.style.background = "transparent";
    Object.assign($("stage").style, { background: "transparent", filter: "none", opacity: "1" });
    Object.assign($("scene").style, { filter: "none", clipPath: "none", visibility: "visible", opacity: "1" });
    $("cam").style.transform = "none"; Object.assign($("persoW").style, { transform: "none", filter: "none" });
    const p = $("perso"); p.setAttribute("data-expr", expr); p.setAttribute("data-pose", pose); p.setAttribute("data-talk", "0");
    p.querySelectorAll(".extra").forEach((e) => (e.style.opacity = "1"));
  }, EXPR, POSE);
  await page.screenshot({ path: path.join(ROOT, "assets/thumb-v2-perso.png"), omitBackground: true, clip: { x: 0, y: 700, width: 1080, height: 1220 } });
  for (const [file, w, h, out] of [["thumb-v2-tiktok.html", 1080, 1920, "miniature-v2-tiktok.png"], ["thumb-v2-youtube.html", 1280, 720, "miniature-v2-youtube.png"]]) {
    await page.setViewport({ width: w, height: h });
    await page.goto(url(file), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready.then(() => true));
    await page.screenshot({ path: path.join(ROOT, "renders", out) });
  }
  await browser.close();
  console.log("miniatures v2 OK");
})();
