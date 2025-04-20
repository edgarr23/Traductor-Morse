import network
import time

# Activar modo Access Point (AP)
ap = network.WLAN(network.AP_IF)
ap.active(True)

# Configurar nombre de red y contraseña (opcional)
ap.config(essid='ESP-NET', password='12345678')  # Puedes cambiar el nombre y la clave

# Esperar a que esté activo
while not ap.active():
    time.sleep(1)

# Mostrar IP del ESP en modo AP (normalmente es 192.168.4.1)
print('Conéctate a esta red WiFi: ESP-NET')
print('IP para acceder desde el navegador:', ap.ifconfig()[0])
