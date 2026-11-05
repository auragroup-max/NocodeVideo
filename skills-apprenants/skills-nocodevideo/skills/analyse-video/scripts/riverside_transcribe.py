"""Transcrit un fichier audio via https://riverside.fm/transcription (Playwright).

Usage :
  python riverside_transcribe.py AUDIO.mp3 SORTIE_DIR [--lang fr] [--headful] [--timeout 1800]

Sorties dans SORTIE_DIR :
  transcription.txt          texte brut
  transcription_horodatee.md lignes "[mm:ss] texte"
  riverside_*.png            captures en cas d'échec

Codes retour : 0 OK, 2 blocage/vérification probable, 3 timeout, 1 autre erreur.
"""
import argparse
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

URL = "https://riverside.fm/transcription"
BLOCK_HINTS = ("captcha", "verify you are human", "are you a robot", "access denied",
               "too many requests", "cloudflare", "sign up to continue", "log in to continue")


def page_text(pg):
    try:
        return pg.evaluate("document.body.innerText").lower()
    except Exception:
        return ""


def extract(pg):
    return pg.evaluate("""() => [...document.querySelectorAll('#transcribed-content .transcribed-content')]
        .map(b => ({t: (b.querySelector('.tr-copy-time')||{}).innerText||'',
                    x: ((b.querySelector('.tr-copy-text')||{}).innerText||'').trim()}))
        .filter(s => s.x)""")


def select_language(pg, lang):
    try:
        ok = pg.evaluate("""code => { const it = document.querySelector(`#languages-dropdown [data-lang-code="${code}"]`);
            if (!it) return false; document.querySelector('#lang-btn')?.click(); it.click();
            document.querySelector('#language').value = code; return true; }""", lang)
        if not ok:
            raise ValueError("code langue absent de la liste Riverside")
        time.sleep(1)
        print(f"Langue sélectionnée : {lang} ({pg.locator('#selected-lang-name').inner_text()})")
    except Exception as e:
        print(f"[!] Impossible de choisir la langue '{lang}' ({e.__class__.__name__}), on garde la langue par défaut.")
        try:
            pg.keyboard.press("Escape")
        except Exception:
            pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("out")
    ap.add_argument("--lang", default=None, help="Code langue ISO de Riverside (ex: fr, en, es, zh)")
    ap.add_argument("--headful", action="store_true", help="Navigateur visible (pour vérification manuelle)")
    ap.add_argument("--timeout", type=int, default=1800, help="Secondes max d'attente de la transcription")
    a = ap.parse_args()

    audio = Path(a.audio).resolve()
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    if not audio.exists():
        print(f"Fichier introuvable : {audio}")
        return 1

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not a.headful)
        pg = browser.new_page(viewport={"width": 1280, "height": 900})
        try:
            pg.goto(URL, wait_until="domcontentloaded", timeout=60000)
            time.sleep(4)
            for label in ("Allow all cookies", "Accept all", "Accept"):
                try:
                    pg.get_by_text(label, exact=True).first.click(timeout=2000)
                    break
                except Exception:
                    pass

            pg.locator("input[type=file]").first.set_input_files(str(audio))
            pg.get_by_text("Start transcribing", exact=True).locator("visible=true").first.wait_for(timeout=30000)
            if a.lang:
                select_language(pg, a.lang)
            for opt in ("Video content", "Key insights"):
                try:
                    pg.get_by_text(opt, exact=True).locator("visible=true").first.click(timeout=3000)
                except Exception:
                    pass
            pg.locator("button.ts-button:visible").first.click(timeout=10000)
            print("Upload envoyé, transcription en cours…")

            start, last_n, stable = time.time(), -1, 0
            while time.time() - start < a.timeout:
                time.sleep(5)
                txt = page_text(pg)
                if any(h in txt for h in BLOCK_HINTS) and "your transcripts are ready" not in txt:
                    pg.screenshot(path=str(out / "riverside_blocage.png"), full_page=True)
                    print("BLOCAGE : le site demande une vérification ou une connexion. Capture : riverside_blocage.png")
                    if a.headful:
                        print("Fais la vérification dans la fenêtre ouverte, j'attends…")
                        continue
                    return 2
                if "your transcripts are ready" in txt:
                    n = len(extract(pg))
                    stable = stable + 1 if n == last_n and n > 0 else 0
                    last_n = n
                    if stable >= 2:
                        break
                elapsed = int(time.time() - start)
                if elapsed % 60 < 5:
                    print(f"… {elapsed}s")
            else:
                pg.screenshot(path=str(out / "riverside_timeout.png"), full_page=True)
                print("TIMEOUT : transcription non terminée. Capture : riverside_timeout.png")
                return 3

            segs = extract(pg)
            if not segs:
                pg.screenshot(path=str(out / "riverside_vide.png"), full_page=True)
                print("Transcription vide ou format de page changé. Capture : riverside_vide.png")
                return 1
            (out / "transcription.txt").write_text("\n".join(s["x"] for s in segs), encoding="utf-8")
            (out / "transcription_horodatee.md").write_text(
                "\n\n".join(f"**[{s['t']}]** {s['x']}" for s in segs), encoding="utf-8")
            print(f"OK : {len(segs)} segments -> {out / 'transcription.txt'}")
            return 0
        except Exception as e:
            try:
                pg.screenshot(path=str(out / "riverside_erreur.png"), full_page=True)
            except Exception:
                pass
            print(f"ERREUR : {e}")
            return 1
        finally:
            browser.close()


if __name__ == "__main__":
    sys.exit(main())
