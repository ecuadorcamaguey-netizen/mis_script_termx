import os
import time
import sqlite3
import re

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

DB_PATH = os.path.expanduser("~/mis_script/registro_central.db")

def inicializar_base_datos():
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alertas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            tipo_evento TEXT,
            descripcion TEXT
        )
    ''')
    conexion.commit()
    conexion.close()

def registrar_evento(tipo, descripcion):
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    fecha_actual = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO alertas (fecha, tipo_evento, descripcion)
        VALUES (?, ?, ?)
    ''', (fecha_actual, tipo, descripcion))
    conexion.commit()
    conexion.close()

def ver_historial_db():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🗄️  HISTORIAL DE ALERTAS - BASE DE DATOS LOCAL")
    print(f"{CYAN}======================================================={RESET}")
    
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('SELECT id, fecha, tipo_evento, descripcion FROM alertas ORDER BY id DESC LIMIT 15')
    filas = cursor.fetchall()
    conexion.close()
    
    if not filas:
        print(f"\n{AMARILLO} No hay eventos registrados en la base de datos aún.{RESET}\n")
    else:
        print(f"{VERDE}{'ID':<5}{'FECHA / HORA':<22}{'EVENTO':<12}{'DESCRIPCIÓN':<20}{RESET}")
        print(f"{CYAN}-------------------------------------------------------{RESET}")
        for fila in filas:
            print(f"{str(fila[0]):<5}{str(fila[1]):<22}{str(fila[2]):<12}{str(fila[3]):<20}")
            
    print(f"{CYAN}======================================================={RESET}")
    input(f"\nPresiona {AMARILLO}[Enter]{RESET} para regresar al menú central...")

def escanear_objetivo_nmap():
    """Módulo Avanzado: Escaneo e interrogación de puertos con registro SQL."""
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🌐 AUDITORÍA PROFUNDA DE RED (NMAP INTERGADO)")
    print(f"{CYAN}======================================================={RESET}")
    target = "192.168.43.249"
    print(f"Lanzando Nmap táctico al host objetivo: {AMARILLO}{target}{RESET}...")
    print(f"{AMARILLO}[!] Analizando los puertos principales, por favor espere...{RESET}\n")
    
    # Ejecutamos Nmap y capturamos su salida de texto directamente en Python
    with os.popen(f"nmap -F {target}") as pipe:
        salida_nmap = pipe.read()
    
    print(f"{CYAN}------------------- SALIDA DE NMAP --------------------{RESET}")
    print(salida_nmap)
    print(f"{CYAN}-------------------------------------------------------{RESET}")
    
    # Procesamos la salida usando expresiones regulares para buscar puertos "open"
    puertos_abiertos = re.findall(r"(\d+/tcp\s+open\s+\S+)", salida_nmap)
    
    if puertos_abiertos:
        print(f"\n{ROJO}⚠️  PUERTOS ABIERTOS DETECTADOS EN EL OBJETIVO:{RESET}")
        for puerto in puertos_abiertos:
            print(f" {ROJO}• {puerto}{RESET}")
        
        # Guardamos la lista en la Base de Datos SQL
        descripcion_evento = f"Puertos abiertos detectados: {', '.join(puertos_abiertos)}"
        registrar_evento("NET_VULN", descripcion_evento[:100])
    else:
        print(f"\n{VERDE}✅ ESCÁNER LIMPIO: No se encontraron puertos abiertos expuestos.{RESET}")
        registrar_evento("NET_SECURE", f"Host {target} verificado sin puertos expuestos")
        
    print(f"{CYAN}======================================================={RESET}")
    input(f"\nPresiona {AMARILLO}[Enter]{RESET} para regresar al menú central...")

def menu_operaciones():
    inicializar_base_datos()
    while True:
        os.system("clear")
        print(f"{CYAN}======================================================={RESET}")
        print(f"      🎛️  CENTRO DE COMANDO V2.0 - PROYECTO LIBERTAD")
        print(f"{CYAN}======================================================={RESET}")
        print(f" {VERDE}1.{RESET} Lanzar Monitor Guardián de CPU e Hilos V1.1")
        print(f" {VERDE}2.{RESET} Auditoría Nmap Completa al Android (192.168.43.249)")
        print(f" {VERDE}3.{RESET} Consultar Base de Datos de Alertas Seguras (SQL)")
        print(f" {VERDE}4.{RESET} Lanzar Trampa de Evidencias (Honeypot)")
        print(f" {ROJO}5. Salir del Centro de Comando y Regresar a Base{RESET}")
        print(f"{CYAN}======================================================={RESET}")
        
        opcion = input(f"{CYAN}[👉 SELECCIÓN] Ingrese una opción de ingeniería:{RESET} ")
        
        if opcion == "1":
            os.system("python ~/mis_script/guardian.py")
        elif opcion == "2":
            escanear_objetivo_nmap()
        elif opcion == "3":
            ver_historial_db()
        elif opcion == "4":
            os.system("python ~/mis_script/evidencias_secretas.py")
        elif opcion == "5":
            print(f"\n{AMARILLO}⚙️ Cerrando terminal central. Sistemas en resguardo...{RESET}\n")
            break
        else:
            print(f"\n{ROJO}❌ Opción inválida. Reintente.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    menu_operaciones()
