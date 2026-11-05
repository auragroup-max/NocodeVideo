// Miniatures 100 % code : détoure le personnage de index.html (PNG transparent), puis photographie les pages de miniature.
//   node scripts/thumbs.js [instant]  → assets/thumb-perso.png, renders/miniature-tiktok.png, renders/miniature-youtube.png
const puppeteer = require("puppeteer-core");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe";
const url = (f, q = "") => "file:///" + path.join(ROOT, f).replace(/\\/g, "/") + q;
const T = Number(process.argv[2] || 64.95);

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ["--allow-file-access-from-files", "--hide-scrollbars", "--force-device-scale-factor=1"] });
  const page = await browser.newPage();
  page.on("pageerror", (e) => console.error("[page]", e.message));
  await page.setViewport({ width: 1080, height: 1920 });
  await page.goto(url("index.html", "?render=1"), { waitUntil: "load" });
  await page.evaluate(() => window.__ready);
  await page.evaluate((t) => {
    window.__seek(t);
    const $ = (id) => document.getElementById(id);
    ["bgFull", "dim", "bg", "bokeh", "light", "halo", "ui", "prog", "subs", "vig", "hud", "k3d", "trail", "fx", "ring", "streak1"].forEach((id) => $(id) && ($(id).style.visibility = "hidden"));
    document.documentElement.style.background = document.body.style.background = "transparent";
    Object.assign($("stage").style, { background: "transparent", filter: "none", opacity: "1" });
    Object.assign($("scene").style, { filter: "none", clipPath: "none", visibility: "visible", opacity: "1" });
    $("cam").style.transform = "none"; Object.assign($("persoW").style, { transform: "none", filter: "none" });
    // bouche fermée avec sourire, yeux ouverts
    $("bouchev").setAttribute("ry", "6"); $("dents").setAttribute("opacity", "0.2"); $("smile").style.opacity = "0.9"; $("yeux").setAttribute("transform", "");
  }, T);
  await page.screenshot({ path: path.join(ROOT, "assets/thumb-perso.png"), omitBackground: true, clip: { x: 0, y: 560, width: 1080, height: 1360 } });
  for (const [file, w, h, out] of [["thumb-tiktok.html", 1080, 1920, "miniature-tiktok.png"], ["thumb-youtube.html", 1280, 720, "miniature-youtube.png"]]) {
    await page.setViewport({ width: w, height: h });
    await page.goto(url(file), { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready.then(() => true));
    await page.screenshot({ path: path.join(ROOT, "renders", out) });
  }
  await browser.close();
  console.log("miniatures OK");
})();
