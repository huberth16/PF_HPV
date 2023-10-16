#                   -----Bibliotecas---
import smtplib, ssl #para acceder a la cuenta de correo por dónde se enviarán los correos
import threading # Para utilizar la multitarea en hilos.
from email import encoders #para interactuar con los correos
from email.mime.base import MIMEBase #para interactuar con los correos
from email.mime.multipart import MIMEMultipart #para interactuar con los correos
from email.mime.text import MIMEText #para interactuar con los correos
#                   ---Funciones---
def sendQuickMail(subject:str, message:str, destination:str):
 """
 Envía un correo electrónico rápido al destino indicado.
 La función debe preguntar cual es el correo electrónico con el que se enviará así
 como su contraseña
 Se utilizará el puerto 587 y se utilizará TLS
 Se utilizará el servidor de correo smtp.gmail.com
 """
 #solicitud de información complementaria para enviar el correo
 direccion = input("\nPor favor ingrese la dirección de correo electronico al que desea enviar el correo: ")
 pswrd = input("\nPor favor ingrese la dirección de correo electronico al que desea enviar el correo: ")
# Creo una función para mandar el correo que luego meteré la función en porcesos en hilos
 def enviocorreo():
  context = ssl.create_default_context()
  #      ---Construción de la información del mensaje---
  mailbody = MIMEMultipart()
  mailbody['From'] = direccion
  mailbody['To'] = destination
  mailbody['Subject'] = subject 
  mailbody.attach(MIMEText(message, 'plain'))
 #      ---Se conceta al servidor y se manda el mensaje---
  with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=context, context=context) as servidor:
     servidor.ehlo() #Saludo al servidor
     servidor.starttls(context=context) # me cambio a la conexión tls
     servidor.ehlo()# vuelvo a saludarlo para ver si la conexion fue exitosa.
     servidor.login(direccion, pswrd)
     servidor.sendmail(direccion, destination, mailbody.as_string())
 #Creo procesos en hilos y llamo a la función "correohilos"
 correohilo = threading.Thread(target=enviocorreo)
 correohilo.start()
 correohilo.join() # esto para que espere antes de seguir ejecutando el programa principal que invocó a la biblioteca.
 #
def sendAttachEmail(subject:str, message:str, destination:str, path:str):
 """
 Envía un correo electrónico con un archivo adjunto a la dirección indicada
 La función debe preguntar cual es el correo electrónico con el que se enviará así
 como su contraseña
 Se utilizará el puerto 587 y se utilizará TLS
 Se utilizará el servidor de correo smtp.gmail.com
 """
 #solicitud de información complementaria para enviar el correo
 direccion = input("\nPor favor ingrese la dirección de correo electronico desde el que desea enviar el correo: ")
 pswrd = input("\nPor favor ingrese la constraseña del correo electronico desde el que desea enviar el correo: ")
 # Creo una función para mandar el correo que luego meteré la función en porcesos en hilos
 def enviarcorreo():
  cuerpo = message
  #      ---Construción de la información del mensaje---
  mensaje = MIMEMultipart()
  mensaje['From'] = direccion
  mensaje['To'] = destination
  mensaje['Subject'] = subject
  # Agregar el cuerpo del correo
  mensaje.attach(MIMEText(cuerpo, 'plain'))
  #ruta del archivo
  ruta = path
  #Adjunto el archivo al correo
  with open(ruta, 'rb') as adjunto:
    carga = MIMEBase('application', 'octet-stream')
    carga.set_payload(adjunto.read())
    encoders.encode_base64(carga)
    carga.add_header('Content-Disposition', "attachment; filename=archivo_adjunto.txt")
    mensaje.attach(carga)
  # Me logeo en el servidor y envío el mensaje
  with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
     servidor.starttls()
     servidor.login(direccion, pswrd)
     #Acá envío el correo
     servidor.sendmail(direccion, destination, mensaje.as_string())
 correohilo = threading.Thread(target=enviarcorreo)
 correohilo.start()
 correohilo.join() # esto para que espere antes de seguir ejecutando el programa principal que invocó a la biblioteca.