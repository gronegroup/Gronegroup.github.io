import re
from collections import Counter

# Leer el archivo
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar todas las subcategorías
matches = re.findall(r"subcategory: '([^']+)'", content)
counts = Counter(matches)

print('✓ Subcategorías encontradas:')
print()
for cat, count in sorted(counts.items()):
    print(f'  • {cat}: {count} productos')
print()
print(f'Total: {sum(counts.values())} productos con subcategoría')
