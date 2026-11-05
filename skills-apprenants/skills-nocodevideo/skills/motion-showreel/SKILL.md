---
name: motion-showreel
description: Créer un court film de motion design (showreel, intro, pub de 10 à 30 s) entièrement en code, piloté par le temps, où chaque plan se transforme en le suivant sans coupe ni fondu. Rythme calé sur un tempo (ex. 120 BPM, un événement par temps), bande-son écrite avec Web Audio, flou de mouvement par sous-images. Utiliser quand l'utilisateur demande un showreel, une intro animée, une boucle ou « une vidéo qui prouve un niveau de motion designer ».
---

# Showreel de motion design en code

Exemple complet fourni : `template/` (« Un point devient une entreprise », 15 s, 1920×1080, 120 BPM) avec `index.html`, `render.js` et `STORYBOARD.md`.

## Méthode

1. **Concept en une ligne**, puis un storyboard temps par temps (1 temps = 60/BPM s). Mesure 1 = accroche, une technique par mesure (typo animée, morphing de formes, passage 2D → 3D, données / interface), dernière mesure pleine = moment le plus fort, dernière demi-mesure = titre de fin. La dernière image = la première (boucle).
2. **Chaque plan naît du précédent** : forme, texte ou couleur se transforme. Un échange d'éléments n'est permis que s'ils sont identiques à l'écran au moment de l'échange.
3. **Contraintes visuelles** : une police (Inter, Geist ou une display Google Fonts), 3 couleurs au plus + noir et blanc, une seule langue de caméra (ex. poussée lente + léger roulis périodiques sur toute la durée). Interdits : particules, lueurs, reflets d'objectif, secousses, séparation RVB, fondus enchaînés, dégradés génériques, courbes à rebond, pauses de plus d'une demi-seconde.

## Construction

- **Un seul fichier HTML.** Tout style est calculé à partir du temps dans `window.seek(t)` : aucune animation CSS, aucun minuteur, aucun état gardé d'une image à l'autre.
- **Courbes écrites comme fonctions du temps** : `expOut`, `expIn`, `expInOut`, ressort presque critique (amortissement 0,82, dépassement d'environ 1 %).
- **Flou de mouvement** : vitesse = dérivée numérique de la fonction de position ; flou directionnel SVG (`feGaussianBlur stdDeviation="x y"`) proportionnel à la vitesse.
- **Mesures au chargement** (largeurs de mots, forme exacte d'un glyphe via canvas, ligne de base) pour que les échanges soient invisibles.
- **Bande-son** : `OfflineAudioContext` (kick sur chaque temps, charleston, basse, coup à chaque changement de scène, montée avant le moment fort), encodée en WAV dans la page. Ne pas utiliser `DynamicsCompressor` (gain automatique qui sature) ; viser des crêtes vers -1 dB.
- **Rendu** (`node render.js`) : Playwright à 60 i/s × 3 sous-images, fondues avec `ffmpeg tmix=frames=3` puis `select` une image sur trois, son ajouté.

## Vérifications avant le rendu complet

- `node render.js --stills` : une image par temps → planche. Corriger tout ce qui est encombré, décalé du temps, superposé, coupé par le bord ou difficile à lire.
- `--at t1,t2,…` : vérifier chaque raccord juste avant et juste après (ex. 3.99 / 4.01).
- Après le rendu : comparer la première et la dernière image (boucle) et mesurer le son (`volumedetect`).
