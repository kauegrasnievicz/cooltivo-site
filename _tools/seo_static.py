"""Aplica título, descrição e blocos de SEO às páginas estáticas. Idempotente."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WEBSITE = {'@context': 'https://schema.org', '@type': 'WebSite', '@id': seo.BASE + '/#site', 'name': 'Cooltivo Estúdio',
           'url': seo.BASE + '/', 'inLanguage': 'pt-BR', 'publisher': {'@id': seo.ORG_ID}}
PAGES = {
 'index.html': ('/', 'Cooltivo Estúdio · Branding e estratégia de marca na Serra Gaúcha',
   'Estúdio de branding e estratégia de marca da Serra Gaúcha. Posicionamento, comunicação e presença digital para empresas de Caxias do Sul, Bento Gonçalves e RS.',
   'home.jpg', [seo.ORG, WEBSITE], True),
 'conversa.html': ('/conversa', 'Reunião de diagnóstico de marca · Cooltivo Estúdio',
   'Branding e comunicação para empresas da Serra Gaúcha que querem crescer sem competir só por preço. Agende uma reunião de diagnóstico de marca de 45 minutos.',
   'conversa.jpg', [seo.crumbs([('Cooltivo', '/'), ('Diagnóstico de marca', '/conversa')])], True),
 'diagnostico-de-marca.html': ('/diagnostico-de-marca', 'Diagnóstico de marca · Cooltivo Estúdio',
   'Responda ao diagnóstico de marca da Cooltivo: passado, presente e futuro do seu negócio, em cerca de 10 minutos.',
   'diagnostico.jpg', [], False),
 '_tools/diag_src.html': ('/diagnostico-de-marca', 'Diagnóstico de marca · Cooltivo Estúdio',
   'Responda ao diagnóstico de marca da Cooltivo: passado, presente e futuro do seu negócio, em cerca de 10 minutos.',
   'diagnostico.jpg', [], False),
 'tese.html': ('/tese', 'Marcas que resistem ao tempo · A tese de branding da Cooltivo',
   'Por que algumas marcas atravessam gerações? A tese da Cooltivo, com pesquisas e cases de Apple, LEGO, Tramontina, Sicredi e outras marcas que resistem ao tempo.',
   'tese.jpg', [{'@context': 'https://schema.org', '@type': 'Article', 'headline': 'Marcas que resistem ao tempo', 'inLanguage': 'pt-BR',
     'url': seo.BASE + '/tese', 'image': seo.BASE + '/img/og/tese.jpg', 'author': {'@type': 'Person', 'name': 'Kauê Grasnievicz'},
     'publisher': {'@id': seo.ORG_ID}, 'about': ['Branding', 'Posicionamento de marca', 'Longevidade de marcas']}], True),
}
for f, (path, t, d, og, sch, idx) in PAGES.items():
    p = os.path.join(ROOT, f); s = open(p, encoding='utf-8').read()
    s = re.sub(r'\n<!-- seo -->.*?<!-- /seo -->', '', s, flags=re.S)
    s = re.sub(r'\n<meta name="robots"[^>]*>', '', s)
    s = re.sub(r'<title>.*?</title>', '<title>' + seo.e(t) + '</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + seo.e(d) + '">', s, count=1)
    s = s.replace('</head>', '<!-- seo -->\n' + seo.head(path, t, d, og, 'article' if f == 'tese.html' else 'website', sch, idx) + '\n<!-- /seo -->\n</head>', 1)
    open(p, 'w', encoding='utf-8').write(s); print('ok', f)
