path = r'd:\No Code Video\video-paiement-chine\index-v3.html'
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

p = text.find('let eyeT, headT, exprT, msT;')
assert p != -1, 'let eyeT not found'
p_end = text.find('const LIFE = { t: 0 };')
assert p_end != -1, 'const LIFE not found'

lines = [
    "let eyeT, headT, exprT, msT;",
    "  // v3 · reactions de tete : non (secoue) et oui (hoche), amorties",
    "  const SHK = [], NODS = [];",
    "  const wobble = (list, t, f, k) => list.reduce((s, a) => { const x = t - a; return x > 0 && x < 1 ? s + Math.sin(x * 2 * Math.PI * f) * Math.exp(-x * k) : s; }, 0);",
    "",
    "  const life = (t) => {",
    "    if (!eyeT) { eyeT = track(GK, 0.13, eOut); headT = track(GK.map(([a, v]) => [a, v]), 0.5, eIO, 0.06); exprT = track(EK, 0.26, eIO); msT = track(MSK, 0.05, eOut); }",
    "    const br = 0.5 + 0.5 * Math.sin((2 * Math.PI * t) / PER(3.4)), sway = Math.sin((2 * Math.PI * t) / PER(7.4));",
    "    let nod = 0, roll = 0, lift = 0, beat = 0;",
    "    for (const a of ACC) { const p = pulse(t - a.t); if (!p) continue; nod += p * a.a; roll += p * a.s * a.a; if (a.br) lift += p * a.a; beat += p * a.a; }",
    "    const o = talking(t) ? clamp(envAt(t) * 1.1) : 0;",
    "    const [gx, gy] = eyeT(t), [hx, hy] = headT(t), [mx, my] = msT(t), e = exprT(t);",
    "    const shk = wobble(SHK, t, 3.2, 4), ndy = wobble(NODS, t, 2.6, 4.5);",
    "    const yaw = hx * 0.95 + 9 * shk, pitch = hy * 0.5 + 8 * nod + 7 * ndy;",
    "    // corps dynamique v3 : respiration, balancement, elan",
    "    P_.style.translate = `${(6 * sway + 3 * roll).toFixed(2)}px ${(-9 * br - 4 * beat).toFixed(2)}px`;",
    "    P_.style.rotate = `${(1.4 * sway + 0.8 * roll).toFixed(3)}deg`;",
    "    // tete : roulis, suivi du regard, hochements",
    "    TETE.style.rotate = `${(-0.8 * sway + 2.6 * roll + 2.5 * shk + qTilt(t) + 0.8 * Math.sin((2 * Math.PI * t) / PER(4.7))).toFixed(3)}deg`;",
    "    TETE.style.translate = `${(hx * 0.35).toFixed(2)}px ${(2 * br + 2.4 * nod + 1.3 * o + hy * 0.18).toFixed(2)}px`;",
    "    // tete en 3/4",
    "    VZ.forEach((g) => (g.style.translate = `${yaw.toFixed(2)}px ${pitch.toFixed(2)}px`));",
    "    NEZ.style.translate = `${(yaw * 0.35).toFixed(2)}px ${(pitch * 0.25).toFixed(2)}px`;",
    "    BARBE.style.translate = `${(yaw * 0.45).toFixed(2)}px ${(pitch * 0.5).toFixed(2)}px`;",
    "    COIFFE.style.translate = `${(yaw * 0.3).toFixed(2)}px ${(-pitch * 0.35).toFixed(2)}px`;",
    "    ORG.style.translate = `${(-0.6 * Math.min(yaw, 0)).toFixed(2)}px ${(-pitch * 0.5).toFixed(2)}px`;",
    "    ORD.style.translate = `${(-0.6 * Math.max(yaw, 0)).toFixed(2)}px ${(-pitch * 0.5).toFixed(2)}px`;",
    "    EYG.style.scale = `${(1 - 0.006 * Math.max(0, -yaw)).toFixed(4)} 1`;",
    "    EYD.style.scale = `${(1 - 0.006 * Math.max(0, yaw)).toFixed(4)} 1`;",
    "    // yeux",
    "    PUPS.forEach((p) => { p.style.transform = `translate(${e[0].toFixed(2)}px, ${e[1].toFixed(2)}px) scale(${e[2].toFixed(3)})`; p.style.translate = `${(gx + mx).toFixed(2)}px ${(gy * 0.8 + my).toFixed(2)}px`; });",
    "    PHG.style.transform = `translateY(${e[3].toFixed(2)}px) rotate(${e[4].toFixed(2)}deg)`;",
    "    PHD.style.transform = `translateY(${e[5].toFixed(2)}px) rotate(${e[6].toFixed(2)}deg)`;",
    "    const bl = blinkAt(t); PHS.forEach((p) => (p.style.translate = `0 ${(72 * bl).toFixed(1)}px`));",
    "    PBS.forEach((p) => { p.style.transform = `translateY(${e[7].toFixed(2)}px)`; p.style.translate = `0 ${(-6 * bl).toFixed(1)}px`; });",
    "    SCG.style.transform = `translateY(${(e[8] - 7 * lift - 2 * bl).toFixed(2)}px) rotate(${e[9].toFixed(2)}deg)`;",
    "    SCD.style.transform = `translateY(${(e[10] - 7 * lift - 2 * bl).toFixed(2)}px) rotate(${e[11].toFixed(2)}deg)`;",
    "    // bouche",
    "    P_.setAttribute('data-talk', o > 0 || talking(t) ? '1' : '0');",
    "    MOUTHS.forEach((m) => (m.style.scale = `${(1 - 0.08 * o).toFixed(3)} ${(0.25 + 0.75 * o).toFixed(3)}`));",
    "    MENTON.style.translate = `0 ${(5 * o).toFixed(2)}px`;",
    "    // mains",
    "    let tp = -9; for (const p of POSES) if (p <= t) tp = p; const dt = t - tp, settle = dt < 1 ? 11 * Math.exp(-dt * 6) * Math.cos(dt * 15) : 0;",
    "    MP.style.translate = `0 ${(13 * beat - 5 * Math.sin((2 * Math.PI * t) / PER(2.3))).toFixed(2)}px`;",
    "    MP.style.rotate = `${(-8 * beat + settle).toFixed(2)}deg`;",
    "    MO.style.rotate = `${(6 * Math.sin((2 * Math.PI * t) / PER(2.4)) - 6 * beat + settle).toFixed(2)}deg`;",
    "  };",
    "  "
]

new_block = "\n".join(lines)
text = text[:p] + new_block + "\n" + text[p_end:]

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated life function successfully!')
