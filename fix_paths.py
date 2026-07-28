from pathlib import Path
files = [
    Path('src/pages/camping-outdoor/index.astro'),
    Path('src/pages/camping-outdoor/shambololo/index.astro'),
    Path('src/pages/camping-outdoor/riverview-farm/index.astro'),
]
for path in files:
    text = path.read_text(encoding='utf-8')
    text = text.replace('..//images/camping-outdoor/', '/images/camping-outdoor/')
    text = text.replace('../images/camping-outdoor/', '/images/camping-outdoor/')
    text = text.replace('../../images/camping-outdoor/', '/images/camping-outdoor/')
    path.write_text(text, encoding='utf-8')
