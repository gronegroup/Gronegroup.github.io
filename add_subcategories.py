import re

# Leer el archivo
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Mapeo de comentarios a subcategorías
subcats = {
    '// GRABADORES NVR': 'Grabadores NVR',
    '// CAMARAS IP 2MP': 'Cámaras IP 2MP',
    '// CAMARAS IP 4MP': 'Cámaras IP 4MP',
    '// CAMARAS IP 6MP': 'Cámaras IP 6MP',
    '// CAMARAS IP 8MP': 'Cámaras IP 8MP',
    '// CAMARAS IP PTZ': 'Cámaras IP PTZ',
    '// HDD': 'Discos Duros',
    '// CAMARAS ANALOGICAS 720P': 'Cámaras Analógicas 720P',
    '// CAMARAS ANALOGICAS 1080P': 'Cámaras Analógicas 1080P',
    '// CAMARAS COLOR VU 1080P': 'Cámaras ColorVu 1080P',
    '// CAMARAS 3K (5MP)': 'Cámaras 3K (5MP)',
    '// CAMARAS 4K (8MP)': 'Cámaras 4K (8MP)',
    '// GRABADORES DVR 720P/1080P LITE': 'Grabadores DVR 720P/1080P',
    '// DVR 1080P REAL/5MP LITE': 'DVR 1080P Real',
    '// DVR 5MP/4K': 'DVR 5MP/4K'
}

current_subcat = None
lines = content.split('\n')
new_lines = []

for line in lines:
    # Detectar comentario de categoría
    for comment, subcat in subcats.items():
        if comment in line:
            current_subcat = subcat
            break
    
    # Si encontramos category: 'camaras' y no tiene subcategory, agregarlo
    if current_subcat and "category: 'camaras'" in line and 'subcategory' not in line:
        # Agregar subcategory después de category
        line = line.replace(
            "category: 'camaras'",
            f"category: 'camaras',\n                subcategory: '{current_subcat}'"
        )
    
    new_lines.append(line)

# Escribir el archivo
with open('index.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))

print(f'✓ Subcategorías agregadas exitosamente')
print(f'Total de líneas procesadas: {len(new_lines)}')
