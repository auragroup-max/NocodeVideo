new_timeline = """  const LIFE = { t: 0 }; tl.fromTo(LIFE, { t: 0 }, { t: DURATION, duration: DURATION, ease: "none", immediateRender: false, onUpdate: () => life(LIFE.t) }, 0);
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
   [tDis - 0.1, -9, -3]].forEach(([t, x, y]) => LOOK(t, x, y));\n\n  """

path = r'd:\No Code Video\video-paiement-chine\index-v3.html'
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

p1 = text.find('const LIFE = { t: 0 };')
p2 = text.find('for (let i = 1; i < GK.length; i++)')
assert p1 != -1 and p2 != -1, "Delimiters not found"

result = text[:p1] + new_timeline + text[p2:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(result)

print("Patch applied successfully! New length:", len(result))
