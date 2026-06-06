import random
import os

# Generamos un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("=========================================")
print(" 🎯 ¡BIENVENIDO AL CAMPEONATO TERMINAL! 🎯")
print("    Adivina el número secreto (1 al 100) ")
print("=========================================")

while True:
    try:
        # Pedimos el número al jugador
        intento = int(input("\nEscribe tu número: "))
        intentos += 1
        
        # Validamos la lógica del juego
        if intento < numero_secreto:
            print("❌ ¡Muy bajo! Intenta con uno más grande.")
        elif intento > numero_secreto:
            print("❌ ¡Muy alto! Intenta con uno más chico.")
        else:
            print(f"\n🏆 ¡Felicidades! Adivinaste en {intentos} intentos.")
            
            # El teléfono te felicita usando la API de voz de Android
            mensaje_voz = f"Felicidades, ganaste el campeonato en {intentos} intentos."
            os.system(f'termux-tts-speak "{mensaje_voz}"')
            break
            
    except ValueError:
        print("⚠️ Por favor, introduce un número válido.")
