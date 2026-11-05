# Skills NocodeVideo · pour les apprenants

Un skill est un mode d'emploi que Claude charge tout seul quand ta demande correspond. Tu lui écris « fais-moi une vidéo explicative sur la LLC », et il suit la méthode du skill : script, animation, rendu.

## Ce qu'il y a dans le dossier

| Skill | À quoi il sert | Exemple de demande |
|---|---|---|
| `video-papier` | **Le style actuel** : vidéo verticale (TikTok, Reels, Shorts) sur fond papier crème, avec le présentateur à lunettes qui parle, change d'expression et de tenue. Script, voix calée, animation, rendu en boucle parfaite, miniatures et pack de publication | « Fais une vidéo style papier sur la perte de temps, avec le présentateur » |
| `video-explicative` | Le même travail dans l'ancien style « Nuit bleue » : fond bleu nuit, rouge et cyan | « Fais une vidéo explicative Nuit bleue sur la LLC » |
| `analyse-video` | Décortique une vidéo à partir d'un lien : transcription, accroche, structure, pourquoi elle marche, titre et hashtags, prompts d'images | « Analyse cette vidéo : <lien TikTok> » |
| `motion-showreel` | Court film de motion design (10 à 30 s) calé sur un tempo, sans coupe : intro, pub, boucle | « Fais-moi une intro animée de 15 s pour ma marque » |
| `ui-ux-pro-max` | Conseils de design pour sites et applications : styles, couleurs, polices, mise en page | « Propose un design pour la page d'accueil de ma boutique » |

## Installer dans l'application Claude (claude.ai, ordinateur ou téléphone)

1. Ouvre les **Paramètres**, puis la partie **Skills**. Active l'exécution de code si on te le demande.
2. Importe les fichiers du dossier `pour-application-claude/`, **un zip par skill**, sans les décompresser.
3. Dans une nouvelle conversation, écris ta demande normalement. Claude choisit le bon skill.

## Installer dans Claude Code (sur ton ordinateur)

**Méthode simple :** copie chaque dossier de `skills-nocodevideo/skills/` dans ton dossier de skills :
- Windows : `C:\Users\<ton nom>\.claude\skills\`
- Mac et Linux : `~/.claude/skills/`

**Méthode plugin** (installe les 5 d'un coup) : dans Claude Code, tape ces deux commandes en remplaçant le chemin :

```
/plugin marketplace add <chemin vers>/skills-nocodevideo
/plugin install nocodevideo@nocodevideo
```

Relance Claude Code ensuite.

## Les logiciels à avoir

Claude peut les installer avec toi s'ils manquent, mais c'est plus rapide s'ils sont déjà là.

- **video-papier** : Google Chrome, Node.js (avec `puppeteer-core`), FFmpeg, Python (avec numpy et faster-whisper pour caler les animations sur la voix).
- **video-explicative** : Node.js (avec Puppeteer ou Playwright), FFmpeg, Python (avec faster-whisper pour caler les animations sur la voix).
- **analyse-video** : Python, yt-dlp, FFmpeg, faster-whisper.
- **motion-showreel** : Node.js (avec Playwright) et FFmpeg.
- **ui-ux-pro-max** : Python 3.

La voix des vidéos se fait à part, par exemple avec ElevenLabs. Tu donnes le MP3 à Claude.

## Bon à savoir

- Pour le style papier, demande « style papier » ou « avec le présentateur ». Le skill `video-papier` contient un modèle prêt à l'emploi avec une démo de 17 s : Claude le copie, y met ta voix et remplace la démo par tes scènes.
- Change la tenue du présentateur, l'intro et le concept de miniature à chaque vidéo : le skill garde la même DA mais évite que tes vidéos se ressemblent toutes.
- Claude te montre des images de contrôle avant le rendu complet. Regarde-les : c'est là que tu corriges.
- Chaque correction donne une nouvelle version (v2, v3…). Rien n'est écrasé.
- Claude ne publie jamais sur les réseaux à ta place : tu gardes la main.

## Licences

- `video-papier`, `video-explicative`, `analyse-video` et `motion-showreel` : NocodeVideo (présentateur compris).
- `ui-ux-pro-max` : licence MIT, Daniel Ávila (github.com/davila7/claude-code-templates). Garde le fichier `LICENSE` dans son dossier.
- Les polices Inter et Instrument Serif sont sous licence libre (SIL Open Font License). GSAP est gratuit, y compris pour un usage commercial.
