import pathlib, re
md_files = list(pathlib.Path('content').rglob('*.md'))
links = set()
for fp in md_files:
    try:
        text = fp.read_text()
    except Exception:
        continue
    for m in re.findall(r'\[.*?\]\((.*?)\)', text):
        k = m.split('#')[0].split('?')[0]
        if k.startswith('/'):
            k = k[1:]
        if k.endswith('/'):
            k = k[:-1]
        links.add(k)
unreferenced = []
for fp in md_files:
    rel = str(fp.relative_to(pathlib.Path('content')))
    rel_strip = rel[:-3]
    if rel_strip not in links and not rel_strip.endswith('/index') and not rel_strip.endswith('_index'):
        unreferenced.append(rel)
print('\n'.join(unreferenced))
