# ------------------------------------------------------------------------------------------------------------------
#                                                       Red_Dragon
# ------------------------------------------------------------------------------------------------------------------
# Este programa es desarrollado por Sergio aka: W17CHeR
# ------------------------------------------------------------------------------------------------------------------
# Importante: Este programa es para fines educativos y de entretenimiento, no se debe usar para actividades ilegales.
# ------------------------------------------------------------------------------------------------------------------
import os
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
    print(colored("Version 1.0.1", 'blue').center(75))
    print("="*75)
# ------------------------------------------------------------------------------------------------------------------

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

        elif opcion == '2':
            script_path = "./J-Ripper.py"
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
