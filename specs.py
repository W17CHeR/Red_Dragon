# --------------------------------------------------------------------------.
# Specs.py - Módulo para mostrar especificaciones del sistema
# ---------------------------------------------------------------------------
# Programa desarrollado por Sergio aka: W17CHeR
# -------------------------------------------------------------------------------
# Este programa es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# -------------------------------------------------------------------------------

import os
from termcolor import colored

def mostrar_menu():
    os.system("clear")  # o "cls" en Windows
    print(colored("=== Menú de Especificaciones del Sistema ===", "cyan"))
    print("\nSelecciona una opción:")
    print("1. Ejecutar fastfetch")
    print("2. Volver al menú principal")
    print("q. Salir")

def ejecutar_fastfetch():
    resultado = os.system("fastfetch")
    if resultado != 0:
        print(colored("Error al ejecutar fastfetch. Asegúrate de tenerlo instalado.", "red"))

def specs_menu():
    while True:
        mostrar_menu()
        opcion = input("\nOpción: ")

        if opcion == "1":
            ejecutar_fastfetch()
        elif opcion == "2":
            print(colored("\nRegresando al menú principal...\n", "yellow"))
            break
        elif opcion.lower() == "q":
            print(colored("\nSaliendo del programa Specs...", "green"))
            exit()
        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))

        input(colored("\nPresiona Enter para continuar...", "magenta"))

if __name__ == "__main__":
    specs_menu()
