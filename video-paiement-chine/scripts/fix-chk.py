path = r'd:\No Code Video\video-paiement-chine\index-v3.html'
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

text = text.replace(
    'tl.set("#chk", { autoAlpha: 1, x: 0, y: 0, scale: 1, rotation: 0 }, 0);',
    'tl.set("#chk", { autoAlpha: 1, x: 0, y: 0, scale: 1, rotation: 0, filter: B(0) }, 0);'
)
text = text.replace(
    'tl.fromTo("#chk", { autoAlpha: 0, x: -300, scale: 0.9 }, { autoAlpha: 1, x: 0, scale: 1, duration: 0.55, ease: "back.out(1.4)", immediateRender: false }, tDis - 0.05);',
    'tl.fromTo("#chk", { autoAlpha: 0, x: -300, scale: 0.9, filter: B(10) }, { autoAlpha: 1, x: 0, scale: 1, filter: B(0), duration: 0.55, ease: "back.out(1.4)", immediateRender: false }, tDis - 0.05);'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed #chk filter successfully!')
