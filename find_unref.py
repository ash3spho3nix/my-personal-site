import pathlib, re

# 1. Get all markdown files
md_files = list(pathlib.Path('content').rglob('*.md'))
all_paths = set()
for fp in md_files:
    # Store as relative path from 'content' directory, normalized
    rel = str(fp.relative_to(pathlib.Path('content'))).replace('\\', '/')
    all_paths.add(rel)

# 2. Collect all links mentioned in all markdown files
referenced_paths = set()
link_pattern = re.compile(r'\[.*?\]\((.*?)\)')

for fp in md_files:
    try:
        text = fp.read_text(encoding='utf-8')
    except Exception:
        continue
    
    for match in link_pattern.findall(text):
        # Clean the link: remove anchor, query params
        link = match.split('#')[0].split('?')[0]
        
        # Handle absolute paths starting with '/'
        if link.startswith('/'):
            link = link[1:]
            
        # Normalize .md extensions (remove if present for comparison)
        if link.endswith('.md'):
            link_no_ext = link[:-3]
        else:
            link_no_ext = link
            
        # Check this link against all files in the content folder
        for path in all_paths:
            path_no_ext = path[:-3] if path.endswith('.md') else path
            # Match if the normalized link matches the normalized path
            if link_no_ext == path_no_ext or link == path:
                referenced_paths.add(path)

# 3. Identify files that are NOT referenced
unreferenced = sorted(list(all_paths - referenced_paths))

# 4. Filter out index files as they are often entry points
final_unreferenced = [f for f in unreferenced if not (f.endswith('_index.md') or f.endswith('index.md'))]

print('\n'.join(final_unreferenced))