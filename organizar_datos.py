import os
import shutil
import kaggle # Asegúrate de tener configurado tu kaggle.json

# 1. Configuración de carpetas
RAW_DIR = './descargas_raw'
BASE_DIR = './datasets'
PARTES = ['manos', 'brazos', 'piernas']
ESTADOS = ['con_fractura', 'sin_fractura', 'prueba']

# Crear estructura
for p in PARTES:
    for e in ESTADOS:
        os.makedirs(os.path.join(BASE_DIR, p, e), exist_ok=True)

# 2. Descargar (Ejemplo con Kaggle)
def descargar():
    print("Descargando datasets...")
    # Reemplaza con el dataset real de tu elección
    kaggle.api.dataset_download_files('orvile/bone-fracture-dataset', path=RAW_DIR, unzip=True)

# 3. Organizar (Lógica simplificada)
def organizar():
    for archivo in os.listdir(RAW_DIR):
        nombre = archivo.lower()
        # Clasificar por parte
        if 'hand' in nombre: parte = 'manos'
        elif 'arm' in nombre: parte = 'brazos'
        elif 'leg' in nombre: parte = 'piernas'
        else: continue

        # Clasificar por estado
        estado = 'con_fractura' if 'fracture' in nombre or 'positive' in nombre else 'sin_fractura'
        
        # Mover a la carpeta final
        shutil.move(os.path.join(RAW_DIR, archivo), os.path.join(BASE_DIR, parte, estado, archivo))

# Ejecución
# descargar() # Descomenta cuando tengas la API lista
# organizar()
