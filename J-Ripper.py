# -------------------------------------------------------------------------
#    J-Ripper: Herramienta para crackear contraseñas y generar diccionarios
# -------------------------------------------------------------------------
#    Desarrollado por Sergio aka: W17CHeR
# -------------------------------------------------------------------------
#    Este programa es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# -------------------------------------------------------------------------

import os
import sys
import subprocess
from termcolor import colored

def mostrar_menu():
    os.system("clear")
    print(colored("=== John The Ripper - J-Ripper ===", "cyan"))
    print("Selecciona una opción:")
    print("1. Crackear una contraseña (modo rápido)")
    print("2. Generar diccionario (wordlist personalizado)")
    print("3. Añadir fichero protegido y crackear")
    print("4. Volver al menú principal")
    print("q. Salir")

def crackear_contraseña():
    hash_file = input("Ruta del archivo con el hash: ")
    try:
        subprocess.run(["john", hash_file], check=True)
    except Exception as e:
        print(colored(f"Error al ejecutar John: {e}", "red"))

def generar_diccionario():
    nombre_diccionario = input("Nombre del archivo para guardar el diccionario: ")
    try:
        palabras = []
        print("Introduce palabras clave para generar el diccionario (ENTER para terminar):")
        while True:
            palabra = input("> ")
            if palabra == "":
                break
            palabras.append(palabra)

        with open(nombre_diccionario, "w") as f:
            for palabra in palabras:
                f.write(palabra + "\n")

        print(colored(f"Diccionario guardado como '{nombre_diccionario}'", "green"))
    except Exception as e:
        print(colored(f"Error al generar diccionario: {e}", "red"))

def crackear_fichero_protegido():
    fichero = input("Ruta del fichero protegido por contraseña: ")
    try:
        subprocess.run(["zip2john", fichero], stdout=open("hash.txt", "w"), check=True)
        print(colored("Hash extraído en 'hash.txt'. Ejecutando John...", "yellow"))
        subprocess.run(["john", "hash.txt"], check=True)
    except Exception as e:
        print(colored(f"Error en el proceso: {e}", "red"))

def j_ripper_menu():
    while True:
        mostrar_menu()
        opcion = input("\nOpción: ")

        if opcion == "1":
            crackear_contraseña()
        elif opcion == "2":
            generar_diccionario()
        elif opcion == "3":
            crackear_fichero_protegido()
        elif opcion == "4":
            print(colored("Regresando al menú principal...", "yellow"))
            try:
                subprocess.run(["python", "Red_Dragon.py"], check=True)
            except Exception as e:
                print(colored(f"No se pudo regresar a Red_Dragon: {e}", "red"))
                exit()
            break
        elif opcion.lower() == "q":
         print(colored("Saliendo de J-Ripper... Gracias por usar Red_Dragon ¡Hasta luego!", "green"))
         sys.exit(99)

        else:
            print(colored("Opción no válida. Intenta de nuevo.", "red"))

        input(colored("\nPresiona Enter para continuar...", "magenta"))

if __name__ == "__main__":
    j_ripper_menu()
