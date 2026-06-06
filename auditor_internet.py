import os
import subprocess
import time
import urllib.request
from datetime import datetime

def borrar_pantalla():
    os.system('clear')

def medir_ping():
    try:
        inicio = time.time()
        urllib.request.urlopen("https://google.com", timeout=4)
        fin = time.time()
        latencia = (fin - inicio) * 1000
        return round(latencia, 1)
    except Exception:
        return None

def medir_velocidad():
    try:
        url = "https://hetzner.de" 
        inicio = time.time()
        # Descargamos un bloque pequeño (1MB) para no saturar tu red en cada bucle
        req = urllib.request.Request(url, headers={'Range': 'bytes=0-1048576'})
        with urllib.request.urlopen(req, timeout=5) as respuesta:
            respuesta.read()
        fin = time.time()
        tiempo_total = fin - inicio
        megabits = (1048576 * 8) / 1000000
        mbps = megabits / tiempo_total
        return round(mbps, 2)
    except Exception:
        return 0.0

# === INICIO DEL RASTREADOR INFINITO ===
try:
    while True:
        borrar_pantalla()
        print("==========================================")
        print(" 🛰️   RASTREADOR DE RED EN VIVO (ACTIVO)   🛰️")
        print("==========================================")
        print(" [ Escaneando latencia actual... ]")
        ping_promedio = medir_ping()

        print(" [ Analizando tasa de transferencia... ]")
        velocidad_mbps = medir_velocidad()

        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        borrar_pantalla()
        print("==========================================")
        print(" 📊   RASTREADOR DE INTERNET EN SEGUNDOS  📊")
        print("==========================================")
        print(f" 📅  Último escaneo: {ahora}")

        if ping_promedio:
            print(f" ⚡  Latencia:      {ping_promedio} ms (Ping)")
        else:
            print(" ❌  Latencia:      Error de conexión")

        print(f" 🚀  Descarga:      {velocidad_mbps} Mbps")
        print("==========================================")
        print(" 🛑 Presiona CTRL + C para detener el rastreo")
        print("==========================================")

        # Guardamos en el archivo el historial de este segundo
        with open("reporte_red.txt", "a") as archivo:  # Usamos 'a' para acumular el historial
            archivo.write(f"[{ahora}] Ping: {ping_promedio if ping_promedio else 'Fallo'} ms | Speed: {velocidad_mbps} Mbps\n")

        # Tiempo de espera antes de la siguiente actualización (10 segundos)
        # Puedes cambiar este 10 por el número de segundos que prefieras
        time.sleep(10)

except KeyboardInterrupt:
    print("\n\n🛑 Rastreador detenido por el usuario. ¡Buen trabajo, campeón!")
