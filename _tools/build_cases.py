"""Gera a área interna de cases do site da Cooltivo.

Uso: python3 _tools/build_cases.py   (a partir da raiz do repositório)

Cria cases/index.html (todos os cases) e uma página por case em cases/<slug>.html.
Para trocar as fotos da galeria, substitua img/cases/<slug>-1.jpg, -2.jpg e -3.jpg
(hoje são quadros tirados dos vídeos de cada case) e rode o script de novo, se mudar o texto.
A pasta _tools não é publicada no site.
"""
import html, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo
import footer_fab

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'cases')
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- conteúdo
SEO = {
 'introduce': ('Introduce · Posicionamento e marketing B2B | Case Cooltivo', 'Case Introduce: posicionamento de marca, performance digital e consultoria de marketing em cibersegurança B2B. Dois anos de recorde de faturamento.'),
 'soprano': ('Soprano · Posicionamento e presença digital | Case Cooltivo', 'Case Soprano: o novo posicionamento da indústria gaúcha levado ao digital, com as pessoas à frente dos produtos. Mais de 400% de crescimento no engajamento.'),
 'santa-clara': ('Santa Clara · Programa Plantando o Bem | Case Cooltivo', 'Case Santa Clara: conceito, comunicação e direção criativa do programa Plantando o Bem, em que os alunos criam e tocam projetos sustentáveis.'),
 'zen-design-milao': ('Zen Design em Milão · Zen Pet Collection | Case Cooltivo', 'Case Zen Design: direção criativa e conteúdo da primeira participação da marca gaúcha em Milão, no lançamento da Zen Pet Collection.'),
 'dsf-advogados': ('DSF Advogados · Marketing jurídico digital | Case Cooltivo', 'Case DSF Advogados: verticais de conteúdo e posicionamento digital que levaram a reputação de um dos escritórios mais admirados do RS para o digital.'),
 'neomot': ('Neomot · Reposicionamento de marca | Case Cooltivo', 'Case Neomot: reposicionamento, identidade visual e go-to-market de uma marca de elevadores que virou ecossistema de tecnologia para prédios inteligentes.'),
 'zen-design-expo-revestir': ('Zen Design + Ana Hickmann · Expo Revestir | Case Cooltivo', 'Case Zen Design: a campanha com Ana Hickmann levada à Expo Revestir como experiência de marca, estande e produção de conteúdo.'),
 'garbo': ('Garbo · Clube de vinhos e comunidade de marca | Case Cooltivo', 'Case Garbo Enologia Criativa: estratégia de mídia e conteúdo orgânico que transformou o clube de vinhos da vinícola da Serra Gaúcha em comunidade de marca.'),
 'vallontano': ('Vallontano · Comunicação para vinícola | Case Cooltivo', 'Case Vallontano: posicionamento da comunicação, presença digital e produções com direção criativa própria para a vinícola do Vale dos Vinhedos.'),
 'vino-verace': ('Vino Verace · Marketing para e-commerce de vinhos | Case Cooltivo', 'Case Vino Verace: comunicação focada em valor de marca para um e-commerce de vinhos premium crescer sem competir só por preço.'),
}

ABOUT = {'introduce': 'A Introduce é uma empresa de segurança da informação e transformação digital de Caxias do Sul (RS). Assessora empresas em governança, maturidade digital e proteção de ativos críticos, e criou a Guardiões Digitais, comunidade de profissionais de cibersegurança com mais de 1.500 membros, que realiza o Encontro Guardiões Digitais.', 'soprano': 'Fundada em 1954 em Farroupilha, na Serra Gaúcha, a Soprano é uma das grandes indústrias do Rio Grande do Sul. Produz mais de 4.000 itens em quatro frentes (fechaduras e ferragens, materiais elétricos, componentes para móveis e utilidades térmicas), tem cerca de 1.000 colaboradores e uma estrutura própria em Xangai há mais de duas décadas.', 'santa-clara': 'Fundada em 1911 em Carlos Barbosa, na Serra Gaúcha, a Cooperativa Santa Clara é considerada a mais antiga cooperativa de laticínios em atividade no Brasil. Reúne cerca de 5.000 famílias associadas e mais de 2.300 colaboradores, com unidades industriais em Getúlio Vargas e Casca, e é referência em leite, queijos e derivados no RS.', 'zen-design-milao': 'Fundada em 2004 em Bento Gonçalves (RS), a Zen Design é uma marca brasileira de puxadores e acessórios de alto padrão para arquitetura e interiores. Une matérias-primas naturais, trabalho artesanal e design contemporâneo, com coleções autorais apresentadas em feiras como a Expo Revestir, em São Paulo, e em Milão.', 'dsf-advogados': 'Com quase cinco décadas de história, a Dupont Spiller Fadanelli Advogados tem escritórios em Porto Alegre, Caxias do Sul, Bento Gonçalves, Florianópolis e São Paulo, além de correspondentes no Brasil e no exterior. Em 2021, foi eleita o escritório jurídico mais lembrado e preferido no prêmio Marcas de Quem Decide, do Jornal do Comércio.', 'neomot': 'A Neomot é uma empresa de elevadores e tecnologia para edifícios inteligentes de Caxias do Sul (RS), fundada e liderada por Gustavo Zolet. Além de elevadores e quadros de comando, desenvolve o Cubo, que recupera energia, o software Zeus, que monitora o prédio, a assistente virtual Anna e o app Neo, com o qual o morador chama o elevador e reserva áreas comuns.', 'garbo': 'A Garbo Enologia Criativa nasceu em Bento Gonçalves (RS) há cerca de dez anos, pelas mãos dos enólogos Andrei Bellé, Guilherme Caio e Jhonatan Marini. É conhecida pela "enologia criativa": cortes autorais, amadurecimento em madeiras brasileiras e exóticas e castas pouco usuais. Tem loja na rota Caminhos de Pedra e o clube de vinhos Experientia.', 'vallontano': 'Fundada em 1999, a Vallontano Vinhos Nobres é uma vinícola familiar de Bento Gonçalves, no Vale dos Vinhedos, sob o comando e a direção de Ana Paula Valduga e com o enólogo Luís Henrique Zanini. Produz vinhos e espumantes em pequena escala, como o Vallontano Reserva Merlot e o espumante LaToller, e recebe visitantes para degustações na Serra Gaúcha.', 'vino-verace': 'Fundada em 2020, a Vino Verace é uma curadoria especializada de vinhos com loja online. Trabalha com pequenos produtores, produções limitadas e rótulos de mais de 30 países, da Serra Gaúcha a regiões menos óbvias do Velho e do Novo Mundo. Mais de 100 mil garrafas já passaram pela sua curadoria, com atendimento de sommeliers e a Confraria da Vino Verace, de degustações guiadas.', 'zen-design-expo-revestir': 'Fundada em 2004 em Bento Gonçalves (RS), a Zen Design é uma marca brasileira de puxadores e acessórios de alto padrão para arquitetura e interiores. Une matérias-primas naturais, trabalho artesanal e design contemporâneo, com coleções autorais apresentadas em feiras como a Expo Revestir, em São Paulo, e em Milão.'}

CASES = [
 dict(slug='introduce', name='Introduce', logo=('introduce.png', 30), seg='Tecnologia · Cibersegurança B2B',
  title='Recorde de faturamento e um canal de crescimento exponencial.',
  summary='Posicionamento, performance digital e consultoria estratégica para uma empresa de cibersegurança B2B ganhar escala.',
  desafio='A Introduce atua em cibersegurança B2B, um mercado técnico e competitivo. O desafio era ganhar escala, autoridade e previsibilidade comercial.',
  estrategia='Criamos o posicionamento da marca, estruturamos a performance digital e atuamos com consultoria estratégica, conectando marca, conteúdo e geração de demanda.',
  fizemos=['Posicionamento de marca', 'Estruturação da performance digital', 'Consultoria estratégica de marketing', 'Direção criativa de conteúdo e eventos'],
  resultado='Dois anos seguidos de recorde de faturamento e uma comunidade com mais de 1.500 membros, a Guardiões Digitais.',
  nums=[('2 anos', 'seguidos de recorde de faturamento'), ('1.500+', 'membros na comunidade Guardiões Digitais')],
  chips=['Consultoria de marketing', 'Presença e performance', 'Direção criativa'],
  collab='Vitral Filmes, Produtora Balsa e Impulse Company', video='introduce', ig='https://www.instagram.com/p/DWZwsjIEgHx/'),
 dict(slug='soprano', name='Soprano', logo=('soprano.png', 20), seg='Indústria · Presença digital',
  title='Uma gigante da indústria mais nativa no digital.',
  summary='O novo posicionamento da Soprano levado para o digital, com as pessoas à frente dos produtos.',
  desafio='A Soprano, uma gigante da indústria, tinha um novo posicionamento e precisava levá-lo para o digital de um jeito mais próximo das pessoas.',
  estrategia='Construímos uma comunicação que coloca as histórias à frente dos produtos: as pessoas, os bastidores e quem usa a marca no dia a dia.',
  fizemos=['Tradução do posicionamento para o digital', 'Linha editorial com pessoas como protagonistas', 'Produção de conteúdo', 'Gestão da presença digital'],
  resultado='Mais de 400% de crescimento no engajamento, com as pessoas como protagonistas da marca.',
  nums=[('+400%', 'de crescimento no engajamento'), ('Pessoas', 'como protagonistas da marca')],
  chips=['Posicionamento', 'Presença digital', 'Produção de conteúdo'],
  collab='Fabu Design e Vitral Filmes', video='soprano-digital', ig='https://www.instagram.com/p/DdRaOx4Ae9v/'),
 dict(slug='santa-clara', name='Santa Clara', logo=('santa-clara.png', 44), seg='Cooperativa · Programa Plantando o Bem',
  title='1º Concurso de Sustentabilidade Criativa.',
  summary='Um programa de educação reinventado para que os próprios alunos criem e toquem projetos sustentáveis.',
  desafio='O Plantando o Bem leva educação alimentar e hortas orgânicas a escolas do interior gaúcho, com cartilhas e teatro. Só que as hortas não tinham continuidade depois da implantação.',
  estrategia='Reinventamos o programa: nasceu o primeiro concurso de sustentabilidade criativa, em que os próprios alunos criam e tocam projetos sustentáveis, com prêmios para alunos e professores.',
  fizemos=['Conceito do concurso', 'Comunicação do programa', 'Direção criativa', 'Gestão do projeto'],
  resultado='58 projetos inscritos, R$ 35 mil em prêmios para alunos e professores e o reconhecimento no Top de Marketing ADVB/RS 2024.',
  nums=[('58', 'projetos inscritos'), ('R$ 35 mil', 'em prêmios para alunos e professores')],
  award='Top de Marketing ADVB/RS 2024',
  chips=['Conceito', 'Comunicação', 'Direção criativa'],
  collab='Marlon Vieira', video='santa-clara', ig=None),
 dict(slug='zen-design-milao', name='Zen Design', logo=('zen.png', 28), seg='Indústria · Design para a casa',
  title='Uma marca brasileira no Salone del Mobile de Milão.',
  summary='A primeira vez da Zen Design em Milão, com o lançamento da Zen Pet Collection.',
  desafio='Levar a Zen Design pela primeira vez ao Salone del Mobile, em Milão, com o lançamento de uma linha exclusiva para pets.',
  estrategia='Criamos a narrativa da Zen Pet Collection como extensão de um lifestyle em que o pet também expressa quem somos e como vivemos, com direção criativa e conteúdo para o lançamento. Também gerimos um time internacional, entre modelo, video maker e influencer pet.',
  fizemos=['Narrativa da coleção', 'Direção criativa', 'Conteúdo do lançamento', 'Gestão de um time internacional: modelo, video maker e influencer pet'],
  resultado='A primeira participação da marca em Milão e o lançamento da Zen Pet Collection, em 2025.',
  nums=[('1ª vez', 'da marca em Milão'), ('2025', 'lançamento da Zen Pet Collection')],
  chips=['Direção criativa', 'Lançamento', 'Conteúdo'],
  collab='David Schwab', video='zen-milao', ig=None),
 dict(slug='dsf-advogados', name='DSF Advogados', logo=('dsf.png', 46), seg='Advocacia · Posicionamento digital',
  title='Recorde em geração de leads e posicionamento digital.',
  summary='Verticais de conteúdo que levaram a reputação de um dos escritórios mais admirados do RS para o digital.',
  desafio='Entre os 3 escritórios mais lembrados e admirados do Rio Grande do Sul, a DSF Advogados precisava levar essa reputação para o digital e transformá-la em novos negócios.',
  estrategia='Criamos verticais de conteúdo a partir das expertises do escritório, dando voz aos especialistas de cada área de atuação, com materiais ricos, eventos segmentados e automação de marketing.',
  fizemos=['Posicionamento digital', 'Verticais de conteúdo com os especialistas', 'Materiais ricos', 'Eventos segmentados', 'Automação de marketing', 'Estratégia de geração de leads'],
  resultado='Recorde em geração de leads, com uma presença digital à altura da reputação do escritório.',
  nums=[('Top 3', 'entre os escritórios mais lembrados e admirados do RS'), ('Recorde', 'em geração de leads')],
  chips=['Posicionamento digital', 'Verticais de conteúdo', 'Geração de leads'],
  collab='Impulse Company e Berrô Strategy', video='dsf', wide=True, ig=None),
 dict(slug='neomot', name='Neomot', logo=('neomot.png', 30), seg='Tecnologia · Prédios inteligentes',
  title='Muito além do elevador.',
  summary='O reposicionamento de uma marca conhecida por elevadores como ecossistema de tecnologia para prédios inteligentes.',
  desafio='Reconhecida por elevadores, a Neomot precisava mostrar ao mercado que ia além disso, com uma visão de ecossistema de tecnologia para prédios inteligentes.',
  estrategia='Unimos um time de especialistas e, depois da imersão e do diagnóstico, conduzimos o workshop de posicionamento, a direção criativa e o refresh da identidade. Também entregamos o plano de go-to-market para levar a nova mensagem ao mercado.',
  fizemos=['Imersão e diagnóstico', 'Workshop de posicionamento', 'Refresh da identidade visual', 'Plano de go-to-market'],
  resultado='Um novo posicionamento, uma identidade renovada e um plano de go-to-market para apresentar a Neomot como ecossistema de tecnologia.',
  nums=[('Imersão', 'diagnóstico e workshop de posicionamento'), ('GTM', 'plano de go-to-market')],
  chips=['Reposicionamento', 'Identidade visual', 'Go-to-market'],
  collab='Marlon Vieira, Luis Fernando Menti, Sérgio Smidt, Claudia Schroeder e Studio Mateus Araújo', video='neomot', ig=None),
 dict(slug='zen-design-expo-revestir', name='Zen Design', logo=('zen.png', 28), extra='+ Ana Hickmann', seg='Indústria · Expo Revestir',
  title='Sua Casa Veste Zen: moda e arquitetura no mesmo lugar.',
  summary='A campanha com Ana Hickmann levada à Expo Revestir como experiência de marca e conteúdo.',
  desafio='Levar o posicionamento Sua Casa Veste Zen, que conecta a inspiração da moda à arquitetura, para a Expo Revestir.',
  estrategia='Levamos a campanha estrelada por Ana Hickmann até a feira e transformamos a presença da marca em uma experiência de marca e de conteúdo.',
  fizemos=['Conceito Sua Casa Veste Zen', 'Campanha com Ana Hickmann', 'Experiência de marca na Expo Revestir', 'Produção de conteúdo'],
  resultado='Uma presença na Expo Revestir que virou experiência de marca e conteúdo, com Ana Hickmann como rosto da campanha.',
  nums=[('Ana Hickmann', 'rosto da campanha'), ('Expo Revestir', 'experiência de marca e conteúdo')],
  chips=['Posicionamento', 'Campanha', 'Experiência de marca'],
  collab=None, video='zen-ana-hickmann', ig=None),
 dict(slug='garbo', name='Garbo Enologia Criativa', logo=('garbo.png', 44), seg='Vinícola · Serra Gaúcha',
  title='Um clube de vinhos que virou comunidade de marca.',
  summary='Estratégia de mídia e conteúdo orgânico que transformou o clube de vinhos da Garbo em um motor de clientes apaixonados.',
  desafio='Posicionar de maneira única nas redes uma das vinícolas mais criativas do Brasil e fazer do seu clube de vinhos mais do que uma assinatura.',
  estrategia='Criamos a estratégia de mídia e de conteúdo orgânico do clube, com direção criativa e uma operação de conteúdo eficiente. O conteúdo construiu uma comunidade em torno da marca.',
  fizemos=['Estratégia de mídia', 'Conteúdo orgânico', 'Direção criativa', 'Operação de conteúdo'],
  resultado='O clube de vinhos gera mais de R$ 700 mil de receita por ano e se tornou um motor de clientes apaixonados pela marca.',
  nums=[('R$ 700 mil+', 'de receita anual gerada pelo clube de vinhos'), ('Comunidade', 'de clientes apaixonados pela marca')],
  chips=['Estratégia de mídia', 'Conteúdo orgânico', 'Comunidade de marca'],
  collab='Alba Arte', video='garbo', ig='https://www.instagram.com/reel/DMiEqAKq_YA/'),
 dict(slug='vallontano', name='Vallontano', logo=('vallontano.png', 44), seg='Vinícola · Serra Gaúcha',
  title='Uma imagem à altura do vinho.',
  summary='Posicionamento da comunicação, presença digital e produções com direção criativa própria.',
  desafio='A Vallontano precisava de uma comunicação e de uma imagem à altura dos seus vinhos, consistentes em todos os canais.',
  estrategia='Construímos a estratégia de posicionamento da comunicação e do conteúdo e fazemos a gestão da presença digital. Nas produções, a direção criativa e de arte é nossa.',
  fizemos=['Posicionamento da comunicação', 'Gestão da presença digital', 'Direção criativa e de arte nas produções'],
  resultado='Uma direção criativa que nos permite manter um posicionamento claro, verdadeiro e relevante em todos os canais.',
  nums=[('Direção criativa', 'posicionamento claro, verdadeiro e relevante')],
  chips=['Posicionamento', 'Presença digital', 'Direção criativa'],
  collab='Vitral Filmes e Alba Arte', video='vallontano', ig=None),
 dict(slug='vino-verace', name='Vino Verace', logo=None, seg='E-commerce · Vinhos premium',
  title='De R$ 20 mil para R$ 672 mil no mês.',
  summary='Uma comunicação focada em valor de marca para um e-commerce de vinhos crescer sem competir só por preço.',
  desafio='Um e-commerce com mais de 1.000 rótulos de 30 países precisava crescer sem competir só por preço. A marca vivia de conteúdo de terceiros.',
  estrategia='Criamos uma cultura de comunicação focada em valor de marca, integrada a campanhas mensais em Google Ads, Meta Ads, e-mail, WhatsApp e CRM. O posicionamento foi o diferencial: além do e-commerce, nasceu a VERACE, uma marca própria de vinhos, e uma linha de serviços de experiência.',
  fizemos=['Comunicação focada em valor de marca', 'Posicionamento: marca própria VERACE e linha de serviços de experiência', 'Campanhas mensais integradas', 'Mídia em Google Ads e Meta Ads', 'Relacionamento por e-mail, WhatsApp e CRM'],
  resultado='Quando chegamos, a Vino Verace faturava R$ 20 mil por mês. Entregamos um mês recorde de Black Friday, com R$ 672 mil: um crescimento de 33,6 vezes (+3.260%).',
  nums=[('33,6x', 'de crescimento: de R$ 20 mil por mês a R$ 672 mil no recorde de Black Friday'), ('1.000+', 'rótulos de 30 países')],
  chips=['Consultoria de marketing', 'Presença e performance', 'Direção criativa'],
  collab='Impulse Company e Balsa Produtora', video='vino-verace', ig='https://www.instagram.com/p/DN1TI1sZil0/'),
]

e = html.escape
tese = open(os.path.join(ROOT, 'tese.html'), encoding='utf-8').read()
DEFS = re.search(r'<svg width="0" height="0".*?</svg>', tese, re.S).group(0)

HEAD = '''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="../img/favicon.svg">
<link rel="stylesheet" href="cases.css">
{seo}
</head>
<body>
''' + DEFS + '''
<nav id="nav">
  <div class="wrap">
    <a class="brand" href="../index.html" aria-label="Cooltivo Estúdio, página inicial"><svg class="sym"><use href="#sym"/></svg><b>cooltivo</b><span>estúdio</span></a>
    <ul>
      <li><a href="./" aria-current="page">Cases</a></li>
      <li><a href="../index.html#historia">Nossa história</a></li>
      <li><a href="../index.html#jeito">Método</a></li>
      <li><a href="../index.html#entregas">Serviços</a></li>
      <li><a href="../index.html#conteudos">Conteúdos</a></li>
      <li><a href="../comunidade/">Comunidade</a></li>
    </ul>
    <a class="btn" href="../index.html#contato"><span>Conversar<span class="nl"> sobre minha marca</span></span> <svg><use href="#arr"/></svg></a>
  </div>
</nav>
'''

FOOT = '''
<section class="cta">
  <svg class="bg-sym sym" aria-hidden="true"><use href="#sym"/></svg>
  <div class="wrap">
    <div class="inner">
      <div class="eyebrow">Vamos conversar</div>
      <h2>Vamos <span>cultivar</span> sua marca?</h2>
      <p class="lead">Conte o momento do seu negócio. Conte conosco para crescer.</p>
      <div class="btns">
        <a class="btn btn-soft" href="../index.html#contato">Falar com a Cooltivo <svg><use href="#arr"/></svg></a>
        <a class="btn btn-line-inv" href="./">Ver todos os cases</a>
      </div>
    </div>
    <div class="contact">
      <a href="mailto:kaue@cooltivo.com.br"><small>E-mail</small><span>kaue@cooltivo.com.br</span></a>
      <a href="https://wa.me/5554991000102" target="_blank" rel="noopener"><small>WhatsApp</small><span>(54) 9.9100-0102</span></a>
      <div><small>Onde estamos</small><span>Made in Serra Gaúcha (RS)</span></div>
    </div>
  </div>
  <footer>
    <div class="wrap">
      <a class="brand" href="../index.html"><svg class="sym"><use href="#sym"/></svg><b>cooltivo</b><span>estúdio</span></a>
      <div class="sig"><svg class="sym"><use href="#sym"/></svg>NOTHING GREAT<br>IS MADE ALONE</div>
      <div class="links"><a href="https://www.instagram.com/cooltivoestudio/" target="_blank" rel="noopener">Instagram</a><a href="https://www.linkedin.com/in/kauegrasnievicz/" target="_blank" rel="noopener">LinkedIn</a><span>© 2026 Cooltivo</span></div>
    </div>
  </footer>
</section>

<script>
/* Menu sólido depois da capa */
(function(){
  const nav=document.getElementById('nav'),hero=document.getElementById('topo');let busy=false;
  const upd=()=>{busy=false;nav.classList.toggle('solid',scrollY>hero.offsetHeight-80)};
  upd();addEventListener('scroll',()=>{if(!busy){busy=true;requestAnimationFrame(upd)}},{passive:true});addEventListener('resize',upd);
})();
/* Vídeo do case: "Assistir com som" liga o som e mostra os controles */
(function(){
  document.querySelectorAll('.ch-vid').forEach(f=>{const v=f.querySelector('video'),b=f.querySelector('.watch');if(!v||!b)return;
    b.addEventListener('click',()=>{v.muted=false;v.controls=true;v.currentTime=0;v.play().catch(()=>{});f.classList.add('playing')})});
})();
</script>
</body>
</html>
'''


def logo_html(c, cls=''):
    if not c['logo']:
        return f'<span class="wordmark">{e(c["name"])}</span>'
    src, h = c['logo']
    extra = f'<em>{e(c["extra"])}</em>' if c.get('extra') else ''
    return f'<img class="clogo {cls}" src="../logos/{src}" alt="{e(c["name"])}" style="height:{h}px">{extra}'


def nums_html(nums, cls='nums'):
    return f'<div class="{cls}">' + ''.join(f'<div><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in nums) + '</div>'


def case_page(i, c):
    nxt = CASES[(i + 1) % len(CASES)]
    wide = c.get('wide')
    vid = f'../video/cases/{c["video"]}'
    ig = f'<a class="ig" href="{c["ig"]}" target="_blank" rel="noopener">Ver no Instagram <svg><use href="#arr"/></svg></a>' if c.get('ig') else ''
    award = f'<div class="award"><span class="medal">TOP</span>{e(c["award"])}</div>' if c.get('award') else ''
    collab = (f'<div><small>Collab · Ecossistema Cooltivo</small><b>{e(c["collab"])}</b></div>' if c.get('collab') else '')
    gal_cls = 'h' if wide else 'v'
    gallery = ''.join(f'<figure><img src="../img/cases/{c["slug"]}-{k}.jpg" alt="Bastidores do case {e(c["name"])}, imagem {k}" loading="lazy"></figure>' for k in (1, 2, 3))
    ab = ABOUT.get(c['slug'])
    short = c['name'].split(' ')[0] if c['slug'] in ('garbo', 'dsf-advogados') else c['name']
    sobre = (f'<section class="sobre" aria-label="Sobre a {e(c["name"])}"><div class="wrap"><h2><small>Quem é</small>Sobre a {e(short)}</h2><p>{e(ab)}</p></div></section>') if ab else ''
    fizemos = ''.join(f'<li>{e(x)}</li>' for x in c['fizemos'])
    body = f'''
<header class="ch" id="topo">
  <svg class="bg-sym sym" aria-hidden="true"><use href="#sym"/></svg>
  <div class="wrap ch-grid{' wide' if wide else ''}">
    <div class="ch-txt">
      <a class="back" href="./"><svg style="transform:scaleX(-1)"><use href="#chev"/></svg>Todos os cases</a>
      <div class="ch-brand">{logo_html(c)}<span class="seg">{e(c['seg'])}</span></div>
      <h1>{e(c['title'])}</h1>
      <p class="sum">{e(c['summary'])}</p>
      {nums_html(c['nums'])}
    </div>
    <figure class="ch-vid{' h' if wide else ''}">
      <video autoplay muted loop playsinline preload="metadata" poster="{vid}.jpg" aria-label="Vídeo do case {e(c['name'])}"><source src="{vid}.mp4" type="video/mp4"></video>
      <button class="watch" type="button"><svg><use href="#play"/></svg>Assistir com som</button>
      {ig}
    </figure>
  </div>
</header>

<section class="ficha" aria-label="Ficha do case">
  <div class="wrap">
    <div><small>Cliente</small><b>{e(c['name'])}</b></div>
    <div><small>Segmento</small><b>{e(c['seg'])}</b></div>
    <div><small>Entregas</small><span class="chips">{''.join(f'<span>{e(x)}</span>' for x in c['chips'])}</span></div>
    {collab}
  </div>
</section>
{sobre}

<main class="story wrap">
  <section class="st" id="desafio">
    <div class="st-lab"><i>01</i>Desafio</div>
    <div class="st-body"><p class="big">{e(c['desafio'])}</p></div>
  </section>
  <section class="st" id="estrategia">
    <div class="st-lab"><i>02</i>Estratégia</div>
    <div class="st-body">
      <p class="big">{e(c['estrategia'])}</p>
      <h2 class="did-t">O que fizemos</h2>
      <ul class="did">{fizemos}</ul>
    </div>
  </section>
</main>

<section class="gal" aria-label="Bastidores">
  <div class="wrap"><div class="gal-grid {gal_cls}">{gallery}</div></div>
</section>

<section class="res" id="resultado">
  <div class="wrap res-grid">
    <div class="st-lab"><i>03</i>Resultado</div>
    <div>
      <p class="big">{e(c['resultado'])}</p>
      {nums_html(c['nums'], 'rnums')}
      {award}
    </div>
  </div>
</section>

<a class="next" href="{nxt['slug']}.html">
  <div class="wrap">
    <small>Próximo case</small>
    <span class="nx-brand">{logo_html(nxt, 'dark')}</span>
    <b>{e(nxt['title'])}</b>
    <span class="nx-arr"><svg><use href="#arr"/></svg></span>
  </div>
</a>
'''
    t, d = SEO.get(c['slug'], (f'{c["name"]} · Case Cooltivo', c['summary']))
    path = '/cases/' + c['slug']
    c = dict(c, about=c.get('about') or ABOUT.get(c['slug']))
    work = {'@context': 'https://schema.org', '@type': 'CreativeWork', 'name': f'Case {c["name"]}: {c["title"]}',
            'headline': c['title'], 'description': d, 'url': seo.BASE + path, 'inLanguage': 'pt-BR',
            'image': seo.BASE + '/img/og/' + c['slug'] + '.jpg', 'creator': {'@id': seo.ORG_ID},
            'publisher': {'@id': seo.ORG_ID}, 'keywords': ', '.join(c['chips']),
            'about': {'@type': 'Organization', 'name': c['name']}}
    if c.get('about_url'):
        work['about']['url'] = c['about_url']
    if c.get('about'):
        work['about']['description'] = c['about']
    sch = [work, seo.crumbs([('Cooltivo', '/'), ('Cases', '/cases/'), (c['name'], path)])]
    head = HEAD.format(title=e(t), desc=e(d), seo=seo.head(path, t, d, c['slug'] + '.jpg', 'article', sch))
    return footer_fab.apply(head + body + FOOT, '../', False)


def index_page():
    cards = []
    for c in CASES:
        a, b = c['nums'][0]
        cards.append(f'''
    <a class="cc" href="{c['slug']}.html">
      <span class="cc-img"><img src="../video/cases/{c['video']}.jpg" alt="Case {e(c['name'])}: {e(c['title'])}" loading="lazy"></span>
      <span class="cc-body">
        <span class="ch-brand">{logo_html(c)}<span class="seg">{e(c['seg'])}</span></span>
        <span class="cc-t">{e(c['title'])}</span>
        <span class="cc-n"><b>{e(a)}</b><span>{e(b)}</span></span>
        <span class="cc-go">Ver case <svg><use href="#arr"/></svg></span>
      </span>
    </a>''')
    body = f'''
<header class="ch ci" id="topo">
  <svg class="bg-sym sym" aria-hidden="true"><use href="#sym"/></svg>
  <div class="wrap">
    <div class="eyebrow"><svg class="sym"><use href="#sym"/></svg>Cases</div>
    <h1>Resultados que <span>cultivamos.</span></h1>
    <p class="sum">O desafio, a estratégia e o resultado de marcas que cultivamos com clareza, coragem e criatividade.</p>
  </div>
</header>
<main class="cgrid wrap">{''.join(cards)}
</main>
'''
    t = 'Cases de branding e marketing · Cooltivo Estúdio'
    d = 'Cases de branding, posicionamento e comunicação da Cooltivo com marcas do RS: Introduce, Soprano, Santa Clara, Zen Design, DSF Advogados, Neomot e mais.'
    lst = {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': t, 'description': d, 'url': seo.BASE + '/cases/',
           'publisher': {'@id': seo.ORG_ID}, 'hasPart': [{'@type': 'CreativeWork', 'name': 'Case ' + c['name'], 'url': seo.BASE + '/cases/' + c['slug']} for c in CASES]}
    head = HEAD.format(title=e(t), desc=e(d), seo=seo.head('/cases/', t, d, 'cases.jpg', 'website', [lst, seo.crumbs([('Cooltivo', '/'), ('Cases', '/cases/')])]))
    return footer_fab.apply(head + body + FOOT, "../", False)


for i, c in enumerate(CASES):
    open(os.path.join(OUT, c['slug'] + '.html'), 'w', encoding='utf-8').write(case_page(i, c))
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(index_page())
print('ok:', len(CASES), 'cases')
