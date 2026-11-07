"""Gera as páginas de serviço em servicos/. Rodar: python3 _tools/build_servicos.py"""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo
import build_cases as bc  # reaproveita HEAD, FOOT, CASES e logo_html (e regera os cases)

e = html.escape
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'servicos')
os.makedirs(OUT, exist_ok=True)

SERRA = ('Vocês atendem empresas fora da Serra Gaúcha?',
         'Sim. A gente atende empresas de todo o Rio Grande do Sul e de outros estados. Mas a Serra Gaúcha é a nossa casa. Foi aqui que a gente aprendeu o jogo das marcas que resistem ao tempo.')
START = ('Por onde começar?',
         'Por uma reunião de diagnóstico de 45 minutos, para entender o momento da sua marca e os movimentos necessários.')

S = [
 dict(slug='posicionamento-de-marca', name='Posicionamento de marca', tipo='Projeto pontual', dur='6 a 8 semanas',
  seo_t='Posicionamento de marca para empresas · Cooltivo · Serra Gaúcha',
  seo_d='Projeto de 6 a 8 semanas para definir o lugar que a sua empresa ocupa na cabeça do cliente. Para empresas de Caxias do Sul, Bento Gonçalves e do RS.',
  h1='O lugar que a sua empresa ocupa na cabeça do cliente.',
  intro='Toda empresa que dura tem um motivo para ser escolhida. Muitas vezes, quem trabalha nela sabe esse motivo, mas ele não aparece no site, no catálogo nem na fala do vendedor. Posicionamento de marca é encontrar esse motivo, dizer em uma frase e fazer a empresa inteira contar a mesma história.',
  quando=['A empresa cresceu, mas a marca ficou com cara de quando começou.',
          'O cliente compara só preço, porque não enxerga a diferença.',
          'Cada vendedor explica a empresa de um jeito.',
          'Uma nova geração vai assumir o negócio e precisa de uma direção clara.',
          'A empresa entrou em um mercado novo e o nome antigo já não conta tudo o que ela faz.'],
  c3=['A gente conversa com os sócios, com o time e com clientes, e estuda os concorrentes e o mercado. É aqui que aparece o que a empresa tem de único.',
      'A gente reúne a liderança em um workshop de co-criação para decidir junto quem a empresa é, o que defende e como quer ser lembrada.',
      'A gente organiza tudo na plataforma de marca, um guia para o marketing, para o comercial e para quem chega na empresa.'],
  recebe=[('Posicionamento único', 'O lugar que a sua empresa ocupa na cabeça do cliente e que nenhum concorrente consegue ocupar. A resposta para a pergunta: por que escolher a sua empresa?'),
          ('Mensagem clara', 'A forma de dizer isso que qualquer pessoa entende de primeira: o cliente, o vendedor, o pessoal da produção e a próxima geração da família.'),
          ('Ecossistema estratégico', 'Todos os lugares onde a marca aparece contando a mesma história: site, Instagram, LinkedIn, catálogo, apresentação de vendas, feira e fachada.')],
  cases=['neomot', 'soprano', 'vallontano'],
  faq=[('Quanto tempo leva um projeto de posicionamento?', 'De 6 a 8 semanas, do diagnóstico à entrega da plataforma de marca.'),
       ('Posicionamento é a mesma coisa que logo novo?', 'Não. O posicionamento vem antes e define o que a marca precisa dizer. Logo, identidade visual, site e conteúdo vêm depois, a partir dessa direção.'),
       ('Quem da empresa precisa participar?', 'Os sócios e a liderança, principalmente no workshop. A gente também conversa com pessoas do time e com alguns clientes.'),
       SERRA, START]),
 dict(slug='presenca-digital', name='Presença digital', tipo='Contrato recorrente', dur='6 a 12 meses',
  seo_t='Presença digital e gestão de redes para empresas · Cooltivo',
  seo_d='Planejamento, produção de conteúdo e gestão de canais, mês a mês, para empresas da Serra Gaúcha e do RS que querem mostrar no digital o tamanho que têm.',
  h1='A sua empresa no digital do tamanho que ela é.',
  intro='Muita empresa forte some no digital. Posta quando sobra tempo, cada canal fala de um jeito e o Instagram não mostra a história nem o tamanho do negócio. A gente planeja e conduz a comunicação da sua marca no digital, mês a mês, com conteúdo que mostra quem a empresa é e ajuda a vender.',
  quando=['A empresa posta quando sobra tempo.',
          'O Instagram não mostra a história e o tamanho da empresa.',
          'Cada canal fala de um jeito diferente.',
          'O time interno não dá conta de planejar, produzir e acompanhar.',
          'A marca acabou de ganhar um posicionamento novo e ele precisa chegar nas redes.'],
  c3=['A gente entende a marca, o cliente que vocês querem atrair e o que já funciona nos canais.',
      'A gente define junto com vocês os temas, a linha de conteúdo e o papel de cada canal.',
      'A gente produz, publica e acompanha todo mês, com fotos e vídeos reais da empresa e do seu pessoal.'],
  recebe=[('Planejamento de presença digital', 'O plano do que a marca vai dizer, em quais canais e com qual frequência, ligado aos objetivos do negócio.'),
          ('Produção de conteúdo', 'Roteiro, gravação, fotos, vídeos e textos com direção criativa da Cooltivo e dos parceiros do nosso ecossistema.'),
          ('Estratégia e gestão de canais', 'Publicação, acompanhamento dos números e ajustes mês a mês para o conteúdo trazer resultado.')],
  cases=['soprano', 'dsf-advogados', 'garbo'],
  faq=[('Quanto tempo dura o contrato?', 'Os contratos de presença digital são de 6 a 12 meses. É o tempo para a marca ganhar constância e para os resultados aparecerem.'),
       ('Vocês produzem as fotos e os vídeos?', 'Sim. A gente conduz as produções com direção criativa própria e com parceiros do nosso ecossistema, como a Vitral Filmes.'),
       ('Em quais canais vocês atuam?', 'Nos que fazem sentido para o seu cliente, como Instagram, LinkedIn, YouTube e site. Isso é definido no planejamento.'),
       SERRA, START]),
 dict(slug='consultoria-de-marketing', name='Consultoria de marketing', tipo='Pontual ou recorrente', dur='Formato flexível',
  seo_t='Consultoria de marketing com Kauê Grasnievicz · Cooltivo · Serra Gaúcha',
  seo_d='Consultoria de marketing conduzida por Kauê Grasnievicz, estrategista com mais de 10 anos de marketing, para empresas de Caxias do Sul, Bento Gonçalves e do RS.',
  h1='Um estrategista sentado na mesa, pensando o marketing com você.',
  intro='A consultoria de marketing da Cooltivo é conduzida pessoalmente por Kauê Grasnievicz, cofundador e diretor de estratégia do estúdio. Ele mergulha no negócio, senta com os sócios e com o time e acompanha de perto o plano de marketing, construído a partir dos objetivos da empresa.',
  hero_video='capa',
  num2=('10+ anos', 'de marketing de quem conduz a consultoria'),
  lead=dict(name='Kauê Grasnievicz', role='Cofundador e diretor de estratégia da Cooltivo', img='../img/historia/h2.jpg',
    alt='Kauê Grasnievicz conduzindo um workshop de estratégia',
    bio=['Kauê é estrategista, com mais de 10 anos de marketing e especialista em marca e comunicação. Antes de cofundar a Cooltivo, foi gerente de marketing de uma grande rede hoteleira e líder de digital de uma agência de comunicação que atendia grandes marcas gaúchas.',
         'Já trabalhou com marcas como Sicredi, Santa Clara, Soprano, Zen Design e Casa Valduga. Na consultoria, ele ocupa a cadeira de quem pensa o marketing junto com a liderança: participa das decisões, orienta o time e responde pelo plano.'],
    quote='A comunicação é uma das ferramentas mais poderosas para transformar pessoas, sociedade e negócios.',
    link='https://www.linkedin.com/in/kauegrasnievicz/'),
  quando=['A empresa não tem um líder de marketing.',
          'O time de marketing executa, mas falta direção.',
          'As decisões de marketing são tomadas no improviso.',
          'A empresa vive um momento de crescimento, sucessão ou mudança de mercado.'],
  c3=['Kauê faz uma imersão no negócio, nos números e no time, conversando com sócios, liderança e clientes.',
      'Kauê monta junto com a liderança o plano estratégico de marketing, com metas ligadas aos objetivos da empresa.',
      'Kauê acompanha toda semana, com o time e com os parceiros, para o plano sair do papel.'],
  recebe=[('Planejamento estratégico de marketing', 'O plano de marketing da empresa, com prioridades, metas e investimento, construído por Kauê a partir dos objetivos do negócio.'),
          ('Encontros semanais com Kauê', 'Uma conversa por semana com a liderança e o time para decidir, ajustar e destravar.'),
          ('Imersões com liderança e time', 'Encontros de trabalho conduzidos por Kauê para alinhar a empresa inteira em torno da marca e do plano.')],
  cases=['introduce', 'vino-verace'],
  faq=[('Quem conduz a consultoria?', 'Kauê Grasnievicz, cofundador e diretor de estratégia da Cooltivo, conduz pessoalmente cada consultoria, com o apoio do time do estúdio quando o plano pede execução.'),
       ('A consultoria é pontual ou recorrente?', 'Os dois. A gente monta o formato com você: uma imersão pontual ou um acompanhamento contínuo.'),
       ('Para que tamanho de empresa faz sentido?', 'Para empresas médias e grandes que querem tratar o marketing como parte da estratégia do negócio.'),
       SERRA, START]),
]
BY = {c['slug']: c for c in bc.CASES}


def card(c):
    a, b = c['nums'][0]
    return f'''
    <a class="cc" href="../cases/{c['slug']}.html">
      <span class="cc-img"><img src="../video/cases/{c['video']}.jpg" alt="Case {e(c['name'])}: {e(c['title'])}" loading="lazy"></span>
      <span class="cc-body">
        <span class="ch-brand">{bc.logo_html(c)}<span class="seg">{e(c['seg'])}</span></span>
        <span class="cc-t">{e(c['title'])}</span>
        <span class="cc-n"><b>{e(a)}</b><span>{e(b)}</span></span>
        <span class="cc-go">Ver case <svg><use href="#arr"/></svg></span>
      </span>
    </a>'''


def fix(t):
    t = t.replace('href="cases.css"', 'href="../cases/cases.css"')
    t = t.replace('<li><a href="./" aria-current="page">Cases</a></li>', '<li><a href="../cases/">Cases</a></li>')
    t = t.replace('<li><a href="../index.html#entregas">Serviços</a></li>', '<li><a href="../index.html#entregas" aria-current="page">Serviços</a></li>')
    t = t.replace('href="./"', 'href="../cases/"')
    return t


def page(s):
    others = ''.join(f'<a href="{o["slug"]}.html"><small>{e(o["tipo"])} · {e(o["dur"])}</small><b>{e(o["name"])}</b></a>' for o in S if o is not s)
    path = '/servicos/' + s['slug']
    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in s['faq'])
    n2 = s.get('num2', ("3C's", 'Context, Concept e Craft'))
    L = s.get('lead')
    lead = ''
    if L:
        bio = ''.join(f'<p>{e(x)}</p>' for x in L['bio'])
        lead = f'''
<section class="lead-sec" aria-label="Quem conduz a consultoria">
  <div class="wrap lead-grid">
    <figure class="lead-img"><img src="{L['img']}" alt="{e(L['alt'])}" loading="lazy"></figure>
    <div class="lead-txt">
      <small>Quem conduz</small>
      <h2>{e(L['name'])}</h2>
      <p class="lead-role">{e(L['role'])}</p>
      {bio}
      <blockquote>“{e(L['quote'])}”</blockquote>
      <a class="lead-link" href="{L['link']}" target="_blank" rel="noopener">Conheça Kauê no LinkedIn <svg><use href="#arr"/></svg></a>
    </div>
  </div>
</section>'''
    hv, hv_cls = '', ' wide'
    if s.get('hero_video'):
        v = s['hero_video']
        hv_cls = ' sv-hero'
        hv = f'''
    <figure class="sv-vid"><video autoplay muted loop playsinline preload="metadata" poster="../video/{v}-poster.jpg" aria-hidden="true"><source src="../video/{v}.mp4" type="video/mp4"></video></figure>'''
    names = ['Context', 'Concept', 'Craft']
    c3 = ''.join(f'<div class="c3c"><span>0{i + 1}</span><h3>{names[i]}</h3><p>{e(t)}</p></div>' for i, t in enumerate(s['c3']))
    rec = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in s['recebe'])
    quando = ''.join(f'<li>{e(q)}</li>' for q in s['quando'])
    cards = ''.join(card(BY[x]) for x in s['cases'])
    from urllib.parse import quote
    wa = 'https://wa.me/5554991000102?text=' + quote(f'Olá, Cooltivo! Quero conversar sobre {s["name"]}.')
    body = f'''
<header class="ch" id="topo">
  <svg class="bg-sym sym" aria-hidden="true"><use href="#sym"/></svg>
  <div class="wrap ch-grid{hv_cls}">
    <div class="ch-txt">
      <a class="back" href="../index.html#entregas"><svg style="transform:scaleX(-1)"><use href="#chev"/></svg>Todos os serviços</a>
      <div class="ch-brand"><span class="seg">{e(s['name'])} · {e(s['tipo'])}</span></div>
      <h1>{e(s['h1'])}</h1>
      <p class="sum">{e(s['intro'])}</p>
      <div class="btns sv-btns"><a class="btn btn-soft" href="../conversa.html">Agendar diagnóstico de 45 min <svg><use href="#arr"/></svg></a><a class="btn btn-line-inv" href="{wa}" target="_blank" rel="noopener">Falar no WhatsApp</a></div>
      <div class="nums"><div><b>{e(s['dur'])}</b><span>{e(s['tipo'])}</span></div><div><b>{e(n2[0])}</b><span>{e(n2[1])}</span></div></div>
    </div>{hv}
  </div>
</header>
{lead}
<main class="story wrap">
  <section class="st">
    <div class="st-lab"><i>01</i>Quando faz sentido</div>
    <div class="st-body"><ul class="did one">{quando}</ul></div>
  </section>
  <section class="st">
    <div class="st-lab"><i>02</i>Como a gente trabalha</div>
    <div class="st-body"><p class="big">Método 3C's: entender antes de criar, decidir junto e executar com excelência.</p><div class="c3g">{c3}</div></div>
  </section>
  <section class="st">
    <div class="st-lab"><i>03</i>O que você recebe</div>
    <div class="st-body"><ul class="rcv">{rec}</ul></div>
  </section>
</main>

<section class="sv-cases">
  <div class="wrap">
    <div class="eyebrow"><svg class="sym"><use href="#sym"/></svg>Cases de {e(s['name'].lower())}</div>
    <h2>Marcas que já <span>cultivamos.</span></h2>
  </div>
  <div class="cgrid wrap">{cards}
  </div>
</section>

<section class="faq">
  <div class="wrap faq-grid">
    <h2><small>Perguntas frequentes</small>{e(s['name'])}</h2>
    <div class="faq-list">{faq}</div>
  </div>
</section>

<section class="sv-other">
  <div class="wrap"><small class="lab">Outros serviços</small><div class="sv-links">{others}</div></div>
</section>
'''
    service = {'@context': 'https://schema.org', '@type': 'Service', 'name': s['name'], 'serviceType': s['name'],
               'description': s['seo_d'], 'url': seo.BASE + path, 'provider': {'@id': seo.ORG_ID},
               'areaServed': [{'@type': 'City', 'name': 'Caxias do Sul'}, {'@type': 'City', 'name': 'Bento Gonçalves'},
                              {'@type': 'Place', 'name': 'Serra Gaúcha'}, {'@type': 'State', 'name': 'Rio Grande do Sul'}],
               'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'O que você recebe', 'itemListElement': [
                   {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': a, 'description': b}} for a, b in s['recebe']]}}
    if L:
        service['provider'] = [{'@id': seo.ORG_ID}, {'@type': 'Person', 'name': L['name'], 'jobTitle': L['role'], 'sameAs': [L['link']], 'worksFor': {'@id': seo.ORG_ID}}]
    faqld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in s['faq']]}
    sch = [service, faqld, seo.crumbs([('Cooltivo', '/'), ('Serviços', '/#entregas'), (s['name'], path)])]
    head = bc.HEAD.format(title=e(s['seo_t']), desc=e(s['seo_d']), seo=seo.head(path, s['seo_t'], s['seo_d'], s['slug'] + '.jpg', 'website', sch))
    return bc.footer_fab.apply(fix(head + body + bc.FOOT), '../', False)


for s in S:
    open(os.path.join(OUT, s['slug'] + '.html'), 'w', encoding='utf-8').write(page(s))
print('ok:', len(S), 'serviços')

# Endereço antigo: Estratégia de canais saiu do site; redireciona para os serviços da home
open(os.path.join(OUT, 'estrategia-de-canais.html'), 'w', encoding='utf-8').write('''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Serviços · Cooltivo</title>
<meta name="robots" content="noindex"><link rel="canonical" href="https://cooltivo.com.br/#entregas">
<meta http-equiv="refresh" content="0; url=../index.html#entregas"></head>
<body><a href="../index.html#entregas">Serviços da Cooltivo</a></body></html>
''')
