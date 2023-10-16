# Tomé una plantilla de archivo de configuración y lo modifiqué a mis necesidades
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' #Es mi versión
PACKAGE_NAME = 'proyectofinal_imagenes-correos' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Huberth Perez Villalobos' 
AUTHOR_EMAIL = 'huberth16@gmail.com' 
URL = 'https://github.com/huberth16/proyectofinal_imagenes-correos' 

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Librería para mostrar,descargar, guardar y enviar por correo imagenes' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'pillow',
      'requests',
      'unittest',
      'io',
      'smtplib',
      'ssl',
      'threading',
      'email',
      'unittest'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)