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
DRAFT = True

CASE_NAME = {c['slug']: (c['name'] + (' + ' + c['extra'] if c.get('extra') else '')) for c in bc.CASES}

# Categorias: (nome, o que a categoria entrega no ecossistema)
CATS = [
 ('Produtora audiovisual', 'Filmes, fotografia e trilhas para campanhas, lançamentos e conteúdo.'),
 ('Mídia e tráfego pago', 'Planejamento e gestão de mídia paga para levar a mensagem certa a quem precisa ouvir.'),
 ('Consultores de negócio', 'Visão de negócio, vendas, growth e marketing ao lado da liderança dos clientes.'),
 ('Estúdios de design', 'Identidade visual, sistemas de marca e design aplicado, cada estúdio com a sua assinatura.'),
 ('Tecnologia', 'Sites, sistemas e integrações para a marca funcionar bem no digital.'),
 ('Redação', 'Conceito criativo, redação e direção de conteúdo.'),
]

# Parceiros: nome, categoria, papel, descrição (só fatos confirmados), cases (slugs), site
P = [
 dict(nome='Alba Arte', cat=0, papel='Produtora de filmes, fotografia e música',
      desc='Produtora de Bento Gonçalves, comandada por dois irmãos artistas gaúchos. Faz filmes institucionais e publicitários, fotografia e trilhas originais gravadas em estúdio próprio.',
      cases=['garbo', 'vallontano'], site='https://albaarte.com/'),
 dict(nome='Impulse', cat=1, papel='Mídia e tráfego pago', desc='', cases=['introduce', 'dsf-advogados', 'vino-verace'], site=''),
 dict(nome='Esdras Moreira', cat=2, papel='Consultor de negócios', desc='', cases=[], site=''),
 dict(nome='Maurício', cat=2, papel='Consultor de vendas', desc='', cases=[], site=''),
 dict(nome='Rodolfo da Costa', cat=2, papel='Estratégia de marca · Berrô Strategy', desc='', cases=['dsf-advogados'], site=''),
 dict(nome='Marcius Dal Bó', cat=2, papel='Conselheiro independente de marketing', desc='', cases=[], site=''),
 dict(nome='Marlon Vieira', cat=2, papel='Consultor de marketing', desc='', cases=['santa-clara', 'neomot'], site=''),
 dict(nome='Luis Fernando Menti', cat=2, papel='Consultor de growth e negócios digitais', desc='', cases=['neomot'], site=''),
 dict(nome='Fabu Design', cat=3, papel='Estúdio de design', desc='', cases=['soprano'], site=''),
 dict(nome='Ghost ID Studio', cat=3, papel='Estúdio de design', desc='', cases=[], site=''),
 dict(nome='Mateus Araújo Estúdio', cat=3, papel='Estúdio de design', desc='', cases=['neomot'], site=''),
 dict(nome='Cave Design', cat=3, papel='Estúdio de design', desc='', cases=[], site=''),
 dict(nome='Ato Estúdio', cat=3, papel='Estúdio de design', desc='', cases=[], site=''),
 dict(nome='Lucas Miotto', cat=4, papel='Tecnologia', desc='', cases=[], site=''),
 dict(nome='Triacca', cat=4, papel='Tecnologia', desc='', cases=[], site=''),
 dict(nome='Estratégia Criativa', cat=5, papel='Claudia Schroeder · estratégia criativa e redação',
      desc='Consultoria de comunicação e branding de Porto Alegre, comandada por Claudia Schroeder, estrategista criativa, diretora de criação e redatora com mais de 30 anos de agência.',
      cases=['neomot'], site='https://www.estrategiacriativa.com.br/'),
]

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


def wheel():
    """Duas rodas de cartões girando em sentidos opostos, como o vídeo dos parceiros."""
    names = [p['nome'] for p in P]
    icons = ['ast', 'arr', 'ast', 'grad']

    def ring(items, cls):
        n = len(items)
        out = ''
        for i, it in enumerate(items):
            a = 360 / n * i
            if it.startswith('@'):
                kind = it[1:]
                inner = {'ast': '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M10.6 2h2.8v6.6l4.7-4.7 2 2-4.7 4.7H22v2.8h-6.6l4.7 4.7-2 2-4.7-4.7V22h-2.8v-6.6l-4.7 4.7-2-2 4.7-4.7H2v-2.8h6.6L3.9 5.9l2-2 4.7 4.7z"/></svg>',
                         'arr': '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M4 10.6h11.3l-4.6-4.6 2-2L20.7 12l-8 8-2-2 4.6-4.6H4z"/></svg>',
                         'grad': '<svg viewBox="0 0 24 24"><path fill="currentColor" d="M4 10.6h11.3l-4.6-4.6 2-2L20.7 12l-8 8-2-2 4.6-4.6H4z"/></svg>'}[kind]
                out += f'<span class="wc ic {kind}" style="--a:{a:.2f}deg">{inner}</span>'
            else:
                out += f'<span class="wc nm" style="--a:{a:.2f}deg"><i>{e(initials(it))}</i><b>{e(it)}</b></span>'
        return f'<div class="ring {cls}">{out}</div>'

    outer, inner = [], []
    for k, n in enumerate(names):
        (outer if k % 2 == 0 else inner).append(n)
    def mix(lst, start):
        res = []
        for j, n in enumerate(lst):
            res.append(n)
            res.append('@' + icons[(j + start) % len(icons)])
        return res
    return ring(mix(outer, 0), 'r1') + ring(mix(inner, 1), 'r2')


def card(p, k):
    cases = ''.join(f'<a href="../cases/{s}.html">{e(CASE_NAME[s])}</a>' for s in p['cases'])
    cases_html = f'<p class="eco-cases"><b>Cases:</b> {cases}</p>' if cases else ''
    site = f'<a class="eco-site" href="{e(p["site"])}" target="_blank" rel="noopener">Conhecer <svg><use href="#arr"/></svg></a>' if p['site'] else ''
    desc = f'<p class="eco-faz">{e(p["desc"])}</p>' if p['desc'] else ''
    return f'''
        <article class="eco-card">
          <div class="eco-top"><span class="eco-mono m{k % 3}">{e(initials(p['nome']))}</span><div><h4>{e(p['nome'])}</h4><p class="eco-esp">{e(p['papel'])}</p></div></div>
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
  <div class="wrap ch-grid wide">
    <div class="ch-txt">
      <div class="ch-brand"><span class="seg">Ecossistema Cooltivo · Nothing great is made alone</span></div>
      <h1>Nada grande é feito <span>sozinho.</span></h1>
      <p class="sum">Acreditamos que bons projetos nascem de pessoas boas e talentosas, unidas pelo mesmo objetivo. Acreditamos também que cada especialista deve atuar no seu lugar de potência. Por isso, nos últimos 10 anos, construímos um ecossistema que conecta todas as pontas do marketing às necessidades dos negócios que atendemos.</p>
      <div class="btns sv-btns"><a class="btn btn-soft" href="#marcas">Conhecer o ecossistema <svg><use href="#arr"/></svg></a><a class="btn btn-line-inv" href="../conversa.html">Agendar diagnóstico</a></div>
    </div>
  </div>
</header>

<section class="eco-wheel" aria-label="Parceiros do ecossistema Cooltivo">
  <div class="wheel">{wheel()}</div>
  <div class="wheel-sig"><b>cooltivo</b><span><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M10.6 2h2.8v6.6l4.7-4.7 2 2-4.7 4.7H22v2.8h-6.6l4.7 4.7-2 2-4.7-4.7V22h-2.8v-6.6l-4.7 4.7-2-2 4.7-4.7H2v-2.8h6.6L3.9 5.9l2-2 4.7 4.7z"/></svg>NOTHING GREAT<br>IS MADE ALONE</span></div>
</section>

<main class="story wrap">
  <section class="st">
    <div class="st-lab"><i>01</i>O que a Cooltivo faz</div>
    <div class="st-body">
      <p class="big">A Cooltivo é um estúdio de estratégia e criatividade da Serra Gaúcha. A nossa especialidade é construir marcas que resistem ao tempo, e a gente fica no centro do ecossistema, na estratégia e na orquestração.</p>
      <ul class="rcv">
        <li><b>Posicionamento</b><span>O lugar que a sua empresa ocupa na cabeça do cliente, a mensagem que só ela pode dizer e onde essa mensagem precisa aparecer.</span></li>
        <li><b>Presença digital</b><span>Planejamento, produção de conteúdo e gestão dos canais, mês a mês, com a mesma história em tudo.</span></li>
        <li><b>Consultoria de marketing</b><span>Kauê Grasnievicz na mesa com a liderança, pensando e acompanhando o plano de marketing.</span></li>
      </ul>
    </div>
  </section>
  <section class="st">
    <div class="st-lab"><i>02</i>Como o ecossistema funciona</div>
    <div class="st-body"><p class="big">Para cada projeto, a Cooltivo monta um time sob medida. O método é o mesmo de sempre: Context, Concept e Craft.</p><div class="c3g">{passos}</div></div>
  </section>
  <section class="st">
    <div class="st-lab"><i>03</i>Especialidades</div>
    <div class="st-body"><p class="big">Uma rede de confiança e excelência em todas as áreas do marketing.</p><div class="eco-areas">{areas}</div></div>
  </section>
</main>

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
    out = out.replace('href="./"', 'href="../cases/"')
    return footer_fab.apply(out, '../', False)


open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page())
print('ok: ecossistema', '(rascunho)' if DRAFT else '')
