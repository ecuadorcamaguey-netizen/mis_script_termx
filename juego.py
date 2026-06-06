import random
import os
import time

def borrar_pantalla():
    os.system('clear')

def leer_record():
    if os.path.exists(".record_juego"):
        with open(".record_juego", "r") as f:
            return int(f.read().strip())
    return 999

def guardar_record(intentos):
    with open(".record_juego", "w") as f:
        f.write(str(intentos))

def jugar():
    borrar_pantalla()
    numero_secreto = random.randint(1, 100)
    intentos = 0
    record_actual = leer_record()
    
    print("=========================================")
    print(" 🎯 ¡BIENVENIDO AL CAMPEONATO TERMINAL! 🎯")
    print("    Adivina el número secreto (1 al 100)")
    if record_actual != 999:
        print(f" 🏆 Récord actual a batir: {record_actual} intentos")
    print("=========================================")
    
    # Comentamos la API por si estás en un entorno silencioso, pero puedes descomentarla si quieres voz
    # os.system('termux-tts-speak "Intenta adivinar el número secreto del uno al cien"')

    while True:
        try:
            intento = int(input("\nEscribe tu número: "))
            intentos += 1
            
            if intento < 1 or intento > 100:
                print("❌ ¡Oye! Dijimos entre 1 y 100.")
                continue
                
            if intento < numero_secreto:
                print("📈 Más alto... ¡Inténtalo de nuevo!")
            elif intento > numero_secreto:
                print("📉 Más bajo... ¡Inténtalo de nuevo!")
            else:
                print(f"\n🏆 ¡Felicidades! Adivinaste en {intentos} intentos.")
                
                if intentos < record_actual:
                    print("🎉 ¡NUEVO RÉCORD HISTÓRICO REGISTRADO! 🎉")
                    guardar_record(intentos)
                    os.system(f'termux-tts-speak "Felicidades campeón, rompiste el récord con {intentos} intentos"')
                else:
                    os.system(f'termux-tts-speak "Buen trabajo, lo lograste en {intentos} intentos"')
                break
        except ValueError:
            print("❌ Por favor, introduce un número válido.")

while True:
    jugar()
    print("\n-----------------------------------------")
    opcion = input("¿Quieres otra ronda campeón? (s/n): ").lower()
    if opcion != 's':
        print("\n¡Gracias por jugar! Volviendo a la consola...")
        time.sleep(1)
        break
