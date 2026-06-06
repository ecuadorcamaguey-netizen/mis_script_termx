import requests

print("Consultando el servidor de tiempo de Google...")
try:
    # Usamos los encabezados de respuesta de Google que incluyen la fecha y hora oficial
    respuesta = requests.get("https://google.com", timeout=5)
    fecha_servidor = respuesta.headers.get('Date')
    
    print("\n====================================")
    print(f" -> Tiempo del servidor: {fecha_servidor}")
    print("====================================")
except Exception as e:
    print(f"Error de conexión: {e}")

