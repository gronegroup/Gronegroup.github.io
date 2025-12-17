import re

# Leer el archivo
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Eliminar subcategorías duplicadas (mantener solo la primera)
content = re.sub(
    r"(subcategory: '[^']+'),\s*subcategory: '[^']+'",
    r'\1',
    content
)

# Escribir el archivo
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('✓ Subcategorías duplicadas eliminadas')
