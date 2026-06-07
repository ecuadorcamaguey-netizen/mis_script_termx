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

def obtener_almacenamiento():
    try:
        # Comando para ver el espacio en la memoria interna de Termux
        resultado = subprocess.check_output("df -h /data | tail -n 1", shell=True).decode().split()
        return f"{resultado[2]} Usado / {resultado[3]} Disponible ({resultado[4]})"
    except:
        return "No disponible"

def mostrar_menu():
    while True:
        os.system("clear")
        espacio = obtener_almacenamiento()
        
        print(f"{CYAN}======================================================={RESET}")
        print(f"     🛸 CENTRAL TÁCTICA V1.0 - PROYECTO LIBERTAD 2026")
        print(f"{CYAN}======================================================={RESET}")
        print(f"📱 {VERDE}Dispositivo:{RESET} Infinix X6870 (Android 15)")
        print(f"💾 {VERDE}Almacenamiento:{RESET} {espacio}")
        print(f"⏰ {VERDE}Hora Local:{RESET} {time.strftime('%H:%M:%S')}")
        print(f"{CYAN}======================================================={RESET}")
        print(f"        📂 SELECCIONE UNA HERRAMIENTA DEL ARSENAL:")
        print(f"{CYAN}-------------------------------------------------------{RESET}")
        print(f" [{VERDE}1{RESET}] 📡 Escáner de Puertos Táctico (`puertos`)")
        print(f" [{VERDE}2{RESET}] 🛡️  Cazador de Intrusos Multihilo (`caza`)")
        print(f" [{VERDE}3{RESET}] 🛰️  Geolocalizador IP Satelital (`rastreo`)")
        print(f" [{VERDE}4{RESET}] 📊 Sistema Guardián de CPU y RAM (`guardian`)")
        print(f" [{VERDE}5{RESET}] 🚀 Inyector Automático a GitHub (`subir`)")
        print(f" [{VERDE}6{RESET}] 🎮 Campeonato Terminal (Adivina el Número)")
        print(f" [{VERDE}7{RESET}] ⏱️  Reloj Atómico Sincronizado UTC-5")
        print(f" [{ROJO}0{RESET}] ❌ Salir de la Central")
        print(f"{CYAN}-------------------------------------------------------{RESET}")
        
        opcion = input(f"{CYAN}[👉 SELECCIÓN] Ingrese un número (0-7): {RESET}").strip()
        
        if opcion == "1":
            subprocess.run(["python", os.path.expanduser("~/mis_script/puertos.py")])
            input(f"\n{AMARILLO}Presione Enter para volver al menú...{RESET}")
        elif opcion == "2":
            subprocess.run(["python", os.path.expanduser("~/mis_script/caza_intrusos.py")])
            input(f"\n{AMARILLO}Presione Enter para volver al menú...{RESET}")
        elif opcion == "3":
            subprocess.run(["python", os.path.expanduser("~/mis_script/rastreo_ip.py")])
            input(f"\n{AMARILLO}Presione Enter para volver al menú...{RESET}")
        elif opcion == "4":
            subprocess.run(["python", os.path.expanduser("~/mis_script/guardian.py")])
        elif opcion == "5":
            subprocess.run(["python", os.path.expanduser("~/mis_script/despliegue.py")])
            input(f"\n{AMARILLO}Presione Enter para volver al menú...{RESET}")
        elif opcion == "6":
            # Ejecutamos el juego si está en la ruta
            subprocess.run(["python", os.path.expanduser("~/mis_script/juego.py")])
            input(f"\n{AMARILLO}Presione Enter para volver al menú...{RESET}")
        elif opcion == "7":
            subprocess.run(["python", os.path.expanduser("~/mis_script/hora.py")])
            input(f"\n{AMARILLO}Presione Enter para volver al menú...{RESET}")
        elif opcion == "0":
            print(f"\n{ROJO}⚠️  Apagando Central Táctica. Conexión cerrada.{RESET}\n")
            break
        else:
            print(f"\n{ROJO}❌ Opción inválida. Intente de nuevo.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    mostrar_menu()
