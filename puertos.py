import os
import sys
import socket
import time
from datetime import datetime

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Diccionario de puertos comunes y sus servicios
PUERTOS_COMUNES = {
    21: "FTP (Transferencia de archivos)",
    22: "SSH (Acceso Remoto Seguro)",
    23: "Telnet (Acceso no seguro)",
    25: "SMTP (Correo Electrónico)",
    53: "DNS (Resolución de Nombres)",
    80: "HTTP (Servidor Web Estándar)",
    110: "POP3 (Correo Electrónico)",
    443: "HTTPS (Servidor Web Cifrado)",
    3306: "MySQL (Base de Datos)",
    8080: "HTTP-Proxy / Servidor Local"
}

def escanear_puertos():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       📡 ESCÁNER DE PUERTOS TÁCTICO - PROYECTO LIBERTAD")
    print(f"{CYAN}======================================================={RESET}")
    
    objetivo = input(f"{CYAN}[👉 OBJETIVO] Ingrese IP o Host a auditar\n(Ejemplo: 192.168.43.1): {RESET}").strip()
    
    if not objetivo:
        print(f"\n{ROJO}❌ Error: No ingresó un objetivo válido.{RESET}")
        return

    print(f"\n{AMARILLO}[!] Resolviendo dirección IP del objetivo...{RESET}")
    try:
        ip_objetivo = socket.gethostbyname(objetivo)
    except socket.gaierror:
        print(f"\n{ROJO}❌ Error: No se pudo resolver el host.{RESET}")
        return

    print(f"{VERDE}✅ Objetivo fijado:{RESET} {ip_objetivo}")
    print(f"⏰ Inicio de Auditoría: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{CYAN}-------------------------------------------------------{RESET}")
    print(f"{CYAN}{'PUERTO':<10}{'ESTADO':<15}{'SERVICIO':<30}{RESET}")
    print(f"{CYAN}-------------------------------------------------------{RESET}")

    puertos_abiertos = 0

    for puerto, servicio in PUERTOS_COMUNES.items():
        # Configuramos el socket para un escaneo ultra rápido
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.3) # Tiempo de espera corto para agilizar
        
        resultado = s.connect_ex((ip_objetivo, puerto))
        
        if resultado == 0:
            print(f"{VERDE}{puerto:<10}{'ABIERTO [🔓]':<15}{servicio:<30}{RESET}")
            puertos_abiertos += 1
        else:
            print(f"{ROJO}{puerto:<10}{'CERRADO [🔒]':<15}{RESET}{RESET}{servicio:<30}")
            
        s.close()

    print(f"{CYAN}-------------------------------------------------------{RESET}")
    print(f"📊 Auditoría Finalizada. Puertos abiertos encontrados: {VERDE}{puertos_abiertos}{RESET}")
    print(f"{CYAN}======================================================={RESET}")

if __name__ == "__main__":
    escanear_puertos()
