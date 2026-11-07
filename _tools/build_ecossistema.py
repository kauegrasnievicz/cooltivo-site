"""Gera ecossistema/index.html.
DRAFT=True: noindex, fora do menu e do sitemap. Para publicar: DRAFT=False e rodar de novo.
Rodar: python3 _tools/build_ecossistema.py"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo
import build_cases as bc
import footer_fab

e = html.escape
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'ecossistema')
os.makedirs(OUT, exist_ok=True)
DRAFT = False

CASE_NAME = {c['slug']: (c['name'] + (' + ' + c['extra'] if c.get('extra') else '')) for c in bc.CASES}

# Categorias: (nome, o que a categoria entrega no ecossistema)
CATS = [
 ('Negócios', 'Visão de negócio, vendas, growth e marketing ao lado da liderança dos clientes.'),
 ('Criativos', 'Filmes, fotografia, identidade visual, sistemas de marca, conceito criativo e redação.'),
 ('Tecnologia', 'Sites, sistemas e integrações para a marca funcionar bem no digital.'),
 ('Mídia', 'Mídia paga, assessoria de imprensa e conteúdo para levar a mensagem a quem precisa ouvir.'),
]

# Parceiros: nome, categoria, papel, descrição (só fatos confirmados), cases (slugs), site
P = [
 dict(nome='Alba Arte', cat=1, papel='Produtora de filmes, fotografia e música',
      desc='Produtora de Bento Gonçalves: filmes, fotografia e trilhas originais gravadas em estúdio próprio.',
      cases=['garbo', 'vallontano'], site='https://albaarte.com/'),
 dict(nome='Vitral Filmes', cat=1, papel='Produtora audiovisual',
      desc='Apaixonados por cinema e por contar histórias, levam esse olhar para cada marca que filmam.',
      cases=['introduce', 'soprano', 'vallontano'], site=''),
 dict(nome='Balsa Produtora', cat=1, papel='Produtora audiovisual e estúdio de podcast',
      desc='Médias e grandes produções com foco em eficiência operacional, além de estúdio próprio de podcast.',
      cases=['introduce', 'vino-verace'], site=''),
 dict(nome='Impulse Company', cat=3, papel='Marketing de performance B2B',
      desc='Funis de aquisição para vendas complexas, com geração de demanda do tráfego ao fechamento.',
      cases=['introduce', 'dsf-advogados', 'vino-verace'], site='https://impulsecompany.com.br/'),
 dict(nome='Dinâmica', cat=3, papel='Assessoria de imprensa e conteúdo',
      desc='De Caxias do Sul desde 1984: há 40 anos mostra ao mundo a potência e o diferencial das empresas.',
      cases=[], site='https://dinamicaconteudo.com.br/quem-somos/'),
 dict(nome='Esdras Moreira', cat=0, papel='Consultor de negócios · CEO da Introduce',
      desc='CEO Mais Inovador de 2025 (Prêmio CCB), fundou 8 negócios e hoje é mentor de founders em escala.',
      cases=[], site='https://www.linkedin.com/in/esdras-moreira'),
 dict(nome='Mauricio Gimenes', cat=0, papel='Consultor de vendas · CSO da Introduce',
      desc='Cofundador da Introduce, com mais de 10 anos em estratégia comercial, processos, marketing e atendimento.',
      cases=[], site='https://www.linkedin.com/in/mauriciogimenesoficial/'),
 dict(nome='Rodolfo da Costa', cat=0, papel='Inteligência estratégica · Berrô Strategy',
      desc='À frente da Berrô Strategy desde 2011, une disciplinas e especialistas em estratégias de marketing.',
      cases=['dsf-advogados'], site='https://berrostrategy.com.br/about/'),
 dict(nome='Marcius Dal Bó', cat=0, papel='Conselheiro independente de marketing',
      desc='Mais de 40 anos de marketing; dirigiu marca e comunicação da Grendene, de Melissa a Ipanema.',
      cases=[], site='https://www.linkedin.com/in/marcius-dal-bo'),
 dict(nome='Marlon Vieira', cat=0, papel='Consultor de gestão de marketing',
      desc='Organiza o marketing de indústrias da Serra com quatro palavras: objetivo, número, dono e ritual.',
      cases=['santa-clara', 'neomot'], site=''),
 dict(nome='Luis Fernando Menti', cat=0, papel='Consultor de growth e negócios digitais',
      desc='Geração de demanda B2B para quem vende com representantes: +R$ 100 mi investidos e 600 clientes.',
      cases=['neomot'], site=''),
 dict(nome='Fabu Design', cat=1, papel='Estúdio de branding e comunicação',
      desc='Branding, identidade visual, social media e audiovisual, com as sócias Caroline e Débora desde 2018.',
      cases=['soprano'], site='https://fabudesign.com.br/'),
 dict(nome='Ghost ID Studio', cat=1, papel='Ariel de Carli · estúdio de branding',
      desc='Identidade visual, naming e sistemas verbais, inclusive para outros estúdios de branding.',
      cases=[], site='https://ghostid.cc/'),
 dict(nome='Studio Mateus Araújo', cat=1, papel='Estúdio de comunicação visual',
      desc='Desde 2011 especializado em branding e design gráfico: cria, assessora e posiciona marcas.',
      cases=['neomot'], site='https://studiomateusaraujo.com.br/'),
 dict(nome='Tainan Ferrari', cat=1, papel='Caligrafia, lettering e design gráfico · Āto',
      desc='Calígrafo, letrista e designer, fundador da Āto, com trabalhos para Grêmio, Salton e Melissa.',
      cases=[], site='https://tainanferrari.com/about'),
 dict(nome='Lucas Miotto', cat=2, papel='Desenvolvimento web',
      desc='Desenvolvedor desde 2015: sites gerenciáveis em WordPress, JavaScript e PHP com Laravel.',
      cases=[], site='https://br.linkedin.com/in/lucas-miotto'),
 dict(nome='Triacca', cat=2, papel='Design digital e desenvolvimento de software',
      desc='De Bento Gonçalves: sites, software sob medida, e-commerce e plataformas de enoturismo.',
      cases=[], site='https://triacca.com.br/'),
 dict(nome='Estratégia Criativa', cat=1, papel='Claudia Schroeder · estratégia criativa e redação',
      desc='Estratégia criativa, direção de criação e redação, com mais de 30 anos de agência.',
      cases=['neomot'], site='https://www.estrategiacriativa.com.br/'),
]

# Mídia dos cards: nome -> (tipo, arquivo em img/eco/, fundo). tipo: foto (rosto), logo (sobre fundo), logo-full (imagem já quadrada)
MEDIA = {
 'Alba Arte': ('logo', 'alba-arte.jpg', '#fff;border:1px solid #dfe8e1'),
 'Esdras Moreira': ('foto', 'esdras-moreira.jpg', ''),
 'Mauricio Gimenes': ('foto', 'mauricio-gimenes.jpg', ''),
 'Studio Mateus Araújo': ('foto', 'studio-mateus-araujo.jpg', ''),
 'Lucas Miotto': ('foto', 'lucas-miotto.jpg', ''),
 'Triacca': ('logo-full', 'triacca.jpg', ''),
 'Balsa Produtora': ('logo-full', 'balsa.jpg', ''),
 'Impulse Company': ('logo', 'impulse.png', '#0f2a1d'),
 'Vitral Filmes': ('logo', 'vitral.png', '#1d1d1b'),
 'Dinâmica': ('logo', 'dinamica.svg', '#1d3a2a'),
 'Ghost ID Studio': ('foto', 'ghost-id.jpg', ''),
 'Estratégia Criativa': ('foto', 'estrategia-criativa.jpg', ''),
}

AREAS = ['Audiovisual', 'Mídia paga', 'Assessoria de imprensa', 'Redação publicitária', 'Consultoria de negócios', 'Design',
         'Marketing', 'Tecnologia', 'Treinamento comercial e de liderança', 'Análise de dados', 'Growth marketing']

PASSOS = [('Context', 'A Cooltivo entende o negócio, o momento da marca e o que o projeto precisa resolver.'),
          ('Concept', 'Com a estratégia definida, a gente monta o time sob medida, chamando os especialistas certos para cada frente.'),
          ('Craft', 'Cada especialista atua no seu lugar de potência. A Cooltivo orquestra o trabalho, cuida da mensagem e responde pela entrega.')]

GANHOS = [('Um time sob medida', 'Cada projeto reúne só os especialistas de que ele precisa, no tamanho certo para o seu negócio.'),
          ('Uma estratégia no centro', 'Todas as frentes partem da mesma plataforma de marca, então tudo conta a mesma história.'),
          ('Um ponto de contato', 'A Cooltivo conduz e orquestra o ecossistema. Você fala com a gente e a gente coordena o resto.')]


def initials(n):
    w = [x for x in n.replace('·', ' ').split() if x[0].isalpha() and x.lower() not in ('da', 'de', 'do', 'dal')]
    return (w[0][0] + (w[1][0] if len(w) > 1 else '')).upper()


AST = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M10.6 2h2.8v6.6l4.7-4.7 2 2-4.7 4.7H22v2.8h-6.6l4.7 4.7-2 2-4.7-4.7V22h-2.8v-6.6l-4.7 4.7-2-2 4.7-4.7H2v-2.8h6.6L3.9 5.9l2-2 4.7 4.7z"/></svg>'
ARR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 10.6h11.3l-4.6-4.6 2-2L20.7 12l-8 8-2-2 4.6-4.6H4z"/></svg>'


SHORT = {'Alba Arte': 'Audiovisual', 'Vitral Filmes': 'Audiovisual', 'Balsa Produtora': 'Audiovisual', 'Estratégia Criativa': 'Redação', 'Impulse Company': 'Mídia paga', 'Dinâmica': 'Imprensa e conteúdo'}


def wheel():
    """Duas faixas de cartões deslizando em sentidos opostos (parceiros + blocos gráficos)."""
    icons = [('ast', AST), ('arr', ARR), ('grad', ARR), ('ast', AST)]

    def row(ps, start, cls):
        items = ''
        for j, p in enumerate(ps):
            cat = SHORT.get(p['nome'], CATS[p['cat']][0])
            items += f'<span class="mc nm"><i>{e(initials(p["nome"]))}</i><b>{e(p["nome"])}</b><small>{e(cat)}</small></span>'
            k, svg = icons[(j + start) % len(icons)]
            items += f'<span class="mc ic {k}">{svg}</span>'
        # duas cópias para o loop sem emenda
        dup = items.replace('class="mc', 'aria-hidden="true" class="mc')
        return f'<div class="mrow {cls}"><div class="mtrack">{items}{dup}</div></div>'

    a = [p for k, p in enumerate(P) if k % 2 == 0]
    b = [p for k, p in enumerate(P) if k % 2 == 1]
    return row(a, 0, 'm1') + row(b, 1, 'm2')


def media(p, k):
    m = MEDIA.get(p['nome'])
    if not m:
        return f'<span class="eco-mono m{k % 3}">{e(initials(p["nome"]))}</span>'
    kind, f, bg = m
    alt = e(p['nome'])
    if kind == 'foto':
        return f'<span class="eco-mono ph"><img src="../img/eco/{f}" alt="Foto de {alt}" width="64" height="64" loading="lazy"></span>'
    if kind == 'logo-full':
        return f'<span class="eco-mono lf"><img src="../img/eco/{f}" alt="Logo {alt}" width="64" height="64" loading="lazy"></span>'
    return f'<span class="eco-mono lg" style="background:{bg}"><img src="../img/eco/{f}" alt="Logo {alt}" width="64" height="64" loading="lazy"></span>'


def card(p, k):
    cases = ''.join(f'<a href="../cases/{s}.html">{e(CASE_NAME[s])}</a>' for s in p['cases'])
    cases_html = f'<p class="eco-cases"><b>Cases:</b> {cases}</p>' if cases else ''
    site = f'<a class="eco-site" href="{e(p["site"])}" target="_blank" rel="noopener">Conhecer <svg><use href="#arr"/></svg></a>' if p['site'] else ''
    desc = f'<p class="eco-faz">{e(p["desc"])}</p>' if p['desc'] else ''
    return f'''
        <article class="eco-card">
          <div class="eco-top">{media(p, k)}<div><h4>{e(p['nome'])}</h4><p class="eco-esp">{e(p['papel'])}</p></div></div>
          {desc}{cases_html}{site}
        </article>'''


def page():
    areas = ''.join(f'<span>{e(a)}</span>' for a in AREAS)
    passos = ''.join(f'<div class="c3c"><span>0{i + 1}</span><h3>{a}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(PASSOS))
    ganhos = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in GANHOS)
    grupos = ''
    k = 0
    for ci, (cn, cd) in enumerate(CATS):
        ps = [p for p in P if p['cat'] == ci]
        cards = ''
        for p in ps:
            cards += card(p, k); k += 1
        grupos += f'''
      <div class="eco-group">
        <div class="eco-gh"><h3>{e(cn)}</h3><p>{e(cd)}</p></div>
        <div class="eco-grid">{cards}
        </div>
      </div>'''
    from urllib.parse import quote
    wa = 'https://wa.me/5554991000102?text=' + quote('Olá, Cooltivo! Quero conversar sobre fazer parte do ecossistema.')
    draft = '<div class="eco-draft">Rascunho: esta página ainda não aparece no Google nem no menu do site.</div>' if DRAFT else ''
    body = f'''{draft}
<header class="ch eco-hero" id="topo">
  <svg class="bg-sym sym" aria-hidden="true"><use href="#sym"/></svg>
  <div class="wrap ch-grid sv-hero">
    <div class="ch-txt">
      <div class="ch-brand"><span class="seg">Ecossistema Cooltivo · Nothing great is made alone</span></div>
      <h1>Nada grande é feito <span>sozinho.</span></h1>
      <p class="sum">Acreditamos que bons projetos nascem de pessoas boas e talentosas, unidas pelo mesmo objetivo. Acreditamos também que cada especialista deve atuar no seu lugar de potência. Por isso, nos últimos 10 anos, construímos um ecossistema que conecta todas as pontas do marketing às necessidades dos negócios que atendemos.</p>
      <div class="btns sv-btns"><a class="btn btn-soft" href="#marcas">Conhecer o ecossistema <svg><use href="#arr"/></svg></a><a class="btn btn-line-inv" href="../conversa.html">Agendar diagnóstico</a></div>
    </div>
    <figure class="eco-vid"><video autoplay muted loop playsinline preload="metadata" poster="../video/rede-poster.jpg" aria-label="Parceiros do ecossistema Cooltivo"><source src="../video/rede.mp4" type="video/mp4"></video></figure>
  </div>
</header>



<section class="tl-vagas eco-marcas" id="marcas">
  <div class="wrap">
    <div class="eyebrow"><svg class="sym"><use href="#sym"/></svg>Quem faz parte</div>
    <h2>Quem <span>cultiva</span> com a gente.</h2>
    {grupos}
  </div>
</section>

<section class="faq">
  <div class="wrap faq-grid">
    <h2><small>Para quem contrata</small>O que você ganha</h2>
    <ul class="rcv">{ganhos}</ul>
  </div>
</section>

<section class="sv-other eco-join">
  <div class="wrap eco-join-in">
    <div><small class="lab">Para especialistas e estúdios</small><h2>Quer fazer parte do ecossistema?</h2><p>Se você é referência no que faz e compartilha dos nossos valores, vamos conversar.</p></div>
    <a class="btn btn-dark" href="{wa}" target="_blank" rel="noopener">Quero fazer parte <svg><use href="#arr"/></svg></a>
  </div>
</section>
'''
    path = '/ecossistema/'
    t = 'Ecossistema Cooltivo · Nothing great is made alone'
    d = 'O ecossistema da Cooltivo: especialistas em audiovisual, mídia, design, tecnologia, redação e negócios, com a Cooltivo na estratégia e na orquestração.'
    sch = [] if DRAFT else [seo.crumbs([('Cooltivo', '/'), ('Ecossistema', path)])]
    head = bc.HEAD.format(title=e(t), desc=e(d), seo=seo.head(path, t, d, 'home.jpg', 'website', sch, index=not DRAFT))
    out = head + body + bc.FOOT
    out = out.replace('href="cases.css"', 'href="../cases/cases.css"')
    out = out.replace('<li><a href="./" aria-current="page">Cases</a></li>', '<li><a href="../cases/">Cases</a></li>')
    out = out.replace('<li><a href="../ecossistema/">Ecossistema</a></li>', '<li><a href="../ecossistema/" aria-current="page">Ecossistema</a></li>')
    out = out.replace('href="./"', 'href="../cases/"')
    return footer_fab.apply(out, '../', False)


open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page())
print('ok: ecossistema', '(rascunho)' if DRAFT else '')
