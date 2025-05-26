# ----------------------------------------------------------------------------
# Bienvenido a la herramienta de Aircrack-ng
# Esta herramienta te permite realizar ataques de fuerza bruta a redes WiFi protegidas por WPA/WPA2.
# Asegúrate de tener los permisos necesarios para realizar estas pruebas.
# ----------------------------------------------------------------------------
# Desarrollado por Sergio aka: W17CHeR
# ----------------------------------------------------------------------------
# Esta herramienta es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# ----------------------------------------------------------------------------

import os
import subprocess
import sys
from termcolor import colored


def print_title():
    os.system('clear')  # Limpia la terminal
    print(colored("=== Aircrack-ng CLI Tool ===", "cyan"))


def escanear_wifi():
    try:
        print(colored("Iniciando escaneo de redes Wi-Fi...", "cyan"))
        resultado = subprocess.check_output(["nmcli", "device", "wifi", "list"], stderr=subprocess.STDOUT)
        print(resultado.decode())
    except subprocess.CalledProcessError as e:
        print(colored(f"Error durante el escaneo: {e.output.decode()}", "red"))


def identificar_proteccion():
    bssid = input("Introduce el BSSID del punto de acceso: ")
    print(colored(f"Buscando información de protección para {bssid} (simulado)...", "yellow"))
    # Aquí se podría integrar una lógica real con herramientas como airodump-ng
    print(colored("Tipo de cifrado: WPA2 (simulado)", "green"))


def crackear_wifi():
    handshake = input("Ruta al archivo .cap con el handshake: ")
    wordlist = input("Ruta a la wordlist (diccionario): ")

    try:
        print(colored("Iniciando ataque de fuerza bruta con aircrack-ng...", "cyan"))
        subprocess.run(["aircrack-ng", "-w", wordlist, "-b", "XX:XX:XX:XX:XX:XX", handshake], check=True)
    except subprocess.CalledProcessError as e:
        print(colored(f"Error durante el crackeo: {e}", "red"))


def mostrar_menu():
    print_title()
    print("Selecciona una opción:")
    print("1. Buscar señales Wi-Fi")
    print("2. Identificar protección de la red")
    print("3. Crackear contraseña Wi-Fi con aircrack-ng")
    print("4. Volver al menú principal")
    print("5. Salir")


def aircrack_menu():
    while True:
        mostrar_menu()
        opcion = input("\nOpción: ")

        if opcion == "1":
            escanear_wifi()
        elif opcion == "2":
            identificar_proteccion()
        elif opcion == "3":
            crackear_wifi()
        elif opcion == "4":
            print(colored("Regresando al menú principal...", "yellow"))
            try:
                subprocess.run(["python3", "Red_Dragon.py"], check=True)
            except Exception as e:
                print(colored(f"No se pudo regresar al menú principal: {e}", "red"))
            break
        elif opcion == "5":
            print(colored("Saliendo de aircrack.py... Gracias por usar Red_Dragon ¡Hasta luego!", "green"))
            sys.exit(99)
        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))

        input(colored("\nPresiona Enter para continuar...", "magenta"))


if __name__ == "__main__":
    aircrack_menu()
