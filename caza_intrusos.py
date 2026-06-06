import os
import socket
import time
from concurrent.futures import ThreadPoolExecutor

# Paletas cromáticas ANSI
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
BLANCO = "\033[1;37m"
RESET = "\033[0m"

def borrar_pantalla():
    os.system('clear')

def comprobar_host(ip):
    # Intentamos tocar el puerto 80 (HTTP) o 53 (DNS) o 443 (HTTPS) que casi todo equipo tiene abierto o responde
    puertos = [80, 53, 443]
    for puerto in puertos:
        try:
            # Conexión ultra rápida de 0.3 segundos para no demorar el script
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            resultado = s.connect_ex((ip, puerto))
            s.close()
            
            # Si el resultado es 0 (conectado) o 111 (conexión rechazada pero el host respondió), está VIVO
            if resultado == 0 or resultado == 111:
                return ip
        except Exception:
            pass
    return None

def escanear_red_pura():
    # Detectamos tu IP base de forma interna
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close()
        partes = ip_local.split('.')
        base_ip = f"{partes[0]}.{partes[1]}.{partes[2]}."
    except Exception:
        base_ip = "192.168.1." # Respaldo clásico en Ecuador
        ip_local = "192.168.1.50"

    print(f" 🟢 Tu IP local: {VERDE}{ip_local}{RESET}")
    print(f" 🛰️  Escaneando el rango: {CYAN}{base_ip}1 hasta la 30{RESET}")
    print(f" {AMARILLO}⏳ Realizando barrido táctico por sockets internos...{RESET}\n")

    # Lista de IPs a escanear (revisamos las primeras 30 que es donde se conectan los celulares y TVs de casa)
    lista_ips = [f"{base_ip}{i}" for i in range(1, 31)]
    activos = []

    # Usamos hilos en paralelo para que el escaneo se haga en menos de 5 segundos
    with ThreadPoolExecutor(max_workers=30) as ejecutor:
        resultados = ejecutor.map(comprobar_host, lista_ips)
        for res in resultados:
            if res:
                # Identificamos etiquetas básicas
                if res.endswith(".1"):
                    tipo = "Router Principal"
                elif res == ip_local:
                    tipo = "Tu Infinix X6870 (Este Móvil)"
                else:
                    tipo = "Dispositivo Activo"
                activos.append({"ip": res, "tipo": tipo})
                
    return activos

borrar_pantalla()
print(f"{CYAN}=========================================={RESET}")
print(f"{CYAN} 🛡️     AUDITOR DE SEGURIDAD WI-FI v2.0    🛡️{RESET}")
print(f"{CYAN}=========================================={RESET}")

equipos = escanear_red_pura()

borrar_pantalla()
print(f"{CYAN}=========================================={RESET}")
print(f"{CYAN} 🛡️     REPORTE DE DISPOSITIVOS EN VIVO    🛡️{RESET}")
print(f"{CYAN}=========================================={RESET}")
print(f" Total detectados: {VERDE}{len(equipos)} equipos activos{RESET}")
print(f"{CYAN}------------------------------------------{RESET}")

if len(equipos) == 0:
    print(f" {ROJO}No se encontraron respuestas en los puertos estándar.{RESET}")
else:
    for i, dev in enumerate(equipos, 1):
        print(f" {i}. {BLANCO}IP:{RESET} {AMARILLO}{dev['ip']:<15}{RESET} | {VERDE}{dev['tipo']}{RESET}")

print(f"{CYAN}=========================================={RESET}")

# Alerta por voz
msg_voz = f"Escaneo finalizado. Detectados {len(equipos)} dispositivos en los canales de red."
os.system(f'termux-tts-speak "{msg_voz}"')

# Guardamos el reporte
ahora = time.strftime('%Y-%m-%d %H:%M:%S')
with open("reporte_intrusos.txt", "w") as f:
    f.write(f"=== AUDITORÍA SOCKETS PRIVADOS {ahora} ===\n")
    f.write(f"Total Equipos: {len(equipos)}\n")
    for dev in equipos:
        f.write(f"IP: {dev['ip']} | Identificación: {dev['tipo']}\n")

print(" 💾 Historial respaldado en 'reporte_intrusos.txt'")
print(f"{CYAN}=========================================={RESET}")
