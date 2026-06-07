import os
import time

VERDE = "\033[1;32m"
ROJO = "\033[1;31m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

archivo_registro = "historial_financiero.txt"

def registrar_movimiento(tipo, detalle, monto):
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    linea = f"[{fecha}] | {tipo:<7} | {detalle:<25} | ${monto}\n"
    with open(archivo_registro, "a") as f:
        f.write(linea)

def ver_historial():
    if not os.path.exists(archivo_registro):
        print(f"\n{ROJO}No hay registros financieros todavía.{RESET}\n")
        return
    print(f"\n{CYAN}================ HISTORIAL DE TRANSACCIONES ================{RESET}")
    with open(archivo_registro, "r") as f:
        for linea in f:
            if "INGRESO" in linea:
                print(f"{VERDE}{linea.strip()}{RESET}")
            else:
                print(f"{ROJO}{linea.strip()}{RESET}")
    print(f"{CYAN}============================================================{RESET}\n")

def menu_finanzas():
    while True:
        print(f"{CYAN}====================================={RESET}")
        print(f"       💰 SISTEMA DE TRANSACCIONES   ")
        print(f"{CYAN}====================================={RESET}")
        print(" 1. Registrar INGRESO (Dinero ganado)")
        print(" 2. Registrar GASTO (Comida/Alimentos)")
        print(" 3. Ver Historial Completo")
        print(" 4. Volver al Menú Principal")
        print(f"{CYAN}====================================={RESET}")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            detalle = input("Detalle del ingreso (ej: Optimizacion Celular): ")
            monto = input("Monto en COP (ej: 15000): ")
            registrar_movimiento("INGRESO", detalle, monto)
            print(f"{VERDE}✔ Ingreso registrado con éxito.{RESET}\n")
        elif opcion == "2":
            detalle = input("Detalle del gasto (ej: Compra de huevos): ")
            monto = input("Monto en COP (ej: 5000): ")
            registrar_movimiento("GASTO", detalle, monto)
            print(f"{ROJO}✔ Gasto registrado con éxito.{RESET}\n")
        elif opcion == "3":
            ver_historial()
        elif opcion == "4":
            print("\nSaliendo del sistema financiero...\n")
            break
        else:
            print(f"{ROJO}Opción inválida.{RESET}\n")

if __name__ == "__main__":
    menu_finanzas()
