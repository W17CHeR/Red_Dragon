# ------------------------------------------------------------------------------------------------------------------
#                                                       Red_Dragon
# ------------------------------------------------------------------------------------------------------------------
# Este programa es desarrollado por Sergio aka: W17CHeR
# ------------------------------------------------------------------------------------------------------------------
# En este programa se integran la herramienta de Metasploit-framework
# -------------------------------------------------------------------------------------------------------------------
# Importante: Este programa es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# ------------------------------------------------------------------------------------------------------------------

import os
import subprocess
import sys
from termcolor import colored

def print_title():
    os.system("clear")
    print(colored(os.popen("figlet Metasploit").read(), "green"))
    print("-" * 40)

def mostrar_menu():
    print(colored("(1) Ejecutar Metasploit", "cyan"))
    print(colored("(2) Regresar al menú principal", "cyan"))
    print(colored("(q) Salir completamente del programa", "cyan"))

def main():
    while True:
        print_title()
        mostrar_menu()
        opcion = input(colored("\nSelecciona una opción: ", "yellow"))

        if opcion == "1":
            print(colored("Iniciando Metasploit Framework...\n", "green"))
            try:
                subprocess.run(["msfconsole"])
            except FileNotFoundError:
                print(colored("Error: msfconsole no está instalado o no está en el PATH.", "red"))
            input(colored("\nPresiona Enter para volver al menú...", "magenta"))

        elif opcion == "2":
            print(colored("Regresando al menú principal...\n", "yellow"))
            sys.exit(99)

        elif opcion.lower() == "q":
            print(colored("Saliendo completamente del programa... ¡Hasta luego!", "green"))
            sys.exit(0)

        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))

if __name__ == "__main__":
    main()

