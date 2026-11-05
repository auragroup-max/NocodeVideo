# DA « Nuit bleue · Motion » (série dropshipping)

Référence : test 10 s v2 (`video-drop-02/test-style.html`) + test 30 s (`video-drop-01/test-anim.html`). Méthode complète : `.claude/skills/video-explicative/SKILL.md`.

## 1. Voix off

- **Ton : expert sérieux.** Posé, crédible, vouvoiement, phrases courtes. On explique comme un consultant, on ne vend pas.
- Pas de mots de vente forcée (« refusé ! », « bloqué ! », « ta clé », « solution parfaite »). Pas de promesse absolue.
- Rythme : environ 150 mots par minute, une pause courte avant chaque idée forte.
- Voix ElevenLabs : Isac (réglages vus dans les noms de fichiers : vitesse 1,03, stabilité 50, similarité 100). Balises utilisées : `[calm]`, `[serious]`, `[thoughtful]`, `[confident]`, `[short pause]`.
- Durée : environ 1 min à 1 min 20. Pas de fiscalité ni de détails de coûts sauf demande.

## 2. Couleurs

| Rôle | Couleur |
|---|---|
| Fond (nuit) | `#060B19` → `#1B2A4A` (image `shared/fond-nuit-bleue.jpg`) |
| Accent principal (mots-clés, alertes) | rouge `#FF2D2D` / `#E8242B` |
| Lumière froide, validation | cyan `#39B6EE`, liseré `#6FD3FF` |
| Texte | blanc `#FFFFFF`, secondaire blanc à 45-70 % |
| Panneaux (pastilles, cartes) | `rgba(10,18,38,.78)` + flou 14 px + bordure cyan 2 px |
| Argent (pièces seulement) | or `#FFC94D` / `#D68A12` |
| Peau du personnage | `#8A5536` (ombre `#5A3220`) |
| Cheveux et barbe | `#17110E` |
| Chemise | bleu nuit `#1B2847` (ombre `#121B33`, col `#26375F`) |

Règle de lumière : **toujours cyan à gauche, rouge à droite** (personnages, objets, fond).

## 3. Typographie

- **Inter** (dans `assets/fonts`) :
  - grandes phrases : 700, 86-92 px, interlettrage -0,045 em, ombre douce ;
  - pastilles et bulles : 800, 44-46 px ;
  - étiquettes et chapitres : 700, 24-26 px, majuscules, interlettrage +0,14 à 0,22 em.
- **Instrument Serif italique** : le mot fort d'une phrase, en rouge, 1,45 fois plus grand (ex. « tout. », « limitée »).
- Mot-clé : texte blanc sur un bloc rouge qui le balaie de gauche à droite au moment où la voix le dit.
- Jamais la police payante « Stay With Me » dans Git.

## 4. Style graphique

- **Illustration vectorielle plate**, formes simples, pas de contour noir, ombres en aplat, liseré lumineux cyan et rouge sur les bords.
- **Personnage principal** : homme malgache, trentaine, cheveux noirs ondulés, barbe pleine, chemise bleu nuit. Toujours net et au premier plan, dans le tiers bas de l'écran. Les autres personnages suivent le même style.
- **Fond** : `fond-nuit-bleue.jpg` flouté (14 px, luminosité 80 %) + **bokeh** (ronds lumineux rouges et bleus, flous, qui flottent). Le bokeh reste derrière les personnages et ne touche jamais leur zone.
- **Interface** : pastilles en verre sombre, bulles de conversation, cartes en perspective, coches cyan, croix rouges, tampons, compteurs ($ et Ar).
- **HUD discret (intros)** : règle graduée à droite, coins d'angle, petites étiquettes en majuscules, fines lignes cyan.
- **Barre de progression** en haut (y ≈ 74 px), découpée en chapitres, du début à la fin : rouge pour la partie en cours, gris pour les suivantes, nom du chapitre dessous.

## 5. Mise en page (1080 × 1920)

- Marges : 70-90 px sur les côtés.
- Barre de progression : 74-130 px.
- Zone des grandes phrases : 230-700 px.
- Zone personnage : 900-1920 px.
- Sous-titres courts (2-3 mots) : vers 1640 px, seulement quand aucun grand texte ne dit la même chose.

## 6. Animation (HTML, CSS, GSAP)

- Courbes : `sine.inOut` pour la vie (respiration, flottement), `power3.out` pour les entrées, `power2.in` pour les sorties, `back.out` seulement pour les petites pastilles.
- Texte : la phrase entière arrive en 0,5 s (flou 14 px → net, +40 px → 0, échelle 0,94 → 1), puis dérive lentement vers le haut et sort en flou en 0,35 s.
- Personnage : respiration de 1,6 s, tête qui oscille de ±2°, bouche calculée en continu, clignements, gestes lents de 0,8 à 0,9 s. Jamais saccadé.
- Caméra : poussée lente et parallaxe (le fond bouge moins que le bokeh, qui bouge moins que les personnages). Glissement et mise au point quand un 2e personnage parle (le 1er se floute de 3 px).
- Intro : mots en 3D à différentes profondeurs, la caméra les traverse ; ou le personnage dans un rond qui s'ouvre en plein écran.
- **Une seule transition marquée par vidéo** (lueur rouge de lentille). Ailleurs : fondu, flou ou ouverture du rond. Pas de flash blanc répété, pas de reflet blanc qui traverse l'image, pas de coup de zoom sur chaque mot.

## 7. Son

- Pas de musique de fond sauf demande.
- Effets courts synchronisés : `syn-pop` (texte), `syn-tick` (mot-clé), `syn-coins` (argent), `syn-ding0/1/2` (validation), `syn-error` (problème), `syn-stamp` (tampon), `syn-whip` (mouvement de caméra), `syn-swell` (ouverture), `syn-glass` (mur ou verre). Volume -14 à -28 dB.
