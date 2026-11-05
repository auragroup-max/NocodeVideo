# Le présentateur

Planche de référence : `presentateur.jpg` (expressions, poses, tenues, options).

Le présentateur est un SVG dans `index.html` (`<svg id="perso" …>`), dans le style de la DA :
- trait noir ;
- ombre en trame de points ;
- lunettes de soleil qui glissent sur le nez quand l'émotion monte.

Il est piloté par des attributs `data-…`.

## Expressions : `data-expr`

| Valeur | Quand l'utiliser |
|---|---|
| `neutre` | écoute, transition |
| `parle` | explication normale (le plus fréquent) |
| `insiste` | ordre, accroche, chiffre important |
| `sceptique` | doute, « vraiment ? », fausse bonne idée |
| `surpris` | révélation, chiffre choc (rayons et gouttes) |
| `content` | solution, bonne nouvelle (étincelle et joues) |
| `inquiet` | problème, échec, fatigue (larme et sueur) |
| `panique` | catastrophe, urgence |
| `malin` | clin d'œil, astuce, « tu sais de quoi je parle » |
| `question` | question au public (point d'interrogation) |

## Poses : `data-pose`

- `pointe` : le doigt levé, pour expliquer ou insister.
- `salue` : la main ouverte, pour accueillir, dire une bonne nouvelle ou conclure.
- `croise` : les bras croisés, pour douter, écouter ou faire le malin.

## Le jeu d'acteur dans la timeline

```js
[[S("voici") - 0.05, "content", "salue"],
 [S("le probleme") - 0.05, "inquiet", "croise"],
 [S("trois regles") - 0.05, "insiste", "pointe"]].forEach(([t, e, p]) => ACT(t, e, p));
```

- Un `ACT` par phrase environ.
- Changer de pose seulement quand le sens change. Chaque changement fait un petit rebond.
- Le dernier `ACT` remet l'expression et la pose de la première image (boucle).
- **Calculé tout seul à chaque image dans `life(t)`, à partir de `WORDS` :**
  - la bouche suit les syllabes, en grand pour `insiste` et `panique` ;
  - la respiration ;
  - le hochement de tête ;
  - les clignements ;
  - le doigt et la main qui bougent un peu.

## Tenue et options (sur la balise `<svg id="perso">`)

| Attribut | Valeurs | Effet |
|---|---|---|
| `style="--sweat:#3D5A80"` | une couleur | couleur du haut |
| `data-tenue` | `sweat`, `polo`, `chemise` | capuche et cordons, col polo, ou chemise avec patte et stylo |
| `data-casque` | `oui` / `non` | casque audio autour du cou |
| `data-pin` | `oui` / `non` | pin's sur la poitrine |
| `data-bandeau` | `oui` / `non` | bandeau de sport rouge |
| `data-montre` | `oui` / `non` | montre au poignet du bras levé |
| `data-lunettes` | `oui` / `non` | lunettes de soleil |
| `data-barbe`, `data-moustache` | `oui` / `non` | barbe et moustache |
| `data-trame` | `oui` / `non` | ombre en trame de points |

**Changer de tenue à chaque vidéo.** Par exemple :
- sweat jaune + casque ;
- polo bleu + pin's ;
- chemise violette ;
- sweat bleu marine + montre ;
- sweat gris + bandeau rouge.

**Pour un nouvel accessoire :**
1. Ajouter un `<g class="mon-objet">` au bon endroit du SVG.
2. Ajouter son interrupteur dans le `<style>` du personnage, sur le modèle de `#perso[data-bandeau="non"] .bandeau { display: none; }`.

## Place à l'écran

- `gsap.set("#persoW", { x: 43, y: 236, scaleX: 0.8, scaleY: 0.8 })` place le présentateur en bas, la tête vers y 1286.
- Pour lui faire de la place, déplacer ou réduire `#persoW` avec la timeline. Mais en boucle parfaite, il doit revenir à sa place à la fin.
- Pour les miniatures, `scripts/thumbs-perso.js <expression> <pose> -v1` le photographie seul, sur fond transparent.
