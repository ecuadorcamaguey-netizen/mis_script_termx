import os
import sys
import time
import requests

# Paleta de colores táctica
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def rastrear_ip():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       🛰️  SISTEMA DE GEOLOCALIZACIÓN IP - PROYECTO LIBERTAD")
    print(f"{CYAN}======================================================={RESET}")
    
    ip_objetivo = input(f"{CYAN}[👉 INGRESE IP] Coloque la dirección IP a rastrear\n(Deje vacío para rastrear su propia IP pública): {RESET}").strip()
    
    print(f"\n{AMARILLO}[!] Estableciendo conexión con el satélite HTTPS seguro...{RESET}")
    time.sleep(1)
    
    # Usamos la API alternativa de FreeIPAPI que sí permite HTTPS nativo y libre
    url = f"https://freeipapi.com/api/json/{ip_objetivo}"
    
    # Cabeceras de seguridad para simular un navegador real
    cabeceras = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 15; Infinix X6870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    }
    
    try:
        respuesta = requests.get(url, headers=cabeceras, timeout=10)
        datos = respuesta.json()
        
        # Estructuramos la lectura según el formato de la nueva API
        if respuesta.status_code == 200 and datos.get("ipAddress"):
            print(f"\n{VERDE}✅ LOCALIZACIÓN ESTABLECIDA CON ÉXITO:{RESET}")
            print(f"{CYAN}-------------------------------------------------------{RESET}")
            print(f"🌐 {VERDE}IP Consultada:{RESET}  {datos.get('ipAddress')}")
            print(f"📍 {VERDE}País:{RESET}           {datos.get('countryName')} ({datos.get('countryCode')})")
            print(f"🏙️  {VERDE}Ciudad:{RESET}         {datos.get('cityName')}, {datos.get('regionName')}")
            print(f"🏢 {VERDE}Versión IP:{RESET}     IPv{datos.get('ipVersion')}")
            print(f"🧭 {VERDE}Coordenadas:{RESET}    Lat: {datos.get('latitude')} | Lon: {datos.get('longitude')}")
            print(f"⏰ {VERDE}Zona Horaria:{RESET}   {datos.get('timeZone')}")
            print(f"{CYAN}-------------------------------------------------------{RESET}")
        else:
            print(f"\n{ROJO}❌ Error: La dirección IP no arrojó resultados válidos.{RESET}")
            
    except requests.exceptions.RequestException as e:
        print(f"\n{ROJO}❌ Error de Red: No se pudo romper el cifrado del servidor.{RESET}")
        
    print(f"{CYAN}======================================================={RESET}")
    print(f" Regresando a la consola de comandos...")

if __name__ == "__main__":
    rastrear_ip()
