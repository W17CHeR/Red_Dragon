# --------------------------------------------------------------------------
# Bienvenido a la herramienta de Aircrack-ng
# Esta herramienta te permite realizar ataques de fuerza bruta a redes WiFi protegidas por WPA/WPA2.
# Asegúrate de tener los permisos necesarios para realizar estas pruebas.
# --------------------------------------------------------------------------
# Desarrollado por Sergio aka: W17CHeR
# --------------------------------------------------------------------------
# Este programa es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# --------------------------------------------------------------------------

import os
import subprocess
import sys
from termcolor import colored

def print_title():
    os.system('clear')
    print(colored("=== Aircrack-ng Toolkit ===", "red", attrs=["bold"]))
    print(colored("Desarrollado por Sergio aka: W17CHeR", "green"))
    print("=" * 60)

def buscar_wifi():
    os.system("clear")
    print(colored("Iniciando escaneo de redes Wi-Fi...", "cyan"))
    try:
        result = subprocess.run(["nmcli", "device", "wifi", "list"], capture_output=True, text=True, check=True)
        print(colored(result.stdout, "yellow"))
    except subprocess.CalledProcessError as e:
        print(colored(f"Error durante el escaneo:\n{e.stderr}", "red"))
    input(colored("\nPresiona Enter para continuar...", "magenta"))

def identificar_proteccion():
    os.system("clear")
    print(colored("Identificación del tipo de protección Wi-Fi", "cyan"))
    bssid = input("Introduce el BSSID de la red objetivo: ")
    try:
        result = subprocess.run(["airodump-ng", "--bssid", bssid, "wlan0"], check=True)
    except Exception as e:
        print(colored(f"Error al identificar la protección: {e}", "red"))
    input(colored("\nPresiona Enter para continuar...", "magenta"))

def crackear_contraseña():
    os.system("clear")
    print(colored("Crackeo de contraseña con aircrack-ng", "cyan"))
    captura = input("Introduce el nombre del archivo .cap: ")
    diccionario = input("Introduce la ruta del diccionario: ")
    try:
        subprocess.run(["aircrack-ng", "-w", diccionario, "-b", "00:11:22:33:44:55", captura], check=True)
    except Exception as e:
        print(colored(f"Error durante el ataque: {e}", "red"))
    input(colored("\nPresiona Enter para continuar...", "magenta"))

def aircrack_menu():
    while True:
        print_title()
        print(colored("1. Buscar señales Wi-Fi", "cyan"))
        print(colored("2. Identificar tipo de protección", "cyan"))
        print(colored("3. Crackear contraseña con aircrack-ng", "cyan"))
        print(colored("4. Volver al menú principal", "cyan"))
        print(colored("5. Salir del programa", "cyan"))

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            buscar_wifi()
        elif opcion == "2":
            identificar_proteccion()
        elif opcion == "3":
            crackear_contraseña()
        elif opcion == "4":
            print(colored("Regresando al menú principal...\n", "yellow"))
            sys.exit(99)
        elif opcion == "5":
            print(colored("Saliendo de Aircrack... Gracias por usar Red_Dragon. ¡Hasta luego!", "green"))
            sys.exit(0)
        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))

if __name__ == "__main__":
    aircrack_menu()
