import os
import time
import sys

ROJO = "\033[1;31m"
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def activar_alarma():
    # 1. Registro silencioso en la bitácora oculta de auditoría
    fecha_hora = time.strftime('%Y-%m-%d %H:%M:%S')
    with open(".registro_intrusos.log", "a") as f:
        f.write(f"[{fecha_hora}] ALERTA: Intento de violación de seguridad detectado.\n")
    
    # 2. Contraataque por Voz (Asusta al intruso)
    # Revisa si termux-tts-speak está instalado para hablar
    os.system("termux-tts-speak 'Alerta. Acceso denegado. Intruso detectado en el sistema.' 2>/dev/null")
    
    print(f"\n{ROJO}☠️  SISTEMA BLOQUEADO - REPORTE ENVIADO AL COMANDANTE  ☠️{RESET}")
    time.sleep(2)

def boveda_falsa():
    os.system("clear")
    print(f"{ROJO}======================================================={RESET}")
    # Usamos barras invertidas dobles \\ para que Python no se confunda al renderizar el escudo
    print(f"  🔒 MASTER SECURE VAULT - ARCHIVOS DE EVIDENCIA 2026")
    print(f"{ROJO}======================================================={RESET}")
    print(f"{AMARILLO}⚠️ ADVERTENCIA: Solo personal autorizado (Yorvis).{RESET}\n")
    
    intentos = 0
    while intentos < 3:
        try:
            clave = input(f"{CYAN}[🔑 CREDENCIAL] Ingrese Clave Maestra:{RESET} ")
            
            # Una clave falsa que tú sabes que nunca usarás
            if clave == "LibertadAbsoluta2026":
                print(f"\n{VERDE}🔓 Acceso concedido...{RESET}")
                return
            else:
                intentos += 1
                print(f"{ROJO}❌ Clave incorrecta. Intentos restantes: {3 - intentos}{RESET}\n")
                time.sleep(1)
        except KeyboardInterrupt:
            # Si el intruso intenta salir con Ctrl+C, ¡activamos la alarma de todas formas!
            print(f"\n{ROJO}\n[!] Intento de cancelación forzada detectado.{RESET}")
            activar_alarma()
            sys.exit()
            
    activar_alarma()

if __name__ == "__main__":
    boveda_falsa()
