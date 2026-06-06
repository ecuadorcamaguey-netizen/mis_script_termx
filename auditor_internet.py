import os
import sys
import time
import urllib.request
import json
import subprocess
from datetime import datetime

def borrar_pantalla():
    os.system('clear')

def generar_barra(mbps, max_esperado=20):
    # Genera una barra gráfica visual basada en los Mbps
    ancho_barra = 20
    porcentaje = min(int((mbps / max_esperado) * ancho_barra), ancho_barra)
    bloques = "█" * porcentaje
    espacios = "░" * (ancho_barra - porcentaje)
    return f"[{bloques}{espacios}]"

def leer_sensor_proximidad():
    try:
        # Consultamos el sensor limitando a 1 sola lectura rápida
        proceso = subprocess.run(['termux-sensor', '-s', 'Proximity', '-n', '1'], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        if proceso.returncode == 0:
            datos = json.loads(proceso.stdout)
            # Buscamos dinámicamente cualquier sensor que contenga la palabra Proximity
            for nombre_sensor in datos.keys():
                if "Proximity" in nombre_sensor or "ps" in nombre_sensor:
                    valores = datos[nombre_sensor]['values']
                    return float(valores[0])
    except Exception:
        pass
    return 5.0  # Por defecto asumimos que está lejos (Lejos)

def medir_ping():
    try:
        inicio = time.time()
        urllib.request.urlopen("https://google.com", timeout=4)
        fin = time.time()
        return round((fin - inicio) * 1000, 1)
    except Exception:
        return None

def medir_velocidad():
    try:
        url = "https://hetzner.de" 
        inicio = time.time()
        req = urllib.request.Request(url, headers={'Range': 'bytes=0-1048576'}) # 1MB
        with urllib.request.urlopen(req, timeout=5) as respuesta:
            respuesta.read()
        fin = time.time()
        mbps = (1048576 * 8) / 1000000 / (fin - inicio)
        return round(mbps, 2)
    except Exception:
        return 0.0

# === BUCLE PRINCIPAL DEL RADAR ===
try:
    while True:
        borrar_pantalla()
        print("==========================================")
        print(" 🛰️   RADAR ECO-SENSORIAL DE RED ACTIVO   🛰️")
        print("==========================================")
        
        # Leemos el hardware antes de la prueba de red
        proximidad = leer_sensor_proximidad()
        modo_mano = " 🚫 MANO DETECTADA (Escaneo Forzado) " if proximidad == 0.0 else " 🟢 Monitoreo Normal "
        print(f" [ Sensor:{modo_mano}]")
        
        print(" [ Escaneando latencia... ]")
        ping = medir_ping()
        
        print(" [ Analizando Mbps... ]")
        mbps = medir_velocidad()
        
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        barra_visual = generar_barra(mbps)
        
        borrar_pantalla()
        print("==========================================")
        print(" 📊   PANEL GRÁFICO DE INTERNET EN VIVO  📊")
        print("==========================================")
        print(f" 📅  Último escaneo: {ahora}")
        print(f" ⚡  Latencia:      {ping if ping else 'Error'} ms")
        print(f" 🚀  Descarga:      {mbps} Mbps")
        print(f" 📈  Rendimiento:   {barra_visual}")
        print("==========================================")
        
        if proximidad == 0.0:
            print(" 🔥 ¡MODO TURBO ACTIVADO POR HARDWARE! 🔥")
            print("==========================================")
            os.system('termux-vibrate -d 100')
        
        print(" 🛑 Presiona CTRL + C para salir")
        print("==========================================")
        
        with open("reporte_red.txt", "a") as f:
            f.write(f"[{ahora}] Ping: {ping} ms | Speed: {mbps} Mbps | Sensor: {proximidad}\n")
        
        if proximidad == 0.0:
            time.sleep(3)
        else:
            time.sleep(10)

except KeyboardInterrupt:
    print("\n\n🛑 Radar sensorial apagado. ¡Impecable trabajo, campeón!")
