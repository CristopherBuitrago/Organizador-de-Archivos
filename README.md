# Organizador de Archivos

Un programa en Python que organiza archivos en carpetas basándose en su tipo, nombre o contenido. Ideal para gestionar grandes cantidades de PDFs, eBooks u otros archivos en tu computadora.

---

## Características

- Organiza archivos por **extensión** (`.pdf`, `.epub`, `.mobi`).
- Filtra archivos por palabras clave en sus nombres.
- Crea carpetas automáticamente para clasificar los resultados.
- Soporte multiplataforma: Windows, Linux y macOS.
- Interfaz sencilla por terminal (CLI).

---

## Requisitos

1. **Python 3.8 o superior**.
2. Dependencias de Python (se instalan automáticamente con `pip`).

Si no tienes Python instalado, sigue las instrucciones en la sección [Cómo instalar Python](#cómo-instalar-python).

---

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/Organizador-de-Archivos.git
   cd Organizador-de-Archivos
Instala las dependencias necesarias:

bash
Copiar código
pip install -r requirements.txt
Ejecuta el programa:

bash
Copiar código
python main.py
Cómo instalar Python
Windows
Descarga Python desde la página oficial: https://www.python.org/downloads/.
Durante la instalación:
Asegúrate de marcar la opción "Add Python to PATH" antes de continuar.
Sigue las instrucciones del instalador.
Verifica que Python está instalado correctamente:
Abre una terminal (Windows + R, escribe cmd y presiona Enter).
Ejecuta:
bash
Copiar código
python --version
Deberías ver la versión instalada de Python.
macOS
Abre la Terminal.
Instala Python usando Homebrew:
bash
Copiar código
brew install python
Verifica la instalación:
bash
Copiar código
python3 --version
Linux (Ubuntu/Debian)
Abre una terminal.
Actualiza el sistema e instala Python:
bash
Copiar código
sudo apt update
sudo apt install python3 python3-pip
Verifica la instalación:
bash
Copiar código
python3 --version
Uso del Programa
Coloca los archivos que deseas organizar en una carpeta específica.
Ejecuta el programa con los siguientes argumentos:
bash
Copiar código
python main.py <directorio_entrada> <palabra_clave> <extension> <directorio_salida>
directorio_entrada: Carpeta donde están los archivos.
palabra_clave: Palabra clave que se buscará en los nombres de los archivos.
extension: Tipo de archivo (e.g., .pdf).
directorio_salida: Carpeta donde se guardarán los archivos organizados.
Ejemplo
Si tienes esta estructura:

bash
Copiar código
/archivos_entrada
  Docker.pdf
  Kubernetes.pdf
  Manual.txt
  Libro.epub
Ejecutando:

bash
Copiar código
python main.py ./archivos_entrada Docker .pdf ./archivos_organizados
Obtendrás:

bash
Copiar código
/archivos_organizados
  /Docker
    Docker.pdf
Licencia
Este proyecto está licenciado bajo la MIT License.

Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto, crea un "issue" o envía un "pull request".