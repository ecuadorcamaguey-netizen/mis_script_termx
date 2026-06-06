import os
import time
import sqlite3

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

DB_PATH = os.path.expanduser("~/mis_script/registro_central.db")

def inicializar_base_datos():
    """Crea la base de datos local y la tabla de auditoría si no existen."""
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
    """Guarda una alerta de seguridad directamente en la base de datos."""
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
    """Consulta y despliega las alertas guardadas en la base de datos."""
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

def escanear_objetivo_rapido():
    """Módulo integrado de escaneo de red agresivo."""
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🌐 ESCÁNER TÁCTICO DE HARDWARE DE RED")
    print(f"{CYAN}======================================================={RESET}")
    target = "192.168.43.249"
    print(f"Rastreando conectividad con el dispositivo: {AMARILLO}{target}{RESET}...")
    
    # Lanzamos un barrido rápido de ping directo
    respuesta = os.system(f"ping -c 2 -W 1 {target} > /dev/null")
    if respuesta == 0:
        print(f"\n{VERDE}✅ OBJETIVO EN VIVO: {target} está respondiendo.{RESET}")
        registrar_evento("RED_PING", f"Host {target} detectado en línea")
    else:
        print(f"\n{ROJO}❌ OBJETIVO INACTIVO: {target} no responde al ping.{RESET}")
        registrar_evento("RED_FALLO", f"Host {target} fuera de línea o protegido")
        
    print(f"{CYAN}======================================================={RESET}")
    input(f"\nPresiona {AMARILLO}[Enter]{RESET} para regresar al menú central...")

def menu_operaciones():
    inicializar_base_datos()
    while True:
        os.system("clear")
        print(f"{CYAN}======================================================={RESET}")
        print(f"      🎛️  CENTRO DE COMANDO V1.0 - PROYECTO LIBERTAD")
        print(f"{CYAN}======================================================={RESET}")
        print(f" {VERDE}1.{RESET} Lanzar Monitor Guardián de CPU e Hilos")
        print(f" {VERDE}2.{RESET} Verificar Segundo Android (192.168.43.249)")
        print(f" {VERDE}3.{RESET} Consultar Base de Datos de Alertas Seguras")
        print(f" {VERDE}4.{RESET} Lanzar Trampa de Evidencias (Honeypot)")
        print(f" {ROJO}5. Salir del Centro de Comando y Regresar a Base{RESET}")
        print(f"{CYAN}======================================================={RESET}")
        
        opcion = input(f"{CYAN}[👉 SELECCIÓN] Ingrese una opción de ingeniería:{RESET} ")
        
        if opcion == "1":
            os.system("python ~/mis_script/guardian.py")
        elif opcion == "2":
            escanear_objetivo_rapido()
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
