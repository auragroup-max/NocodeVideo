# Transcription mot à mot de la voix (faster-whisper) → assets/audio/words-<v>.json, lu ensuite par align.py
# Usage (depuis le dossier de la vidéo) : python scripts/transcribe.py final [modèle] ["mots, difficiles, à, reconnaître"]
#   modèle : base (rapide, ~1 min) ou medium (plus juste, plus lent). Le premier lancement télécharge le modèle.
import json, sys
from faster_whisper import WhisperModel

v = sys.argv[1]
size = sys.argv[2] if len(sys.argv) > 2 else "base"
hint = sys.argv[3] if len(sys.argv) > 3 else None
model = WhisperModel(size, device="cpu", compute_type="int8")
segs, _ = model.transcribe(f"assets/audio/voix-{v}.mp3", language="fr", word_timestamps=True, vad_filter=False, initial_prompt=hint)
words = [{"text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)} for s in segs for w in s.words]
json.dump(words, open(f"assets/audio/words-{v}.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(words), "mots")
