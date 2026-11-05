# Recale le script exact sur les minutages de la transcription (ancres = mots identiques).
# Usage (depuis le dossier de la vidéo) : python scripts/align.py final
# Lit assets/audio/script-final.txt (le texte exact) + words-final.json (transcribe.py) → assets/audio/words-final.js
import json, re, sys, unicodedata, difflib, subprocess
v = sys.argv[1]
script = open(f"assets/audio/script-{v}.txt", encoding="utf-8").read()
sw = [w for w in script.split() if re.search(r"\w", w)]
raw = json.load(open(f"assets/audio/words-{v}.json", encoding="utf-8"))
norm = lambda s: re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode())
# La transcription coupe « t'épuises » en « t » + « 'épuises » : on recolle avant de comparer.
tw = []
for w in raw:
    if tw and (w["text"].startswith("'") or w["text"].startswith("-") or tw[-1]["text"].endswith("'")):
        tw[-1] = {"text": tw[-1]["text"] + w["text"], "start": tw[-1]["start"], "end": w["end"]}
    else: tw.append(dict(w))
sm = difflib.SequenceMatcher(None, [norm(w) for w in sw], [norm(w["text"]) for w in tw], autojunk=False)
anchor = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): anchor[a + k] = tw[b + k]
END = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"assets/audio/voix-{v}.mp3"]))
out = [None] * len(sw)
for i in anchor: out[i] = {"text": sw[i], "start": anchor[i]["start"], "end": anchor[i]["end"]}
i = 0
while i < len(sw):
    if out[i]: i += 1; continue
    j = i
    while j < len(sw) and not out[j]: j += 1
    t0 = out[i - 1]["end"] if i > 0 else 0.0
    t1 = out[j]["start"] if j < len(sw) else END
    chars = [len(w) + 2 for w in sw[i:j]]; tot = sum(chars); t = t0
    for k, c in zip(range(i, j), chars):
        d = (t1 - t0) * c / tot; out[k] = {"text": sw[k], "start": round(t, 3), "end": round(t + d, 3)}; t += d
    i = j
open(f"assets/audio/words-{v}.js", "w", encoding="utf-8").write(f"window.WORDS=" + json.dumps(out, ensure_ascii=False) + f";window.VOICE_END={END};")
print(v, len(anchor), "/", len(sw), "ancres")
print(" ".join(f"{k}|{w['start']:.2f}|{w['text']}" for k, w in enumerate(out)))
