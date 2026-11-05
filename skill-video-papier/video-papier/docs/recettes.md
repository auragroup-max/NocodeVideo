# Recettes : scènes, intros, miniatures, pack de publication

Chaque recette est en deux parties :
- le HTML va dans `<div id="ui">` ;
- le JS va dans la timeline, après les repères de la voix.

Tout élément qui apparaît porte la classe `.u` : il est caché au départ.

## Scènes toutes faites

**Titre avec un mot clé balayé en rouge**
```html
<div class="u st" id="t1" style="top:420px"><span class="tag">// le vrai problème</span>
  <h2>Ce n'est pas un <span class="k" id="kHab">manque<i></i></span><br>de <span class="it">temps.</span></h2></div>
```
```js
IN("#t1", S("ce nest pas") - 0.05); HL("kHab", S("manque")); SFX("pop", S("manque"), -20);
OUT("#t1", S("phrase suivante") - 0.3);
```

**Carte qui rebondit, avec une icône et une étiquette**
```html
<div class="u ink ctr" id="shop" style="left:540px;top:360px;width:440px;height:420px;border-radius:40px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">
  <svg style="width:200px;height:200px"><use href="#i-shop"/></svg><b style="font:800 46px Inter">ta boutique</b><span class="tag">// ouverte 24 h/24</span></div>
```
```js
POP("#shop", S("boutique") - 0.05); SFX("card", S("boutique"), -20);
```

**Liste de pastilles qui se cochent**
```html
<div class="u pill ink" id="r1" style="left:540px;top:760px"><div class="pi">1</div>téléphone hors de la chambre<svg class="ck"><use href="#i-check"/></svg></div>
```
```js
IN("#r1", S("un le soir") - 0.1, { x: -60, y: 0 });
XPOP("#r1 .ck", S("chambre") + 0.2); SFX("ding0", S("chambre") + 0.2, -20);   // ding1, ding2 pour les suivantes
```

**Compteur qui défile**
```html
<div class="u ink ctr" id="cnt" style="left:540px;top:500px;padding:30px 50px;border-radius:30px;font:800 120px Inter"><span id="cntN">0</span> Ar</div>
```
```js
POP("#cnt", S("gagner") - 0.1); ROLL("cntN", 0, 500000, S("gagner"), 1.2); SFX("coins", S("gagner") + 0.4, -24);
// pour les espaces des milliers, remplacer le onUpdate de ROLL par toLocaleString("fr-FR")
```

**Rature** (fausse promesse, mauvaise idée)
```html
<div class="u pill ink" id="promise" style="left:540px;top:640px"><div class="pi"><svg><use href="#i-spark"/></svg></div><span class="strike">« riche en 30 jours »<i id="prS"></i></span></div>
```
```js
POP("#promise", S("promesse") - 0.2); STRIKE("prS", S("promesse") + 0.3); SFX("strike", S("promesse") + 0.3, -20);
```

**Trait qui se dessine** (flèche, cercle autour d'un mot, câble)
```html
<svg class="u" id="arr" viewBox="0 0 200 120" style="left:440px;top:700px;width:200px"><path id="arrP" pathLength="1" d="M10 60 C 60 10 140 10 190 60" fill="none" stroke="#141414" stroke-width="8" stroke-linecap="round"/></svg>
```
```js
show("#arr", S("vers") - 0.1); DRAW("#arrP", S("vers"), 0.5);
```

**Mot censuré « BIP »** (un mot qui ferait baisser la portée de la vidéo s'il était écrit)
```html
<h2>Arrête de te <span class="cens" id="cens"><span>mot</span><b><em>✱</em>BIP<em>✱</em></b></span></h2>
```
```js
SFX("bip", S("mot") - 0.02, -18);
tl.fromTo("#cens b", { scale: 1 }, { keyframes: [{ scale: 1.12, rotation: -2, duration: 0.08 }, { scale: 0.96, rotation: 2, duration: 0.08 }, { scale: 1, rotation: 0, duration: 0.1 }], immediateRender: false }, S("mot"));
```

**Coup de caméra** (seulement sur 2 ou 3 moments forts)
```js
tl.fromTo("#cam", { scale: 1 }, { scale: 1.04, duration: 0.25, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, S("mot fort"));
```

**Changer un texte en direct**
```js
SWAP("heure", "02:47", S("deux heures")); SFX("tick", S("deux heures"), -22);
```

**Fil rouge calculé dans `life(t)`** (jauge, batterie…)
```js
// avant life() : la valeur à chaque instant, identique au début et à la fin pour la boucle
const smooth = (u) => (u <= 0 ? 0 : u >= 1 ? 1 : u * u * (3 - 2 * u)), lerp = (a, b, u) => a + (b - a) * smooth(u);
const jauge = (t) => { let v = 0.8;
  if (t >= tProbleme) v = lerp(0.8, 0.1, (t - tProbleme) / 1.5);
  if (t >= tSolution) v = lerp(0.1, 1, (t - tSolution) / 0.8);
  if (t >= tFin) v = lerp(1, 0.8, (t - tFin) / 1.2);
  return v; };
// dans life(t) :
$("jaugeFill").style.transform = `scaleX(${jauge(t).toFixed(3)})`;
```

**Fin de boucle**
```js
OUT("#derniereScene", S("derniere phrase") - 0.2);           // tout ce qui est visible à la fin…
ACT(S("derniere phrase") - 0.05, "insiste", "pointe");      // …et le présentateur reviennent à l'état de la première image
```

## Icônes disponibles (`<svg><use href="#i-…"/></svg>`)

check, x, person, shop, phone, star, plane, live, page, globe, browser, shirt, shoe, lip, eye, menu, call, search, pin, plate, chat, spark, heart, play, box, clock, book, bolt, glass, door, moon, up, idea, castle, ear.

## Intros : en changer à chaque vidéo

Intros déjà faites par l'auteur du modèle. Ne pas les refaire telles quelles : s'en inspirer.
- **Main qui s'abat :** une main levée s'abat sur « doigts » avec un choc et des traits d'impact. Le mot qui suit est caché sous une barre « BIP ».
- **Fil de téléphone :** un fil défile sous un pouce, puis s'arrête net sur un gros bouton pause rouge.
- **Cartes retournées :** 5 cartes face cachée se retournent, puis deviennent la barre de progression en haut.
- **Éditeur de code :** un éditeur écrit la vidéo ligne par ligne, puis la page apparaît.
- **Ticket de caisse :** une question imprimée en grand, puis une caisse qui sort un ticket.

Autres pistes :
- une notification qui tombe ;
- un tampon qui claque sur le titre ;
- un chronomètre qui démarre ;
- une page de cahier qu'on corrige ;
- un objet du sujet qui tombe et rebondit.

## Miniatures : un concept nouveau à chaque fois

Concepts déjà faits par l'auteur du modèle :
- page de cahier d'écolier corrigée « très bien ! » ;
- clap de cinéma sur fond de code ;
- éventail de 5 cartes, dont la 5e est cachée et tamponnée « RARE » ;
- écran verrouillé à 23 h 47 avec la notification « Temps d'écran : 5 h par jour » ;
- titre censuré par une grosse barre « ✱ BIP ✱ » avec un tampon « SANS FILTRE ».

Règles :
- un titre de 3 à 6 mots, lisible en tout petit ;
- un seul mot en rouge ;
- le présentateur dans une expression forte, différente de la miniature précédente ;
- toujours la DA papier.

## Pack de publication (seulement après « c'est bon »)

**TikTok**
- Légende : 2 ou 3 phrases courtes. L'idée clé, puis l'appel (« Enregistre-la et envoie-la à… »).
- Une question pour les commentaires, facile à répondre (« 1, 2 ou 3 ? 👇 »).
- 3 à 5 hashtags.

**YouTube Shorts**
- Titre : moins de 60 caractères, l'accroche de la vidéo.
- Description : le résumé (étapes numérotées si la vidéo en donne), puis l'appel à l'action.
- 3 à 5 hashtags, dont `#shorts`.

**Bon à savoir :** un mot sensible caché par « BIP » à l'écran ne doit pas apparaître non plus dans la légende ni dans le titre.
