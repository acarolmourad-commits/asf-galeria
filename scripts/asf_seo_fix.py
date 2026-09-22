# -*- coding: utf-8 -*-
"""ASF SEO/a11y fix: adiciona texto alternativo ao template de imagem da galeria. Idempotente."""
p = 'index.html'
s = open(p, encoding='utf-8').read()
old = '<img src="${f.url}" loading="lazy" onerror="this.parentNode.remove()">'
new = '<img src="${f.url}" alt="Foto de surf enviada pela comunidade ASF" loading="lazy" onerror="this.parentNode.remove()">'
if old in s:
    open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    print('alt adicionado')
else:
    print('Nada a corrigir.')