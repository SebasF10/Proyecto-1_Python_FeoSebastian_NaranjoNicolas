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
    print("-----------------------------------------------")
    print("Que es lo que quieres hacer?")
    print("1. Visualizar tus datos personales")
    print("2. ver sus notas de cada modulo")
    print("3. Revisar Estado")
    print("4. Salir")
    print("-----------------------------------------------")
    opcion = input("Ingrese el numero de la opcion que desea: ")