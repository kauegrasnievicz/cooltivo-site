"""Injeta o sistema de movimento (assets/motion.css e motion.js) nas páginas. Idempotente. Rodar por último."""
import os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['index.html', 'tese.html', 'conversa.html', 'diagnostico-de-marca.html'] + \
    sorted(glob.glob(os.path.join(ROOT, 'cases', '*.html')) + glob.glob(os.path.join(ROOT, 'servicos', '*.html')) +
           glob.glob(os.path.join(ROOT, 'comunidade', '*.html')) + glob.glob(os.path.join(ROOT, 'talentos', '*.html')))
for f in FILES:
    p = f if os.path.isabs(f) else os.path.join(ROOT, f)
    if not os.path.exists(p) or os.path.getsize(p) < 3000:
        continue
    s = open(p, encoding='utf-8').read()
    if 'assets/motion.css' in s:
        continue
    pre = '../' * (os.path.relpath(p, ROOT).count(os.sep))
    s = s.replace('</head>', f'<link rel="stylesheet" href="{pre}assets/motion.css"><!-- motion -->\n</head>', 1)
    s = s.replace('</body>', f'<script src="{pre}assets/motion.js" defer></script><!-- /motion -->\n</body>', 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('ok', os.path.relpath(p, ROOT))
