"""Blocos de SEO compartilhados (canonical, Open Graph, JSON-LD)."""
import html, json

BASE = 'https://cooltivo.com.br'
ORG_ID = BASE + '/#org'
e = html.escape

ORG = {
    '@context': 'https://schema.org',
    '@type': 'ProfessionalService',
    '@id': ORG_ID,
    'name': 'Cooltivo Estúdio',
    'alternateName': 'Cooltivo',
    'description': 'Estúdio de branding, estratégia de marca e comunicação da Serra Gaúcha. Posicionamento, presença digital e consultoria de marketing para empresas de Caxias do Sul, Bento Gonçalves e do Rio Grande do Sul.',
    'slogan': 'Cultivamos marcas que resistem ao tempo.',
    'url': BASE + '/',
    'logo': BASE + '/img/favicon.svg',
    'image': BASE + '/img/og/home.jpg',
    'email': 'kaue@cooltivo.com.br',
    'telephone': '+55 54 99100-0102',
    'priceRange': '$$',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Gramado', 'addressRegion': 'RS', 'addressCountry': 'BR'},
    'areaServed': [
        {'@type': 'City', 'name': 'Caxias do Sul'},
        {'@type': 'City', 'name': 'Bento Gonçalves'},
        {'@type': 'City', 'name': 'Gramado'},
        {'@type': 'Place', 'name': 'Serra Gaúcha'},
        {'@type': 'State', 'name': 'Rio Grande do Sul'},
    ],
    'founder': {'@type': 'Person', 'name': 'Kauê Grasnievicz', 'jobTitle': 'Cofundador e diretor de estratégia',
                'sameAs': ['https://www.linkedin.com/in/kauegrasnievicz/']},
    'sameAs': ['https://www.instagram.com/cooltivoestudio/'],
    'knowsAbout': ['Branding', 'Posicionamento de marca', 'Estratégia de marca', 'Comunicação', 'Marketing digital', 'Produção de conteúdo', 'Direção criativa'],
    'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Serviços da Cooltivo', 'itemListElement': [
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': 'Posicionamento de marca', 'description': 'Projeto de 6 a 8 semanas para definir essência, diferenciação e narrativa da marca.'}},
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': 'Presença digital', 'description': 'Estratégia, conteúdo e gestão dos canais digitais da marca, de 6 a 12 meses.'}},
        {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': 'Consultoria de marketing', 'description': 'Acompanhamento estratégico de marketing e marca, em formato flexível.'}},
    ]},
}


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '</script>'


def crumbs(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': BASE + u} for i, (n, u) in enumerate(items)]}


def head(path, title, desc, og, kind='website', schemas=(), index=True):
    """path: caminho canônico ('/', '/cases/introduce'); og: arquivo em img/og/."""
    url = BASE + path
    img = BASE + '/img/og/' + og
    tags = [
        f'<link rel="canonical" href="{url}">',
        '<meta name="robots" content="' + ('index, follow, max-image-preview:large' if index else 'noindex') + '">',
        '<meta name="geo.region" content="BR-RS"><meta name="geo.placename" content="Gramado, Serra Gaúcha">',
        '<meta name="theme-color" content="#24503a">',
        f'<meta property="og:type" content="{kind}">',
        '<meta property="og:site_name" content="Cooltivo Estúdio">',
        '<meta property="og:locale" content="pt_BR">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:title" content="{e(title)}">',
        f'<meta property="og:description" content="{e(desc)}">',
        f'<meta property="og:image" content="{img}">',
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{e(title)}">',
        f'<meta name="twitter:description" content="{e(desc)}">',
        f'<meta name="twitter:image" content="{img}">',
    ] + [ld(s) for s in schemas]
    return '\n'.join(tags)
