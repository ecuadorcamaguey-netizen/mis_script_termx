import os
import sys
import time
import urllib.request
import json
import subprocess
from datetime import datetime

# Paleta de colores ANSI para la consola de Termux
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
AZUL = "\033[1;34m"
CYAN = "\033[1;36m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"

def borrar_pantalla():
    os.system('clear')

def generar_barra_color(mbps, max_esperado=20):
    ancho_barra = 20
    porcentaje = min(int((mbps / max_esperado) * ancho_barra), ancho_barra)
    
    # Asignamos el color de la barra según la velocidad real
    if mbps < 5.0:
        color_actual = ROJO
    elif mbps < 15.0:
        color_actual = AMARILLO
    else:
        color_actual = VERDE
        
    bloques = "█" * porcentaje
    espacios = "░" * (ancho_barra - porcentaje)
    return f"{color_actual}[{bloques}{espacios}]{RESET}"

def leer_sensor_proximidad():
    try:
        proceso = subprocess.run(['termux-sensor', '-s', 'Proximity', '-n', '1'], 
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=2)
        if proceso.returncode == 0:
            datos = json.loads(proceso.stdout)
            for nombre_sensor in datos.keys():
                if "Proximity" in nombre_sensor or "ps" in nombre_sensor:
                    valores = datos[nombre_sensor]['values']
                    return float(valores)
    except Exception:
        pass
    return 5.0

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

# === BUCLE PRINCIPAL CON CÓDIGOS DE COLOR ===
try:
    while True:
        borrar_pantalla()
        print(f"{CYAN}=========================================={RESET}")
        print(f"{CYAN} 🛰️   RADAR ECO-SENSORIAL DE RED ACTIVO   🛰️{RESET}")
        print(f"{CYAN}=========================================={RESET}")
        
        proximidad = leer_sensor_proximidad()
        if proximidad == 0.0:
            modo_mano = f"{ROJO} 🚫 MANO DETECTADA (Escaneo Forzado) {RESET}"
        else:
            modo_mano = f"{VERDE} 🟢 Monitoreo Normal {RESET}"
        print(f" [ Sensor:{modo_mano}]")
        
        print(f" {BLANCO}[ Escaneando latencia... ]{RESET}")
        ping = medir_ping()
        
        print(f" {BLANCO}[ Analizando Mbps... ]{RESET}")
        mbps = medir_velocidad()
        
        ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        barra_visual = generar_barra_color(mbps)
        
        # Evaluamos el estado general del internet para pintar las etiquetas
        if mbps < 5.0:
            alerta_estado = f"{ROJO}CRÍTICO{RESET}"
            color_metrica = ROJO
        elif mbps < 15.0:
            alerta_estado = f"{AMARILLO}MODERADO{RESET}"
            color_metrica = AMARILLO
        else:
            alerta_estado = f"{VERDE}EXCELENTE{RESET}"
            color_metrica = VERDE

        borrar_pantalla()
        print(f"{AZUL}=========================================={RESET}")
        print(f"{AZUL} 📊   PANEL MULTICOLOR DE INTERNET VIVO  📊{RESET}")
        print(f"{AZUL}=========================================={RESET}")
        print(f" 📅  Último escaneo: {BLANCO}{ahora}{RESET}")
        print(f" ⚡  Latencia:      {color_metrica}{ping if ping else 'Error'} ms{RESET}")
        print(f" 🚀  Descarga:      {color_metrica}{mbps} Mbps{RESET} ({alerta_estado})")
        print(f" 📈  Rendimiento:   {barra_visual}")
        print(f"{AZUL}=========================================={RESET}")
        
        if proximidad == 0.0:
            print(f"{AMARILLO} 🔥 ¡MODO TURBO ACTIVADO POR HARDWARE! 🔥{RESET}")
            print(f"{AZUL}=========================================={RESET}")
            os.system('termux-vibrate -d 100')
        
        print(f" {ROJO}🛑 Presiona CTRL + C para salir{RESET}")
        print(f"{AZUL}=========================================={RESET}")
        
        with open("reporte_red.txt", "a") as f:
            f.write(f"[{ahora}] Ping: {ping} ms | Speed: {mbps} Mbps | Sensor: {proximidad}\n")
        
        if proximidad == 0.0:
            time.sleep(3)
        else:
            time.sleep(10)

except KeyboardInterrupt:
    print(f"\n\n{VERDE}🛑 Radar sensorial apagado correctamente. ¡Impecable, campeón!{RESET}")
