import os
import sys
import time

VERDE = "\033[1;32m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
AMARILLO = "\033[1;33m"
RESET = "\033[0m"

def ejecutar_script(nombre_script):
    ruta = os.path.expanduser(f"~/mis_script/{nombre_script}")
    if os.path.exists(ruta):
        print(f"\n{VERDE}🚀 Lanzando {nombre_script}...{RESET}\n")
        time.sleep(1)
        os.system(f"python {ruta}")
    else:
        print(f"\n{ROJO}❌ Error: El script '{nombre_script}' no se encuentra en la carpeta.{RESET}\n")
    input(f"\n{AMARILLO}Presione Enter para regresar al Menú Central...{RESET}")

def mostrar_menu():
    while True:
        os.system("clear")
        print(f"{CYAN}======================================================={RESET}")
        print(f"       🛡️  CENTRAL TÁCTICA V1.5 - PROYECTO LIBERTAD")
        print(f"{CYAN}======================================================={RESET}")
        print(" 1. Ejecutar Menú Musical Integrado (juego.py)")
        print(" 2. Sincronizar Reloj Atómico Local (hora.py)")
        print(" 3. Activar Radar de Conectividad Infinito (auditor_internet.py)")
        print(" 4. Lanzar Cazador por Sockets Multihilo (caza_intrusos.py)")
        print(" 5. Monitor Guardián de Procesos y CPU (guardian.py)")
        print(" 6. Generador de Contraseñas de Alta Entropía (llave_maestra.py)")
        print(" 7. Automatizador de Envío y Respaldos (subir)")
        print(" 8. Analizador de Registros Locales (reportador.py)")
        print(" 9. Servidor de Despliegue Web Local (Port 8080)")
        print(" 10. Limpiar Historiales y Temporales (clear)")
        print(" 11. Verificar Estado del Almacenamiento Interno")
        print(f" 12. {VERDE}SISTEMA DE TRANSACCIONES FINANCIERAS (finanzas.py){RESET}")
        print(" 13. Cerrar Operaciones y Salir de la Central")
        print(f"{CYAN}======================================================={RESET}")
        
        opcion = input("Seleccione la herramienta a desplegar: ")
        
        if opcion == "1": ejecutar_script("juego.py")
        elif opcion == "2": ejecutar_script("hora.py")
        elif opcion == "3": ejecutar_script("auditor_internet.py")
        elif opcion == "4": ejecutar_script("caza_intrusos.py")
        elif opcion == "5": ejecutar_script("guardian.py")
        elif opcion == "6": ejecutar_script("llave_maestra.py")
        elif opcion == "7": os.system("bash ~/mis_script/subir")
        elif opcion == "8": ejecutar_script("reportador.py")
        elif opcion == "9": 
            print(f"\n{VERDE}Encendiendo servidor local en http://localhost:8080...{RESET}")
            print(f"{AMARILLO}Use Ctrl + C para apagarlo cuando termine.{RESET}\n")
            os.system("python -m http.server 8080")
        elif opcion == "10": 
            os.system("clear")
            print(f"{VERDE}Terminal purgada con éxito.{RESET}\n")
            time.sleep(1)
        elif opcion == "11": 
            print(f"\n{CYAN}📊 Estado del almacenamiento en el Infinix:{RESET}")
            os.system("df -h .")
            input(f"\n{AMARILLO}Presione Enter para regresar...{RESET}")
        elif opcion == "12": ejecutar_script("finanzas.py")
        elif opcion == "13":
            print(f"\n{ROJO}Cerrando Central Táctica. Conexión segura finalizada. ¡Hasta pronto, Yorvis!{RESET}\n")
            break
        else:
            print(f"\n{ROJO}Opción inválida. Intente de nuevo.{RESET}\n")
            time.sleep(1)

if __name__ == "__main__":
    mostrar_menu()
