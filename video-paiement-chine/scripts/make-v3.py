import os

input_file = r'd:\No Code Video\video-paiement-chine\index.html'
output_file = r'd:\No Code Video\video-paiement-chine\index-v3.html'

with open(input_file, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update .plat CSS
old_plat = '''  .plat { width:440px; height:250px; border-radius:34px; display:flex; flex-direction:column; justify-content:center; padding:0 34px; box-sizing:border-box; gap:10px; }
  .plat b { font-weight:800; font-size:52px; letter-spacing:-0.03em; }
  .plat span { font:600 28px/1.25 "Inter"; color:var(--gris); }
  .plat i { position:absolute; right:26px; top:26px; width:22px; height:22px; border-radius:50%; border:4px solid var(--encre); }'''

new_plat = '''  .plat { width:460px; height:200px; border-radius:28px; display:flex; flex-direction:column; justify-content:center; padding:0 30px; box-sizing:border-box; gap:6px; }
  .plat b { font-weight:800; font-size:46px; letter-spacing:-0.03em; }
  .plat span { font:600 24px/1.2 "Inter"; color:var(--gris); }
  .plat i { position:absolute; right:26px; top:26px; width:22px; height:22px; border-radius:50%; border:4px solid var(--encre); }'''

# Normalize line endings for replacement
c = c.replace(old_plat.replace('\n', '\r\n'), new_plat.replace('\n', '\r\n'))

# 2. Update UI DOM
old_ui = '''    <!-- 1 · la page de paiement (première ET dernière image) -->
    <div class="u ink ctr" id="chk" style="left:540px;top:280px"><div class="scr">
      <div class="hd">TAOBAO · panier</div>
      <div class="pr"><svg viewBox="0 0 120 120"><use href="#i-gadget"/></svg></div>
      <div class="px">¥ 89<small>+ livraison</small></div>
      <div id="payBtn">Payer</div>
      <div id="refus">✕ Carte refusée</div>
    </div><svg id="tap" viewBox="0 0 120 120"><use href="#i-finger"/></svg></div>

    <!-- 2 · ça arrive à tout le monde -->
    <div class="u crowd ctr" id="crowd" style="left:540px;top:520px">
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
    </div>
    <div class="u st" id="tTout" style="top:300px"><span class="tag">// presque tout le monde</span><h2>Plateformes <span class="it">+</span> paiement</h2></div>
    <div class="u ink ctr cd" id="save" style="left:540px;top:720px"><svg viewBox="0 0 120 120"><use href="#i-bookmark"/></svg><b>enregistre-la</b></div>

    <!-- 3 · les plateformes -->
    <div class="u ban ctr" id="bP" style="left:540px;top:220px">les <em>plateformes</em></div>
    <div class="u ink plat" id="p1" style="left:70px;top:330px"><i style="background:#FF6A00"></i><b>Taobao</b><span>le plus de choix, prix bas<br>en chinois</span></div>
    <div class="u ink plat" id="p2" style="left:570px;top:330px"><i style="background:#F6C21C"></i><b>1688</b><span>prix d'usine<br>pour acheter en gros</span></div>
    <div class="u ink plat" id="p3" style="left:70px;top:620px"><i style="background:#E0402A"></i><b>AliExpress</b><span>en français, livré chez toi<br>mais plus cher</span></div>
    <div class="u ink plat" id="p4" style="left:570px;top:620px"><i style="background:#7CC8F2"></i><b>Alibaba</b><span>pour les grosses<br>quantités</span></div>

    <!-- 4 · trois solutions -->
    <div class="u st" id="t3s" style="top:240px"><span class="tag">// le paiement</span><h2>3 <span class="k" id="kSol">solutions<i></i></span></h2></div>
    <div class="u num3" id="n1" style="left:150px;top:500px">1</div>
    <div class="u num3" id="n2" style="left:435px;top:500px">2</div>
    <div class="u num3" id="n3" style="left:720px;top:500px">3</div>

    <!-- 5 · la Visa Akory -->
    <div class="u ban ctr" id="b1" style="left:540px;top:220px"><em>1</em> · une carte Visa</div>
    <div class="u card3 ctr" id="visa" style="left:540px;top:340px;background:linear-gradient(135deg,#FF7A00,#E0402A)"><div class="chip"></div><div class="num">•••• •••• •••• 2026</div><div class="nm">AKORY</div><div class="br">VISA</div></div>
    <div class="u ink ctr" id="dial" style="left:540px;top:760px">#144# → 6</div>
    <div class="u ink ctr" id="globeOk" style="left:540px;top:900px"><svg viewBox="0 0 120 120"><use href="#i-globe"/></svg>sites internationaux<svg viewBox="0 0 64 64" style="width:56px;height:56px"><use href="#i-check"/></svg></div>

    <!-- 6 · Alipay -->
    <div class="u ban ctr" id="b2" style="left:540px;top:220px"><em>2</em> · Alipay</div>
    <div class="u card3 ctr" id="ali" style="left:540px;top:340px;background:linear-gradient(135deg,#3BA6F5,#1677FF)"><div class="chip" style="background:#fff"></div><div class="num">portefeuille · Taobao</div><div class="nm" style="font-size:44px">Alipay</div></div>
    <div class="u pill ink big" id="a1" style="left:540px;top:780px"><div class="pi">1</div>crée ton compte</div>
    <div class="u pill ink big" id="a2" style="left:540px;top:900px"><div class="pi">2</div>ton passeport<svg class="ck"><use href="#i-check"/></svg></div>
    <div class="u pill ink big" id="a3" style="left:540px;top:1020px"><div class="pi">3</div>relie ta Visa<svg class="ck"><use href="#i-check"/></svg></div>

    <!-- 7 · carte crypto -->
    <div class="u ban ctr" id="b3" style="left:540px;top:220px"><em>3</em> · une carte crypto</div>
    <div class="u card3 ctr" id="cry" style="left:540px;top:340px;background:linear-gradient(135deg,#6A4BD8,#2A1E5C)"><div class="chip"></div><div class="num">rechargeable</div><div class="nm" style="font-size:42px">CRYPTO</div><div class="br" style="font-size:40px">₿</div></div>
    <div class="u coin" id="cr1" style="left:330px;top:760px">₿</div>
    <div class="u coin" id="cr2" style="left:640px;top:760px">$</div>
    <div class="u pill ink big" id="dispo" style="left:540px;top:960px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-pin"/></svg></div>dispo dans ton pays ?</div>

    <!-- 8 · le petit test -->
    <div class="u st" id="tTest" style="top:240px"><span class="tag">// un conseil</span><h2>Un petit <span class="k" id="kTest">paiement test<i></i></span></h2></div>
    <div class="u ink ctr score" id="ok1" style="left:540px;top:520px">ça passe <small>→ TU COMMANDES</small><svg class="ck" style="width:70px;height:70px"><use href="#i-check"/></svg></div>
    <div class="u ink ctr score" id="ok2" style="left:540px;top:700px">ça bloque <small>→ RIEN PERDU</small></div>

    <!-- 9 · l'offre + CHINE -->
    <div class="u ink ctr" id="accomp" style="left:540px;top:300px">
      <div class="hd">On le fait ensemble</div><span class="tag">// je t'accompagne</span>
      <div id="steps4"><div class="s" id="sa">1</div><div class="ln"><b id="la"></b></div><div class="s" id="sb">2</div><div class="ln"><b id="lb"></b></div><div class="s" id="sc">3</div><div class="ln"><b id="lc"></b></div><div class="s" id="sd">4</div></div>
      <div class="fin" id="fin1">jusqu'à ton <span class="k" id="kArt">premier article<i></i></span></div>
    </div>
    <div class="u stamp ctr" id="prix" style="left:540px;top:880px">MOINS DE 60 000 Ar</div>
    <div class="u ink ctr" id="cIn" style="left:540px;top:1040px"><small>commentaire :</small><span id="typed"></span></div>

    <!-- 10 · partage -->
    <div class="u st" id="tEnv" style="top:250px"><span class="tag">// à quelqu'un qui commande en Chine</span><h2>Envoie-la.</h2></div>
    <div class="u" id="shareB" style="left:180px;top:610px"><svg><use href="#i-plane"/></svg></div>
    <div class="u ink" id="vcard" style="left:218px;top:605px"><svg><use href="#i-yt"/></svg></div>
    <div class="u pill ink big" id="ami" style="left:780px;top:710px"><div class="pi" style="background:#F6C21C">M</div><div><span>Mialy</span><small>commande en Chine</small></div></div>'''

new_ui = '''    <!-- 1 · la page de paiement (première ET dernière image, à gauche du présentateur) -->
    <div class="u ink ctr" id="chk" style="left:330px;top:380px"><div class="scr">
      <div class="hd">TAOBAO · panier</div>
      <div class="pr"><svg viewBox="0 0 120 120"><use href="#i-gadget"/></svg></div>
      <div class="px">¥ 89<small>+ livraison</small></div>
      <div id="payBtn">Payer</div>
      <div id="refus">✕ Carte refusée</div>
    </div><svg id="tap" viewBox="0 0 120 120"><use href="#i-finger"/></svg></div>

    <!-- 2 · ça arrive à tout le monde (présentateur au centre en grand) -->
    <div class="u crowd ctr" id="crowd" style="left:540px;top:260px">
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
    </div>
    <div class="u st" id="tTout" style="top:370px"><span class="tag">// presque tout le monde</span><h2>Plateformes <span class="it">+</span> paiement</h2></div>
    <div class="u ink ctr cd" id="save" style="left:540px;top:540px"><svg viewBox="0 0 120 120"><use href="#i-bookmark"/></svg><b>enregistre-la</b></div>

    <!-- 3 · les plateformes (à droite du présentateur) -->
    <div class="u ban ctr" id="bP" style="left:770px;top:170px">les <em>plateformes</em></div>
    <div class="u ink plat ctr" id="p1" style="left:770px;top:310px"><i style="background:#FF6A00"></i><b>Taobao</b><span>le plus de choix, prix bas<br>en chinois</span></div>
    <div class="u ink plat ctr" id="p2" style="left:770px;top:540px"><i style="background:#F6C21C"></i><b>1688</b><span>prix d'usine<br>pour acheter en gros</span></div>
    <div class="u ink plat ctr" id="p3" style="left:770px;top:770px"><i style="background:#E0402A"></i><b>AliExpress</b><span>en français, livré chez toi<br>mais plus cher</span></div>
    <div class="u ink plat ctr" id="p4" style="left:770px;top:1000px"><i style="background:#7CC8F2"></i><b>Alibaba</b><span>pour les grosses<br>quantités</span></div>

    <!-- 4 · trois solutions (autour du présentateur au centre) -->
    <div class="u st" id="t3s" style="top:220px"><span class="tag">// le paiement</span><h2>3 <span class="k" id="kSol">solutions<i></i></span></h2></div>
    <div class="u num3" id="n1" style="left:160px;top:480px">1</div>
    <div class="u num3" id="n2" style="left:435px;top:400px">2</div>
    <div class="u num3" id="n3" style="left:710px;top:480px">3</div>

    <!-- 5 · la Visa Akory (à gauche du présentateur) -->
    <div class="u ban ctr" id="b1" style="left:340px;top:190px"><em>1</em> · une carte Visa</div>
    <div class="u card3 ctr" id="visa" style="left:340px;top:380px;background:linear-gradient(135deg,#FF7A00,#E0402A)"><div class="chip"></div><div class="num">•••• •••• •••• 2026</div><div class="nm">AKORY</div><div class="br">VISA</div></div>
    <div class="u ink ctr" id="dial" style="left:340px;top:760px">#144# → 6</div>
    <div class="u ink ctr" id="globeOk" style="left:340px;top:900px"><svg viewBox="0 0 120 120"><use href="#i-globe"/></svg>sites internationaux<svg viewBox="0 0 64 64" style="width:56px;height:56px"><use href="#i-check"/></svg></div>

    <!-- 6 · Alipay (à droite du présentateur) -->
    <div class="u ban ctr" id="b2" style="left:740px;top:190px"><em>2</em> · Alipay</div>
    <div class="u card3 ctr" id="ali" style="left:740px;top:380px;background:linear-gradient(135deg,#3BA6F5,#1677FF)"><div class="chip" style="background:#fff"></div><div class="num">portefeuille · Taobao</div><div class="nm" style="font-size:44px">Alipay</div></div>
    <div class="u pill ink big ctr" id="a1" style="left:740px;top:740px"><div class="pi">1</div>crée ton compte</div>
    <div class="u pill ink big ctr" id="a2" style="left:740px;top:870px"><div class="pi">2</div>ton passeport<svg class="ck"><use href="#i-check"/></svg></div>
    <div class="u pill ink big ctr" id="a3" style="left:740px;top:1000px"><div class="pi">3</div>relie ta Visa<svg class="ck"><use href="#i-check"/></svg></div>

    <!-- 7 · carte crypto (à gauche du présentateur) -->
    <div class="u ban ctr" id="b3" style="left:340px;top:190px"><em>3</em> · une carte crypto</div>
    <div class="u card3 ctr" id="cry" style="left:340px;top:380px;background:linear-gradient(135deg,#6A4BD8,#2A1E5C)"><div class="chip"></div><div class="num">rechargeable</div><div class="nm" style="font-size:42px">CRYPTO</div><div class="br" style="font-size:40px">₿</div></div>
    <div class="u coin" id="cr1" style="left:240px;top:300px">₿</div>
    <div class="u coin" id="cr2" style="left:440px;top:300px">$</div>
    <div class="u pill ink big ctr" id="dispo" style="left:340px;top:760px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-pin"/></svg></div>dispo dans ton pays ?</div>

    <!-- 8 · le petit test (présentateur au centre en grand) -->
    <div class="u st" id="tTest" style="top:190px"><span class="tag">// un conseil</span><h2>Un petit <span class="k" id="kTest">paiement test<i></i></span></h2></div>
    <div class="u ink ctr score" id="ok1" style="left:540px;top:440px">ça passe <small>→ TU COMMANDES</small><svg class="ck" style="width:70px;height:70px"><use href="#i-check"/></svg></div>
    <div class="u ink ctr score" id="ok2" style="left:540px;top:600px">ça bloque <small>→ RIEN PERDU</small></div>

    <!-- 9 · l'offre + CHINE (présentateur au centre) -->
    <div class="u ink ctr" id="accomp" style="left:540px;top:230px">
      <div class="hd">On le fait ensemble</div><span class="tag">// je t'accompagne</span>
      <div id="steps4"><div class="s" id="sa">1</div><div class="ln"><b id="la"></b></div><div class="s" id="sb">2</div><div class="ln"><b id="lb"></b></div><div class="s" id="sc">3</div><div class="ln"><b id="lc"></b></div><div class="s" id="sd">4</div></div>
      <div class="fin" id="fin1">jusqu'à ton <span class="k" id="kArt">premier article<i></i></span></div>
    </div>
    <div class="u stamp ctr" id="prix" style="left:540px;top:470px">MOINS DE 60 000 Ar</div>
    <div class="u ink ctr" id="cIn" style="left:540px;top:620px"><small>commentaire :</small><span id="typed"></span></div>

    <!-- 10 · partage -->
    <div class="u st" id="tEnv" style="top:220px"><span class="tag">// à quelqu'un qui commande en Chine</span><h2>Envoie-la.</h2></div>
    <div class="u" id="shareB" style="left:180px;top:560px"><svg><use href="#i-plane"/></svg></div>
    <div class="u ink" id="vcard" style="left:218px;top:555px"><svg><use href="#i-yt"/></svg></div>
    <div class="u pill ink big" id="ami" style="left:760px;top:640px"><div class="pi" style="background:#F6C21C">M</div><div><span>Mialy</span><small>commande en Chine</small></div></div>'''

c = c.replace(old_ui.replace('\n', '\r\n'), new_ui.replace('\n', '\r\n'))

# 3. Update life(t) head reactions
old_life_intro = '''  let eyeT, headT, exprT, msT;

  const life = (t) => {'''

new_life_intro = '''  let eyeT, headT, exprT, msT;
  // v3 · réactions de tête : « non » (secoue) et « oui » (hoche), amorties
  const SHK = [], NODS = [];
  const wobble = (list, t, f, k) => list.reduce((s, a) => { const x = t - a; return x > 0 && x < 1 ? s + Math.sin(x * 2 * Math.PI * f) * Math.exp(-x * k) : s; }, 0);

  const life = (t) => {'''

c = c.replace(old_life_intro.replace('\n', '\r\n'), new_life_intro.replace('\n', '\r\n'))

old_yaw_pitch = '''    const yaw = hx * 0.95, pitch = hy * 0.5 + 5 * nod;
    // corps : respiration, léger balancement du poids
    P_.style.translate = `0 ${(-5 * br).toFixed(2)}px`;
    P_.style.rotate = `${(0.6 * sway).toFixed(3)}deg`;
    // tête : roulis (accents, questions, contre-balancement), un peu de suivi du regard, hochement
    TETE.style.rotate = `${(-0.45 * sway + 1.5 * roll + qTilt(t) + 0.5 * Math.sin((2 * Math.PI * t) / PER(4.7))).toFixed(3)}deg`;'''

new_yaw_pitch = '''    const shk = wobble(SHK, t, 3.2, 4), ndy = wobble(NODS, t, 2.6, 4.5);
    const yaw = hx * 0.95 + 9 * shk, pitch = hy * 0.5 + 8 * nod + 7 * ndy;
    // corps dynamique v3 : respiration, balancement, élan
    P_.style.translate = `${(6 * sway + 3 * roll).toFixed(2)}px ${(-9 * br - 4 * beat).toFixed(2)}px`;
    P_.style.rotate = `${(1.4 * sway + 0.8 * roll).toFixed(3)}deg`;
    // tête : roulis, suivi du regard, hochements
    TETE.style.rotate = `${(-0.8 * sway + 2.6 * roll + 2.5 * shk + qTilt(t) + 0.8 * Math.sin((2 * Math.PI * t) / PER(4.7))).toFixed(3)}deg`;'''

c = c.replace(old_yaw_pitch.replace('\n', '\r\n'), new_yaw_pitch.replace('\n', '\r\n'))

old_hands = '''    MP.style.translate = `0 ${(7 * beat - 3 * Math.sin((2 * Math.PI * t) / PER(2.3))).toFixed(2)}px`;
    MP.style.rotate = `${(-4 * beat + settle).toFixed(2)}deg`;
    MO.style.rotate = `${(3 * Math.sin((2 * Math.PI * t) / PER(2.4)) - 3 * beat + settle).toFixed(2)}deg`;'''

new_hands = '''    MP.style.translate = `0 ${(13 * beat - 5 * Math.sin((2 * Math.PI * t) / PER(2.3))).toFixed(2)}px`;
    MP.style.rotate = `${(-8 * beat + settle).toFixed(2)}deg`;
    MO.style.rotate = `${(6 * Math.sin((2 * Math.PI * t) / PER(2.4)) - 6 * beat + settle).toFixed(2)}deg`;'''

c = c.replace(old_hands.replace('\n', '\r\n'), new_hands.replace('\n', '\r\n'))

# 4. Update initial positioning & full timeline
old_tl = '''  const LIFE = { t: 0 }; tl.fromTo(LIFE, { t: 0 }, { t: DURATION, duration: DURATION, ease: "none", immediateRender: false, onUpdate: () => life(LIFE.t) }, 0);
  gsap.set("#persoW", { x: 43, y: 196, scaleX: 0.8, scaleY: 0.8 });
  tl.fromTo("#paper", { x: 0, y: 0 }, { x: -36, y: -36, duration: DURATION, ease: "none", immediateRender: false }, 0);
  gsap.set("#cam", { transformOrigin: "50% 40%" });
  // =====================================================================
  // LES SCÈNES · « Plateformes chinoises + comment payer »
  // =====================================================================
  const tCliques = S("cliques"), tRefusee = S("refusee"), tArrive = S("ca arrive"), tAlors = S("alors voici"), tEnr = S("enregistre");
  const tDabord = S("dabord"), tTaob = S("taobao", 0, find("dabord")), t1688 = S("1688"), tAli = S("aliexpress"), tAlib = S("alibaba"), tQuant = S("quantites");
  const tMaint = S("maintenant"), tSolu = S("solutions");
  const tUn = S("un une carte visa"), tOrange = S("orange money"), tAkory = S("akory"), tActive = S("sactive"), tInter = S("internationaux");
  const tDeux = S("deux alipay"), tPortef = S("portefeuille"), tCrees = S("tu crees"), tPass = S("passeport"), tRelies = S("relies");
  const tTroisC = S("trois une carte crypto"), tRedot = S("redotpay"), tRech = S("recharges"), tVerif = S("verifie juste");
  const tConseil = S("un conseil"), tTest = S("test"), tPasse = S("si ca passe"), tBloque = S("si ca bloque");
  const tEnsemble = S("ensemble"), tPremier = S("premier"), tPour = S("pour moins"), tEcris = S("ecris"), tCHINE = S("chine", 0, find("ecris"));
  const tEnvoie = S("envoie"), tVid = S("video", 0, find("envoie")), tQqn = S("quelquun"), tDis = S("et dis-lui");

  // ========== 1 · LA PAGE DE PAIEMENT (première et dernière image) ==========
  tl.set("#chk", { autoAlpha: 1, x: 0, y: 0, scale: 1, rotation: 0 }, 0); tl.set("#refus", { autoAlpha: 0 }, 0); tl.set("#tap", { autoAlpha: 0 }, 0);
  tl.fromTo("#tap", { autoAlpha: 0, x: 120, y: 160 }, { autoAlpha: 1, x: 0, y: 0, duration: 0.4, ease: "power3.out", immediateRender: false }, tCliques - 0.4);
  tl.fromTo("#payBtn", { scale: 1 }, { scale: 0.92, duration: 0.1, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, tCliques + 0.25); SFX("tick", tCliques + 0.25, -20);
  tl.to("#tap", { autoAlpha: 0, duration: 0.25 }, tRefusee - 0.6);
  tl.fromTo("#refus", { autoAlpha: 0, y: -40, scale: 0.8 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.3, ease: "back.out(2.5)", immediateRender: false }, tRefusee - 0.05); SFX("error", tRefusee, -18);
  tl.fromTo("#chk", { x: 0 }, { x: 14, duration: 0.05, yoyo: true, repeat: 7, ease: "none", immediateRender: false }, tRefusee);
  tl.to("#chk", { autoAlpha: 0, y: -80, scale: 0.9, filter: B(10), duration: 0.4, ease: "power3.in" }, tArrive - 0.3);
  tl.set("#refus", { autoAlpha: 0 }, tArrive + 0.3); // la dernière image remontre la page sans le refus

  // ========== 2 · ÇA ARRIVE À TOUT LE MONDE ==========
  IN("#crowd", tArrive - 0.05, { y: 30 });
  ["1", "2", "3", "4", "5"].forEach((n, i) => XPOP(`#crowd span:nth-child(${n}) i`, tArrive + 0.3 + i * 0.1)); SFX("error", tArrive + 0.4, -26);
  OUT("#crowd", tAlors - 0.2);
  IN("#tTout", tAlors - 0.05, { y: 26 });
  hide("#save"); tl.fromTo("#save", { autoAlpha: 0, y: -120, rotation: -8 }, { autoAlpha: 1, y: 0, rotation: 0, duration: 0.5, ease: "bounce.out", immediateRender: false }, tEnr - 0.1); SFX("thud", tEnr + 0.25, -22);
  OUT("#tTout, #save", tDabord - 0.3);

  // ========== 3 · LES PLATEFORMES ==========
  IN("#bP", tDabord - 0.05, { y: -30 }); SFX("whip", tDabord, -22);
  [["#p1", tTaob], ["#p2", t1688], ["#p3", tAli], ["#p4", tAlib]].forEach(([p, t], i) => { IN(p, t - 0.15, { y: 40, s: 0.9 }); SFX("card", t, -23); });
  OUT("#bP, #p1, #p2, #p3, #p4", tMaint - 0.3);

  // ========== 4 · TROIS SOLUTIONS ==========
  IN("#t3s", tMaint - 0.05, { y: 26 }); HL("kSol", tSolu); SFX("pop", tSolu, -22);
  ["#n1", "#n2", "#n3"].forEach((n, i) => { POP(n, tSolu - 0.45 + i * 0.1, 0.3); SFX("ding" + i, tSolu - 0.4 + i * 0.1, -22); });
  OUT("#t3s, #n1, #n2, #n3", tUn + 0.5, 0.3);

  // ========== 5 · LA VISA AKORY ==========
  IN("#b1", tUn + 0.75, { y: -30 }); SFX("whip", tUn + 0.8, -22);
  hide("#visa"); tl.fromTo("#visa", { autoAlpha: 0, rotationY: 80, scale: 0.8 }, { autoAlpha: 1, rotationY: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, tOrange - 0.2); SFX("card", tOrange, -21);
  PULSE("#visa", tAkory, 1.05);
  IN("#dial", tActive - 0.1, { y: 30 }); SFX("keys", tActive, -24);
  IN("#globeOk", tInter - 0.3, { y: 24 }); SFX("ding1", tInter, -22);
  OUT("#b1, #visa, #dial, #globeOk", tDeux - 0.3);

  // ========== 6 · ALIPAY ==========
  IN("#b2", tDeux - 0.05, { y: -30 }); SFX("whip", tDeux, -22);
  hide("#ali"); tl.fromTo("#ali", { autoAlpha: 0, rotationY: 80, scale: 0.8 }, { autoAlpha: 1, rotationY: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, tPortef - 0.3); SFX("card", tPortef, -21);
  IN("#a1", tCrees - 0.1, { x: -60, y: 0 }); SFX("tick", tCrees, -23);
  IN("#a2", tPass - 0.5, { x: -60, y: 0 }); XPOP("#a2 .ck", tPass + 0.2); SFX("ding0", tPass + 0.2, -22);
  IN("#a3", tRelies - 0.1, { x: -60, y: 0 }); XPOP("#a3 .ck", tRelies + 0.6); SFX("ding1", tRelies + 0.6, -22);
  OUT("#b2, #ali, #a1, #a2, #a3", tTroisC - 0.3);

  // ========== 7 · LA CARTE CRYPTO ==========
  IN("#b3", tTroisC - 0.05, { y: -30 }); SFX("whip", tTroisC, -22);
  hide("#cry"); tl.fromTo("#cry", { autoAlpha: 0, rotationY: 80, scale: 0.8 }, { autoAlpha: 1, rotationY: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, tRedot - 0.3); SFX("card", tRedot, -21);
  [["#cr1", 0], ["#cr2", 0.15]].forEach(([c, d]) => { hide(c); tl.fromTo(c, { autoAlpha: 0, y: 120 }, { autoAlpha: 1, y: -200, duration: 0.6, ease: "power2.out", immediateRender: false }, tRech + d); tl.to(c, { autoAlpha: 0, scale: 0.4, duration: 0.25 }, tRech + d + 0.55); });
  SFX("coins", tRech + 0.2, -23);
  IN("#dispo", tVerif - 0.1, { y: 30 }); SFX("pop", tVerif, -22);
  OUT("#b3, #cry, #dispo", tConseil - 0.3);

  // ========== 8 · LE PETIT TEST ==========
  IN("#tTest", tConseil - 0.05, { y: 26 }); HL("kTest", tTest); SFX("pop", tTest, -22);
  IN("#ok1", tPasse - 0.05, { x: -60, y: 0 }); SFX("ding2", tPasse + 0.3, -21);
  IN("#ok2", tBloque - 0.05, { x: -60, y: 0 }); SFX("tick", tBloque + 0.3, -22);
  OUT("#tTest, #ok1, #ok2", tEnsemble - 0.6);

  // ========== 9 · L'OFFRE ET « CHINE » ==========
  IN("#accomp", tEnsemble - 0.5, { y: 50, s: 0.94 }); SFX("card", tEnsemble - 0.4, -21);
  [["#sa", "#la"], ["#sb", "#lb"], ["#sc", "#lc"], ["#sd", null]].forEach(([s, l], i) => { const t = tEnsemble + 0.2 + i * 0.3;
    tl.fromTo(s, { backgroundColor: "#ffffff", color: "#141414" }, { backgroundColor: "#141414", color: "#ffffff", duration: 0.2, immediateRender: false }, t); SFX("tick", t, -24);
    if (l) { tl.set(l, { scaleX: 0 }, 0); tl.fromTo(l, { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power2.out", immediateRender: false }, t + 0.1); } });
  hide("#fin1"); tl.fromTo("#fin1", { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.3, immediateRender: false }, tPremier - 0.4); HL("kArt", tPremier); SFX("ding2", tPremier, -20);
  STAMP("#prix", tPour + 0.3, -5); SFX("stamp", tPour + 0.3, -18);
  IN("#cIn", tEcris - 0.1, { y: 30 });
  ["C", "CH", "CHI", "CHIN", "CHINE"].forEach((s, i) => tl.set("#typed", { textContent: s }, tCHINE - 0.2 + i * 0.07)); tl.set("#typed", { textContent: "" }, 0); SFX("keys", tCHINE - 0.2, -24);
  OUT("#accomp, #prix, #cIn", tEnvoie - 0.3);

  // ========== 10 · ENVOIE-LA… ET LA BOUCLE ==========
  IN("#tEnv", tEnvoie - 0.05, { y: 26 });
  POP("#shareB", tEnvoie, 0.4); SFX("pop", tEnvoie + 0.05, -22);
  hide("#vcard"); tl.fromTo("#vcard", { autoAlpha: 0, scale: 0.5, rotation: -12 }, { autoAlpha: 1, scale: 1, rotation: -6, duration: 0.3, ease: "back.out(2)", immediateRender: false }, tVid - 0.05);
  tl.fromTo("#vcard", { x: 0 }, { x: 520, duration: 0.75, ease: "power1.inOut", immediateRender: false }, tVid + 0.3);
  tl.fromTo("#vcard", { y: 0 }, { y: -100, duration: 0.375, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, tVid + 0.3);
  tl.to("#vcard", { scale: 0.3, autoAlpha: 0, rotation: 10, duration: 0.2, ease: "power2.in" }, tVid + 0.9); SFX("whip", tVid + 0.3, -22);
  POP("#ami", tQqn - 0.15, 0.4); PULSE("#ami", tVid + 1.05, 1.1); SFX("ding2", tVid + 1.05, -21);
  OUT("#tEnv, #shareB, #ami", tDis - 0.3);
  tl.fromTo("#chk", { autoAlpha: 0, y: 90, scale: 0.9, filter: B(10) }, { autoAlpha: 1, y: 0, scale: 1, filter: B(0), duration: 0.55, ease: "back.out(1.4)", immediateRender: false }, tDis - 0.05); SFX("card", tDis + 0.05, -21);

  // ---------- jeu d'acteur ----------
  [[tRefusee - 0.1, "surpris"], [tArrive - 0.1, "parle", "salue"], [tEnr - 0.05, "content", "pointe"], [tDabord - 0.1, "parle"], [tAli - 0.1, "sceptique"], [tAlib - 0.1, "parle"],
   [tMaint - 0.1, "insiste", "pointe"], [tOrange - 0.1, "content", "salue"], [tDeux - 0.1, "parle", "pointe"], [tPass - 0.1, "insiste"], [tTroisC - 0.1, "malin", "croise"], [tVerif - 0.1, "sceptique"],
   [tConseil - 0.1, "insiste", "pointe"], [tPasse - 0.05, "content"], [tBloque - 0.05, "parle", "salue"], [tEnsemble - 0.4, "content"], [tPour - 0.05, "malin", "pointe"],
   [tEcris - 0.05, "insiste"], [tEnvoie - 0.05, "content", "salue"], [tDis - 0.1, INIT_EXPR, INIT_POSE]].forEach(([t, e, p]) => ACT(t, e, p));
  // ---------- regard ----------
  [[0, -2, -10], [tArrive, 0, -4], [tAlors + 0.3, 0, 0], [tDabord, 0, -8], [tTaob, -8, -9], [t1688, 8, -9], [tAli, -8, -6], [tAlib, 8, -6], [tMaint, 0, 0],
   [tUn, 0, -9], [tActive, -2, -5], [tInter + 0.4, 0, 0], [tDeux, 0, -9], [tCrees, -3, -4], [tRelies + 0.6, 0, 0], [tTroisC, 0, -9], [tVerif, -2, -3], [tConseil, 0, 0],
   [tPasse, -2, -7], [tBloque + 0.5, 0, 0], [tEnsemble, 0, -9], [tPour, 0, -3], [tEcris + 0.6, 0, 0], [tEnvoie, -8, -6], [tQqn, 9, -6], [tDis - 0.2, -2, -10]].forEach(([t, x, y]) => LOOK(t, x, y));'''

new_tl = '''  const LIFE = { t: 0 }; tl.fromTo(LIFE, { t: 0 }, { t: DURATION, duration: DURATION, ease: "none", immediateRender: false, onUpdate: () => life(LIFE.t) }, 0);
  // v3 · Positionnement initial pour la boucle parfaite : personnage à droite, smartphone à gauche
  const POS_INIT = { x: 210, y: 30, s: 0.95 };
  gsap.set("#persoW", { x: POS_INIT.x, y: POS_INIT.y, scaleX: POS_INIT.s, scaleY: POS_INIT.s });
  tl.fromTo("#paper", { x: 0, y: 0 }, { x: -36, y: -36, duration: DURATION, ease: "none", immediateRender: false }, 0);
  gsap.set("#cam", { transformOrigin: "50% 40%" });

  // =====================================================================
  // LES SCÈNES v3 · Mise en scène dynamique : le présentateur acteur principal
  // =====================================================================
  const tCliques = S("cliques"), tRefusee = S("refusee"), tArrive = S("ca arrive"), tAlors = S("alors voici"), tEnr = S("enregistre");
  const tDabord = S("dabord"), tTaob = S("taobao", 0, find("dabord")), t1688 = S("1688"), tAli = S("aliexpress"), tAlib = S("alibaba"), tQuant = S("quantites");
  const tMaint = S("maintenant"), tSolu = S("solutions");
  const tUn = S("un une carte visa"), tOrange = S("orange money"), tAkory = S("akory"), tActive = S("sactive"), tInter = S("internationaux");
  const tDeux = S("deux alipay"), tPortef = S("portefeuille"), tCrees = S("tu crees"), tPass = S("passeport"), tRelies = S("relies");
  const tTroisC = S("trois une carte crypto"), tRedot = S("redotpay"), tRech = S("recharges"), tVerif = S("verifie juste");
  const tConseil = S("un conseil"), tTest = S("test"), tPasse = S("si ca passe"), tBloque = S("si ca bloque");
  const tEnsemble = S("ensemble"), tPremier = S("premier"), tPour = S("pour moins"), tEcris = S("ecris"), tCHINE = S("chine", 0, find("ecris"));
  const tEnvoie = S("envoie"), tVid = S("video", 0, find("envoie")), tQqn = S("quelquun"), tDis = S("et dis-lui");

  // Re-initialisation explicite au point zéro (boucle parfaite)
  tl.set("#persoW", { x: POS_INIT.x, y: POS_INIT.y, scaleX: POS_INIT.s, scaleY: POS_INIT.s }, 0);
  tl.set("#chk", { autoAlpha: 1, x: 0, y: 0, scale: 1, rotation: 0 }, 0);
  tl.set("#refus", { autoAlpha: 0 }, 0);
  tl.set("#tap", { autoAlpha: 0 }, 0);

  // ========== 1 · LA PAGE DE PAIEMENT (0 à 8s) ==========
  tl.fromTo("#tap", { autoAlpha: 0, x: 120, y: 160 }, { autoAlpha: 1, x: 0, y: 0, duration: 0.4, ease: "power3.out", immediateRender: false }, tCliques - 0.4);
  tl.fromTo("#payBtn", { scale: 1 }, { scale: 0.92, duration: 0.1, yoyo: true, repeat: 1, ease: "power2.out", immediateRender: false }, tCliques + 0.25); SFX("tick", tCliques + 0.25, -20);
  tl.to("#tap", { autoAlpha: 0, duration: 0.25 }, tRefusee - 0.6);

  // Refus : sursaut, secousse, caméra shake
  tl.fromTo("#refus", { autoAlpha: 0, y: -40, scale: 0.8 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.3, ease: "back.out(2.5)", immediateRender: false }, tRefusee - 0.05); SFX("error", tRefusee, -18);
  tl.fromTo("#chk", { x: 0 }, { x: 16, duration: 0.05, yoyo: true, repeat: 7, ease: "none", immediateRender: false }, tRefusee);
  tl.to("#persoW", { x: 240, y: 60, duration: 0.15, yoyo: true, repeat: 1, ease: "power2.out" }, tRefusee);
  tl.fromTo("#cam", { scale: 1 }, { scale: 1.05, duration: 0.2, yoyo: true, repeat: 1, ease: "power2.out" }, tRefusee);
  SHK.push(tRefusee + 0.2);

  // Disparition smartphone vers la gauche
  tl.to("#chk", { autoAlpha: 0, x: -450, scale: 0.85, filter: B(10), duration: 0.45, ease: "power3.in" }, tArrive - 0.3);
  tl.set("#refus", { autoAlpha: 0 }, tArrive + 0.3);

  // ========== 2 · ÇA ARRIVE À TOUT LE MONDE (présentateur au GRAND CENTRE) ==========
  tl.to("#persoW", { x: 43, y: -140, scaleX: 1.18, scaleY: 1.18, duration: 0.6, ease: "power2.out" }, tArrive - 0.25);
  IN("#crowd", tArrive - 0.05, { y: 30 });
  ["1", "2", "3", "4", "5"].forEach((n, i) => XPOP(`#crowd span:nth-child(${n}) i`, tArrive + 0.3 + i * 0.1)); SFX("error", tArrive + 0.4, -26);
  OUT("#crowd", tAlors - 0.2);
  IN("#tTout", tAlors - 0.05, { y: 26 });

  hide("#save");
  tl.fromTo("#save", { autoAlpha: 0, y: -120, rotation: -8 }, { autoAlpha: 1, y: 0, rotation: 0, duration: 0.5, ease: "bounce.out", immediateRender: false }, tEnr - 0.1);
  tl.to("#persoW", { y: -160, duration: 0.2, yoyo: true, repeat: 1, ease: "back.out(2)" }, tEnr);
  SFX("thud", tEnr + 0.25, -22);
  NODS.push(tEnr + 0.1);
  OUT("#tTout, #save", tDabord - 0.3);

  // ========== 3 · LES PLATEFORMES (présentateur à GAUCHE, plateformes à DROITE) ==========
  tl.to("#persoW", { x: -240, y: 30, scaleX: 0.95, scaleY: 0.95, duration: 0.6, ease: "power2.inOut" }, tDabord - 0.25);
  IN("#bP", tDabord - 0.05, { y: -30 }); SFX("whip", tDabord, -22);
  [["#p1", tTaob], ["#p2", t1688], ["#p3", tAli], ["#p4", tAlib]].forEach(([p, t], i) => {
    IN(p, t - 0.15, { x: 60, s: 0.92 });
    PULSE("#persoPop", t, 1.03);
    SFX("card", t, -23);
  });
  OUT("#bP, #p1, #p2, #p3, #p4", tMaint - 0.3);

  // ========== 4 · TROIS SOLUTIONS (présentateur au GRAND CENTRE) ==========
  tl.to("#persoW", { x: 43, y: -160, scaleX: 1.2, scaleY: 1.2, duration: 0.55, ease: "power2.out" }, tMaint - 0.25);
  IN("#t3s", tMaint - 0.05, { y: 26 }); HL("kSol", tSolu); SFX("pop", tSolu, -22);
  ["#n1", "#n2", "#n3"].forEach((n, i) => { POP(n, tSolu - 0.45 + i * 0.1, 0.3); SFX("ding" + i, tSolu - 0.4 + i * 0.1, -22); });
  OUT("#t3s, #n1, #n2, #n3", tUn + 0.4, 0.3);

  // ========== 5 · LA VISA AKORY (présentateur à DROITE, Visa à GAUCHE) ==========
  tl.to("#persoW", { x: 230, y: 30, scaleX: 0.95, scaleY: 0.95, duration: 0.6, ease: "power2.inOut" }, tUn + 0.25);
  IN("#b1", tUn + 0.75, { y: -30 }); SFX("whip", tUn + 0.8, -22);
  hide("#visa"); tl.fromTo("#visa", { autoAlpha: 0, rotationY: 80, scale: 0.8 }, { autoAlpha: 1, rotationY: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, tOrange - 0.2); SFX("card", tOrange, -21);
  PULSE("#visa", tAkory, 1.05);
  IN("#dial", tActive - 0.1, { y: 30 }); SFX("keys", tActive, -24);
  IN("#globeOk", tInter - 0.3, { y: 24 }); SFX("ding1", tInter, -22);
  OUT("#b1, #visa, #dial, #globeOk", tDeux - 0.3);

  // ========== 6 · ALIPAY (présentateur à GAUCHE, étapes à DROITE) ==========
  tl.to("#persoW", { x: -230, y: 30, scaleX: 0.95, scaleY: 0.95, duration: 0.6, ease: "power2.inOut" }, tDeux - 0.25);
  IN("#b2", tDeux - 0.05, { y: -30 }); SFX("whip", tDeux, -22);
  hide("#ali"); tl.fromTo("#ali", { autoAlpha: 0, rotationY: 80, scale: 0.8 }, { autoAlpha: 1, rotationY: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, tPortef - 0.3); SFX("card", tPortef, -21);
  IN("#a1", tCrees - 0.1, { x: 60, y: 0 }); SFX("tick", tCrees, -23);
  IN("#a2", tPass - 0.5, { x: 60, y: 0 }); XPOP("#a2 .ck", tPass + 0.2); SFX("ding0", tPass + 0.2, -22);
  IN("#a3", tRelies - 0.1, { x: 60, y: 0 }); XPOP("#a3 .ck", tRelies + 0.6); SFX("ding1", tRelies + 0.6, -22);
  NODS.push(tRelies + 0.4);
  OUT("#b2, #ali, #a1, #a2, #a3", tTroisC - 0.3);

  // ========== 7 · LA CARTE CRYPTO (présentateur à DROITE, Crypto à GAUCHE) ==========
  tl.to("#persoW", { x: 220, y: 30, scaleX: 0.95, scaleY: 0.95, duration: 0.6, ease: "power2.inOut" }, tTroisC - 0.25);
  IN("#b3", tTroisC - 0.05, { y: -30 }); SFX("whip", tTroisC, -22);
  hide("#cry"); tl.fromTo("#cry", { autoAlpha: 0, rotationY: 80, scale: 0.8 }, { autoAlpha: 1, rotationY: 0, scale: 1, duration: 0.6, ease: "back.out(1.4)", immediateRender: false }, tRedot - 0.3); SFX("card", tRedot, -21);
  [["#cr1", 0], ["#cr2", 0.15]].forEach(([c, d]) => { hide(c); tl.fromTo(c, { autoAlpha: 0, y: 120 }, { autoAlpha: 1, y: -200, duration: 0.6, ease: "power2.out", immediateRender: false }, tRech + d); tl.to(c, { autoAlpha: 0, scale: 0.4, duration: 0.25 }, tRech + d + 0.55); });
  SFX("coins", tRech + 0.2, -23);
  IN("#dispo", tVerif - 0.1, { y: 30 }); SFX("pop", tVerif, -22);
  OUT("#b3, #cry, #dispo", tConseil - 0.3);

  // ========== 8 · LE PETIT TEST (présentateur au GRAND CENTRE EN GROS PLAN) ==========
  tl.to("#persoW", { x: 43, y: -160, scaleX: 1.22, scaleY: 1.22, duration: 0.6, ease: "power2.out" }, tConseil - 0.25);
  IN("#tTest", tConseil - 0.05, { y: 26 }); HL("kTest", tTest); SFX("pop", tTest, -22);
  IN("#ok1", tPasse - 0.05, { y: 20 }); SFX("ding2", tPasse + 0.3, -21); NODS.push(tPasse + 0.2);
  IN("#ok2", tBloque - 0.05, { y: 20 }); SFX("tick", tBloque + 0.3, -22); SHK.push(tBloque + 0.2);
  OUT("#tTest, #ok1, #ok2", tEnsemble - 0.6);

  // ========== 9 · L'OFFRE ET « CHINE » (présentateur au centre) ==========
  tl.to("#persoW", { x: 43, y: -90, scaleX: 1.12, scaleY: 1.12, duration: 0.55, ease: "power2.out" }, tEnsemble - 0.25);
  IN("#accomp", tEnsemble - 0.5, { y: 50, s: 0.94 }); SFX("card", tEnsemble - 0.4, -21);
  [["#sa", "#la"], ["#sb", "#lb"], ["#sc", "#lc"], ["#sd", null]].forEach(([s, l], i) => { const t = tEnsemble + 0.2 + i * 0.3;
    tl.fromTo(s, { backgroundColor: "#ffffff", color: "#141414" }, { backgroundColor: "#141414", color: "#ffffff", duration: 0.2, immediateRender: false }, t); SFX("tick", t, -24);
    if (l) { tl.set(l, { scaleX: 0 }, 0); tl.fromTo(l, { scaleX: 0 }, { scaleX: 1, duration: 0.3, ease: "power2.out", immediateRender: false }, t + 0.1); } });
  hide("#fin1"); tl.fromTo("#fin1", { autoAlpha: 0, y: 16 }, { autoAlpha: 1, y: 0, duration: 0.3, immediateRender: false }, tPremier - 0.4); HL("kArt", tPremier); SFX("ding2", tPremier, -20);
  NODS.push(tPremier);
  STAMP("#prix", tPour + 0.3, -5); SFX("stamp", tPour + 0.3, -18);
  IN("#cIn", tEcris - 0.1, { y: 30 });
  tl.to("#persoW", { y: -115, duration: 0.2, yoyo: true, repeat: 1, ease: "back.out(2)" }, tEcris);
  ["C", "CH", "CHI", "CHIN", "CHINE"].forEach((s, i) => tl.set("#typed", { textContent: s }, tCHINE - 0.2 + i * 0.07)); tl.set("#typed", { textContent: "" }, 0); SFX("keys", tCHINE - 0.2, -24);
  OUT("#accomp, #prix, #cIn", tEnvoie - 0.3);

  // ========== 10 · ENVOIE-LA… ET BOUCLE PARFAITE ==========
  IN("#tEnv", tEnvoie - 0.05, { y: 26 });
  POP("#shareB", tEnvoie, 0.4); SFX("pop", tEnvoie + 0.05, -22);
  tl.to("#persoW", { y: -115, duration: 0.2, yoyo: true, repeat: 1, ease: "back.out(2)" }, tEnvoie);
  hide("#vcard"); tl.fromTo("#vcard", { autoAlpha: 0, scale: 0.5, rotation: -12 }, { autoAlpha: 1, scale: 1, rotation: -6, duration: 0.3, ease: "back.out(2)", immediateRender: false }, tVid - 0.05);
  tl.fromTo("#vcard", { x: 0 }, { x: 520, duration: 0.75, ease: "power1.inOut", immediateRender: false }, tVid + 0.3);
  tl.fromTo("#vcard", { y: 0 }, { y: -100, duration: 0.375, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, tVid + 0.3);
  tl.to("#vcard", { scale: 0.3, autoAlpha: 0, rotation: 10, duration: 0.2, ease: "power2.in" }, tVid + 0.9); SFX("whip", tVid + 0.3, -22);
  POP("#ami", tQqn - 0.15, 0.4); PULSE("#ami", tVid + 1.05, 1.1); SFX("ding2", tVid + 1.05, -21);
  OUT("#tEnv, #shareB, #ami", tDis - 0.3);

  // Retour exact à la position de départ pour fermer la boucle
  tl.to("#persoW", { x: POS_INIT.x, y: POS_INIT.y, scaleX: POS_INIT.s, scaleY: POS_INIT.s, duration: 0.55, ease: "power2.inOut" }, tDis - 0.15);
  tl.fromTo("#chk", { autoAlpha: 0, x: -300, scale: 0.9 }, { autoAlpha: 1, x: 0, scale: 1, duration: 0.55, ease: "back.out(1.4)", immediateRender: false }, tDis - 0.05); SFX("card", tDis + 0.05, -21);

  // ---------- jeu d'acteur v3 ----------
  [[tRefusee - 0.1, "surpris", "croise"], [tArrive - 0.1, "parle", "salue"], [tAlors - 0.05, "malin"], [tEnr - 0.05, "content", "pointe"],
   [tDabord - 0.1, "parle", "pointe"], [t1688 - 0.1, "insiste"], [tAli - 0.1, "sceptique"], [tAlib - 0.1, "parle"],
   [tMaint - 0.1, "insiste", "croise"], [tSolu - 0.05, "content"],
   [tUn + 0.2, "parle", "salue"], [tOrange - 0.1, "content", "salue"], [tInter - 0.1, "insiste"],
   [tDeux - 0.1, "parle", "pointe"], [tPass - 0.1, "insiste"], [tRelies - 0.1, "content"],
   [tTroisC - 0.1, "malin", "croise"], [tRech - 0.1, "parle"], [tVerif - 0.1, "sceptique"],
   [tConseil - 0.1, "insiste", "pointe"], [tPasse - 0.05, "content"], [tBloque - 0.05, "parle", "salue"],
   [tEnsemble - 0.4, "content", "salue"], [tPour - 0.05, "malin", "pointe"],
   [tEcris - 0.05, "insiste", "pointe"], [tEnvoie - 0.05, "content", "salue"],
   [tDis - 0.1, INIT_EXPR, INIT_POSE]].forEach(([t, e, p]) => ACT(t, e, p));

  // ---------- regard v3 synchronisé avec les mouvements ----------
  [[0, -9, -3],
   [tArrive, 0, -2], [tAlors + 0.3, 0, 0],
   [tDabord, 8, -6], [tTaob, 8, -8], [t1688, 8, -5], [tAli, 8, -2], [tAlib, 8, 1],
   [tMaint, 0, -2],
   [tUn, -8, -6], [tOrange, -8, -4], [tActive, -8, 2], [tInter + 0.4, -8, 0],
   [tDeux, 8, -6], [tCrees, 8, -3], [tPass, 8, 0], [tRelies + 0.4, 8, 3],
   [tTroisC, -8, -5], [tRech, -8, -2], [tVerif, -8, 2],
   [tConseil, 0, -2], [tPasse, 0, -4], [tBloque + 0.3, 0, 0],
   [tEnsemble, 0, -3], [tPour, 0, 1], [tEcris + 0.4, 0, 0],
   [tEnvoie, -6, -4], [tQqn, 8, -5],
   [tDis - 0.1, -9, -3]].forEach(([t, x, y]) => LOOK(t, x, y));'''

c = c.replace(old_tl.replace('\n', '\r\n'), new_tl.replace('\n', '\r\n'))

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(c)

print('Success: index-v3.html written!')
