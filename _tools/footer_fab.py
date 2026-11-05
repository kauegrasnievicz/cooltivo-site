"""Rodapé com navegação e botão flutuante do WhatsApp (index, tese e FOOT dos cases/serviços). Idempotente."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = 'M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z'

def fnav(p):
    return (f'<!-- fnav --><div class="wrap fwrap"><div class="fnav">'
            f'<div><small>Serviços</small><a href="{p}servicos/posicionamento-de-marca.html">Posicionamento de marca</a><a href="{p}servicos/presenca-digital.html">Presença digital</a><a href="{p}servicos/consultoria-de-marketing.html">Consultoria de marketing</a></div>'
            f'<div><small>Cooltivo</small><a href="{p}cases/">Cases</a><a href="{p}conversa.html">Agendar diagnóstico</a><a href="{p}diagnostico-de-marca.html">Diagnóstico de marca</a><a href="{p}tese.html">Nossa tese</a></div>'
            f'</div></div><!-- /fnav -->')

FAB = ('<!-- fab --><a class="wa-fab" id="waFab" href="https://wa.me/5554991000102?text=Ol%C3%A1%2C%20Cooltivo!" target="_blank" rel="noopener" aria-label="Falar com a Cooltivo no WhatsApp">'
       f'<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="{PATH}"/></svg><span>Falar no WhatsApp</span></a>'
       '<script>(function(){var f=document.getElementById("waFab"),c=document.querySelector("#contato,section.cta");if(!f||!c||!("IntersectionObserver" in window))return;'
       'new IntersectionObserver(function(e){f.classList.toggle("hide",e[0].isIntersecting)},{threshold:.05}).observe(c)})();</script><!-- /fab -->')

CSS = '''/* fab+fnav */
footer .fnav{width:100%;display:grid;grid-template-columns:repeat(2,minmax(0,auto));justify-content:start;gap:18px 88px;padding-bottom:26px;margin-bottom:26px;border-bottom:1px solid rgba(249,243,227,.18)}
footer .fnav>div{display:flex;flex-wrap:wrap;align-items:baseline;gap:8px 22px}
footer .fnav small{width:100%;font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;opacity:.6;margin-bottom:4px}
footer .fnav a{font-size:15px;font-weight:600;text-decoration:none;opacity:.88}
footer .fnav a:hover{opacity:1;text-decoration:underline;text-underline-offset:4px}
.wa-fab{position:fixed;right:24px;bottom:calc(24px + env(safe-area-inset-bottom,0px));z-index:60;display:inline-flex;align-items:center;gap:10px;height:54px;padding:0 22px 0 16px;border-radius:999px;background:#366c4c;color:#fff;font:700 15px/1 var(--font);text-decoration:none;box-shadow:0 12px 30px rgba(23,38,29,.28);transition:opacity .3s,transform .3s,background .25s}
.wa-fab svg{width:24px;height:24px;flex:none}
.wa-fab:hover{background:#1d3a2a;transform:translateY(-2px)}
.wa-fab.hide{opacity:0;transform:scale(.85);pointer-events:none}
@media (max-width:760px){.wa-fab{right:16px;bottom:calc(16px + env(safe-area-inset-bottom,0px));width:56px;height:56px;padding:0;justify-content:center}.wa-fab span{display:none}.wa-fab svg{width:28px;height:28px}footer .fnav{grid-template-columns:1fr;gap:22px}}
@media print{.wa-fab{display:none}}
/* /fab+fnav */'''

def apply(html, p, css_inline=True):
    html = re.sub(r'\s*<!-- fnav -->.*?<!-- /fnav -->', '', html, flags=re.S)
    html = re.sub(r'<footer>\s*<div class="wrap">', '<footer>\n    <div class="wrap">', html, count=1)
    html = re.sub(r'<!-- fab -->.*?<!-- /fab -->', '', html, flags=re.S)
    html = re.sub(r'<a class="wa-fab" id="waFab".*?</a>\n?', '', html, flags=re.S)
    html = html.replace('<footer>\n    <div class="wrap">', '<footer>\n    ' + fnav(p) + '\n    <div class="wrap">', 1)
    html = html.replace('</body>', FAB + '\n</body>', 1)
    if css_inline:
        html = re.sub(r'/\* fab\+fnav \*/.*?/\* /fab\+fnav \*/\n?', '', html, flags=re.S)
        html = html.replace('</style>', CSS + '\n</style>', 1)
    return html

if __name__ == '__main__':
    for f in ['index.html', 'tese.html']:
        fp = os.path.join(ROOT, f); h = open(fp, encoding='utf-8').read()
        if f == 'index.html':
            # remove regras antigas do fab (mobile) e o script antigo
            h = re.sub(r'\n  \.wa-fab\{display:flex;position:fixed[^\n]*', '', h)
            h = re.sub(r'\n  \.wa-fab svg\{width:28px;height:28px\}', '', h)
            h = re.sub(r'\n  \.wa-fab\.hide\{[^\n]*', '', h)
            h = h.replace("\n  const fab=document.getElementById('waFab'),cta=document.getElementById('contato');if(!fab||!cta)return;\n  const io=new IntersectionObserver(es=>fab.classList.toggle('hide',es[0].isIntersecting),{threshold:.05});io.observe(cta);", '')
        h = apply(h, '')
        open(fp, 'w', encoding='utf-8').write(h); print('ok', f)
    c = os.path.join(ROOT, 'cases', 'cases.css'); t = open(c, encoding='utf-8').read()
    t = re.sub(r'/\* fab\+fnav \*/.*?/\* /fab\+fnav \*/\n?', '', t, flags=re.S) + '\n' + CSS + '\n'
    open(c, 'w', encoding='utf-8').write(t); print('ok cases.css')
