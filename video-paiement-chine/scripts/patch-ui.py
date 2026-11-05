path = r'd:\No Code Video\video-paiement-chine\index-v3.html'
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

p1 = text.find('<div id="ui">')
p_hud = text.find('<div id="hud">')
assert p1 != -1 and p_hud != -1, "UI or HUD not found"

# Find the closing </div> of #ui just before #hud
p2 = text.rfind('</div>', p1, p_hud) + len('</div>')

print('p1:', p1, 'p2:', p2)
print('Current block preview head:\n', text[p1:p1+120])
print('Current block preview tail:\n', text[p2-120:p2])

new_ui = '''<div id="ui">
    <!-- 1 · la page de paiement (à gauche du présentateur qui est à droite) -->
    <div class="u ink ctr" id="chk" style="left:310px;top:380px"><div class="scr">
      <div class="hd">TAOBAO · panier</div>
      <div class="pr"><svg viewBox="0 0 120 120"><use href="#i-gadget"/></svg></div>
      <div class="px">¥ 89<small>+ livraison</small></div>
      <div id="payBtn">Payer</div>
      <div id="refus">✕ Carte refusée</div>
    </div><svg id="tap" viewBox="0 0 120 120"><use href="#i-finger"/></svg></div>

    <!-- 2 · ça arrive à tout le monde (présentateur en grand au centre) -->
    <div class="u crowd ctr" id="crowd" style="left:540px;top:260px">
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
      <span><svg viewBox="0 0 120 120"><use href="#i-person"/></svg><i><svg viewBox="0 0 64 64"><use href="#i-x"/></svg></i></span>
    </div>
    <div class="u st" id="tTout" style="top:370px"><span class="tag">// presque tout le monde</span><h2>Plateformes <span class="it">+</span> paiement</h2></div>
    <div class="u ink ctr cd" id="save" style="left:540px;top:540px"><svg viewBox="0 0 120 120"><use href="#i-bookmark"/></svg><b>enregistre-la</b></div>

    <!-- 3 · les plateformes (à droite du présentateur qui est à gauche) -->
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

    <!-- 5 · la Visa Akory (à gauche du présentateur qui est à droite) -->
    <div class="u ban ctr" id="b1" style="left:320px;top:190px"><em>1</em> · une carte Visa</div>
    <div class="u card3 ctr" id="visa" style="left:320px;top:380px;background:linear-gradient(135deg,#FF7A00,#E0402A)"><div class="chip"></div><div class="num">•••• •••• •••• 2026</div><div class="nm">AKORY</div><div class="br">VISA</div></div>
    <div class="u ink ctr" id="dial" style="left:320px;top:760px">#144# → 6</div>
    <div class="u ink ctr" id="globeOk" style="left:320px;top:900px"><svg viewBox="0 0 120 120"><use href="#i-globe"/></svg>sites internationaux<svg viewBox="0 0 64 64" style="width:56px;height:56px"><use href="#i-check"/></svg></div>

    <!-- 6 · Alipay (à droite du présentateur qui est à gauche) -->
    <div class="u ban ctr" id="b2" style="left:760px;top:190px"><em>2</em> · Alipay</div>
    <div class="u card3 ctr" id="ali" style="left:760px;top:380px;background:linear-gradient(135deg,#3BA6F5,#1677FF)"><div class="chip" style="background:#fff"></div><div class="num">portefeuille · Taobao</div><div class="nm" style="font-size:44px">Alipay</div></div>
    <div class="u pill ink big ctr" id="a1" style="left:760px;top:740px"><div class="pi">1</div>crée ton compte</div>
    <div class="u pill ink big ctr" id="a2" style="left:760px;top:870px"><div class="pi">2</div>ton passeport<svg class="ck"><use href="#i-check"/></svg></div>
    <div class="u pill ink big ctr" id="a3" style="left:760px;top:1000px"><div class="pi">3</div>relie ta Visa<svg class="ck"><use href="#i-check"/></svg></div>

    <!-- 7 · carte crypto (à gauche du présentateur qui est à droite) -->
    <div class="u ban ctr" id="b3" style="left:320px;top:190px"><em>3</em> · une carte crypto</div>
    <div class="u card3 ctr" id="cry" style="left:320px;top:380px;background:linear-gradient(135deg,#6A4BD8,#2A1E5C)"><div class="chip"></div><div class="num">rechargeable</div><div class="nm" style="font-size:42px">CRYPTO</div><div class="br" style="font-size:40px">₿</div></div>
    <div class="u coin" id="cr1" style="left:220px;top:300px">₿</div>
    <div class="u coin" id="cr2" style="left:420px;top:300px">$</div>
    <div class="u pill ink big ctr" id="dispo" style="left:320px;top:760px"><div class="pi" style="border:none;background:none"><svg viewBox="0 0 120 120"><use href="#i-pin"/></svg></div>dispo dans ton pays ?</div>

    <!-- 8 · le petit test (présentateur au centre en gros plan) -->
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
    <div class="u pill ink big" id="ami" style="left:760px;top:640px"><div class="pi" style="background:#F6C21C">M</div><div><span>Mialy</span><small>commande en Chine</small></div></div>
  </div>'''

result = text[:p1] + new_ui + text[p2:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(result)

print("Updated #ui successfully!")
