import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_COORDINADORES = os.path.join(BASE_DIR, "jsons", "Coordinadores.json")

from menuCoordinador import menuCoordinador
from registrarse import registrarse
from menuTrainer import menuTrainer
from menuCamper import menuCamper   

while True:
    print("Biendvenido a la plataforma de Campuslands")
    print("-------------------------------------------------")
    print("Que desea hacer?")
    print("1. Iniciar sesion")
    print("2. Registrarse como camper")
    print("3. Salir")
    opcion = input("Ingrese el numero de la opcion que desea: ")
    print("-------------------------------------------------")

    if opcion == "1":
        print("--------------------------------------------------------")
        print("Como quieres iniciar sesion?")
        print("1. Como camper")
        print("2. Como Trainer")
        print("3. Como Coordinador")
        print("--------------------------------------------------------")
        opcion2 = input("Ingrese el numero de la opcion que desea: ")
       

        if opcion2 == "1":
            gmail = input("Ingrese su correo electronico: ")
            contraseña = input("Ingrese su contraseña: ")
            with open("jsons/Campers.json", "r", encoding="utf-8") as file:
                campers = json.load(file)
                usuario_encontrado = False
                for camper in campers:
                    if camper["gmail"] == gmail and camper["contraseña"] == contraseña:
                        print("Bienvenido " + camper["nombre"])
                        usuario_encontrado = True
                        menuCamper(camper)
                        
                if not usuario_encontrado:
                    print("Correo o contraseña incorrectos")

        elif opcion2 == "2":
            gmail = input("Ingrese su correo electronico: ")
            contraseña = input("Ingrese su contraseña: ")
            with open("jsons/Trainers.json", "r", encoding="utf-8") as file:
                trainers = json.load(file)
                usuario_encontrado = False
                for trainer in trainers:
                    if trainer["gmail"] == gmail and trainer["contraseña"] == contraseña:
                        print("Bienvenido " + trainer["nombre"])
                        usuario_encontrado = True
                        menuTrainer(trainer)
                        
                if not usuario_encontrado:
                    print("Correo o contraseña incorrectos")
        
        elif opcion2 == "3":
            gmail = input("Ingrese su correo electronico: ")
            contraseña = input("Ingrese su contraseña: ")
            with open("jsons/Coordinadores.json", "r", encoding="utf-8") as file:
                coordinadores = json.load(file)
                usuario_encontrado = False
                
                for coordinador in coordinadores:
                    if coordinador["gmail"] == gmail and coordinador["contraseña"] == contraseña:
                        print("Bienvenido " + coordinador["nombre"])
                        usuario_encontrado = True
                        menuCoordinador()
                    
                if not usuario_encontrado:
                    print("Correo o contraseña incorrectos")
        
    elif opcion == "2":
        registrarse()
        
    elif opcion == "3":
        print("Hasta luego!")
        break
        
    else:
        print("Opcion invalida. Intente nuevamente.")

    



