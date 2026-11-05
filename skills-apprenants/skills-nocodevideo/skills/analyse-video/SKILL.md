---
name: analyse-video
description: "Analyse vidéo complète et ingénierie inverse virale. À utiliser dès que l'utilisateur envoie un lien vidéo (TikTok, YouTube, Shorts, Reels, Instagram, Facebook, X, Snapchat, Pinterest, Vimeo…), un fichier audio/vidéo, une transcription brute ou une description, ou demande de transcrire / décortiquer une vidéo, pourquoi elle marche, son hook, son script, un titre / une légende / des hashtags optimisés, ou des prompts Midjourney / Stable Diffusion qui reproduisent son style. Transcription locale Whisper (Riverside en secours), images clés et rapport Markdown."
---

# Analyse vidéo : lien → transcription → ingénierie inverse virale → prompts visuels → rapport

Rôle : expert en marketing digital, en ingénierie inverse de contenu et analyste viral des vidéos courtes. Objectif : décortiquer la vidéo pour extraire sa structure exacte, expliquer les ressorts psychologiques et techniques de son succès, et décrire son esthétique au point de pouvoir la reproduire. Réponse en français, ton précis, analytique et direct. Pas de morale ni de prévention : analyser froidement les mécaniques de viralité. Exécuter tout le workflow sans redemander.

Script : `<Base directory for this skill>/scripts/extraire.py` (chemin donné au chargement du skill, noté `$SK/extraire.py` ci-dessous). Toujours le mettre entre guillemets : il peut contenir des espaces.

## 0. Selon l'entrée

- **Lien ou fichier audio/vidéo** (Riverside compris) : étapes 1 à 3.
- **Transcription brute** : pas de script. La formater proprement (ponctuation, paragraphes) sans changer les mots, puis l'étape 3 sans la section visuelle.
- **Description seule** : travailler à partir d'elle, signaler que le script est reconstitué, pas de section visuelle.
- Si l'utilisateur ne veut que l'analyse virale (« pourquoi ça marche », « le hook », « vite fait »), ne produire que les sections 1 à 4 du rapport.

## 1. Préparation

Vérifier les outils, installer seulement ce qui manque :
- `python -m yt_dlp --version` sinon `python -m pip install -U yt-dlp`
- `ffmpeg -version` sinon `winget install Gyan.FFmpeg` (Windows) ou `brew install ffmpeg` (macOS)
- `python -c "import faster_whisper"` sinon `python -m pip install -U faster-whisper`
- Riverside (secours seulement, à vérifier s'il sert) : `python -c "import playwright"` sinon `python -m pip install playwright` puis `python -m playwright install chromium`

Dossier de travail : `./analyses-video/<AAAA-MM-JJ>_<slug>/` dans le répertoire courant (slug tiré de l'auteur et du sujet).

## 2. Extraction

```bash
PYTHONIOENCODING=utf-8 python "$SK/extraire.py" "<URL ou fichier>" "<dossier>" --lang <code>
```

- Lancer en arrière-plan et regarder les images pendant la transcription.
- `--lang` : code ISO (`fr`, `en`, `es`…) déduit du titre ou de la légende ; sans lui, Whisper détecte la langue.
- **Transcription** : Whisper `base` en local par défaut (~25 s pour 30 s de vidéo). Si Whisper échoue ou n'entend rien, le script passe tout seul à Riverside (riverside.fm dans un navigateur automatisé, plus lent).
  - Whisper se trompe sur les noms propres et les termes anglais : corriger avec le texte visible sur les images, en signalant les passages reconstitués.
  - Si la transcription Whisper est inexploitable, relancer avec `--moteur riverside`. Ne passer à `--model small` ou plus que si l'utilisateur l'accepte : le premier usage télécharge le modèle (~480 Mo) depuis Hugging Face, ce qui peut bloquer longtemps.
  - Si le script ne dépasse pas « Transcription (Whisper…) » au bout de 2 min (téléchargement du modèle bloqué), l'arrêter et relancer avec `--moteur riverside`.
- **Images** : `frames/hook_0.5s.jpg`, `hook_1.5s.jpg`, `hook_2.5s.jpg` puis une image toutes les 3 s (30 au maximum, l'intervalle s'élargit pour les vidéos longues).
- **Place disque** : `video.mp4` et `audio.mp3` sont supprimés dès que la transcription a réussi ; restent `info.json`, les transcriptions et les images (quelques Mo). `--garder` seulement si l'utilisateur veut conserver la vidéo. Un fichier local passé en entrée n'est jamais touché. En cas d'échec, les fichiers restent pour pouvoir relancer.
- **Codes retour** :
  - `0` OK.
  - `1` téléchargement impossible (vidéo privée, connexion requise, géoblocage) : le dire et proposer `--cookies-from-browser chrome` via yt-dlp ou que l'utilisateur fournisse le fichier. Ne jamais saisir d'identifiants soi-même.
  - `2` Riverside demande une vérification : montrer `riverside_blocage.png` et proposer de relancer avec `--moteur riverside --headful` pour que l'utilisateur fasse lui-même la vérification dans la fenêtre. **Ne jamais résoudre un captcha ni créer de compte soi-même.**
  - `3` échec des deux moteurs : lire les messages et les captures `riverside_*.png`. Si la page Riverside a changé, corriger les sélecteurs de `riverside_transcribe.py` (repères : `input[type=file]`, `button.ts-button`, texte « Your transcripts are ready », segments `#transcribed-content .transcribed-content` avec `.tr-copy-time` / `.tr-copy-text`). Si la vidéo n'a pas de voix (musique, texte à l'écran), travailler avec le texte incrusté ou demander la transcription brute.

## 3. Analyse

- `info.json` : plateforme, auteur, date, durée, vues, likes, commentaires, partages, son utilisé, légende et hashtags d'origine. Calculer les taux (likes / vues, partages / vues).
- Regarder les images avec l'outil Read, en commençant par les trois `hook_*` : texte à l'écran, cadrage, visage, mouvement, premier plan choc.
- Situer avec les horodatages le hook (0–3 s), les relances et le CTA.
- Regrouper les images en **scènes / plans** (même décor, même cadrage) et décrire pour chacune :
  1. **Personnes** : âge apparent, morphologie, coiffure, vêtements (matières, couleurs), accessoires, expression, posture, gestuelle. Ne pas chercher à identifier qui sont les personnes réelles.
  2. **Décor** : lieu, objets, arrière-plan, palette, textures, ambiance.
  3. **Image** : éclairage (direction, dureté, température), angle et hauteur de caméra, focale apparente, profondeur de champ, mouvement, étalonnage, habillage graphique.
  - Puis un **prompt Midjourney** (anglais, dense, avec `--ar 9:16` ou `16:9` selon la vidéo, `--style raw --v 7`) et un **prompt Stable Diffusion** (anglais, mots-clés séparés par des virgules) avec son **negative prompt**.

## 4. Rapport

Écrire `rapport.md` dans le dossier de travail. Aucune introduction ni conclusion superflue. Structure exacte :

```markdown
# Analyse : <auteur>, « <titre> »

### 1. Informations
Plateforme, auteur, URL, date, durée, vues, likes, commentaires, partages (avec taux), son, langue, légende d'origine.

### 2. Titre et Description
- **Titre optimisé :** [titre accrocheur adapté à la plateforme]
- **Description :** [légende de la vidéo, avec 4 à 6 hashtags stratégiques]

### 3. Script de la Voix Off
[Texte exact de la voix off, en paragraphes séparant clairement le **Hook** (3 premières secondes), le **Corps** et l'**Outro/CTA**. Marquer [reconstitué] ou [inaudible] les passages incertains. Pour une vidéo longue, découper le corps en parties avec leur horodatage.]

### 4. Ingénierie Inverse : Pourquoi ça marche ?
- **Le Hook (L'accroche) :** [les 3 premières secondes : comment l'attention est captée visuellement ou auditivement]
- **Structure et Rythme :** [comment le storytelling ou le montage maintient la rétention : pattern interrupt, rythme soutenu, modèle ELI5…]
- **Levier Psychologique :** [émotion ou biais cognitif utilisé : FOMO, curiosité, démystification, autorité, validation…]
- **Appel à l'action (CTA) :** [comment le créateur pousse à l'engagement ou à la conversion, et ce qu'il laisse sur la table]

### 5. Idées clés
Résumé en 3 à 5 phrases, idées clés en puces, citations marquantes avec horodatage.

### 6. Éléments visuels et prompts
#### Scène 1 (00:00–00:03) : <titre court>
![](frames/hook_0.5s.jpg)
**Personnes** … **Décor** … **Lumière & caméra** …
**Prompt Midjourney :** ```…```
**Prompt Stable Diffusion :** ```…```  **Negative :** ```…```
(une sous-section par scène)
#### Style global
Synthèse + un prompt « maître » qui reproduit l'esthétique générale.

### Annexe : transcription horodatée
Contenu de transcription_horodatee.md, sans modification, avec le moteur utilisé (Whisper ou Riverside).
```

Dans la réponse, afficher les sections 2 à 4 en entier, résumer les autres en une ou deux lignes, et terminer par un lien cliquable vers `rapport.md`.
