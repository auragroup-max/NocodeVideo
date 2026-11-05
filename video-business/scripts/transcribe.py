# Transcription mot à mot de la voix (faster-whisper) → assets/audio/words-<v>.json, lu ensuite par align.py
# Usage (depuis le dossier de la vidéo) : python scripts/transcribe.py final [modèle]
import json, sys
from faster_whisper import WhisperModel

v = sys.argv[1]
size = sys.argv[2] if len(sys.argv) > 2 else "medium"
model = WhisperModel(size, device="cpu", compute_type="int8", local_files_only=True)  # modèle déjà en cache, pas de téléchargement
segs, _ = model.transcribe(f"assets/audio/voix-{v}.mp3", language="fr", word_timestamps=True, vad_filter=False,
                           initial_prompt="Madagascar, Facebook, TikTok, Google Maps, Orange, WhatsApp, quincaillerie, business, l IA")
words = [{"text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)} for s in segs for w in s.words]
json.dump(words, open(f"assets/audio/words-{v}.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(words), "mots")
