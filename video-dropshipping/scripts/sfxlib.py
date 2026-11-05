# Effets sonores 100 % code : chaque son est synthétisé (numpy), puis posé sur les repères exportés
# par la page (window.__sfx) et mixé sous la voix.
# Musique de fond optionnelle : assets/audio/musique.mp3 (bouclée, fondue, très basse et effacée sous la voix).
# Usage : python3 tools/sfx.py repères.json voix.mp3 durée sortie.wav
import json, os, subprocess, sys, wave
import numpy as np

SR = 48000
rng = np.random.default_rng(7)
MASTER_DB = -19      # effets : nettement sous la voix (environ 20 LU)
MUSIC_DB = -21       # musique : RMS à 21 dB sous la voix
MUSIC_DUCK_DB = -5   # la musique baisse encore de 5 dB quand la voix parle
FX_LOWPASS = 5000    # coupe les aigus perçants des effets  # même graine → même bande-son à chaque rendu


def t_axis(d): return np.arange(int(d * SR)) / SR


def env(d, a=0.005, r=None, shape="exp", tau=0.1):
    t = t_axis(d)
    att = np.clip(t / max(a, 1e-4), 0, 1)
    if shape == "exp": dec = np.exp(-np.maximum(t - a, 0) / tau)
    else: dec = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2  # cloche
    return att * dec


def band_noise(d, fc, bw=0.6, n=1024, hop=256):
    """Bruit filtré dont la bande centrale suit fc(t) (Hz), largeur bw en octaves. Synthèse spectrale + overlap-add."""
    N = int(d * SR) + n
    out = np.zeros(N)
    win = np.hanning(n)
    f = np.fft.rfftfreq(n, 1 / SR); f[0] = 1
    for i, start in enumerate(range(0, N - n, hop)):
        c = fc(start / SR)
        mask = np.exp(-0.5 * (np.log2(f / c) / (bw / 2.355)) ** 2)
        spec = mask * np.exp(1j * rng.uniform(0, 2 * np.pi, f.size))
        out[start:start + n] += np.fft.irfft(spec, n) * win
    out = out[:int(d * SR)]
    return out / (np.abs(out).max() + 1e-9)


def glide(d, f0, f1, curve="exp"):
    t = t_axis(d)
    f = f0 * (f1 / f0) ** (t / d) if curve == "exp" else f0 + (f1 - f0) * t / d
    return np.sin(2 * np.pi * np.cumsum(f) / SR)


def bell(f, d=1.2, partials=((1, 1), (2.0, .35), (3.01, .12)), tau=0.35):
    t = t_axis(d)
    s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * r / tau) for r, a in partials)
    return s * np.clip(t / 0.004, 0, 1)


def lowpass(x, fc):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(x.size, 1 / SR)
    return np.fft.irfft(X / np.sqrt(1 + (f / fc) ** 4), x.size)


# ---------- bibliothèque (sons doux, façon interface Apple : courts, ronds, sans agressivité) ----------
def whoosh(d=0.7, f0=350, f1=2600, **_):
    return band_noise(d, lambda t: f0 * (f1 / f0) ** (t / d), 0.9) * env(d, shape="bell")

def swell(**_):  # bascule noir ↔ clair : souffle aérien qui monte puis s'ouvre
    d = 1.4
    air = band_noise(d, lambda t: 500 * (5000 / 500) ** (t / d), 1.4) * env(d, shape="bell")
    pad = sum(np.sin(2 * np.pi * f * t_axis(d)) for f in (392, 587.3, 784)) / 3 * env(d, shape="bell") * 0.25
    return air + pad

def pop(**_):
    d = 0.16
    s = glide(d, 820, 360) * env(d, 0.002, tau=0.035)
    click = band_noise(0.02, lambda t: 3000, 1.5) * env(0.02, 0.001, tau=0.004) * 0.3
    s[:click.size] += click
    return s

def glass(k=0, **_):  # objet en verre qui apparaît : tintement cristallin
    f = (1760, 2093)[k % 2]
    return bell(f, 1.3, ((1, 1), (2.76, .3), (5.4, .1)), 0.5) * 0.8

def drain(d=2.0, **_):  # batterie qui se vide : glissando descendant feutré
    t = t_axis(d)
    s = glide(d, 520, 110) + 0.25 * glide(d, 1560, 330)
    return lowpass(s, 1800) * np.clip(t / 0.2, 0, 1) * np.clip((d - t) / 0.4, 0, 1) * (1 - 0.4 * t / d)

def notif(**_):  # notification : deux notes en cloche (motif original)
    a = bell(659.3, 0.9, tau=0.25); b = bell(987.8, 0.9, tau=0.3)
    s = np.zeros(int(1.0 * SR)); s[:a.size] += a; o = int(0.11 * SR); s[o:o + b.size] += b[:s.size - o]
    return s

def strike(**_):  # trait rouge tiré : frottement de feutre
    d = 0.45
    return band_noise(d, lambda t: 2500 + 3000 * t / d, 1.0) * env(d, 0.03, tau=0.18)

def shimmer(**_):  # lumière divine : scintillement + accord tenu
    d = 2.2; t = t_axis(d); s = np.zeros(t.size)
    for _ in range(26):
        f = rng.uniform(2200, 7000); t0 = rng.uniform(0, 1.2)
        s += np.sin(2 * np.pi * f * t + rng.uniform(0, 6)) * np.exp(-np.maximum(t - t0, 0) / 0.25) * (t >= t0) * rng.uniform(.2, 1)
    pad = sum(np.sin(2 * np.pi * f * t) for f in (523.3, 659.3, 784, 1046.5)) / 4
    return s / np.abs(s).max() * 0.35 * env(d, 0.05, shape="bell") + pad * env(d, shape="bell") * 0.5

def bloom(**_):  # onde d'impact : pulsation grave et ronde
    d = 1.2
    return glide(d, 180, 120) * env(d, 0.08, tau=0.35)

def fall(d=1.5, **_):  # pierre qui tombe : souffle descendant qui s'intensifie
    t = t_axis(d)
    return band_noise(d, lambda tt: 2400 * (300 / 2400) ** (tt / d), 1.0) * (t / d) ** 1.6

def thud(**_):  # impact sourd
    d = 1.1; t = t_axis(d)
    body = glide(d, 85, 38) * np.exp(-t / 0.28)
    dust = lowpass(band_noise(d, lambda _: 220, 2.0), 900) * np.exp(-t / 0.12) * 0.6
    return (body + dust) * np.clip(t / 0.003, 0, 1)

def card(k=0, **_):  # carte d'interface qui glisse : petit souffle court
    d = 0.32
    return band_noise(d, lambda t: (900, 1100)[k % 2] * (3 ** (t / d)), 0.8) * env(d, shape="bell")

def tick(k=0, **_):
    d = 0.05
    return band_noise(d, lambda t: 3200 + 120 * (k % 6), 0.7) * env(d, 0.001, tau=0.008)

def type_(k=0, **_):  # frappe de clavier iOS
    d = 0.06
    s = band_noise(d, lambda t: 2400 + 300 * (k % 3), 1.2) * env(d, 0.001, tau=0.01)
    s += np.sin(2 * np.pi * 180 * t_axis(d)) * env(d, 0.001, tau=0.012) * 0.4
    return s

def reveal(**_):  # apparition importante : accord en cloche (sol majeur)
    s = np.zeros(int(1.8 * SR))
    for i, f in enumerate((392.0, 493.9, 587.3, 784.0)):
        b = bell(f, 1.6, tau=0.55) * (1 - 0.15 * i); o = int(0.045 * i * SR); s[o:o + b.size] += b[:s.size - o]
    return s

def riser(d=1.5, **_):
    t = t_axis(d)
    return (band_noise(d, lambda tt: 400 * (6000 / 400) ** (tt / d), 1.0) + 0.3 * glide(d, 200, 800)) * (t / d) ** 2 * np.clip((d - t) / 0.05, 0, 1)

def boom(**_):  # coup grave « keynote »
    d = 1.6; t = t_axis(d)
    return (glide(d, 70, 45) * np.exp(-t / 0.5) + 0.3 * lowpass(band_noise(d, lambda _: 150, 2), 600) * np.exp(-t / 0.2)) * np.clip(t / 0.004, 0, 1)

def ding(k=0, **_):  # anneau d'activité qui se ferme : do – mi – sol
    return bell((523.3, 659.3, 784.0)[k % 3], 1.4, tau=0.45)

def down(**_):  # mail mis de côté
    d = 0.35
    return glide(d, 660, 330) * env(d, 0.005, tau=0.1)


LIB = dict(whoosh=whoosh, swell=swell, pop=pop, glass=glass, drain=drain, notif=notif, strike=strike, shimmer=shimmer,
           bloom=bloom, fall=fall, thud=thud, card=card, tick=tick, type=type_, reveal=reveal, riser=riser, boom=boom,
           ding=ding, down=down)


def load_audio(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def main():
    cues = json.load(open(sys.argv[1], encoding="utf-8"))
    voice = load_audio(sys.argv[2]); dur = float(sys.argv[3]); out = sys.argv[4]
    n = int(dur * SR) + SR
    fx = np.zeros(n)
    for c in cues:
        snd = LIB[c["n"]](**{k: v for k, v in c.items() if k in ("d", "k")})
        snd = snd / (np.abs(snd).max() + 1e-9) * 10 ** (c["g"] / 20)
        i = int(c["t"] * SR)
        if i < 0: snd, i = snd[-i:], 0
        m = min(snd.size, n - i)
        if m > 0: fx[i:i + m] += snd[:m]
    # Les effets sont calés sur la crête de la voix ; la voix garde toujours le dessus (effacement quand elle parle).
    fx = lowpass(fx, FX_LOWPASS)
    vp = np.abs(voice).max() + 1e-9
    v = np.zeros(n); v[:voice.size] = voice[:n]
    k = int(0.15 * SR); c = np.concatenate([[0], np.cumsum(np.abs(v) > vp * 0.08)])
    venv = np.zeros(n); venv[k // 2:n - k // 2] = (c[k:] - c[:-k])[:n - 2 * (k // 2)] / k  # moyenne glissante 150 ms
    speaking = np.clip(venv * 3, 0, 1)
    fx *= vp * 10 ** (MASTER_DB / 20) * (1 - 0.5 * speaking)
    mix = v + fx
    music_path = next((p for p in ("assets/audio/musique.mp3", "assets/audio/musique.wav") if os.path.exists(p)), None)
    if music_path:
        mu = load_audio(music_path)
        mu = np.tile(mu, int(np.ceil(n / mu.size)))[:n]
        t = np.arange(n) / SR
        mu *= np.clip(t / 1.5, 0, 1) * np.clip((dur - t) / 3.0, 0, 1)
        vrms = np.sqrt(np.mean(voice[np.abs(voice) > vp * 0.08] ** 2)); mrms = np.sqrt(np.mean(mu[: int(dur * SR)] ** 2)) + 1e-9
        duck = 10 ** (MUSIC_DUCK_DB / 20)
        mix += mu * (vrms / mrms) * 10 ** (MUSIC_DB / 20) * (1 - (1 - duck) * speaking)
        print("musique :", music_path)
    mix = mix[:int(dur * SR)]
    mix /= max(1.0, np.abs(mix).max() / 0.98)
    pcm = (np.repeat(mix[:, None], 2, 1) * 32767).astype("<i2")
    with wave.open(out, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    print(f"sfx : {len(cues)} repères → {out}")


if __name__ == "__main__":
    main()
