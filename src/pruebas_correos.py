# Cargo las librerías necesarías
import unittest
from unittest.mock import patch, MagicMock
from mymail import sendQuickMail, sendAttachEmail  # Reemplaza 'your_module' con el nombre de tu módulo

class PruebasDeEnviosDeCorreos(unittest.TestCase):
    @patch('smtplib.SMTP_SSL') # Decorador para ayudarme con la función de envío de correo
    @patch('builtins.input')   # Decorador para ayudarme a lidiar con los inputs que no fue fácil simularlos 
    def test_send_quick_mail(self, simuldatos_input, simuldatos_smtp):
        # Configurar valores simulados para input()
        simuldatos_input.side_effect = ["direccion_correo@gmail.com", "contrasena"]

        simuldatos_smtp.return_value.ehlo.return_value = "Hola"
        
        sendQuickMail("asunto1", "mensaje1", "correo1@gmail.com")
        # Verifico y evaluo los métodos de las funciones.    
        simuldatos_input.assert_called_with("\nPor favor ingrese la dirección de correo electronico al que desea enviar el correo: ")
        simuldatos_smtp.assert_called_with("smtp.gmail.com", 587, context=MagicMock(), context=MagicMock())
        simuldatos_smtp.return_value.ehlo.assert_called()
        simuldatos_smtp.return_value.starttls.assert_called_with(context=MagicMock())
        simuldatos_smtp.return_value.login.assert_called_with("direccion_correo@gmail.com", "contrasena")
        simuldatos_smtp.return_value.sendmail.assert_called()
        simuldatos_smtp.return_value.quit.assert_called()
# Ahora paso a simular la segunda función
    @patch('smtplib.SMTP') 
    @patch('builtins.input')
    def test_send_attach_email(self, falso_input, falso_smtp):
        # Configurar valores simulados para input()
        falso_input.side_effect = ["direccion_correo@gmail.com", "contrasena"]

        falso_smtp.return_value.login.return_value = (235, "OK")

        sendAttachEmail("Asunto de prueba", "Mensaje de prueba", "destinatario@gmail.com", "path/to/attachment.txt")

        falso_input.assert_called_with("\nPor favor ingrese la dirección de correo electronico desde el que desea enviar el correo: ")
        falso_smtp.assert_called_with("smtp.gmail.com", 587)
        falso_smtp.return_value.starttls.assert_called()
        falso_smtp.return_value.login.assert_called_with("direccion_correo@gmail.com", "contrasena")
        falso_smtp.return_value.sendmail.assert_called()
        falso_smtp.return_value.quit.assert_called()

if __name__ == '__main__':
    unittest.main()