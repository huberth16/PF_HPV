#              ----Importación de librerias necesarias---
import requests # Para manejar solicitudes get, put, push
from PIL import Image #Para manipular imagenes
from io import BytesIO
#                       -----Funciones-----
def showImageFromURL(url:str):
 """
 Descarga una imagen desde una URL y la muestra
 """
 enlace = requests.get(url)
 # Reviso que se pueda descargar bien
 if enlace == 200:     
     print("Descargando la imagen...")
 else:
     print(f"La imagen no está disponible en la dirección{url}")
 # convierto los datos recibidos en un archivo imagen para trabajarlo luego con pillow
 imagen = Image.open(BytesIO(enlace.content)) 
 #Ahora le muestro al usuario la imagen
 imagen.show()
#  
def downloadImageFromUrl(url:str, path:str):
 """
 Descarga una imagen y la guarda en la ruta indicada
 """
 enlace = requests.get(url)
 # Reviso que se pueda descargar bien
 if enlace == 200:     # se escribió 200 porque es un código que indica una operación exitosa en http
     print("Descargando la imagen...")
 else:
     print(f"La imagen no está disponible en la dirección{url}")
 #Guardo el archivo en la ruta dada
 with open(path, 'wb') as imagen: # se usa wb porque vamos a escribir un binario (write binary)
    imagen.write(enlace.content)
    print(f"La imagen fue guardada en {path}")
#
def grayScaleImage(path:str):
 """
 Convierte una imagen a blanco y negro
 """
 with Image.open(path) as imagen:
    imagen.convert("L")