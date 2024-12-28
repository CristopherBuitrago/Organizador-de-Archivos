import os
import shutil
from datetime import datetime
import argparse

def organizar_archivos(directorio_entrada, palabra_clave, extension, directorio_salida):
    """
    Organiza archivos en carpetas por extensión y palabras clave.

    Args:
        directorio_entrada (str): Carpeta con archivos para organizar.
        palabra_clave (str): Palabra clave para filtrar archivos.
        extension (str): Extensión de archivo a buscar (e.g., .pdf).
        directorio_salida (str): Carpeta donde guardar los archivos organizados.
    """
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    for archivo in os.listdir(directorio_entrada):
        ruta_archivo = os.path.join(directorio_entrada, archivo)

        if os.path.isfile(ruta_archivo):
            if archivo.endswith(extension) and palabra_clave.lower() in archivo.lower():
                carpeta_destino = os.path.join(directorio_salida, palabra_clave)
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, archivo))
                print(f"Movido: {archivo} -> {carpeta_destino}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organizador de archivos por extensión y palabras clave")
    parser.add_argument("directorio_entrada", help="Ruta al directorio con archivos a organizar")
    parser.add_argument("palabra_clave", help="Palabra clave para filtrar archivos")
    parser.add_argument("extension", help="Extensión de los archivos a buscar (e.g., .pdf)")
    parser.add_argument("directorio_salida", help="Ruta al directorio donde guardar archivos organizados")

    args = parser.parse_args()

    organizar_archivos(args.directorio_entrada, args.palabra_clave, args.extension, args.directorio_salida)
