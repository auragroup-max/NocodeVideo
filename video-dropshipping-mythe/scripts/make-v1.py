# GÃ©nÃ¨re index.html (vidÃ©o Â« Le dropshipping est mort ? Â») Ã  partir de base.html (= index-v3 de la vidÃ©o paiement Chine)
import re, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
c = open("base.html", encoding="utf-8").read().replace("\r\n", "\n")

def cut(src, a, b, new):
    i = src.index(a); j = src.index(b, i)
    return src[:i] + new + src[j:]

# ---------- titre, tenue ----------
c = c.replace("<title>Payer en Chine</title>", "<title>Le dropshipping est mort ?</title>")
c = c.replace('style="--sweat:#4F8FC0"', 'style="--sweat:#E8742A"')
c = c.replace('data-expr="inquiet" data-pose="croise"', 'data-expr="sceptique" data-pose="croise"')
c = c.replace('data-tenue="sweat"', 'data-tenue="polo"').replace('data-bandeau="non"', 'data-bandeau="oui"').replace('data-montre="non"', 'data-montre="oui"')
c = c.replace('// import Â· payer en Chine', '// dropshipping Â· depuis Madagascar')
c = c.replace('const INIT_EXPR = "inquiet", INIT_POSE = "croise";', 'const INIT_EXPR = "sceptique", INIT_POSE = "croise";')

# ---------- icÃ´nes ----------
ICONS = '''<symbol id="i-belt" viewBox="0 0 120 120"><rect x="6" y="50" width="108" height="20" rx="10" fill="#141414"/><rect x="30" y="34" width="60" height="52" rx="14" fill="#E0402A" stroke="#141414" stroke-width="6"/><path d="M40 52 L80 52" stroke="#141414" stroke-width="6" stroke-linecap="round"/><circle cx="60" cy="70" r="5" fill="#141414"/></symbol>
<symbol id="i-bottle" viewBox="0 0 120 120"><rect x="48" y="6" width="24" height="16" rx="4" fill="#141414"/><path d="M42 22 L78 22 L84 40 L84 106 Q84 114 76 114 L44 114 Q36 114 36 106 L36 40 Z" fill="#7CC8F2" stroke="#141414" stroke-width="6" stroke-linejoin="round"/><path d="M36 62 L84 62 M36 84 L84 84" stroke="#141414" stroke-width="5"/></symbol>
<symbol id="i-lamp" viewBox="0 0 120 120"><path d="M14 70 Q60 30 106 70" fill="none" stroke="#141414" stroke-width="10" stroke-linecap="round"/><rect x="40" y="40" width="40" height="30" rx="8" fill="#F6C21C" stroke="#141414" stroke-width="6"/><circle cx="60" cy="55" r="8" fill="#fff" stroke="#141414" stroke-width="4"/><path d="M44 82 L30 108 M60 84 L60 112 M76 82 L90 108" stroke="#F6C21C" stroke-width="7" stroke-linecap="round"/></symbol>
<symbol id="i-wifi" viewBox="0 0 120 120"><g class="ico" style="stroke-width:10"><path d="M14 46 Q60 6 106 46"/><path d="M30 64 Q60 38 90 64"/><path d="M46 82 Q60 70 74 82"/></g><circle cx="60" cy="100" r="9" fill="#E0402A" stroke="#141414" stroke-width="4"/></symbol>
<symbol id="i-cal" viewBox="0 0 120 120"><rect x="12" y="20" width="96" height="88" rx="12" fill="#fff" stroke="#141414" stroke-width="7"/><path d="M12 46 L108 46" stroke="#141414" stroke-width="7"/><rect x="12" y="20" width="96" height="26" rx="10" fill="#E0402A"/><path d="M36 10 L36 30 M84 10 L84 30" stroke="#141414" stroke-width="7" stroke-linecap="round"/><path d="M38 76 L52 90 L82 60" fill="none" stroke="#141414" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></symbol>
'''
c = c.replace('<symbol id="i-finger"', ICONS + '<symbol id="i-finger"', 1)

# ---------- CSS ----------
CSS = '''
  /* ---------- vidÃ©o dropshipping est mort ---------- */
  #tomb { width:400px; height:540px; border-radius:200px 200px 26px 26px; --carte:#E2DDD3; }
  #tomb .rip { position:absolute; left:0; right:0; top:120px; text-align:center; font:800 130px/1 "Inter"; letter-spacing:-0.05em; }
  #tomb .nm { position:absolute; left:0; right:0; top:285px; text-align:center; font:800 40px/1 var(--mono); letter-spacing:.02em; }
  #tomb .dt { position:absolute; left:0; right:0; top:345px; text-align:center; font:600 30px/1 var(--mono); color:var(--gris); }
  #tomb .grass { position:absolute; left:-50px; right:-50px; bottom:-24px; height:48px; border-radius:24px; background:#9BC59D; border:5px solid var(--encre); }
  #tomb svg.crk { position:absolute; left:0; top:0; width:400px; height:540px; overflow:visible; }
  #tomb svg.crk path { fill:none; stroke:var(--encre); stroke-width:9; stroke-linecap:round; stroke-linejoin:round; }
  .bub2 { padding:18px 30px; border-radius:40px 40px 40px 10px; font-weight:800; font-size:40px; letter-spacing:-0.02em; white-space:nowrap; }
  #cash { width:560px; height:330px; border-radius:40px; }
  #cash .tag { position:absolute; left:44px; top:44px; }
  #cash .n { position:absolute; left:40px; top:96px; font:800 112px/1 "Inter"; letter-spacing:-0.05em; white-space:nowrap; }
  #cash .u2 { position:absolute; left:44px; top:228px; font:800 50px/1 "Inter"; color:var(--rouge); letter-spacing:-0.02em; }
  .ban.sm { font-size:46px; padding:16px 32px; }
  .fr { display:inline-flex; vertical-align:middle; margin-right:14px; border:3px solid #fff; border-radius:6px; overflow:hidden; }
  .fr i { width:16px; height:36px; display:block; }
  .prd { width:470px; height:150px; border-radius:30px; display:flex; align-items:center; gap:22px; padding:0 28px; box-sizing:border-box; font-weight:800; font-size:44px; letter-spacing:-0.03em; }
  .prd svg { width:104px; height:104px; flex:none; }
  .nt { width:480px; height:124px; border-radius:28px; display:flex; align-items:center; gap:18px; padding:0 22px; box-sizing:border-box; }
  .nt .ic { width:74px; height:74px; border-radius:20px; background:var(--rouge); border:5px solid var(--encre); box-sizing:border-box; display:flex; align-items:center; justify-content:center; flex:none; }
  .nt .ic svg { width:46px; height:46px; color:#fff; }
  .nt b { display:block; font-weight:800; font-size:36px; letter-spacing:-0.02em; }
  .nt span { display:block; font:600 22px/1.3 var(--mono); color:var(--gris); }
  .tile { width:160px; height:160px; border-radius:30px; display:flex; align-items:center; justify-content:center; }
  .tile svg { width:100px; height:100px; color:var(--encre); }
  #tile0::after { border-color:var(--rouge); border-width:8px; }
  #tFaim h2 { font-size:170px; }
  .qq { white-space:nowrap; padding:26px 40px; border-radius:30px; font-weight:800; letter-spacing:-0.03em; }
  #q1 { font-size:54px; color:var(--gris); }
  #q2 { font-size:64px; }
'''
c = c.replace("</style>\n<style>", CSS + "</style>\n<style>", 1)

# ---------- DOM ----------
UI = '''<div id="ui">
    <!-- 1 Â· la tombe (premiÃ¨re ET derniÃ¨re image, Ã  gauche du prÃ©sentateur) -->
    <div class="u ink ctr" id="tomb" style="left:320px;top:400px">
      <div class="rip">RIP</div><div class="nm">DROPSHIPPING</div><div class="dt">2015 â€“ 2026</div><div class="grass"></div>
      <svg class="crk" viewBox="0 0 400 540"><path pathLength="1" d="M210 0 L180 80 L230 150 L170 250 L220 330 L190 420 L230 540"/></svg>
    </div>
    <div class="u ink ctr bub2" id="bA" style="left:420px;top:250px">Â« c'est saturÃ© Â»</div>
    <div class="u ink ctr bub2" id="bB" style="left:250px;top:980px">Â« trop tard Â»</div>
    <div class="u ink ctr" id="cash" style="left:320px;top:380px"><span class="tag">// moi, j'ai encaissÃ©</span><div class="n" id="cashN">0</div><div class="u2">Ar / mois</div></div>
    <div class="u pill ink big" id="mada" style="left:320px;top:820px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-pin"/></svg></div>depuis Madagascar</div>

    <!-- 2 Â· qui a raison -->
    <div class="u st" id="tQui" style="top:280px"><span class="tag">// alorsâ€¦</span><h2>Qui a <span class="it" id="rais">raison ?</span></h2></div>
    <div class="u pill ink big" id="reste" style="left:540px;top:560px"><div class="pi"><svg viewBox="0 0 120 120"><use href="#i-clock"/></svg></div>reste jusqu'Ã  la fin</div>

    <!-- 3 Â· la France (Ã  droite du prÃ©sentateur) -->
    <div class="u ban sm ctr" id="bFr" style="left:770px;top:190px"><span class="fr"><i style="background:#2B4FA8"></i><i style="background:#fff"></i><i style="background:#E0402A"></i></span>en France</div>
    <div class="u pill ink" id="f1" style="left:770px;top:360px"><div class="pi">1</div>paiement en 1 clic<svg class="ck"><use href="#i-check"/></svg></div>
    <div class="u pill ink" id="f2" style="left:770px;top:490px"><div class="pi">2</div>livrÃ© en 2 jours<svg class="ck"><use href="#i-check"/></svg></div>
    <div class="u pill ink" id="f3" style="left:770px;top:620px"><div class="pi">3</div>clients qui achÃ¨tent<svg class="ck"><use href="#i-check"/></svg></div>
    <div class="u ink ctr cd" id="door" style="left:770px;top:720px;height:330px"><svg viewBox="0 0 120 120"><use href="#i-door"/></svg><b>portes ouvertes</b></div>
    <div class="u ink ctr cd" id="assis" style="left:770px;top:200px;height:330px"><svg viewBox="0 0 120 120"><use href="#i-sad"/></svg><b>â€¦et ils restent assis</b></div>
    <div class="u ink ctr bub2" id="r1" style="left:770px;top:610px">Â« pfffâ€¦ Â»</div>
    <div class="u ink ctr bub2" id="r2" style="left:770px;top:750px">Â« c'est saturÃ© Â»</div>
    <div class="u stamp ctr" id="zero" style="left:770px;top:920px;font-size:60px">0 ESSAI</div>

    <!-- 4 Â· nous, ici (Ã  gauche du prÃ©sentateur) -->
    <div class="u ban sm ctr" id="bMg" style="left:320px;top:190px">nous, <em>ici</em></div>
    <div class="u pill ink big" id="m1" style="left:320px;top:380px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></div><span class="strike" id="sM1">carte facile<i></i></span></div>
    <div class="u pill ink big" id="m2" style="left:320px;top:520px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></div><span class="strike" id="sM2">raccourci<i></i></span></div>
    <div class="u st" id="tFaim" style="top:300px"><span class="tag">// un truc qu'ils ont perdu</span><h2>la <span class="it">faim.</span></h2></div>

    <!-- 5 Â· le marathon (Ã  droite du prÃ©sentateur) -->
    <div class="u ban sm ctr" id="bNi" style="left:770px;top:180px">1 niche : <em>marathon</em></div>
    <div class="u ink prd ctr" id="c1" style="left:770px;top:310px"><svg viewBox="0 0 120 120"><use href="#i-belt"/></svg>ceintures</div>
    <div class="u ink prd ctr" id="c2" style="left:770px;top:490px"><svg viewBox="0 0 120 120"><use href="#i-bottle"/></svg>gourdes</div>
    <div class="u ink prd ctr" id="c3" style="left:770px;top:670px"><svg viewBox="0 0 120 120"><use href="#i-lamp"/></svg>lampes frontales</div>
    <div class="u pill ink big" id="pas" style="left:770px;top:910px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-heart"/></svg></div>clients passionnÃ©s</div>
    <div class="u pill ink" id="mois" style="left:770px;top:220px"><div class="pi"><svg viewBox="0 0 120 120"><use href="#i-cal"/></svg></div>plusieurs mois</div>
    <div class="u ink nt ctr" id="o1" style="left:770px;top:330px"><div class="ic"><svg viewBox="0 0 120 120"><use href="#i-cart"/></svg></div><div><b>Nouvelle commande</b><span>ceinture de course</span></div></div>
    <div class="u ink nt ctr" id="o2" style="left:770px;top:480px"><div class="ic"><svg viewBox="0 0 120 120"><use href="#i-cart"/></svg></div><div><b>Nouvelle commande</b><span>gourde Â· x2</span></div></div>
    <div class="u ink nt ctr" id="o3" style="left:770px;top:630px"><div class="ic"><svg viewBox="0 0 120 120"><use href="#i-cart"/></svg></div><div><b>Nouvelle commande</b><span>lampe frontale</span></div></div>
    <div class="u ink ctr cd" id="xs" style="left:290px;top:280px;width:400px;height:330px"><svg viewBox="0 0 120 120"><use href="#i-box"/></svg><b>stock</b><svg class="nx" viewBox="0 0 200 200"><path pathLength="1" d="M30 30 L170 170"/><path pathLength="1" d="M170 30 L30 170"/></svg></div>
    <div class="u ink ctr cd" id="xl" style="left:790px;top:280px;width:400px;height:330px"><svg viewBox="0 0 120 120"><use href="#i-shop"/></svg><b>local</b><svg class="nx" viewBox="0 0 200 200"><path pathLength="1" d="M30 30 L170 170"/><path pathLength="1" d="M170 30 L30 170"/></svg></div>
    <div class="u pill ink big" id="wifi" style="left:540px;top:360px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-wifi"/></svg></div>une connexion</div>
    <div class="u pill ink big" id="regu" style="left:540px;top:500px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-cal"/></svg></div>de la rÃ©gularitÃ©<svg class="ck"><use href="#i-check"/></svg></div>

    <!-- 6 Â· des centaines de niches (prÃ©sentateur au centre) -->
    <div class="u pill ink big" id="pers" style="left:540px;top:215px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-pin"/></svg></div>depuis l'Afrique : presque personne</div>
    TILES

    <!-- 7 Â· saturÃ© ? -->
    <div class="u st" id="tSat" style="top:300px"><span class="tag">// donc non</span><h2><span class="strike" id="sSat">saturÃ© ?<i></i></span></h2></div>
    <div class="u st" id="tLache" style="top:240px"><span class="tag">// ce qui est saturÃ©â€¦</span><h2>ceux qui <span class="k" id="kLache">lÃ¢chent<i></i></span></h2></div>
    <div class="u crowd ctr" id="crowd2" style="left:540px;top:500px">
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span style="color:#141414"><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-check"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
    </div>
    <div class="u pill ink big" id="sem" style="left:540px;top:760px"><div class="pi"><svg viewBox="0 0 120 120"><use href="#i-clock"/></svg></div>au bout d'une semaine</div>

    <!-- 8 Â· la vraie question -->
    <div class="u st" id="tQ" style="top:250px"><span class="tag">// la vraie question</span></div>
    <div class="u ink ctr qq" id="q1" style="left:540px;top:340px"><span class="strike" id="sQ1">Â« est-ce que Ã§a marche ? Â»<i></i></span></div>
    <div class="u ink ctr qq" id="q2" style="left:540px;top:540px">Â« toi, tu vas <span class="k" id="kTen">tenir<i></i></span> ? Â»</div>

    <!-- 9 Â· enregistre / envoie -->
    <div class="u ink ctr cd" id="save" style="left:540px;top:300px"><svg viewBox="0 0 120 120"><use href="#i-bookmark"/></svg><b>enregistre-la</b></div>
    <div class="u st" id="tEnv" style="top:230px"><span class="tag">// Ã  celui qui dit que c'est trop tard</span><h2>Envoie-la.</h2></div>
    <div class="u" id="shareB" style="left:150px;top:470px"><svg><use href="#i-plane"/></svg></div>
    <div class="u ink" id="vcard" style="left:188px;top:465px"><svg><use href="#i-yt"/></svg></div>
    <div class="u pill ink big" id="ami" style="left:760px;top:560px"><div class="pi" style="background:#F6C21C">T</div><div><span>Toky</span><small>Â« c'est trop tard Â»</small></div></div>
  </div>

  '''
icons = ["shoe", "shirt", "lip", "gadget", "book", "glass", "clover", "plate", "phone", "bolt", "star", "box", "moon", "photo", "heart"]
tiles = []
k = 1
for r in range(3):
    for col in range(5):
        x = 96 + col * 182; y = 300 + r * 182
        if r == 1 and col == 2:
            tiles.append(f'<div class="u ink tile" id="tile0" style="left:{x}px;top:{y}px"><svg viewBox="0 0 120 120"><use href="#i-shoe"/></svg></div>')
        else:
            tiles.append(f'<div class="u ink tile tl" id="tile{k}" style="left:{x}px;top:{y}px"><svg viewBox="0 0 120 120"><use href="#i-{icons[k]}"/></svg></div>'); k += 1
UI = UI.replace("TILES", "\n    ".join(tiles))
c = cut(c, '<div id="ui">', '<div id="hud">', UI)

# ---------- TIMELINE ----------
TL = r'''const LIFE = { t: 0 }; tl.fromTo(LIFE, { t: 0 }, { t: DURATION, duration: DURATION, ease: "none", immediateRender: false, onUpdate: () => life(LIFE.t) }, 0);
  const P_R = { x: 220, y: 30, s: 0.95 }, P_L = { x: -240, y: 30, s: 0.95 }, P_C = { x: 43, y: -60, s: 1.1 };
  const MOVE = (p, t, d = 0.6) => tl.to("#persoW", { x: p.x, y: p.y, scaleX: p.s, scaleY: p.s, duration: d, ease: "power2.inOut" }, t);
  const STRIKE = (id, t) => { tl.set(`#${id} i`, { scaleX: 0 }, 0); tl.fromTo(`#${id} i`, { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power3.out", immediateRender: false }, t); };
  const HOP = (t, p) => tl.to("#persoW", { y: p.y - 25, duration: 0.18, yoyo: true, repeat: 1, ease: "power2.out" }, t);
  gsap.set("#persoW", { x: P_R.x, y: P_R.y, scaleX: P_R.s, scaleY: P_R.s });
  tl.fromTo("#paper", { x: 0, y: 0 }, { x: -36, y: -36, duration: DURATION, ease: "none", immediateRender: false }, 0);
  gsap.set("#cam", { transformOrigin: "50% 40%" });

  // =====================================================================
  // LES SCÃˆNES Â· Â« Le dropshipping est mort ? Â»
  // =====================================================================
  const tMort = S("est mort"), tDit = S("cest ce quon te dit"), tMoi = S("moi jai encaisse"), tEnc = S("encaisse"), tMill = S("million"), tMois = S("par mois avec"), tMada = S("depuis madagascar");
  const tAlors = S("alors qui"), tRaison = S("raison"), tReste = S("reste jusqua");
  const tFrance = S("regarde la france"), tPay = S("paiement"), tLiv = S("livraison"), tCli = S("des clients qui"), tPortes = S("portes ouvertes");
  const tPourtant = S("et pourtant"), tAssis = S("restent assis"), tRalent = S("ils ralent"), tDisent = S("ils disent"), tEssaient = S("nessaient");
  const tNous = S("nous ici"), tCarte = S("pas de carte"), tRacc = S("pas de raccourci"), tMais = S("mais on a un truc"), tFaim = S("la faim");
  const tNiche = S("moi jai choisi"), tMara = S("le marathon"), tCeint = S("ceintures"), tGourde = S("gourdes"), tLampe = S("lampes"), tPetits = S("des petits"), tPass = S("passionnes");
  const tPendant = S("pendant plusieurs"), tCmd = S("commandes sont"), tTomb = S("tombees"), tStock = S("sans stock"), tLocal = S("sans local"), tJuste = S("juste une"), tCnx = S("connexion"), tReg = S("regularite");
  const tEtMara = S("et le marathon"), tQune = S("quune niche"), tCent = S("centaines"), tPresque = S("presque personne"), tAfr = S("lafrique");
  const tDonc = S("donc non"), tPasSat = S("pas sature"), tCeQui = S("ce qui est sature"), tGens = S("les gens qui"), tAband = S("abandonnent"), tSem = S("semaine");
  const tVraie = S("la vraie question"), tMarche = S("estce que ca marche"), tToi = S("cest estce que toi"), tTenir = S("tenir");
  const tEnr = S("enregistre"), tEnv = S("envoiela"), tTard = S("trop tard"), tEt = S("et la prochaine");

  // Ã©tat de la premiÃ¨re (= derniÃ¨re) image
  tl.set("#persoW", { x: P_R.x, y: P_R.y, scaleX: P_R.s, scaleY: P_R.s }, 0);
  tl.set("#tomb", { autoAlpha: 1, x: 0, y: 0, scale: 1, rotation: 0, filter: B(0) }, 0);

  // ========== 1 Â· Â« LE DROPSHIPPING EST MORT Â» ==========
  PULSE("#tomb", tMort, 1.04); SFX("thud", tMort + 0.05, -22);
  POP("#bA", tDit - 0.05); SFX("pop", tDit, -22);
  POP("#bB", tDit + 0.4); SFX("pop", tDit + 0.45, -23);
  OUT("#bA, #bB", tMoi - 0.1, 0.25);
  DRAW("#tomb .crk path", tMoi + 0.05, 0.3); SFX("glass", tMoi + 0.1, -22);
  tl.fromTo("#tomb", { x: 0 }, { x: 12, duration: 0.05, yoyo: true, repeat: 5, ease: "none", immediateRender: false }, tMoi + 0.1);
  tl.to("#tomb", { y: 260, rotation: -16, autoAlpha: 0, filter: B(8), duration: 0.45, ease: "power3.in" }, tEnc - 0.05); SFX("whip", tEnc, -22);
  IN("#cash", tEnc + 0.25, { y: 40 });
  const fmt = (n) => Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  ROLLF("cashN", 0, 1000000, tMill - 0.3, 1.3, fmt); SFX("coins", tMill, -21);
  PULSE("#cash", tMois, 1.06); SFX("ding2", tMois, -21);
  POP("#mada", tMada - 0.05); SFX("pop", tMada, -22);
  tl.fromTo("#cam", { scale: 1 }, { scale: 1.04, duration: 0.2, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, tMill + 1.0);
  OUT("#cash, #mada", tAlors - 0.3);

  // ========== 2 Â· QUI A RAISON ? (prÃ©sentateur au centre) ==========
  MOVE(P_C, tAlors - 0.3);
  IN("#tQui", tAlors - 0.05, { y: 26 }); PULSE("#rais", tRaison, 1.1); SFX("pop", tRaison, -22);
  POP("#reste", tReste - 0.05); SFX("tick", tReste, -21);
  OUT("#tQui, #reste", tFrance - 0.3);

  // ========== 3 Â· LA FRANCE (prÃ©sentateur Ã  gauche) ==========
  MOVE(P_L, tFrance - 0.3);
  IN("#bFr", tFrance - 0.05, { y: -30 }); SFX("whip", tFrance, -22);
  [["#f1", tPay], ["#f2", tLiv], ["#f3", tCli]].forEach(([p, t], i) => { IN(p, t - 0.1, { x: 60, y: 0 }); XPOP(p + " .ck", t + 0.35); SFX("ding" + i, t + 0.35, -22); });
  IN("#door", tPortes - 0.15, { y: 40 }); SFX("card", tPortes, -22);
  OUT("#bFr, #f1, #f2, #f3, #door", tPourtant - 0.1);
  IN("#assis", tAssis - 0.25, { y: 40 }); SFX("thud", tAssis, -24);
  POP("#r1", tRalent - 0.05); SFX("pop", tRalent, -22);
  POP("#r2", tDisent + 0.1); SFX("pop", tDisent + 0.15, -22);
  STAMP("#zero", tEssaient + 0.3, -6); SFX("stamp", tEssaient + 0.3, -18);
  SHK.push(tEssaient + 0.1);
  OUT("#assis, #r1, #r2, #zero", tNous - 0.3);

  // ========== 4 Â· NOUS, ICI (prÃ©sentateur Ã  droite) ==========
  MOVE(P_R, tNous - 0.3);
  IN("#bMg", tNous - 0.05, { y: -30 }); SFX("whip", tNous, -22);
  IN("#m1", tCarte - 0.1, { x: -60, y: 0 }); STRIKE("sM1", tCarte + 0.45); SFX("strike", tCarte + 0.45, -22);
  IN("#m2", tRacc - 0.1, { x: -60, y: 0 }); STRIKE("sM2", tRacc + 0.4); SFX("strike", tRacc + 0.4, -22);
  OUT("#bMg, #m1, #m2", tMais - 0.25);
  MOVE(P_C, tMais - 0.2);
  IN("#tFaim", tMais + 0.1, { y: 26 }); POP("#tFaim h2", tFaim - 0.05, 0.4);
  tl.fromTo("#cam", { scale: 1 }, { scale: 1.07, duration: 0.18, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, tFaim); SFX("boom", tFaim, -18);
  OUT("#tFaim", tNiche - 0.3);

  // ========== 5 Â· LE MARATHON (prÃ©sentateur Ã  gauche) ==========
  MOVE(P_L, tNiche - 0.3);
  IN("#bNi", tMara - 0.1, { y: -30 }); SFX("whip", tMara, -22);
  [["#c1", tCeint], ["#c2", tGourde], ["#c3", tLampe]].forEach(([p, t]) => { IN(p, t - 0.15, { x: 60, y: 0, s: 0.92 }); SFX("card", t, -23); });
  POP("#pas", tPass - 0.3); SFX("ding2", tPass, -22);
  OUT("#bNi, #c1, #c2, #c3, #pas", tPendant - 0.25);
  IN("#mois", tPendant - 0.05, { y: -20 }); SFX("tick", tPendant, -22);
  [["#o1", tCmd - 0.1], ["#o2", tCmd + 0.3], ["#o3", tTomb + 0.05]].forEach(([p, t]) => { IN(p, t, { x: 80, y: 0, d: 0.35 }); SFX("notif", t + 0.05, -23); });
  NODS.push(tTomb + 0.1);
  OUT("#mois, #o1, #o2, #o3", tStock - 0.25);
  MOVE(P_C, tStock - 0.25);
  IN("#xs", tStock - 0.1, { y: 40 }); DRAW("#xs .nx path", tStock + 0.25, 0.3); SFX("strike", tStock + 0.3, -22);
  IN("#xl", tLocal - 0.1, { y: 40 }); DRAW("#xl .nx path", tLocal + 0.2, 0.3); SFX("strike", tLocal + 0.25, -22);
  OUT("#xs, #xl", tJuste - 0.15);
  POP("#wifi", tCnx - 0.15); SFX("pop", tCnx, -22);
  POP("#regu", tReg - 0.15); XPOP("#regu .ck", tReg + 0.45); SFX("ding2", tReg + 0.45, -21);
  NODS.push(tReg + 0.3);
  OUT("#wifi, #regu", tEtMara - 0.2);

  // ========== 6 Â· DES CENTAINES DE NICHES ==========
  POP("#tile0", tEtMara + 0.05); SFX("card", tEtMara + 0.1, -22);
  gsap.utils.toArray(".tl").forEach((el, i) => { POP(el, tCent - 0.2 + i * 0.045, 0.35); if (i % 3 === 0) SFX("tick", tCent - 0.2 + i * 0.045, -25); });
  tl.to(".tl", { opacity: 0.3, duration: 0.3 }, tPresque);
  PULSE("#tile0", tPresque + 0.1, 1.1);
  POP("#pers", tPresque - 0.05); SFX("pop", tPresque, -22);
  OUT("#tile0, .tl, #pers", tDonc - 0.3);

  // ========== 7 Â· PAS SATURÃ‰â€¦ CEUX QUI LÃ‚CHENT ==========
  IN("#tSat", tDonc - 0.05, { y: 26 }); SHK.push(tDonc + 0.2);
  STRIKE("sSat", tPasSat + 0.35); SFX("strike", tPasSat + 0.35, -21);
  OUT("#tSat", tCeQui - 0.2);
  IN("#tLache", tCeQui - 0.05, { y: 26 });
  IN("#crowd2", tGens - 0.1, { y: 30 });
  [1, 2, 4, 5].forEach((n, i) => XPOP(`#crowd2 span:nth-child(${n}) i`, tAband + i * 0.12)); SFX("error", tAband + 0.1, -24);
  XPOP("#crowd2 span:nth-child(3) i", tAband + 0.6); SFX("ding1", tAband + 0.6, -22);
  HL("kLache", tAband);
  POP("#sem", tSem - 0.4); SFX("tick", tSem - 0.35, -22);
  OUT("#tLache, #crowd2, #sem", tVraie - 0.25);

  // ========== 8 Â· LA VRAIE QUESTION ==========
  IN("#tQ", tVraie - 0.05, { y: 20 });
  IN("#q1", tMarche - 0.1, { y: 30 }); STRIKE("sQ1", tToi - 0.1); SFX("strike", tToi - 0.1, -21);
  IN("#q2", tToi + 0.25, { y: 40, s: 0.9 }); HL("kTen", tTenir); SFX("ding2", tTenir, -20);
  tl.fromTo("#cam", { scale: 1 }, { scale: 1.04, duration: 0.2, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, tTenir);
  OUT("#tQ, #q1, #q2", tEnr - 0.25);

  // ========== 9 Â· ENREGISTRE / ENVOIEâ€¦ ET LA BOUCLE ==========
  hide("#save"); tl.fromTo("#save", { autoAlpha: 0, y: -120, rotation: -8 }, { autoAlpha: 1, y: 0, rotation: 0, duration: 0.5, ease: "bounce.out", immediateRender: false }, tEnr - 0.1); SFX("thud", tEnr + 0.25, -22);
  OUT("#save", tEnv - 0.25);
  IN("#tEnv", tEnv - 0.05, { y: 26 });
  POP("#shareB", tEnv, 0.4); SFX("pop", tEnv + 0.05, -22);
  hide("#vcard"); tl.fromTo("#vcard", { autoAlpha: 0, scale: 0.5, rotation: -12 }, { autoAlpha: 1, scale: 1, rotation: -6, duration: 0.3, ease: "back.out(2)", immediateRender: false }, tEnv + 0.3);
  tl.fromTo("#vcard", { x: 0 }, { x: 500, duration: 0.7, ease: "power1.inOut", immediateRender: false }, tEnv + 0.6);
  tl.fromTo("#vcard", { y: 0 }, { y: -90, duration: 0.35, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, tEnv + 0.6);
  tl.to("#vcard", { scale: 0.3, autoAlpha: 0, rotation: 10, duration: 0.2, ease: "power2.in" }, tEnv + 1.15); SFX("whip", tEnv + 0.6, -22);
  POP("#ami", tEnv + 0.9, 0.4); PULSE("#ami", tTard, 1.1); SFX("ding2", tEnv + 1.25, -21);
  OUT("#tEnv, #shareB, #ami", tEt - 0.3);
  MOVE(P_R, tEt - 0.2, 0.55);
  tl.set("#tomb .crk path", { strokeDashoffset: 1 }, tEt - 0.25);
  tl.fromTo("#tomb", { autoAlpha: 0, x: 0, y: 120, rotation: 0, scale: 0.9, filter: B(10) }, { autoAlpha: 1, x: 0, y: 0, rotation: 0, scale: 1, filter: B(0), duration: 0.55, ease: "back.out(1.4)", immediateRender: false }, tEt - 0.05); SFX("thud", tEt + 0.1, -22);

  // ---------- jeu d'acteur ----------
  [[tDit - 0.05, "parle", "salue"], [tMoi - 0.1, "malin", "pointe"], [tMill - 0.1, "content"], [tMada - 0.05, "content", "salue"],
   [tAlors - 0.1, "question", "croise"], [tReste - 0.05, "malin", "pointe"],
   [tFrance - 0.1, "parle", "pointe"], [tCli - 0.05, "content"], [tPourtant - 0.05, "sceptique", "croise"], [tRalent - 0.05, "sceptique"], [tEssaient - 0.1, "insiste", "pointe"],
   [tNous - 0.1, "parle", "salue"], [tCarte - 0.05, "inquiet"], [tMais - 0.1, "malin", "pointe"], [tFaim - 0.1, "insiste"],
   [tNiche - 0.1, "content", "salue"], [tMara - 0.05, "parle", "pointe"], [tPass - 0.1, "content"], [tCmd - 0.1, "surpris"], [tTomb + 0.2, "content", "salue"],
   [tStock - 0.1, "insiste", "pointe"], [tJuste - 0.05, "parle"], [tReg - 0.05, "content"],
   [tEtMara - 0.05, "parle", "salue"], [tCent - 0.1, "surpris"], [tPresque - 0.1, "malin", "pointe"],
   [tDonc - 0.1, "insiste", "croise"], [tCeQui - 0.05, "sceptique"], [tAband - 0.1, "inquiet"],
   [tVraie - 0.1, "parle", "salue"], [tToi - 0.05, "insiste", "pointe"],
   [tEnr - 0.1, "content", "pointe"], [tEnv - 0.05, "content", "salue"],
   [tEt - 0.1, INIT_EXPR, INIT_POSE]].forEach(([t, e, p]) => ACT(t, e, p));
  // ---------- regard ----------
  [[0, -9, -3], [tDit, -6, -6], [tEnc + 0.3, -8, -4], [tMada, -6, 2],
   [tAlors, 0, -3], [tReste, 0, 0],
   [tFrance, 8, -7], [tPay, 8, -5], [tLiv, 8, -3], [tCli, 8, -1], [tPortes, 8, 3], [tAssis, 8, -6], [tRalent, 8, 0], [tEssaient, 0, 0],
   [tNous, -8, -7], [tCarte, -8, -3], [tRacc, -8, 0], [tMais, 0, -2], [tFaim, 0, -5],
   [tNiche, 0, 0], [tMara, 8, -8], [tCeint, 8, -6], [tGourde, 8, -3], [tLampe, 8, 0], [tPass, 8, 4], [tPendant, 8, -7], [tCmd, 8, -4], [tTomb, 8, -1],
   [tStock, -7, -5], [tLocal, 7, -5], [tJuste, 0, -2],
   [tEtMara, 0, -4], [tCent, -5, -6], [tPresque, 0, -8],
   [tDonc, 0, -4], [tGens, 0, -2], [tSem, 0, 1],
   [tVraie, 0, -5], [tToi, 0, -1],
   [tEnr, 0, -4], [tEnv, -7, -4], [tEnv + 1.0, 8, -3],
   [tEt - 0.1, -9, -3]].forEach(([t, x, y]) => LOOK(t, x, y));

  '''
c = cut(c, "const LIFE = { t: 0 };", "for (let i = 1; i < GK.length; i++)", TL)
open("index.html", "w", encoding="utf-8").write(c)
print("index.html OK", len(c))

