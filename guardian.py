import os
import time

VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def obtener_carga():
    try:
        with open("/proc/loadavg", "r") as f:
            return f.read().split()[:3]
    except:
        return ["0.00", "0.00", "0.00"]

def monitor_sistema():
    try:
        while True:
            os.system("clear")
            print(f"{CYAN}======================================================={RESET}")
            print(f"       🛡️  SISTEMA GUARDIÁN V1.1 - PROYECTO LIBERTAD")
            print(f"{CYAN}======================================================={RESET}")
            
            carga = obtener_carga()
            print(f"📊 CPU Load (1, 5, 15 min): {AMARILLO}{', '.join(carga)}{RESET}")
            print(f"⏰ Hora Local: {VERDE}{time.strftime('%H:%M:%S')}{RESET}")
            print(f"{CYAN}-------------------------------------------------------{RESET}")
            print(f"📋 PROCESOS ACTIVOS FILTRADOS (Limpios):")
            print(f"{CYAN}-------------------------------------------------------{RESET}")
            
            print(f"{VERDE}{'PID':<8}{'PROCESO / SCRIPT':<32}{'ESTADO':<10}{RESET}")
            
            # Usamos opciones avanzadas de ps para separar limpiamente las columnas
            with os.popen("ps -e -o pid,state,comm 2>/dev/null || ps -o pid,state,comm") as procesos:
                lineas = procesos.readlines()[1:15] # Tomamos una muestra de procesos
                for linea in lineas:
                    partes = linea.split()
                    if len(partes) >= 3:
                        pid = partes[0]
                        estado = partes[1]
                        # Tomamos el nombre del comando final eliminando la ruta larga
                        comando = partes[2].split('/')[-1]
                        
                        # Si es un script de Python, intentamos buscar el nombre real del archivo .py
                        if "python" in comando.lower() and len(partes) > 3:
                            comando = partes[3].split('/')[-1]
                            
                        comando_corto = (comando[:30] + '...') if len(comando) > 30 else comando
                        print(f"{pid:<8}{comando_corto:<32}{estado:<10}")
            
            print(f"{CYAN}-------------------------------------------------------{RESET}")
            print(f" {AMARILLO}[Ctrl + C]{RESET} para detener el monitoreo...")
            time.sleep(3)
            
    except KeyboardInterrupt:
        print(f"\n{ROJO}⚠️  Guardián desactivado. Regresando a la base.{RESET}\n")

if __name__ == "__main__":
    monitor_sistema()
