import os
import random
import string
import time

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def generar_llave():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🔑 GENERADOR DE LLAVES MAESTRAS - PROYECTO LIBERTAD")
    print(f"{CYAN}======================================================={RESET}")
    
    try:
        longitud = input(f"{CYAN}[👉 LONGITUD] Ingrese cuántos caracteres desea\n(Recomendado: 16 | Por defecto: 12): {RESET}").strip()
        
        if not longitud:
            longitud = 12
        else:
            longitud = int(longitud)
            
        if longitud < 8:
            print(f"\n{AMARILLO}⚠️ Advertencia: Longitud muy corta. Forzando a 8 caracteres por seguridad.{RESET}")
            longitud = 8
            
        print(f"\n{AMARILLO}[!] Compilando entropía y caracteres seguros...{RESET}")
        time.sleep(0.5)
        
        # Definimos los bloques de caracteres permitidos
        caracteres = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Generamos una contraseña verdaderamente aleatoria
        llave_final = "".join(random.choice(caracteres) for i in range(longitud))
        
        print(f"\n{VERDE}✅ LLAVE MAESTRA GENERADA CON ÉXITO:{RESET}")
        print(f"{CYAN}-------------------------------------------------------{RESET}")
        print(f"🔑 {AMARILLO}{llave_final}{RESET}")
        print(f"{CYAN}-------------------------------------------------------{RESET}")
        print(f"⚠️ {ROJO}Copie y guarde esta llave en un lugar seguro.{RESET}")
        
    except ValueError:
        print(f"\n{ROJO}❌ Error: Debe ingresar un número entero válido.{RESET}")
        
    print(f"{CYAN}======================================================={RESET}")

if __name__ == "__main__":
    generar_llave()
