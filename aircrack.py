# --------------------------------------------------------------------------
# Bienvenido a la herramienta de Aircrack-ng
# Esta herramienta te permite realizar ataques de fuerza bruta a redes WiFi protegidas por WPA/WPA2.
# Asegúrate de tener los permisos necesarios para realizar estas pruebas.
# --------------------------------------------------------------------------
# Desarrollado por Sergio aka: W17CHeR
# ---------------------------------------------------------------------------
# Esta herramienta es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# ----------------------------------------------------------------------------

import os
import subprocess
import sys
from termcolor import colored

def print_title():
    os.system('clear')
    print(colored("=== Aircrack-ng Tool ===", "cyan"))
    print(colored("Desarrollado por Sergio aka: W17CHeR", "green"))
    print("=" * 70)

def mostrar_menu():
    print("\nSelecciona una opción:")
    print("1. Buscar señales Wi-Fi")
    print("2. Identificar tipo de protección")
    print("3. Crackear contraseña Wi-Fi con aircrack-ng")
    print("4. Volver al menú principal")
    print("5. Salir")

def buscar_wifi():
    print(colored("\nIniciando escaneo de redes Wi-Fi (requiere sudo)...", "yellow"))
    try:
        subprocess.run(["sudo", "iwlist", "wlan0", "scanning"], check=True)
    except Exception as e:
        print(colored(f"Error durante el escaneo: {e}", "red"))

def identificar_proteccion():
    interface = input("Introduce el nombre de la interfaz (ej: wlan0): ")
    print(colored(f"\nEscaneando redes con {interface} para identificar tipo de cifrado...", "yellow"))
    try:
        subprocess.run(["sudo", "airodump-ng", interface], check=True)
    except Exception as e:
        print(colored(f"Error al ejecutar airodump-ng: {e}", "red"))

def crackear_wifi():
    cap_file = input("Introduce la ruta del archivo .cap: ")
    wordlist = input("Introduce la ruta del diccionario (wordlist): ")
    try:
        subprocess.run(["aircrack-ng", "-w", wordlist, "-b", "XX:XX:XX:XX:XX:XX", cap_file], check=True)
    except Exception as e:
        print(colored(f"Error al ejecutar aircrack-ng: {e}", "red"))

def aircrack_menu():
    while True:
        print_title()
        mostrar_menu()
        opcion = input("\nOpción: ")

        if opcion == "1":
            buscar_wifi()
        elif opcion == "2":
            identificar_proteccion()
        elif opcion == "3":
            crackear_wifi()
        elif opcion == "4":
            print(colored("Regresando al menú principal...", "yellow"))
            try:
                subprocess.run(["python", "Red_Dragon.py"], check=True)
            except Exception as e:
                print(colored(f"No se pudo volver al menú principal: {e}", "red"))
            break
        elif opcion == "5":
            print(colored("Gracias por usar Red_Dragon. ¡Hasta luego!", "green"))
            sys.exit(0)
        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))

        input(colored("\nPresiona Enter para continuar...", "magenta"))

if __name__ == "__main__":
    aircrack_menu()
