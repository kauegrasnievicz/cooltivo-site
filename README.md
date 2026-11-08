# Cooltivo Estúdio — one page

Site estático (HTML + CSS, sem build). Publicado via GitHub Pages a partir da branch `main`.

- `index.html` — página completa
- `img/` — fotos, símbolo (c) e favicon
- `img/cases/` — imagens dos cases
- `video/` — vídeo da capa e da seção "Nada grande é feito sozinho"
- `fonts/` — Inter (OFL), usada como alternativa à Helvetica Neue

Para atualizar: edite os arquivos e faça commit na `main`.

## Movimento
Padrão único em `assets/motion.css` (tokens `--ease`, `--t`, `--t-slow`, `--rv-t`) e `assets/motion.js` (entrada ao rolar). `_tools/motion.py` injeta nas páginas e deve rodar por último, depois dos builders, `footer_fab.py` e `seo*.py`. `_tools/motion_norm.py` uniformiza as transições de hover.
