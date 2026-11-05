---
name: video-papier
description: Fabriquer une vidéo explicative verticale (TikTok, Reels, Shorts) dans la DA « papier » : fond crème à points, encre noire, accent rouge, cartes à ombre en trame, et un présentateur dessiné en SVG qui parle, change d'expression et de pose, avec une tenue différente à chaque vidéo. Couvre le script et le texte ElevenLabs, le calage de la voix, l'animation GSAP, les images de contrôle, le rendu MP4 en boucle parfaite, les miniatures et le pack de publication donné seulement après « c'est bon ». Utiliser dès que l'utilisateur demande une vidéo TikTok / Reels / Shorts explicative, d'info ou de mindset, « une vidéo avec le présentateur » ou « dans le style papier ».
---

# Vidéo explicative « papier + présentateur »

> **Fichiers fournis**
> - `template/` : le modèle de départ. Il contient `index.html` (page GSAP avec le présentateur et une démo de 17 s), `assets/` (polices, GSAP, 23 effets sonores), `scripts/` (voix, rendu, mixage, miniatures) et les deux pages de miniature.
> - `docs/presentateur.md` et `docs/presentateur.jpg` : les expressions, poses, tenues et options du présentateur.
> - `docs/recettes.md` : les scènes toutes faites, les idées d'intro et de miniature, le pack de publication.
>
> **Logiciels :**
> - Google Chrome ;
> - Node.js avec `puppeteer-core` (`npm i puppeteer-core`, puis `NODE_PATH` = le dossier `node_modules`) ;
> - FFmpeg ;
> - Python 3 avec `numpy` et `faster-whisper`.

## 1. Règles de travail

- Réponses en français simple, en listes courtes. Tutoyer et ne pas flatter. Dire franchement quand une idée ne marche pas.
- **Pendant la fabrication et les corrections**, ne jamais donner de titre, de description, de hashtags ni de miniature. Montrer seulement les images de contrôle, la vidéo et ce qui a changé.
- **Préparer les miniatures et le pack de publication en silence** pendant le montage.
- **Quand l'utilisateur écrit « c'est bon »**, livrer tout d'un coup, sans poser de question :
  - la vidéo ;
  - la miniature TikTok (1080×1920) et la miniature YouTube (1280×720) ;
  - le pack TikTok et le pack YouTube Shorts (format dans `docs/recettes.md`) ;
  - un fichier `publication.md`.
- Chaque correction crée une nouvelle version (v2, v3…). Ne jamais écraser une version livrée.
- Ne jamais publier soi-même sur un réseau social.

## 2. Le script

- **Longueur :** 200 à 240 mots, soit 1 min 15 à 1 min 25.
- **Style :**
  - phrases courtes, une idée par phrase ;
  - du ressenti vécu : la frustration, puis le soulagement ;
  - du rythme : questions, phrases d'un mot, pauses.
- **Accroche :** la première seconde doit arrêter le pouce, par exemple « Pose tes doigts. Arrête de scroller. » ou une phrase choc sur le sujet.
- **Structure type :**
  1. l'accroche ;
  2. une situation vécue ;
  3. le vrai problème ;
  4. 3 actions concrètes ;
  5. la réassurance (« tu vas craquer, c'est normal ») ;
  6. l'appel à l'action.
- **Pas de promesse absolue.** Pas de « garanti » ni de « riche en 30 jours » : dire « tu peux ».
- **Appel à l'action :**
  - vidéo d'info : « Enregistre la vidéo » et « Envoie-la à quelqu'un qui… » ;
  - vidéo de vente : l'appel que l'utilisateur choisit.
- **Boucle parfaite :** la dernière phrase doit s'enchaîner sur la première (« …rappelle-toi ma première phrase » → « Pose tes doigts. »).
- **Livrer deux textes, sans long commentaire :**
  - `script-final-v1.txt` : le texte propre ;
  - `script-tags-v1.txt` : le texte pour ElevenLabs. Mettre une balise d'intention en début de paragraphe (`[serious]`, `[calm]`, `[confident]`, `[thoughtful]`, `[excited]`) et `[short pause]` pour les silences.
- **Prononciation dans le texte ElevenLabs :**
  - écrire les mots comme ils doivent sonner : « Ariary » se prononce mieux écrit « ariar », sans tirets ;
  - écrire les nombres en lettres.
- Les faits à vérifier vont dans `notes.md`. Ne jamais inventer de source.

## 3. Mise en place d'une vidéo

1. Copier `template/` dans un nouveau dossier `video-<sujet>/`.
2. L'utilisateur génère la voix (par exemple ElevenLabs) et donne le MP3.
   - Le copier en `assets/audio/voix-final.mp3`.
   - Mettre le texte propre, sans balises, dans `assets/audio/script-final.txt`.
3. Caler les mots sur la voix (depuis le dossier de la vidéo) :
   - `python scripts/transcribe.py final base "mots, rares, du, script"`
   - `python scripts/align.py final`
   - `align.py` affiche `index|temps|mot`. Si un mot a été mal reconnu (un nombre, un mot anglais), corriger son `start` dans `assets/audio/words-final.js`.
4. Ouvrir `index.html` dans Chrome : un clic lance la voix et l'animation.
5. Supprimer la démo : le HTML de `#ui`, la CSS et la timeline marquées « DÉMO ». Garder le reste.
   - La durée se règle seule : `DURATION = VOICE_END + 0,3 s`.

## 4. La direction artistique (identique d'une vidéo à l'autre)

- **Couleurs :**
  - papier `#F1EEE8` avec des points ;
  - encre `#141414`, gris `#6B675F` ;
  - rouge `#E0402A` (accent unique) ;
  - jaune `#F6C21C` et bleu `#7CC8F2` en petites touches ;
  - cartes blanches.
- **Typo :**
  - Inter 800 pour les titres (`.st h2`, 88 px) ;
  - Instrument Serif italique rouge (`.it`) pour le mot fort ;
  - police mono grise pour les étiquettes `// comme ça` (`.tag`).
- **Briques CSS :**
  - `.ink` : carte blanche, contour noir, ombre en trame de points décalée ;
  - `.pill` : pastille avec une pastille ronde `.pi` et une coche `.ck` ;
  - `.k` : bloc rouge qui balaie le mot, qui passe alors en blanc ;
  - `.strike` : rature rouge ;
  - `.stamp` : tampon ;
  - `.cens` : barre de censure « BIP ».
- **Icônes :** `<svg><use href="#i-nom"/></svg>`. La liste est dans `docs/recettes.md`. Dessiner les nouvelles dans le même style : trait 6 à 8 px, bouts ronds, aplats jaune, rouge ou bleu.
- **Zones de l'écran :**
  - format 1080×1920 ;
  - le contenu tient entre **y 300 et y 1250**, car la tête du présentateur commence vers y 1286 ;
  - l'étiquette du sujet (`#hud`) est en haut à gauche.
- **Mouvements :**
  - les éléments arrivent du flou au net en 0,3 à 0,5 s ;
  - les pastilles rebondissent légèrement ;
  - un « coup de caméra » (`#cam` à 1,04) seulement sur les moments forts ;
  - une seule transition marquée par vidéo.

## 5. Le présentateur

- Tout est dans `docs/presentateur.md`, avec la planche `docs/presentateur.jpg`.
- **À chaque phrase, un `ACT(t, expression, pose)`** :
  - expressions : `neutre`, `parle`, `insiste`, `sceptique`, `surpris`, `content`, `inquiet`, `panique`, `malin`, `question` ;
  - poses : `pointe`, `salue`, `croise`.
- **Calculé tout seul à partir de la voix :** la bouche, la respiration, le hochement de tête et les clignements.
- **Une tenue différente à chaque vidéo** : `data-tenue`, la couleur `--sweat` et un accessoire. Noter dans `notes.md` ce qui a déjà été porté.

## 6. L'animation

- **Caler chaque animation sur un mot de la voix.**
  - `S("phrase exacte", k, depuis)` renvoie le début du mot n° k de la phrase. Les accents et la ponctuation sont ignorés : « c'est » s'écrit `cest`.
  - Pour un mot qui revient plusieurs fois, partir d'un index : `find("…")`.
  - Déclencher 0,05 à 0,1 s avant le mot.
- **Ce qu'on voit = ce qu'on entend.** 1 à 3 éléments par phrase, jamais plus. Faire sortir l'ancienne scène (`OUT`) avant d'ouvrir la suivante.
- **Outils** (détail et exemples dans `docs/recettes.md`) :

  | Outil | Ce qu'il fait |
  |---|---|
  | `IN(sel, t, {x, y, s, b, d})` | entrée du flou au net |
  | `OUT(sel, t, d)` | sortie vers le haut avec flou |
  | `POP(sel, t)` | entrée avec rebond |
  | `XPOP(sel, t)` | coche ou tampon qui tourne en entrant |
  | `HL(id, t)` | balayage rouge d'un mot `.k` |
  | `STRIKE(id, t)` | rature |
  | `DRAW(sel, t, d)` | tracé d'un chemin SVG (`pathLength="1"`) |
  | `SWAP(id, html, t)` | changement de texte avec un rebond |
  | `ROLL(id, de, à, t, d)` | compteur qui défile |
  | `PULSE(sel, t, s)` | petit battement |
  | `SFX(nom, t, gain)` | effet sonore |
  | `ACT(t, expr, pose)` | jeu du présentateur |

- **Sons fournis :** `pop`, `tick`, `ding0`, `ding1`, `ding2`, `card`, `whip`, `swell`, `thud`, `boom`, `stamp`, `strike`, `coins`, `notif`, `glass`, `shimmer`, `reveal`, `bloom`, `lock`, `keys`, `error`, `glitch`, `bip`.
  - Gain de -18 à -26 dB.
  - Pas de musique, sauf si l'utilisateur la demande (`assets/music/`).
- **Un fil rouge visuel** qui vit toute la vidéo : une jauge, une batterie, un compteur, un calendrier… Il se calcule dans `life(t)`.
- **Changer l'intro à chaque vidéo** (idées dans `docs/recettes.md`).
- **Boucle parfaite :** la dernière image doit être identique à la première.
  - Même décor, mêmes éléments visibles, même expression, même pose, fil rouge à la même valeur.
  - Les mouvements continus utilisent `PER(période)` pour retomber juste à la fin.
  - Le papier dérive d'exactement une maille (36 px) sur toute la durée.

## 7. Contrôle et rendu

- **Toujours faire des images de contrôle avant le rendu complet :**
  - commande : `NODE_PATH=<node_modules> node scripts/render.js --stills 0.5,3,7.2,…` ;
  - résultat : `renders/stills/planche.jpg` ;
  - vérifier sur chaque image :
    - ce qu'on voit correspond à ce que dit la voix ;
    - rien n'est coupé, superposé ou caché sous la tête ;
    - le texte reste lisible en petit.
- **Vérifier la boucle :** prendre une image à `0` et une à `DURATION - 0.01`. Elles doivent être identiques.
- **Rendu :**
  - commande : `node scripts/render.js --out <sujet>-v1.mp4` ;
  - résultat : 1080×1920, 60 i/s, voix normalisée à -14 LUFS, effets mixés sous la voix ;
  - pour un test rapide sans son : `--mute --from 0 --to 10`.
- **Copie légère à envoyer :** `ffmpeg -i X.mp4 -c:v libx264 -crf 22 -preset slow -pix_fmt yuv420p -c:a copy -movflags +faststart X-envoi.mp4`
- **Pièges connus :**
  - `window.__seek` ne doit rien renvoyer et doit garder `Math.max(t, 0.001)`. Sinon, l'image 0 ignore les réglages posés à 0 et la boucle saute.
  - Gérer la visibilité avec `tl.set(…, {autoAlpha})` (c'est ce que font les outils). Ne jamais compter sur un seul `from`.
  - Les positions dans la timeline doivent être ≥ 0,02 s.
  - `.u` (caché, en position absolue) ne va jamais sur un enfant d'un bloc flex.
  - `.pill` et `.ctr` sont centrés par `xPercent: -50`. Leur `left` est donc leur centre.
  - Sous Windows, ne pas laisser le terminal ouvert dans `renders/stills` : le script ne peut plus vider le dossier.
  - Certaines versions de FFmpeg refusent `-vsync` : utiliser `-fps_mode passthrough`.

## 8. Les miniatures

- **Un concept nouveau à chaque vidéo, lié au sujet.** Jamais deux fois la même mise en page (idées dans `docs/recettes.md`).
- **Contenu :**
  - un titre de 3 à 6 mots, lisible en tout petit ;
  - un mot en rouge ;
  - le présentateur avec une expression forte, retourné en miroir ou non.
- **Fabrication :**
  1. Copier `thumb-tiktok.html` et `thumb-youtube.html` en `thumb-v1-tiktok.html` et `thumb-v1-youtube.html`, puis changer le concept.
  2. Lancer `node scripts/thumbs-perso.js <expression> <pose> -v1`. Le script détoure le présentateur (`assets/thumb-perso.png`) et produit `renders/miniature-v1-tiktok.png` et `renders/miniature-v1-youtube.png`.

## 9. Après « c'est bon »

- Livrer la vidéo, les deux miniatures et le pack, dans le format de `docs/recettes.md`.
- Enregistrer le tout dans `publication.md`.
- Noter dans `notes.md` ce qu'il ne faudra pas refaire à la prochaine vidéo : l'intro, la tenue, le concept de miniature.
