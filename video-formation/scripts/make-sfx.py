# Fabrique les effets sonores « réaction » de la vidéo LLC (100 % synthétisés, bibliothèque tools/sfxlib.py)
# Sortie : assets/sfx/syn-<nom>.mp3, utilisés par la page via SFX("syn-<nom>", t, gain) et mixés par tools/mix.py.
# Usage (depuis video-llc/) : python3 tools/make-sfx.py
import os, subprocess, sys, wave
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import sfxlib as L

SR = L.SR
def coins():  # pièces qui tombent : cascade de petites cloches aiguës
    s = np.zeros(int(1.4 * SR)); r = np.random.default_rng(3)
    for i in range(9):
        b = L.bell(r.uniform(2600, 4200), 0.5, ((1, 1), (2.4, .4)), 0.12) * r.uniform(.4, 1)
        o = int((0.04 + i * 0.075 + r.uniform(0, .03)) * SR); s[o:o + b.size] += b[:s.size - o]
    return s
def error():  # refus de paiement : double bourdon grave
    d = 0.5; t = L.t_axis(d); s = np.zeros(int(0.75 * SR))
    tone = (np.sign(np.sin(2 * np.pi * 150 * t)) * 0.4 + np.sin(2 * np.pi * 150 * t)) * L.env(d, 0.005, tau=0.12)
    tone = L.lowpass(tone, 1400)
    s[:tone.size] += tone; o = int(0.22 * SR); s[o:o + tone.size] += tone[:s.size - o]
    return s
def stamp():  # tampon officiel : coup sourd + claquement
    s = L.thud() * 0.8; c = L.band_noise(0.05, lambda t: 1800, 1.4) * L.env(0.05, 0.001, tau=0.01)
    s[:c.size] += c * 0.7; return s
def lock():  # verrou qui se ferme
    a = L.band_noise(0.04, lambda t: 2600, 1.0) * L.env(0.04, 0.001, tau=0.006)
    b = L.band_noise(0.06, lambda t: 1500, 1.0) * L.env(0.06, 0.001, tau=0.01)
    s = np.zeros(int(0.3 * SR)); s[:a.size] += a; o = int(0.09 * SR); s[o:o + b.size] += b; return s
def keys():  # quelques frappes de clavier
    s = np.zeros(int(0.7 * SR))
    for k in range(6):
        b = L.type_(k); o = int(k * 0.105 * SR); s[o:o + b.size] += b
    return s

def glitch():  # coupure numérique : salves de bruit et bips carrés hachés
    s = np.zeros(int(0.45 * SR)); r = np.random.default_rng(5)
    for i in range(7):
        d = r.uniform(0.012, 0.04); n = int(d * SR); o = int(i * 0.055 * SR)
        if i % 2: seg = np.sign(np.sin(2 * np.pi * r.uniform(300, 1400) * np.arange(n) / SR)) * 0.6
        else: seg = r.uniform(-1, 1, n)
        s[o:o + n] += seg[: s.size - o]
    return L.lowpass(s, 6000)
def whip():  # fouet rapide : souffle très court qui monte puis tombe
    return L.whoosh(0.28, 600, 5000)

SOUNDS = dict(glitch=glitch, whip=whip, swell=L.swell, pop=L.pop, notif=L.notif, ding0=lambda: L.ding(0), ding1=lambda: L.ding(1), ding2=lambda: L.ding(2), tick=L.tick,
              glass=L.glass, thud=L.thud, boom=L.boom, strike=L.strike, shimmer=L.shimmer, card=L.card, reveal=L.reveal,
              coins=coins, error=error, stamp=stamp, lock=lock, keys=keys, bloom=L.bloom)
os.makedirs("assets/sfx", exist_ok=True)
for name, fn in SOUNDS.items():
    x = np.asarray(fn(), dtype=np.float64); x = x / (np.abs(x).max() + 1e-9) * 0.9
    tmp = f"assets/sfx/syn-{name}.wav"
    with wave.open(tmp, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((x * 32767).astype("<i2").tobytes())
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-b:a", "192k", f"assets/sfx/syn-{name}.mp3"], check=True); os.remove(tmp)
print("sons :", ", ".join(SOUNDS))
