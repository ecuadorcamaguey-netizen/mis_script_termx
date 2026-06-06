import os
import time

print("=========================================")
print(" 🛰️  MONITOR DE CONEXIÓN Y COMPARTICIÓN  ")
print("=========================================")

try:
    while True:
        print("\n[+] Verificando estabilidad con Google...")
        resultado = os.system("ping -c 3 8.8.8.8") 
        
        if resultado == 0:
            print("🟢 Tu internet está respondiendo correctamente.")
        else:
            print("🔴 Alerta: Tu señal es débil o está bloqueada.")
            
        print("\n[+] Revisando si hay dispositivos colgados a tu Hotspot...")
        os.system("ip neigh") 
        
        print("\n-----------------------------------------")
        print("Esperando 10 segundos... (Ctrl+C para salir)")
        time.sleep(10)
except KeyboardInterrupt:
    print("\n👋 Monitor cerrado correctamente.")
