# Enveloppe de la voix à 60 images/s (0 à 1) → assets/audio/env-<v>.js, pour ouvrir la bouche au rythme réel du son
# Usage (depuis le dossier de la vidéo) : python scripts/envelope.py final
import subprocess, sys, numpy as np
v = sys.argv[1]; SR = 16000; FPS = 60
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"assets/audio/voix-{v}.mp3", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
hop = SR // FPS; n = len(x) // hop
rms = np.sqrt(np.array([np.mean(x[i * hop:(i + 2) * hop] ** 2) for i in range(n)]) + 1e-9)
db = 20 * np.log10(rms)
lo, hi = np.percentile(db, 30), np.percentile(db, 97)
e = np.clip((db - lo) / (hi - lo), 0, 1)
# attaque rapide, relâchement doux : la bouche s'ouvre net et se referme sans claquer
out = np.zeros_like(e); a = 0
for i, val in enumerate(e): a = val if val > a else a + (val - a) * 0.45; out[i] = a
open(f"assets/audio/env-{v}.js", "w").write("window.ENV=[" + ",".join(f"{q:.2f}".rstrip("0").rstrip(".") or "0" for q in out) + "];window.ENV_FPS=60;")
print(n, "images")
