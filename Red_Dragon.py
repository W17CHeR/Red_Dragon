# ------------------------------------------------------------------------------------------------------------------
#                                                       Red_Dragon
# ------------------------------------------------------------------------------------------------------------------
# Este programa es desarrollado por Sergio aka: W17CHeR
# ------------------------------------------------------------------------------------------------------------------
import os
import subprocess
from termcolor import colored

def print_title():
    os.system('clear')  # Limpia la terminal
    print(colored(os.popen('figlet -f slant "Red Dragon"').read(), 'red'))

# Aquí mostrara el menú

def menu():
    print("Selecciona una opción:")
    print("1. Mostrar especificaciones del sistema")
    print("2. Ejecutar John The Ripper")
    print("q. Salir")

# Aquí mostrara las opciones del menú
def main():
    while True:
        print_title()
        menu()
        opcion = input("Ingresa tu opción: ")

        if opcion == '1':
            script_path = "./specs.py"
            if os.path.exists(script_path):
                try:
                    subprocess.run(["python", script_path], check=True)
                except subprocess.CalledProcessError as e:
                    print(colored(f"Error al ejecutar el script: {e}", 'red'))
            else:
                print(colored(f"El script {script_path} no existe.", 'red'))
        elif opcion == 'q':
            print(colored("Saliendo del programa...", 'green'))
            break
        else:
            print(colored("Opción no válida. Intenta de nuevo.", 'yellow'))

if __name__ == "__main__":
    main()
    print(colored("Gracias por usar Red_Dragon. ¡Hasta luego!", 'green'))
