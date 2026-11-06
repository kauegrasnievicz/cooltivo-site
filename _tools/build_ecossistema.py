"""Gera ecossistema/index.html. Rascunho: noindex, fora do menu e do sitemap até as marcas serem preenchidas.
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
DRAFT = True  # quando as marcas estiverem preenchidas: False (indexa, entra no menu e no sitemap)

AREAS = ['Audiovisual', 'Mídia paga', 'Assessoria de imprensa', 'Redação publicitária', 'Consultoria de negócios', 'Design',
         'Marketing', 'Tecnologia', 'Treinamento comercial e de liderança', 'Análise de dados', 'Growth marketing']

# Marcas do ecossistema: preencher. Cada item vira um cartão.
MARCAS = [dict(nome='', esp='', faz='', entrega=[], cases=[], site='', logo='') for _ in range(6)]

PASSOS = [('Context', 'A Cooltivo entende o negócio, o momento da marca e o que o projeto precisa resolver.'),
          ('Concept', 'Com a estratégia definida, a gente monta o time sob medida, chamando as marcas do ecossistema certas para cada frente.'),
          ('Craft', 'A Cooltivo orquestra o trabalho de todos, cuida da mensagem e responde pela qualidade da entrega.')]

GANHOS = [('Um time sob medida', 'Cada projeto reúne só os especialistas de que ele precisa, no tamanho certo para o seu negócio.'),
          ('Uma estratégia no centro', 'Todas as frentes partem da mesma plataforma de marca, então tudo conta a mesma história.'),
          ('Um ponto de contato', 'A Cooltivo conduz e orquestra o ecossistema. Você fala com a gente e a gente coordena o resto.')]


def ph(txt, val):
    """Mostra o valor preenchido ou uma marcação [ ] visível."""
    return e(val) if val else f'<span class="ph">[{e(txt)}]</span>'


def marca_html(m, i):
    logo = f'<img src="{e(m["logo"])}" alt="{e(m["nome"])}">' if m['logo'] else '<span class="ph">[Logo]</span>'
    ent = ''.join(f'<li>{e(x)}</li>' for x in m['entrega']) or ''.join(f'<li><span class="ph">[Entrega {k}]</span></li>' for k in (1, 2, 3))
    cases = ', '.join(m['cases']) if m['cases'] else '<span class="ph">[Cases em que participou]</span>'
    site = f'<a class="eco-site" href="{e(m["site"])}" target="_blank" rel="noopener">Conhecer a marca <svg><use href="#arr"/></svg></a>' if m['site'] else '<span class="eco-site ph">[Link do site ou Instagram]</span>'
    filled = ' filled' if m['nome'] else ''
    return f'''
      <article class="eco-card{filled}">
        <div class="eco-logo">{logo}</div>
        <h3>{ph('Nome da marca', m['nome'])}</h3>
        <p class="eco-esp">{ph('Especialidade', m['esp'])}</p>
        <p class="eco-faz">{ph('O que a marca faz, em uma ou duas frases', m['faz'])}</p>
        <h4>O que entrega no ecossistema</h4>
        <ul>{ent}</ul>
        <p class="eco-cases"><b>Cases:</b> {cases}</p>
        {site}
      </article>'''


def page():
    areas = ''.join(f'<span>{e(a)}</span>' for a in AREAS)
    import math
    SHORT = ['Audiovisual', 'Mídia paga', 'Imprensa', 'Redação', 'Negócios', 'Design', 'Marketing', 'Tecnologia', 'Treinamento', 'Dados', 'Growth']
    orbit = ''
    for i, a in enumerate(SHORT):
        ang = math.radians(i / len(SHORT) * 360 - 90)
        orbit += f'<span class="eco-o" style="left:{50 + 40 * math.cos(ang):.2f}%;top:{50 + 40 * math.sin(ang):.2f}%">{e(a)}</span>'
    passos = ''.join(f'<div class="c3c"><span>0{i + 1}</span><h3>{a}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(PASSOS))
    ganhos = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in GANHOS)
    marcas = ''.join(marca_html(m, i) for i, m in enumerate(MARCAS))
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
      <p class="sum">A Cooltivo é um estúdio de estratégia e criatividade da Serra Gaúcha. A nossa especialidade é construir marcas que resistem ao tempo: posicionamento, presença digital e consultoria de marketing. Para ir além do que um estúdio faz sozinho, a gente reuniu uma rede de marcas parceiras, cada uma referência no que faz. A Cooltivo fica na estratégia e na orquestração.</p>
      <div class="btns sv-btns"><a class="btn btn-soft" href="#marcas">Conhecer o ecossistema <svg><use href="#arr"/></svg></a><a class="btn btn-line-inv" href="../conversa.html">Agendar diagnóstico</a></div>
    </div>
    <div class="eco-orbit" aria-hidden="true">
      <div class="eco-core"><svg class="sym"><use href="#sym"/></svg><b>cooltivo</b><small>estratégia e orquestração</small></div>
      {orbit}
    </div>
  </div>
</header>

<main class="story wrap">
  <section class="st">
    <div class="st-lab"><i>01</i>O que a Cooltivo faz</div>
    <div class="st-body">
      <p class="big">A gente entende o negócio, encontra o que a marca tem de único e faz a empresa inteira contar a mesma história.</p>
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
    <div class="eyebrow"><svg class="sym"><use href="#sym"/></svg>Marcas do ecossistema</div>
    <h2>Quem <span>cultiva</span> com a gente.</h2>
    <p class="eco-intro"><span class="ph">[Texto curto de apresentação das marcas parceiras: como foram escolhidas e o que elas têm em comum com a Cooltivo.]</span></p>
    <div class="eco-grid">{marcas}
    </div>
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
    <div><small class="lab">Para marcas parceiras</small><h2>Quer fazer parte do ecossistema?</h2><p>Se a sua marca é referência no que faz e compartilha dos nossos valores, vamos conversar.</p></div>
    <a class="btn btn-dark" href="{wa}" target="_blank" rel="noopener">Quero fazer parte <svg><use href="#arr"/></svg></a>
  </div>
</section>
'''
    path = '/ecossistema/'
    t = 'Ecossistema Cooltivo · Nothing great is made alone'
    d = 'O ecossistema da Cooltivo: estratégia e orquestração da Cooltivo com uma rede de marcas parceiras em audiovisual, mídia, design, tecnologia, dados e mais.'
    sch = [] if DRAFT else [seo.crumbs([('Cooltivo', '/'), ('Ecossistema', path)])]
    head = bc.HEAD.format(title=e(t), desc=e(d), seo=seo.head(path, t, d, 'home.jpg', 'website', sch, index=not DRAFT))
    out = head + body + bc.FOOT
    out = out.replace('href="cases.css"', 'href="../cases/cases.css"')
    out = out.replace('<li><a href="./" aria-current="page">Cases</a></li>', '<li><a href="../cases/">Cases</a></li>')
    out = out.replace('href="./"', 'href="../cases/"')
    return footer_fab.apply(out, '../', False)


open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page())
print('ok: ecossistema', '(rascunho)' if DRAFT else '')
