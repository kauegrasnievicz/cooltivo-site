"""Uniformiza duração e curva das transições (hover/foco/carrossel) com os tokens de assets/motion.css. Idempotente."""
import re, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['index.html', 'tese.html', 'conversa.html', 'diagnostico-de-marca.html', 'cases/cases.css'] 
def split_top(v):
    out, d, cur = [], 0, ''
    for ch in v:
        if ch == '(': d += 1
        if ch == ')': d -= 1
        if ch == ',' and d == 0: out.append(cur); cur = ''
        else: cur += ch
    out.append(cur); return out
TIME = re.compile(r'^-?\d*\.?\d+m?s$')
def seg(sg):
    if 'var(--t' in sg or 'none' in sg: return sg
    toks = re.findall(r'cubic-bezier\([^)]*\)|\S+', sg.strip())
    out, times, has_ease = [], 0, False
    for t in toks:
        if TIME.match(t):
            times += 1
            if times == 1:
                v = float(t[:-1]) if t.endswith('s') and not t.endswith('ms') else 0
                t = 'var(--t,.3s)' if v <= .35 else 'var(--t-slow,.6s)'
        elif t in ('ease', 'ease-out', 'ease-in', 'ease-in-out') or t.startswith('cubic-bezier'):
            t = 'var(--ease,cubic-bezier(.2,.7,.2,1))'; has_ease = True
        elif t == 'linear': has_ease = True
        out.append(t)
    if times and not has_ease:
        # coloca a curva logo depois da duração
        i = next(i for i, t in enumerate(out) if t.startswith('var(--t'))
        out.insert(i + 1, 'var(--ease,cubic-bezier(.2,.7,.2,1))')
    return ' '.join(out)
def fix(m):
    v = m.group(1)
    if v.strip() in ('none', 'inherit'): return m.group(0)
    return 'transition:' + ','.join(seg(s) for s in split_top(v))
for f in FILES:
    p = os.path.join(ROOT, f); s = open(p, encoding='utf-8').read()
    n = re.sub(r'(?<![\w-])transition:([^;}"\']*)', fix, s)
    if n != s: open(p, 'w', encoding='utf-8').write(n); print('norm', f)
