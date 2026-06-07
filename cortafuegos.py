import os
import sys
import time
import subprocess

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def analizar_conexiones():
    try:
        while True:
            os.system("clear")
            print(f"{CYAN}======================================================={RESET}")
            print(f"       🛡️  ESCUDO DE CONEXIÓN DE RED - PROYECTO LIBERTAD")
            print(f"{CYAN}======================================================={RESET}")
            print(f"📡 Monitoreando sockets activos en el dispositivo...")
            print(f"⏰ Actualización: {VERDE}{time.strftime('%H:%M:%S')}{RESET}")
            print(f"{CYAN}-------------------------------------------------------{RESET}")
            print(f"{VERDE}{'PROTO':<6}{'DIRECCIÓN LOCAL':<22}{'DIRECCIÓN REMOTA':<22}{'ESTADO':<10}{RESET}")
            print(f"{CYAN}-------------------------------------------------------{RESET}")

            # Usamos netstat nativo de Linux/Android para capturar conexiones de red
            # Filtramos para mostrar IPv4 e IPv6 activas
            try:
                cmd = "netstat -ntu 2>/dev/null || netstat -an"
                conexiones = subprocess.check_output(cmd, shell=True).decode().split('\n')
                
                contador = 0
                for linea in conexiones:
                    partes = linea.split()
                    # Buscamos líneas que empiecen con tcp, tcp6, udp o udp6
                    if len(partes) >= 6 and ('tcp' in partes[0] or 'udp' in partes[0]):
                        proto = partes[0]
                        local = partes[3]
                        remota = partes[4]
                        estado = partes[5] if len(partes) > 5 else "ESTABLISHED"

                        # Omitimos conexiones de bucle local para limpiar el ruido visual
                        if "127.0.0.1" in local or "::1" in local or "0.0.0.0" in local:
                            continue

                        # Resaltamos estados críticos en colores
                        color_estado = VERDE if estado == "ESTABLISHED" else AMARILLO
                        if estado == "LISTEN":
                            color_estado = CYAN

                        print(f"{proto:<6}{local:<22}{remota:<22}{color_estado}{estado:<10}{RESET}")
                        contador += 1
                        if contador >= 12: # Limitamos el feed para que encaje en la pantalla del Infinix
                            break
                
                if contador == 0:
                    print(f"\n{AMARILLO} No se detectaron conexiones externas salientes activas.{RESET}")
                    print(f" El tráfico actual de aplicaciones se encuentra en reposo.")

            except Exception as e:
                print(f"{ROJO}❌ Error al leer los sockets del núcleo Android.{RESET}")

            print(f"{CYAN}-------------------------------------------------------{RESET}")
            print(f" {AMARILLO}[Ctrl + C]{RESET} para replegar el Escudo de Red...")
            time.sleep(3)

    except KeyboardInterrupt:
        print(f"\n{ROJO}⚠️  Escudo replegado. Regresando a la central.{RESET}\n")

if __name__ == "__main__":
    analizar_conexiones()
