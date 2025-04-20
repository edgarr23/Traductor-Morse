from machine import Pin
import time

led = Pin(5, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(15, Pin.OUT)

V_MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "Ñ": "--.--", "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--.."
}
REV_MORSE = {v: k for k, v in V_MORSE.items()}

def encender_led(ledy, l2=None, l3=None):
    ledy.on()
    if l2: l2.on()
    if l3: l3.on()
    time.sleep(0.4)
    ledy.off()
    if l2: l2.off()
    if l3: l3.off()
    time.sleep(0.4)

def Traducir(m):
    m = ''.join('/' + c  if c.isalpha() and (i == 0 or m[i - 1] != '/') else c for i, c in enumerate(m))
    return ''.join(" " if p == "" else p.upper() if p.isalpha() else REV_MORSE.get(p, "") for p in m.split("/"))
    
def eliminar(contenido):
    contenido = contenido[:-1]
    return contenido

def fundir_ruta(rut, respon):
    if rut == "/r":
        encender_led(led)
        return respon + "."
    elif rut == "/-":
        encender_led(led2, led3)
        return respon + "-"
    elif rut == "/sl":
        encender_led(led, led2, led3)
        return respon + "/"
    elif rut == "/sp":
        for _ in range(2):
            led.on(); led2.on(); led3.on()
            time.sleep(0.5)
            led.off(); led2.off(); led3.off()
            time.sleep(0.5)
        return respon + "//"
    elif rut == "/enter":
        def capitalizar(t): return t[:1].upper() + t[1:].lower() if t else ""
        respon = capitalizar(Traducir(respon))
        return respon
        
    elif rut == "/del":
        respon = eliminar(respon)
        return respon
    elif rut == "/delete":
        respon = ""
        return respon