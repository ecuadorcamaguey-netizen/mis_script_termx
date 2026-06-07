import os
import sys
import subprocess
import time

VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def inyector_github():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🚀 INYECTOR AUTOMÁTICO - PROYECTO LIBERTAD")
    print(f"{CYAN}======================================================={RESET}")
    
    mensaje = input(f"{CYAN}[👉 COMENTARIO] Escriba el cambio realizado\n(O deje vacío para usar un sello automático): {RESET}").strip()
    if not mensaje:
        mensaje = f"Actualización automática: {time.strftime('%d/%m/%Y %H:%M:%S')}"
    
    print(f"\n{AMARILLO}[1/3] Preparando archivos (git add)...{RESET}")
    subprocess.run(["git", "add", "."])
    time.sleep(0.5)
    
    print(f"{AMARILLO}[2/3] Firmando bloque de seguridad (git commit)...{RESET}")
    subprocess.run(["git", "commit", "-m", mensaje])
    time.sleep(0.5)
    
    print(f"{AMARILLO}[3/3] Subiendo flujo al repositorio (git push)...{RESET}")
    print(f"{CYAN}-------------------------------------------------------{RESET}")
    
    resultado = subprocess.run(["git", "push", "origin", "main"])
    
    print(f"{CYAN}-------------------------------------------------------{RESET}")
    if resultado.returncode == 0:
        print(f"{VERDE}✅ ¡DESPLIEGUE EN GITHUB PAGES EXITOSO!{RESET}")
        subprocess.run(["termux-toast", "-b", "black", "-c", "#00ffcc", "🚀 GitHub Sincronizado al 100%"])
    else:
        print(f"{ROJO}❌ Error en la pasarela. Verifique credenciales.{RESET}")
        subprocess.run(["termux-toast", "-b", "black", "-c", "#ff3366", "❌ Fallo en el despliegue"])
        
    print(f"{CYAN}======================================================={RESET}")

if __name__ == "__main__":
    inyector_github()
