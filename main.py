# Hecho por GZ

from machine import Pin
from F_Morse import *
import socket
import time


led = Pin(5, Pin.OUT)# D1
led2 = Pin(13, Pin.OUT) #D7
led3 = Pin(15, Pin.OUT) #D8


def cargar_html():
    with open('index.html', 'r') as archivo:
        return archivo.read()

        
s = socket.socket()

try:
    
    s.bind(('', 80))
    
except OSError as e:
    print("Error de puerto en uso, reiniciando el servidor...")
    s.close()
    time.sleep(1)
    s = socket.socket()
    s.bind(('', 80))  # Reintenta vincular
    
s.listen(1)
print("Servidor web listo...")
mensaje = ""
while True:
    conn, addr = s.accept()
    print("Cliente conectado desde", addr)
    request = conn.recv(1024)
    request = request.decode('utf-8')
    
                                                # Obtener la ruta
    primera_linea = request.split('\r\n')[0]
    partes = primera_linea.split(' ')
    ruta = partes[1] if len(partes) > 1 else "/"
    html = cargar_html()
    if ruta in ["/r","/-","/sp","/sl","/enter","/del","/delete"]:
        mensaje = fundir_ruta(ruta, mensaje)
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n")
        conn.send(mensaje)
        conn.close()

    
    else:
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.sendall(html)
        conn.close()