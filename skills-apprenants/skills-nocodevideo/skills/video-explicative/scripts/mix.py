# Mixage de la vidéo longue : voix (assemblée par prepare.py) + musiques A/B/C en fondu + effets sonores (fichiers fournis).
# Les repères viennent de la page (window.__sfx) :
#   { n: "music", file: "A", t, end, g, fin, fout, loop }   musique de fond (g en dB sous la voix)
#   { n: "sfx",   file: "hit", t, g }                         effet ponctuel (g en dB sous la crête de la voix)
# Usage : python3 tools/mix.py repères.json voix.wav durée sortie.wav
import json, subprocess, sys, wave
import numpy as np

SR = 48000
DUCK_DB = -6  # la musique baisse encore de 6 dB quand la voix parle


def load(path, ch=2):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", str(ch), "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch).astype(np.float64)


def rms(x): return np.sqrt(np.mean(x ** 2) + 1e-12)


def main():
    cues = json.load(open(sys.argv[1], encoding="utf-8"))
    voice = load(sys.argv[2], 1)[:, 0]; dur = float(sys.argv[3]); out = sys.argv[4]
    n = int(dur * SR) + SR
    v = np.zeros(n); v[: min(n, voice.size)] = voice[:n]
    vp = np.abs(v).max() + 1e-9
    active = np.abs(v) > vp * 0.06
    vr = rms(v[active])
    # enveloppe « la voix parle » lissée sur 250 ms
    k = int(0.25 * SR); c = np.concatenate([[0], np.cumsum(active)])
    speak = np.zeros(n); speak[k // 2: n - k // 2] = (c[k:] - c[:-k])[: n - 2 * (k // 2)] / k
    speak = np.clip(speak * 3, 0, 1)

    bed = np.zeros((n, 2)); fx = np.zeros((n, 2))
    for q in cues:
        i0 = int(q["t"] * SR)
        if q["n"] == "music":
            src = load(f"assets/music/{q['file']}.mp3")
            i1 = int(q["end"] * SR); L = i1 - i0
            if L <= 0: continue
            seg = np.tile(src, (int(np.ceil(L / len(src))) + 1, 1))[:L] if q.get("loop") else np.vstack([src, np.zeros((max(0, L - len(src)), 2))])[:L]
            t = np.arange(L) / SR
            env = np.clip(t / q.get("fin", 1.5), 0, 1) * np.clip((L / SR - t) / q.get("fout", 2.0), 0, 1)
            seg = seg * (vr / rms(src)) * 10 ** (q["g"] / 20) * env[:, None]
            bed[i0:i1] += seg[: n - i0]
        else:
            s = load(f"assets/sfx/{q['file']}.mp3")
            s = s / (np.abs(s).max() + 1e-9) * vp * 10 ** (q["g"] / 20)
            m = min(len(s), n - i0)
            if m > 0: fx[i0:i0 + m] += s[:m]
    duck = 10 ** (DUCK_DB / 20)
    bed *= (1 - (1 - duck) * speak)[:, None]
    fx *= (1 - 0.4 * speak)[:, None]
    mix = v[:, None] + bed + fx
    mix = mix[: int(dur * SR)]
    mix /= max(1.0, np.abs(mix).max() / 0.98)
    with wave.open(out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype("<i2").tobytes())
    print(f"mix : {sum(1 for q in cues if q['n'] == 'music')} musiques, {sum(1 for q in cues if q['n'] != 'music')} effets → {out}")


if __name__ == "__main__":
    main()
