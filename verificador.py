import os
import hashlib
import json
import time

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

DB_HASHES = os.path.expanduser("~/mis_script/.firmas_seguridad.json")
SCRIPTS_A_VIGILAR = [
    "menu.py", "caza_intrusos.py", "puertos.py", 
    "rastreo_ip.py", "guardian.py", "reportador.py"
]

def calcular_sha256(archivo):
    ruta = os.path.expanduser(f"~/mis_script/{archivo}")
    if not os.path.exists(ruta):
        return None
    sha256_hash = hashlib.sha256()
    with open(ruta, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256_hash.update(bloque)
    return sha256_hash.hexdigest()

def ejecutar_verificador():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🛡️  VERIFICADOR DE INTEGRIDAD - PROYECTO LIBERTAD")
    print(f"{CYAN}======================================================={RESET}")
    
    # Si no existe la base de datos de firmas, la creamos (Modo Inicialización)
    if not os.path.exists(DB_HASHES):
        print(f"{AMARILLO}[!] Generando línea base de firmas criptográficas...{RESET}")
        firmas = {}
        for archivo in SCRIPTS_A_VIGILAR:
            hash_calc = calcular_sha256(archivo)
            if hash_calc:
                firmas[archivo] = hash_calc
                print(f" ✅ Firma registrada -> {archivo}")
        with open(DB_HASHES, "w") as f:
            json.dump(firmas, f, indent=4)
        print(f"\n{VERDE}🔒 Base de datos blindada con éxito.{RESET}")
        return

    # Modo Auditoría: Comparamos el estado actual con la base de datos
    print(f"{CYAN}[!] Escaneando integridad del arsenal local...{RESET}\n")
    time.sleep(1)
    
    with open(DB_HASHES, "r") as f:
        firmas_guardadas = json.load(f)

    alteraciones = 0
    print(f"{CYAN}{'ARCHIVO':<20}{'ESTADO DE INTEGRIDAD':<25}{RESET}")
    print(f"{CYAN}-------------------------------------------------------{RESET}")
    
    for archivo in SCRIPTS_A_VIGILAR:
        hash_actual = calcular_sha256(archivo)
        hash_guardado = firmas_guardadas.get(archivo)
        
        if hash_actual is None:
            print(f"{AMARILLO}{archivo:<20}{'NO ENCONTRADO [⚠️]':<25}{RESET}")
        elif hash_actual == hash_guardado:
            print(f"{VERDE}{archivo:<20}{'INTEGRO [🔒]':<25}{RESET}")
        else:
            print(f"{ROJO}{archivo:<20}{'¡ALTERADO! [🚨]':<25}{RESET}")
            alteraciones += 1

    print(f"{CYAN}-------------------------------------------------------{RESET}")
    if alteraciones == 0:
        print(f"📊 {VERDE}Auditoría limpia. Todos los archivos mantienen su firma.{RESET}")
    else:
        print(f"📊 {ROJO}¡ALERTA! Se detectaron {alteraciones} archivos modificados.{RESET}")
        print(f"👉 Si usted hizo los cambios, borre '.firmas_seguridad.json' para resetear.")
    print(f"{CYAN}======================================================={RESET}")

if __name__ == "__main__":
    ejecutar_verificador()
