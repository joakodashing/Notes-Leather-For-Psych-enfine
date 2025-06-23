import os
import xml.etree.ElementTree as ET
from PIL import Image

# Rutas actualizadas
XML_PATH = "assets/xml/default.xml"
IMAGES_DIR = "assets/images"
EXPECTED_SIZE = (2450, 1900)  # Ancho x Alto en píxeles

def check_xml_exists():
    if os.path.isfile(XML_PATH):
        print(f"✔ Archivo XML encontrado: {XML_PATH}")
        return True
    else:
        print(f"❌ Archivo XML NO encontrado: {XML_PATH}")
        return False

def check_images_exist():
    if os.path.isdir(IMAGES_DIR):
        png_files = [f for f in os.listdir(IMAGES_DIR) if f.endswith(".png")]
        if png_files:
            print(f"✔ {len(png_files)} archivos PNG encontrados en {IMAGES_DIR}")
            return png_files
        else:
            print(f"❌ No se encontraron archivos PNG en {IMAGES_DIR}")
            return []
    else:
        print(f"❌ Carpeta de imágenes NO encontrada: {IMAGES_DIR}")
        return []

def validate_image_sizes(png_files):
    print("Validando dimensiones de las imágenes PNG...")
    for file in png_files:
        path = os.path.join(IMAGES_DIR, file)
        try:
            with Image.open(path) as img:
                if img.size == EXPECTED_SIZE:
                    print(f"  ✔ {file} tiene tamaño correcto: {img.size}")
                else:
                    print(f"  ⚠ {file} tiene tamaño incorrecto: {img.size} (esperado {EXPECTED_SIZE})")
        except Exception as e:
            print(f"  ❌ Error al abrir {file}: {e}")

def parse_xml_notes():
    print("Parseando XML para listar notas y animaciones...")
    if not os.path.isfile(XML_PATH):
        print("No se puede parsear XML porque no existe.")
        return

    try:
        tree = ET.parse(XML_PATH)
        root = tree.getroot()

        notes = set()
        for subtexture in root.findall('SubTexture'):
            name = subtexture.attrib.get('name', '')
            # Extrae base sin números
            base_name = ''.join([i for i in name if not i.isdigit()]).strip()
