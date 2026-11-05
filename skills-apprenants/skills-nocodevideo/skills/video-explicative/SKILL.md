---
name: video-explicative
description: Fabriquer une vidéo explicative verticale (TikTok, Reels, Shorts) dans la DA « Nuit bleue / écran rouge » en motion design. Un personnage présentateur au premier plan, un fond quadrillé, une barre de progression en haut jusqu'à la fin, des textes en mouvement, des zooms et du flou de profondeur. Utiliser pour tout épisode de la série dropshipping, toute explication (LLC, paiement, produit…) ou dès que l'utilisateur demande « une vidéo comme la LLC expliquée à un enfant ». Couvre le script, le texte ElevenLabs, les prompts d'images, le montage HTML/GSAP, le rendu, les corrections et le pack de publication donné seulement après « c'est bon ».
---


# Vidéo explicative en motion design (DA Nuit bleue)

> **Fichiers fournis avec ce skill** : `assets/` (fond de la série, référence, polices Inter et Instrument Serif, GSAP), `templates/` (`test-style.html` = personnages en code + bokeh ; `test-anim.html` = intro 3D, rond, schémas), `scripts/` (rendu `render.js` + `mix.py`, effets sonores `make-sfx.py`, calage de la voix `align.py`, recoloration du fond `make-fond.py`), `docs/` (fiche DA, template DA, prompts de poses). Pour une nouvelle vidéo : copier un template et `assets/` dans un dossier, y mettre la voix (`assets/audio/voix-final.mp3`), puis suivre les étapes ci-dessous. Le rendu demande Node + Puppeteer (ou Playwright) + FFmpeg + Python.


Une méthode unique pour que chaque vidéo de la série se ressemble : même personnage, même fond, même barre, même façon de bouger. Ne pas réinventer le style à chaque vidéo.

## 1. Règles de travail avec l'utilisateur

- Réponses en français simple, listes à puces, sans flatterie. Contredire si une idée est fausse.
- **Pendant la fabrication et les corrections : ne jamais donner de titre, description, hashtags ni miniature.** Seulement la vidéo, les images de contrôle et ce qui a changé.
- **Préparer la miniature et le pack de publication en silence pendant le montage**, pour qu'ils soient prêts.
- **Quand l'utilisateur écrit « c'est bon » (ou valide clairement)**, livrer d'un coup, sans poser de question :
  1. la vidéo finale en pleine qualité (si elle est trop lourde pour être envoyée : une copie allégée, et le chemin de l'original) ;
  2. la miniature TikTok (1080×1920) et la miniature YouTube (1280×720) ;
  3. pour TikTok : légende courte + question pour les commentaires + 3 à 5 hashtags ;
  4. pour YouTube Shorts : titre + description + hashtags ;
- Ne jamais publier soi-même sur un réseau social.

## 2. Le script

- **Ni trop long ni sec** : environ 1 min 20 (200 à 240 mots). Informer, sans entrer dans le détail, mais avec du **ressenti humain** (la frustration vécue, le soulagement), du rythme (questions, phrases très courtes, pauses) et des moments qui appellent une animation. Une version d'une minute « liste de faits » a été jugée robotique.
- Structure type : accroche par une situation vécue (« Tu as un client à l'étranger… et tu ne peux pas recevoir l'argent ») → définition avec une comparaison locale (par exemple : LLC = une SARL, mais américaine) → pourquoi c'est utile pour un Malgache → exemple concret (dropshipping) → appel à l'action.
- **Ne pas mettre, sauf si l'utilisateur le demande** : impôts, déclarations, entretien annuel, frais, publicité, calculs de marge, longues histoires-images (stand de jus, animal de compagnie). L'utilisateur juge que ça perd le public.
- Pas de promesse absolue (« débloque tout », « garanti ») : dire « ouvre la porte », « tu peux ».
- Phrases courtes, tutoiement, une idée par phrase.
- Fin : « Enregistre », « Envoie-la à… », WhatsApp (lien dans la bio). Pas de lien en commentaire : sur TikTok, il n'est pas cliquable.
- Les faits à vérifier vont dans les notes du projet, pas dans la vidéo. Ne jamais inventer de source.
- Livrer deux versions : le texte propre (`script-final.txt`) et le texte ElevenLabs avec balises (`script-tags.txt`). Dans la réponse, ne donner que le texte à coller, sans long commentaire.

## 3. La direction artistique

- **Couleurs** : fond de base ci-dessous (noir bleuté + lueur bleue), rouge `#FF2D2D` / `#E8242B`, cyan `#39B6EE`, texte blanc. Police du projet (jamais la police payante « Stay With Me » dans Git).
- **Fond de base de toutes les vidéos de la série : l'image `assets/fond-nuit-bleue.jpg`** (1080×1920), à copier dans `assets/` de chaque vidéo.
  - C'est la référence de l'utilisateur (`assets/fond-reference.jpg`) recolorée dans la DA Nuit bleue par `scripts/make-fond.py` : bleu nuit, grande lueur bleue en bas à droite, lueur rouge dans le coin haut gauche, quadrillage dans deux coins.
  - Ne pas la remplacer par un fond refait en CSS (`(ancienne tentative, non fournie)` est une ancienne tentative), et ne pas la changer d'une vidéo à l'autre.
  - Mouvements autorisés : légère poussée de caméra et dérive lente de l'image ; flou quand la caméra zoome sur un texte.
  - Contraste : le mot-clé passe en blanc sur un bloc rouge, le texte normal est blanc avec une ombre.
- **Barre de progression en haut, du début à la fin** (`y ≈ 70–110 px`), découpée en chapitres. Le chapitre en cours est en rouge, les chapitres finis en blanc, ceux à venir en gris, et le nom du chapitre en cours est écrit dessous. Elle avance avec la voix.
- **Le personnage au premier plan** : c'est lui qui explique. Il est détouré, dans le tiers bas de l'écran. À chaque phrase, il prend la pose qui va avec ce qu'il dit (il montre, compte, réfléchit, prévient). Il respire (léger mouvement de haut en bas) et se déplace parfois de gauche à droite pour laisser la place à un schéma.
- **Illustrations pleine page** : seulement si elles collent exactement à la phrase dite. Sinon, quadrillage + personnage + motion design. Une image qui ne colle pas est pire que pas d'image.

## 4. Le mouvement (inspiration : la chaîne YouTube Fern)

- **Textes en mouvement** : la phrase entière arrive d'un coup, passant du flou au net avec une légère montée ou un léger zoom (0,3 à 0,5 s, sans rebond). Ensuite elle dérive lentement avec la caméra. Jamais de mots qui arrivent un par un avec la ponctuation en avance.
- **Mot-clé** : un seul bloc rouge qui balaie le mot (ou le groupe de mots) au moment où la voix le dit, puis le texte passe en blanc.
- **Caméra** : poussée lente permanente ; un zoom franc sur l'information importante (chiffre, mot-clé, schéma) avec flou de profondeur sur tout le reste.
- **Infographies** : barres qui se remplissent, compteurs qui défilent ($ et Ar), étapes numérotées qui se cochent, flèches qui relient (client → boutique → fournisseur), cartes qui se retournent, emoji iPhone qui apparaissent.
- **Transitions entre parties** : fondu doux ou poussée de caméra. **Une seule transition marquée par vidéo au maximum.** Jamais de flash blanc répété, jamais de reflet de lumière blanche qui traverse l'image, pas de coup de zoom sur chaque mot-clé.
- **Sons** : effets courts qui suivent l'action (pop, tick, ding, coins, error) via `scripts/make-sfx.py`. Pas de musique de fond sauf demande.

### Personnages dessinés en code (test validé : `templates/test-style.html`)

- Le personnage est en SVG, dans le même style que les illustrations : peau brune, barbe et cheveux ondulés noirs, chemise bleu nuit, liseré de lumière cyan à gauche et rouge à droite (`filter #rim`). Les autres personnages (clients…) suivent les mêmes règles.
- **Il est toujours net et au premier plan.** Le fond est flou (`blur 14px`) avec un bokeh : ronds lumineux rouges et bleus qui flottent doucement. Le bokeh et les lumières d'ambiance restent derrière les personnages et ne passent jamais devant ni sur eux ; on laisse la zone du personnage dégagée.
- **Mouvements fluides, jamais saccadés** : respiration (`sine.inOut`), tête qui oscille de ±2°, bouche calculée en continu (courbe sinus avec montée et descente, pas de battements au hasard), clignements, gestes lents (0,8 à 0,9 s). Main ouverte paume vers le haut pour expliquer.
- Mise au point : quand un 2e personnage parle, la caméra glisse vers lui et le premier se floute légèrement (3 px maximum).

### Vocabulaire validé par les références de l'utilisateur (Pinterest, motiondesigners.2d)

Gabarit : `templates/test-anim.html` (test de 30 s sur la voix « LLC expliquée »). Partir de ce fichier pour toute nouvelle vidéo.

- **Intro cinéma** : fond assombri et HUD discret (règle graduée à droite, coins, petites étiquettes en capitales, fines lignes cyan). Les mots flottent en 3D à des profondeurs différentes (CSS `perspective` + `z` GSAP). La caméra avance au milieu d'eux puis les traverse, et le mot-clé géant arrive avec une traînée de lumière rouge horizontale.
- **Rond** : l'illustration du personnage apparaît dans un cercle (`clip-path: circle`). Des bulles de conversation (question, « • • • ») apparaissent autour, puis le cercle s'ouvre en plein écran.
- **Trait de lumière** : une courbe rouge lumineuse se dessine sur l'écran (SVG `stroke-dashoffset` + halo).
- **Mot fort** : en italique (Instrument Serif), rouge, plus grand que le reste de la phrase.
- **Information animée** : les mots se déplient (par exemple L·L·C → Limited / Liability / Company → traduction). Schémas en perspective qui tournent lentement (cartes, mur lumineux, éléments qui tombent ou rebondissent), tampons, coches.
- **Personnage** : les illustrations de l'utilisateur (DA Nuit bleue) en plein écran avec poussée de caméra ; son visage dans un médaillon pour les schémas.
- **Sous-titres courts** : 2 à 3 mots, gras, au tiers bas, coupés quand un grand texte dit déjà la même chose.
- **Une seule transition marquée** : une lueur rouge de lentille. Tout le reste en fondu, flou ou ouverture du cercle.

## 5. Les images à générer

**D'abord tout en HTML/CSS/SVG.** Personnage, objets et schémas sont dessinés en code dans la DA (formes plates, lumière cyan d'un côté et rouge de l'autre). L'utilisateur vérifie la vidéo. Si le rendu lui convient, on ne lui demande aucune image. Seulement s'il refuse, lui donner les prompts ci-dessous pour qu'il génère les images lui-même.


Bloc commun à copier à la fin de chaque prompt :

- PERSONNAGE : `the same Malagasy man in his early 30s, short dark wavy hair, full dark beard, dark navy collared shirt`
- STYLE : `flat vector illustration, minimalist editorial style, cinematic two-tone rim lighting: cool cyan-blue light on one side, intense red glow (#E8242B) on the other side, smooth gradients, clean geometric shapes, no outlines, subtle grain, high contrast, vertical 9:16, no text, no letters, no logos --ar 9:16 --style raw`
- DÉTOURAGE (poses) : `waist-up, facing the viewer, centered in the lower two thirds of the frame, isolated on a plain solid flat chroma-key green background (#00FF00), no gradient on the background, no floor, no shadow on the background`
- NÉGATIF : `text, letters, words, watermark, logo, photorealistic, 3D render, extra fingers, cluttered background, bright daylight, green clothes`

Les poses sont réutilisables d'une vidéo à l'autre : les ranger dans `assets/perso/` (partagé) et ne générer que les poses manquantes. Détourage du vert : PIL/numpy (distance au vert, contour adouci de 2 px, suppression du reflet vert), puis vérification sur fond rouge et fond blanc.

## 6. Montage technique

- Une page HTML par vidéo (`video-XXX/index.html`), GSAP, 1080×1920, filmée image par image : `node scripts/render.js --w 1080 --h 1920 --fps 60 --workers 4 --out <fichier>.mp4` (`NODE_PATH` = le dossier `node_modules` où Puppeteer est installé, chemin absolu du script).
- Voix : faster-whisper (medium) puis `python3 scripts/align.py final` → `words-final.js` (window.WORDS, VOICE_END). Repérer les mots avec `at(mot, depuis)` en se méfiant des homonymes (« enregistré » / « Enregistre »).
- Pièges connus :
  - `window.__seek = (t) => { tl.seek(t, false); };` ne doit rien renvoyer ;
  - visibilité par `tl.set(el, {autoAlpha})`, jamais seulement des fromVars ;
  - positions de timeline ≥ 0,02 ;
  - animer `scaleX` plutôt qu'une largeur en % ;
  - un élément qui doit garder sa taille ne va pas dans un calque zoomé.
- **Toujours** des images de contrôle (`--stills t1,t2,…`, planche dans `renders/stills/planche.jpg`) avant le rendu complet. Sur chaque image, vérifier que ce qu'on voit correspond à ce que dit la voix, que rien n'est coupé ni superposé, et que le texte reste lisible.
- Vidéo trop lourde pour l'envoi : copie allégée (`ffmpeg -crf 22`), original à part.
- Voix, effets sonores et rendus ne vont pas dans Git (`.gitignore`).

## 7. Corrections

- Chaque correction donne une nouvelle version (v2, v3…) enregistrée à côté de l'ancienne. Ne jamais écraser l'ancienne.
- Ne changer que ce qui est demandé. Signaler s'il reste un défaut vu en vérifiant.
- Toujours sans titre, description ni miniature (voir §1).
