# ------------------------------------------------------------------------------------------------------------------
#                                                       Red_Dragon
# ------------------------------------------------------------------------------------------------------------------
# Este programa es desarrollado por Sergio aka: W17CHeR
# ------------------------------------------------------------------------------------------------------------------
# Importante: Este programa es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# ------------------------------------------------------------------------------------------------------------------

import os
import sys
import subprocess
from termcolor import colored

def print_title():
    os.system('clear')  # Limpia la terminal
    ascii_logo = """
#            .                                                        
                               .%%*:        -%#-                                                    
                                 #%#*#*=:    =%%%%+-    :                                            
                                   #%##+=*#%%#%@%%%#=*##%%=                                          
                      #@#+-.         =%%%%%*.  .:=+%+:#%%#*%%%*                                      
                        .*%+--+++-::.              -%%=   +. =-=#:                                   
                            -*##%*++===*#%%@@%%#%%@@%%%*+==+=    =%##:                               
                         ....:---+*%%%%%%%%%%%%%%%#+-*%%%%%%%%%*+..: .*%-:..-##==#*                 
                      =#####*+-..:-+*%%%%#***#%%@%%%#-:-==  =%%+=###+.:*=*%#-:+=:  =*               
                         =#%%##########%%%%%*=-.     -+==::-=--=:-#%###. --==++++=:-+               
                      :::::=%%%%%%%%%%%%%%%%%%%%%%%%#*#%%%%%#+=++++#%%%%%%%%#*%%%%#*+               
                         *%%#++%%%%%%%%%%%%#%+. *+=+%%%%%%%##%%%%%%#=+%=%-#+#:.=*===                
                       +=--+@%%%%#%#+.   .:=*####*++++**%%%%%%%**+*%%%%%%#++#+:%%##=                
                      ::-*%#%%*+*%%@@%%%%%%%%%%@%%#*+:+=*%%%%%%%%%%%%%*     .-     .               
                    :::+*+=%#**%%%%%%%%%%%%%==.:=++**##*+#%%#%%%%%%%%%#                             
                   :::--:+%*#%%%%%%%%%%%%***#%%%%%%%@@%##****=*%#++++%+   ==-                       
                  ::.:::+=-#%%%%*%%%%%%%%%%%%=*%%%%%%%%%***+**:-##=::------=*##*                    
                     :::::*%%%%*###%%%%%%%%%%=:%*-%%#*%%%%##%%#+.+%%%%%%%%       =                  
                    .::::=%%%%%--#%%%%%%%%%%+*-:*%%%%%#:  .#%%%%#=+#%*%*#                           
                    .: .:+%=#%%=+%%%##%%%%%%=-+-::-#%%*      =%%%%#.-%*:=%.=%                       
                    .  .:*=-%%%%%%%%#*#%%%%%*- .+##%%%%*     .:=#%%+-+#+%*+%#                       
                       .:-:-%%%%%%%%++%%%*#%#*-.  ---*%%%#=      =%%*::.:::##                       
                        ::::*%%%#%%%#*%%%%+#%#=::=**##%%%%%%#-    +%%%-+*-*=                        
                        ::::-%%#=%%%%%%%%%%%%%%***:   ---:-*%%%=  **-#%%%%%                         
                         ::::=%*:=%%%%%%%%%%%%%%%#---:...:::-*%%+       :#                          
                          : .:=*::=###%%%%%%%%%%%%%%%*-::::::-*%%%.                                 
                              :::::-=-+%%%#%%%%%%%%%%%%#*+=-::-+#%%=                                
                               ::. .:::-*%%==#%%%%%%%%%%%%%%%#*=-+%%*                               
                                 .   ::::-=*=--+%%#-=#@%%%**#%%%%%#%%%                              
                                         ::::::::-=*+::-+#%#=:---=#%%%%=                            
                                           :     .::  :::::. .::::.  .#%#                           
                                                    .      .             :  
"""
    print(colored(ascii_logo, 'red'))
    print(colored(os.popen('figlet -f slant "Red Dragon"').read(), 'red'))
    print("="*75)
    print(colored("Desarrollado por Sergio aka: W17CHeR", 'green').center(75))
    print("="*75)
    print(colored("Este programa fue desarrollado con fines éticos y educativos", 'yellow').center(75))
    print("="*75)
    print(colored("Version 1.0.5", 'blue').center(75))
    print("="*75)

# ------------------------------------------------------------------------------------------------------------------

def menu():
    print("Selecciona una opción:")
    print("1. Mostrar especificaciones del sistema")
    print("2. Ejecutar John The Ripper")
    print("3. Ejecutar Aircrack-ng")
    print("4. Ejecutar Metasploit")
    print("q. Salir")

def main():
    while True:
        print_title()
        menu()
        opcion = input("Ingresa tu opción: ")

        if opcion == '1':
            script_path = "./specs.py"
            if os.path.exists(script_path):
                try:
                    result = subprocess.run(["python3", script_path])
                    if result.returncode == 99:
                        continue
                except subprocess.CalledProcessError as e:
                    print(colored(f"Error al ejecutar el script: {e}", 'red'))
            else:
                print(colored(f"El script {script_path} no existe.", 'red'))

        elif opcion == '2':
            script_path = "./J-Ripper.py"
            if os.path.exists(script_path):
                result = subprocess.run(["python3", script_path])
                if result.returncode == 0:
                    print(colored("Gracias por usar Red_Dragon. ¡Hasta luego!", 'green'))
                    sys.exit(0)

        elif opcion == '3':
            script_path = "./aircrack.py"
            if os.path.exists(script_path):
                result = subprocess.run(["python3", script_path])
                if result.returncode == 0:
                    print(colored("Gracias por usar Red_Dragon. ¡Hasta luego!", 'green'))
                    sys.exit(0)
            else:
                print(colored(f"El script {script_path} no existe.", 'red'))

        elif opcion == '4':
            script_path = "./metasploit.py"
            if os.path.exists(script_path):
                result = subprocess.run(["python3", script_path])
                if result.returncode == 99:
                    continue  # Volver al menú principal
                elif result.returncode == 0:
                    print(colored("Gracias por usar Red_Dragon. ¡Hasta luego!", 'green'))
                    sys.exit(0)
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
