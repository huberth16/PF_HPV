# LLamo las librerias necesarias
import unittest
import requests
from unittest.mock import MagicMock
from io import BytesIO
from PIL import Image
from images import showImageFromURL, downloadImageFromUrl, grayScaleImage
# Realizo las pruebas
class PruebafuncionesImagenes(unittest.TestCase):
    #prueba para la primer función
    def test_showImageFromURL(self):
        url = "https://fotos.com/imagen.jpg"
        respuesta = MagicMock() #simulo la respuesta
        respuesta.status_code = 200
        respuesta.content = b"data_imagen_falsa" #datos falsos para la imagen simulada
        requests.get = MagicMock(return_value=respuesta) #retornamos el valor 

        with unittest.mock.patch('builtins.print') as prueba_print:
            with unittest.mock.patch('PIL.Image.Image.show') as prueba_mostrar:
                showImageFromURL(url)
                requests.get.assert_called_with(url)
                prueba_mostrar.assert_called()
                prueba_print.assert_called_with("Descargando la imagen...")
    #Pureba para la segunda función de manera similar 
    def test_downloadImageFromUrl(self):
        url = "https://otraimagen.com/imagen.jpg"
        path = "imagenfalsa.jpg"
        respuesta2 = MagicMock()
        respuesta2.status_code = 200
        respuesta2.content = b"otra_data_imagen_falsa"
        requests.get = MagicMock(return_value=respuesta2)

        with open(path, 'wb') as falsa:
            falsa.write(b"otra_data_imagen_falsa")

        with unittest.mock.patch('builtins.print') as prueba_impresion:
            downloadImageFromUrl(url, path)
            requests.get.assert_called_with(url)
            prueba_impresion.assert_called_with(f"Descargando la imagen...\nLa imagen fue guardada en {path}")
    # Ahora pruebo la ultima función de este modulo
    def test_grayScaleImage(self):
        ruta_imagen = "test_image.jpg"
        imagen = Image.new('RGB', (100, 100))
        imagen.save(ruta_imagen)

        with unittest.mock.patch('PIL.Image.Image.convert') as prueba_conversion:
            grayScaleImage(ruta_imagen)
            prueba_conversion.assert_called_with("L")

if __name__ == '__main__':
    unittest.main()