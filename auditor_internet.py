import os
import time
import speedtest

print("=========================================")
print(" 🛰️  MONITOR DE CONEXIÓN Y VELOCIDAD  ")
print("=========================================")

try:
    while True:
        print("\n[+] Verificando estabilidad (Ping) con Google...")
        resultado = os.system("ping -c 3 8.8.8.8") 
        
        if resultado == 0:
            print("🟢 Tu internet está respondiendo.")
        else:
            print("🔴 Alerta: Tu señal es débil o está bloqueada.")
            
        print("\n[+] Midiendo velocidad en Mbps (Espera un momento)...")
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            velocidad_descarga = st.download() / 10**6
            velocidad_subida = st.upload() / 10**6
            
            print(f"📥 Velocidad de Descarga: {velocidad_descarga:.2f} Mbps")
            print(f"📤 Velocidad de Subida:   {velocidad_subida:.2f} Mbps")
        except Exception as e:
            print("⚠️ El test de velocidad falló o el servidor está saturado.")
        
        print("\n-----------------------------------------")
        print("Esperando 15 segundos... (Ctrl+C para salir)")
        time.sleep(15)
except KeyboardInterrupt:
    print("\n👋 Monitor cerrado correctamente.")

