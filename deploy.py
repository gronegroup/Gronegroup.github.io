import subprocess
import sys

try:
    # Add changes
    print("Agregando cambios...")
    subprocess.run(["git", "add", "index.html"], check=True)
    
    # Commit
    print("Haciendo commit...")
    subprocess.run(["git", "commit", "-m", "Subcategorías en 4 columnas con ancho 1200px"], check=True)
    
    # Push
    print("Subiendo a GitHub...")
    result = subprocess.run(["git", "push"], check=True, capture_output=True, text=True)
    
    print("\n✅ ÉXITO! Cambios subidos a GitHub Pages")
    print("Espera 1-2 minutos y actualiza gronegroup.github.io")
    
except subprocess.CalledProcessError as e:
    print(f"\n❌ Error: {e}")
    print(f"Output: {e.output if hasattr(e, 'output') else ''}")
    sys.exit(1)
