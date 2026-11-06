"""Gera talentos/index.html (vagas abertas). Rodar: python3 _tools/build_talentos.py
A remuneração NÃO vai para a página: qualquer coisa no HTML fica visível no código-fonte."""
import os, sys, html, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo
import build_cases as bc
import footer_fab

e = html.escape
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'talentos')
os.makedirs(OUT, exist_ok=True)
POSTED = '2026-11-05'

VAGAS = [
 dict(id='designer', name='Designer de marca', fmt='PJ',
  lead='A gente procura alguém apaixonado por criar marcas únicas, autênticas e corajosas, feitas para resistir ao tempo. Alguém que, antes de abrir o software, quer entender o negócio, os clientes e os concorrentes, porque sabe que uma identidade forte nasce de uma estratégia clara.',
  faz=['Mergulhar no negócio dos clientes junto com o time, nos diagnósticos e workshops.',
       'Transformar a estratégia e a plataforma de marca em identidade visual coerente.',
       'Criar sistemas de marca completos: logo, tipografia, cores, grafismos e aplicações.',
       'Cuidar para que a marca apareça inteira em todos os lugares onde ela vive.'],
  quem=['Portfólio com marcas autorais e o raciocínio por trás de cada escolha.',
        'Repertório de design, arte e cultura.',
        'Gosto por apresentar ideias e defender o porquê delas.',
        'Valores parecidos com os nossos: coragem, clareza e criatividade.']),
 dict(id='social', name='Social media', fmt='PJ',
  lead='A gente procura alguém que entenda que rede social é conversa com gente. Você vai cuidar da presença digital das marcas que a Cooltivo atende, do planejamento ao relatório, com o mesmo cuidado em cada etapa.',
  faz=['Criar o planejamento de conteúdo de cada marca.',
       'Montar e manter o calendário editorial.',
       'Operar os canais: publicar, responder e acompanhar a comunidade.',
       'Gerar relatórios de performance e propor ajustes a partir dos números.'],
  quem=['Escrita clara e criativa, no jeito de falar de cada marca.',
        'Organização para cuidar de várias marcas ao mesmo tempo.',
        'Curiosidade pelos números e pelo que eles contam.',
        'Valores parecidos com os nossos: coragem, clareza e criatividade.']),
]

VALORES = [('Coragem', 'Para defender uma ideia, dizer o que precisa ser dito e fazer diferente quando o comum não serve.'),
           ('Clareza', 'Para pensar antes de criar e explicar o porquê de cada escolha de um jeito que todo mundo entende.'),
           ('Criatividade', 'Para encontrar o jeito de dizer que fica na memória e transformar estratégia em algo que as pessoas sentem.')]

FOTOS = [('../img/historia/h1.jpg', 'Time Cooltivo e parceiros em gravação'),
         ('../img/historia/h6.jpg', 'Workshop de posicionamento da Cooltivo'),
         ('../img/historia/h3.jpg', 'Produção audiovisual em vinhedo')]


def vaga_html(v):
    faz = ''.join(f'<li>{e(x)}</li>' for x in v['faz'])
    quem = ''.join(f'<li>{e(x)}</li>' for x in v['quem'])
    return f'''
    <article class="vaga" id="vaga-{v['id']}">
      <div class="vaga-hd">
        <span class="vaga-tag">Vaga aberta</span>
        <h3>{e(v['name'])}</h3>
        <div class="vaga-meta"><span>Formato {e(v['fmt'])}</span><span>Remuneração a conversar</span></div>
      </div>
      <p class="vaga-lead">{e(v['lead'])}</p>
      <div class="vaga-cols">
        <div><h4>O que você vai fazer</h4><ul>{faz}</ul></div>
        <div><h4>Quem a gente procura</h4><ul>{quem}</ul></div>
      </div>
      <a class="btn btn-dark vaga-go" href="#candidatura" data-vaga="{e(v['name'])}">Vamos conversar? <svg><use href="#arr"/></svg></a>
    </article>'''


def page():
    vals = ''.join(f'<div class="c3c"><span>0{i + 1}</span><h3>{e(a)}</h3><p>{e(b)}</p></div>' for i, (a, b) in enumerate(VALORES))
    fotos = ''.join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy"></figure>' for s, a in FOTOS)
    vagas = ''.join(vaga_html(v) for v in VAGAS)
    opts = ''.join(f'<option>{e(v["name"])}</option>' for v in VAGAS) + '<option>Banco de talentos</option>'
    body = f'''
<header class="ch tl-hero" id="topo">
  <svg class="bg-sym sym" aria-hidden="true"><use href="#sym"/></svg>
  <div class="wrap ch-grid sv-hero">
    <div class="ch-txt">
      <div class="ch-brand"><span class="seg">Talentos · Vagas abertas</span></div>
      <h1>Gente acima da média, com valores, visão de mundo e <span>um querer.</span></h1>
      <p class="sum">A Cooltivo cresce com quem é apaixonado por pessoas, comunicação e criatividade. Isso precisa pulsar. Se você quer criar marcas que resistem ao tempo e trabalhar ao lado de quem pensa assim, a gente quer te conhecer.</p>
      <div class="btns sv-btns"><a class="btn btn-soft" href="#vagas">Ver vagas abertas <svg><use href="#arr"/></svg></a><a class="btn btn-line-inv" href="#candidatura">Banco de talentos</a></div>
    </div>
    <figure class="tl-photo"><img src="../img/time.jpg" alt="Time da Cooltivo trabalhando no jardim do estúdio"></figure>
  </div>
</header>

<main class="story wrap">
  <section class="st">
    <div class="st-lab"><i>01</i>O que pulsa aqui</div>
    <div class="st-body"><p class="big">Paixão por pessoas, comunicação e criatividade. Essa é a base. Em cima dela, três valores guiam tudo o que a gente faz.</p><div class="c3g">{vals}</div></div>
  </section>
</main>

<section class="tl-fotos" aria-label="Fotos do time da Cooltivo"><div class="wrap tl-fotos-grid">{fotos}</div></section>

<section class="tl-vagas" id="vagas">
  <div class="wrap">
    <div class="eyebrow"><svg class="sym"><use href="#sym"/></svg>Vagas abertas</div>
    <h2>Quem vem <span>cultivar</span> com a gente?</h2>
    <div class="vagas">{vagas}
    </div>
  </div>
</section>

<section class="faq tl-form" id="candidatura">
  <div class="wrap faq-grid">
    <h2><small>Candidatura</small>Vamos conversar?</h2>
    <form class="tl-f" id="tlForm" novalidate>
      <label><span>Vaga</span><select id="t-vaga" required><option value="" disabled selected>Selecione</option>{opts}</select></label>
      <label><span>Seu nome</span><input id="t-nome" required autocomplete="name"></label>
      <label><span>Cidade</span><input id="t-cidade" autocomplete="address-level2"></label>
      <label><span>Link do portfólio, Behance, Instagram ou LinkedIn</span><input id="t-link" required placeholder="https://"></label>
      <label class="full"><span>Por que você quer trabalhar na Cooltivo?</span><textarea id="t-por" rows="3" required></textarea></label>
      <button class="btn btn-dark" type="submit">Enviar pelo WhatsApp <svg><use href="#arr"/></svg></button>
      <p class="tl-note">Ao enviar, abrimos o WhatsApp do Kauê com a sua mensagem pronta. É só tocar em enviar.</p>
    </form>
  </div>
</section>
<script>
(function(){{
  var sel=document.getElementById('t-vaga');
  document.querySelectorAll('.vaga-go').forEach(function(a){{a.addEventListener('click',function(){{sel.value=a.dataset.vaga;setTimeout(function(){{document.getElementById('t-nome').focus({{preventScroll:true}})}},600)}})}});
  if(location.hash==='#candidatura'&&!sel.value)sel.value='Banco de talentos';
  document.querySelectorAll('a[href="#candidatura"]:not(.vaga-go)').forEach(function(a){{a.addEventListener('click',function(){{if(!sel.value)sel.value='Banco de talentos'}})}});
  document.getElementById('tlForm').addEventListener('submit',function(ev){{
    ev.preventDefault();var ok=true;
    ['t-vaga','t-nome','t-link','t-por'].forEach(function(id){{var el=document.getElementById(id);var bad=!el.value.trim();el.classList.toggle('bad',bad);if(bad)ok=false}});
    if(!ok)return;
    var v=function(id){{return document.getElementById(id).value.trim()}};
    var t='Olá, Kauê! Quero me candidatar na Cooltivo.\\n\\n*Vaga:* '+v('t-vaga')+'\\n*Nome:* '+v('t-nome')+(v('t-cidade')?'\\n*Cidade:* '+v('t-cidade'):'')+'\\n*Portfólio:* '+v('t-link')+'\\n\\n*Por que a Cooltivo:* '+v('t-por');
    window.open('https://wa.me/5554991000102?text='+encodeURIComponent(t),'_blank','noopener');
  }});
}})();
</script>
'''
    path = '/talentos/'
    t = 'Talentos · Vagas abertas na Cooltivo · Designer de marca e Social media'
    d = 'Vagas abertas na Cooltivo, estúdio de branding da Serra Gaúcha: designer de marca e social media, formato PJ. Gente acima da média, com valores e um querer.'
    jobs = [{'@context': 'https://schema.org', '@type': 'JobPosting', 'title': v['name'], 'description': '<p>' + e(v['lead']) + '</p><p>O que você vai fazer:</p><ul>' + ''.join(f'<li>{e(x)}</li>' for x in v['faz']) + '</ul>',
             'datePosted': POSTED, 'employmentType': 'CONTRACTOR', 'hiringOrganization': {'@type': 'Organization', 'name': 'Cooltivo Estúdio', 'sameAs': seo.BASE + '/', 'logo': seo.BASE + '/img/favicon.svg'},
             'jobLocation': {'@type': 'Place', 'address': {'@type': 'PostalAddress', 'addressLocality': 'Gramado', 'addressRegion': 'RS', 'addressCountry': 'BR'}},
             'directApply': True, 'url': seo.BASE + path + '#vaga-' + v['id']} for v in VAGAS]
    sch = jobs + [seo.crumbs([('Cooltivo', '/'), ('Talentos', path)])]
    head = bc.HEAD.format(title=e(t), desc=e(d), seo=seo.head(path, t, d, 'talentos.jpg', 'website', sch))
    out = head + body + bc.FOOT
    out = out.replace('href="cases.css"', 'href="../cases/cases.css"')
    out = out.replace('<li><a href="./" aria-current="page">Cases</a></li>', '<li><a href="../cases/">Cases</a></li>')
    out = out.replace('<li><a href="../talentos/">Talentos</a></li>', '<li><a href="../talentos/" aria-current="page">Talentos</a></li>')
    out = out.replace('href="./"', 'href="../cases/"')
    return footer_fab.apply(out, '../', False)


open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page())
print('ok: talentos')
