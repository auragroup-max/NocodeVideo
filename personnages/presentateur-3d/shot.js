// Photographie test-3d.html dans plusieurs réglages → rendus/*.png + rendus/planche.jpg
//   node shot.js
const puppeteer = require("puppeteer-core");
const path = require("path"), fs = require("fs");
const CHROME = process.env.CHROME || "C:/Program Files/Google/Chrome/Application/chrome.exe";
const SHOTS = [["nuit-34", "bg=nuit&yaw=0.35"], ["nuit-face", "bg=nuit&yaw=0&pose=neutre"], ["papier-34", "bg=papier&yaw=-0.4"], ["papier-face", "bg=papier&yaw=0.1&pose=neutre"], ["papier-pieds", "bg=papier&cam=pieds&pose=neutre"]];
(async () => {
  const out = path.join(__dirname, "rendus"); fs.mkdirSync(out, { recursive: true });
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ["--allow-file-access-from-files", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--force-device-scale-factor=1"] });
  const page = await browser.newPage();
  page.on("pageerror", (e) => console.error("[page]", e.message)); page.on("console", (m) => m.type() === "error" && console.error("[console]", m.text()));
  await page.setViewport({ width: 1080, height: 1920 });
  for (const [name, q] of SHOTS) {
    await page.goto("file:///" + path.join(__dirname, "test-3d.html").replace(/\\/g, "/") + "?" + q, { waitUntil: "load" });
    await page.waitForFunction(() => window.__ready === true, { timeout: 30000 });
    await page.screenshot({ path: path.join(out, name + ".png") });
    console.log("ok", name);
  }
  await browser.close();
})();
