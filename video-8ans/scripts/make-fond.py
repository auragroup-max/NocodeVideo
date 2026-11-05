# Recolore la référence de fond de l'utilisateur (shared/ref/fond-reference.jpg) dans la DA Nuit bleue :
# fond bleu nuit, lueur bleue-cyan à la place du bleu électrique, lueur rouge à la place du violet.
import numpy as np
from PIL import Image
src = Image.open("shared/ref/fond-reference.jpg").convert("RGB")
h = 1920; w = round(src.width * h / src.height); im = src.resize((w, h), Image.LANCZOS)
x0 = 110; im = im.crop((x0, 0, x0 + 1080, h))          # format 9:16 : on garde le coin rouge à gauche et la lueur à droite
a = np.asarray(im).astype(np.float32) / 255
r, g, b = a[..., 0], a[..., 1], a[..., 2]
viol = np.clip((r - 0.03) / 0.27, 0, 1)                            # seul le coin violet contient du rouge
lum = np.clip(b * 0.85 + g * 0.15, 0, 1)
hexc = lambda s: tuple(int(s[i:i + 2], 16) / 255 for i in (1, 3, 5))
def ramp(t, stops):
    out = np.zeros(t.shape + (3,), np.float32)
    for c in range(3): out[..., c] = np.interp(t, [s[0] for s in stops], [hexc(s[1])[c] for s in stops])
    return out
base = ramp(lum, [(0, "#060b19"), (0.15, "#0d1630"), (0.35, "#1B2A4A"), (0.6, "#1a4a8f"), (0.85, "#1e6ad0"), (1, "#2f8ff0")])
red = ramp(viol, [(0, "#060b19"), (0.35, "#4a0d16"), (0.7, "#a81a24"), (1, "#E8242B")])
out = base * (1 - viol[..., None]) + red * viol[..., None]
out += np.random.default_rng(1).normal(0, 0.008, out.shape)          # grain léger contre les bandes
Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8)).save("shared/fond-nuit-bleue.jpg", quality=92)
