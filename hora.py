import urllib.request
import datetime
import os
import time

def borrar_pantalla():
    os.system('clear')

def obtener_hora_ecuador():
    try:
        # Nos conectamos a Google para validar que hay internet y extraer su cabecera de tiempo
        url = "https://google.com"
        respuesta = urllib.request.urlopen(url, timeout=5)
        fecha_gmt_str = respuesta.headers['Date']
        
        # Parseamos la fecha GMT de Google
        # Ejemplo: "Sat, 06 Jun 2026 07:05:00 GMT"
        fecha_gmt = datetime.datetime.strptime(fecha_gmt_str, '%a, %d %b %Y %H:%M:%S %Z')
        
        # Ecuador está en la zona horaria UTC-5 (Restamos 5 horas al GMT)
        fecha_ecuador = fecha_gmt - datetime.timedelta(hours=5)
        return fecha_ecuador, True
    except Exception:
        # Si no hay internet, usamos el reloj interno del Infinix como respaldo
        return datetime.datetime.now(), False

# Ejecución principal
borrar_pantalla()
print("🛰️  Sincronizando con los servidores de Google...")
hora_actual, sincronizado = obtener_hora_ecuador()

# Formateamos los datos para el diseño visual
dia_semana = hora_actual.strftime('%A')
# Traducimos el día rápidamente para mantener el estilo limpio
traducciones = {"Monday": "Lunes", "Tuesday": "Martes", "Wednesday": "Miércoles", 
                "Thursday": "Jueves", "Friday": "Viernes", "Saturday": "Sábado", "Sunday": "Domingo"}
dia_espanol = traducciones.get(dia_semana, dia_semana)

fecha_formateada = hora_actual.strftime(f'{dia_espanol}, %d de %b de %Y')
hora_pantalla = hora_actual.strftime('%I:%M:%S %p')
hora_texto = hora_actual.strftime('%I y %M %p')

# Dibujamos un diseño genial en la terminal
print("\n==========================================")
print(" 🕒   CENTRAL HORARIA DEL CAMPEONATO   🕒")
print("==========================================")
print(f" 📅  Fecha: {fecha_formateada}")
print(f" ⏰  Hora:  {hora_pantalla}")
if sincronizado:
    print(" 🟢  Estado: Sincronizado con precisión atómica (Google)")
else:
    print(" 🟡  Estado: Modo local sin conexión (Reloj Infinix)")
print("==========================================\n")

# Hacemos que el teléfono hable con elegancia
mensaje_voz = f"Hola campeón. Son las {hora_texto} en Ecuador."
os.system(f'termux-tts-speak "{mensaje_voz}"')

print("🤖 Comando de voz ejecutado con éxito.")
