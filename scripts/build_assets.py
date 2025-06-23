import os

def check_assets():
    xml_path = "assets/xml/notas.xml"  # Ajusta el nombre si es otro
    images_dir = "assets/images"

    print("Revisando archivos en el repositorio...")

    # Verificar XML
    if os.path.isfile(xml_path):
        print(f"✔ Archivo XML encontrado: {xml_path}")
    else:
        print(f"❌ Archivo XML NO encontrado: {xml_path}")

    # Verificar imágenes PNG
    if os.path.isdir(images_dir):
        png_files = [f for f in os.listdir(images_dir) if f.endswith(".png")]
        if png_files:
            print(f"✔ {len(png_files)} archivos PNG encontrados en {images_dir}")
        else:
            print(f"❌ No se encontraron archivos PNG en {images_dir}")
    else:
        print(f"❌ Carpeta de imágenes NO encontrada: {images_dir}")

if __name__ == "__main__":
    check_assets()
