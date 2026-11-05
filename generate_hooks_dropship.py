import json

with open('dropship-tiktok-results.json', 'r', encoding='utf-8') as f:
    videos = json.load(f)

md = []
md.append("# Analyse Tendances & Hooks TikTok · Niche Dropshipping 2026\n")
md.append("*Recherche via treg (`treg.tiktok.search.videos`), coût : $0.002 total (2 requêtes).*\n")
md.append("## 1. Données réelles TikTok extraites\n")
md.append("| # | Créateur | Vues | Likes | Angle / Sujet | Lien |")
md.append("|---|---|---|---|---|---|")

for i, v in enumerate(videos[:10]):
    desc_clean = v['desc'].split('#')[0].strip()
    if not desc_clean:
        desc_clean = v['desc'][:80]
    author_display = f"@{v['handle']}"
    md.append(f"| {i+1} | **{author_display}** | {v['views']:,} | {v['likes']:,} | {desc_clean[:75]}... | [Lien]({v['url']}) |")

md.append("\n---\n")
md.append("## 2. Ce qui cartonne le plus en ce moment sur TikTok\n")
md.append("""
1. **Le mythe du « Produit Miracle » vs les « 3 critères concrets » :**
   Les vidéos qui font le plus de vues (ex: @dailyfulfillsource 437k vues, @briac_ecom_ 188k vues) ne parlent plus de trouver un objet magique, mais d'une méthode de tri rapide (problème résolu, marge, effet visuel).
2. **Le ras-le-bol de la théorie et des formations chères :**
   Les contenus les plus partagés (ex: @studioecomstart 12.6k likes, 231k vues) démarrent par : *« Tu veux te lancer mais tu sais pas par où commencer ? »* et donnent 3 à 5 outils gratuits ou démarches sans bla-bla.
3. **Le piège de la livraison / fournisseur :**
   De plus en plus de vidéos soulignent que vendre sans maîtriser les délais ou les frais de livraison détruit le business avant la première vente.
""")

md.append("\n---\n")
md.append("## 3. Les 3 Hooks Dropshipping recommandés pour ta prochaine vidéo\n")
md.append("""
Basé sur le **Plan de contenus Madagascar** (`plan-contenus-dropshipping.md`) et les formats viraux actuels :

### Option 1 : Les 5 critères d'un produit qui se vend (Recommandé)
- **Accroche (0-3s) :** *« Ce produit, toi tu l'aurais acheté… mais personne d'autre. »*
- **Angle :** Pourquoi 90% des débutants choisissent un produit sur un coup de cœur au lieu de vérifier la marge, le transport et le problème qu'il résout.
- **Pourquoi ça marche :** Attaque directe d'un biais psychologique classique chez les débutants.

### Option 2 : Vendre avec TikTok sans payer de pub (Organique)
- **Accroche (0-3s) :** *« Ton meilleur vendeur ne te coûte rien : c'est une vidéo de 15 secondes. »*
- **Angle :** Inutile de brûler de l'argent en pub Facebook si tu ne sais pas faire une vidéo TikTok qui montre l'utilité du produit en 3 secondes.
- **Pourquoi ça marche :** Répond à la première peur des créateurs malgaches : le budget publicitaire.

### Option 3 : Le piège du fournisseur fantôme
- **Accroche (0-3s) :** *« Avant d'envoyer 1 ariary à un fournisseur chinois, vérifie ces 3 détails. »*
- **Angle :** Comment repérer un intermédiaire menteur, les délais cachés, et le test de l'échantillon.
- **Pourquoi ça marche :** Prévient une arnaque ou une déception financière, fort taux de sauvegarde.
""")

with open('hooks-dropshipping.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print("hooks-dropshipping.md written successfully.")
