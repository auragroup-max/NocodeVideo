# Génère les PDF des guides (pieds de page gérés en CSS via @page)
# Usage : python build.py            -> les deux guides
#         python build.py debutant   -> seulement le guide débutant
import pathlib, sys
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
GUIDES = {
    "complet":  ("guide.html",          "Guide-Motion-Design-Claude-Opus-5.5.pdf"),
    "debutant": ("guide-debutant.html", "Guide-Debutant-Motion-Design-Claude.pdf"),
}
wanted = sys.argv[1:] or list(GUIDES)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    for key in wanted:
        src, out = GUIDES[key]
        page.goto((HERE / src).resolve().as_uri(), wait_until="networkidle")
        page.evaluate("document.fonts.ready.then(() => true)")
        page.pdf(path=str(HERE / out), print_background=True, prefer_css_page_size=True)
        print(f"OK : {HERE / out}")
    browser.close()
