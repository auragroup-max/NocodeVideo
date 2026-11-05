"""Télécharge une vidéo, extrait l'audio, la transcrit (Whisper, Riverside en secours) et capture des images clés.

Usage : python extraire.py URL_OU_FICHIER SORTIE_DIR [--moteur auto|whisper|riverside] [--model base]
                           [--lang fr] [--every 3] [--max 30] [--garder] [--headful]

Sorties dans SORTIE_DIR :
  info.json                  métadonnées yt-dlp (absent si on passe un fichier local)
  video.mp4, audio.mp3       supprimés une fois la transcription réussie, sauf avec --garder
  transcription.txt          texte brut
  transcription_horodatee.md segments horodatés
  frames/                    hook_0.5s.jpg, hook_1.5s.jpg, hook_2.5s.jpg puis frame_mm-ss.jpg

Moteur `auto` : Whisper local, puis Riverside si Whisper échoue ou ne renvoie rien.
Codes retour : 0 OK, 1 erreur de téléchargement / ffmpeg, 2 Riverside demande une vérification
(relancer avec --moteur riverside --headful), 3 échec de la transcription.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise RuntimeError(f"{cmd[0]} a échoué :\n{r.stderr.strip()[-2000:]}")
    return r.stdout


def telecharger(src, out):
    video = out / "video.mp4"
    if Path(src).is_file():
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-c", "copy", str(video)])
        return video
    (out / "info.json").write_text(
        run([sys.executable, "-m", "yt_dlp", "--dump-json", "--no-playlist", src]), encoding="utf-8")
    run([sys.executable, "-m", "yt_dlp", "--no-playlist", "-f", "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]/b",
         "--merge-output-format", "mp4", "-o", str(video), src])
    return video


def duree(video):
    return float(json.loads(run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "json", str(video)]))["format"]["duration"])


def capture(video, t, dest):
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1",
         "-vf", "scale='min(1080,iw)':-2", "-q:v", "3", str(dest)])


def images(video, frames, every, maxi):
    frames.mkdir(exist_ok=True)
    dur = duree(video)
    n = 0
    # Le hook (3 premières secondes) est échantillonné finement, le reste toutes les `every` secondes.
    for t in (0.5, 1.5, 2.5):
        if t < dur:
            capture(video, t, frames / f"hook_{t}s.jpg")
            n += 1
    every = max(every, (dur - 3) / max(maxi - n, 1))
    t = 3.0
    while t < dur and n < maxi:
        capture(video, t, frames / f"frame_{int(t // 60):02d}-{int(t % 60):02d}.jpg")
        n += 1
        t += every
    return n, dur


def horo(s):
    return f"{int(s // 60):02d}:{s % 60:04.1f}"


def whisper(audio, out, model, lang):
    from faster_whisper import WhisperModel

    segments, info = WhisperModel(model, device="cpu", compute_type="int8").transcribe(
        str(audio), language=lang, vad_filter=True)
    lignes, texte = [], []
    for s in segments:
        lignes.append(f"[{horo(s.start)}] {s.text.strip()}")
        texte.append(s.text.strip())
    if not lignes:
        raise RuntimeError("aucune parole détectée")
    (out / "transcription_horodatee.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    (out / "transcription.txt").write_text(" ".join(texte) + "\n", encoding="utf-8")
    print(f"Whisper OK : {len(lignes)} segments, langue {info.language} ({info.language_probability:.0%})")


def riverside(audio, out, lang, headful):
    cmd = [sys.executable, str(Path(__file__).with_name("riverside_transcribe.py")), str(audio), str(out)]
    if lang:
        cmd += ["--lang", lang]
    if headful:
        cmd.append("--headful")
    return subprocess.run(cmd).returncode


def transcrire(a, audio, out):
    """Renvoie 0 si une transcription a été écrite, sinon le code retour du script."""
    if a.moteur in ("auto", "whisper"):
        try:
            print(f"Transcription (Whisper {a.model})…", flush=True)
            whisper(audio, out, a.model, a.lang)
            return 0
        except Exception as e:
            print(f"Whisper a échoué : {e}", file=sys.stderr)
            if a.moteur == "whisper":
                return 3
    print("Transcription (Riverside)…", flush=True)
    code = riverside(audio, out, a.lang, a.headful)
    return {0: 0, 2: 2}.get(code, 3)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", help="URL de la vidéo ou chemin d'un fichier local")
    ap.add_argument("out")
    ap.add_argument("--moteur", choices=["auto", "whisper", "riverside"], default="auto")
    ap.add_argument("--model", default="base", help="modèle Whisper : tiny, base, small, medium, large-v3")
    ap.add_argument("--lang", default=None, help="code ISO (fr, en…) ; détection auto si absent")
    ap.add_argument("--every", type=float, default=3)
    ap.add_argument("--max", type=int, default=30)
    ap.add_argument("--garder", action="store_true", help="conserver video.mp4 et audio.mp3 après la transcription")
    ap.add_argument("--headful", action="store_true", help="Riverside dans un navigateur visible (vérification manuelle)")
    a = ap.parse_args()

    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    try:
        print("Téléchargement…", flush=True)
        video = telecharger(a.src, out)
        audio = out / "audio.mp3"
        run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-vn", "-ac", "1", "-ar", "16000",
             "-b:a", "64k", str(audio)])
        n, dur = images(video, out / "frames", a.every, a.max)
        print(f"{n} images, durée {dur:.0f}s", flush=True)
    except RuntimeError as e:
        print(e, file=sys.stderr)
        return 1

    code = transcrire(a, audio, out)
    if code:
        return code
    if not a.garder:
        for f in (video, audio):
            f.unlink(missing_ok=True)
    print(f"OK -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
