import json

def cargar_grupos():
    with open("jsons/grupos.json", "r", encoding="utf-8") as archivo:
        grupos = json.load(archivo)
    return grupos

def guardar_grupos(grupos):
    with open("jsons/grupos.json", "w", encoding="utf-8") as archivo:
        json.dump(grupos, archivo, indent=4, ensure_ascii=False)

def cargar_campers():
    try:
        with open("jsons/Campers.json", "r", encoding="utf-8") as archivo:
            campers = json.load(archivo)
    except FileNotFoundError:
        campers = []
    return campers


def guardar_campers(campers):
    with open("jsons/Campers.json", "w", encoding="utf-8") as archivo:
        json.dump(campers, archivo, indent=4, ensure_ascii=False)

def menuCamper():
    while True:
        print("-----------------------------------------------")
        print("Que es lo que quieres hacer?")
        print("1. Visualizar tus datos personales")
        print("2. ver sus notas de cada modulo")
        print("3. Revisar Estado")
        print("4. Salir")
        print("-----------------------------------------------")
        opcion = input("Ingrese el numero de la opcion que desea: ")

        if opcion == "1":
            print("---Tus datos personales---")
            campers = cargar_campers()
            print("Visualizando datos...")
            for camper in campers:
                print(camper)
            print("-----------------------------------------------")

        elif opcion == "2":
            print("---Tus notas de los modulos---")
            grupos = cargar_grupos()
            print("Visualizando notas...")
            for grupo in grupos:
                print(grupo)
            print("-----------------------------------------------")

        elif opcion == "3":
            print("---Estado actual---")
            campers = cargar_campers()
            print("Revisando estado...")
            for camper in campers:
                print(f"Nombre: {camper.get('nombre')}, Estado: {camper.get('estado')}")
            print("-----------------------------------------------")

        elif opcion == "4":
            print("Saliendo del menu camper...")
            break

        else:
            print("Opcion invalida. Intente nuevamente.")