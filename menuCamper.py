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

def menuCamper(camper_actual):
    while True:
        print("-----------------------------------------------")
        print("Que es lo que quieres hacer?")
        print("1. Visualizar tus datos personales")
        print("2. Ver datos del grupo al que perteneces")
        print("3. ver sus notas de cada modulo")
        print("4. Revisar Estado")
        print("5. Salir")
        print("-----------------------------------------------")
        opcion = input("Ingrese el numero de la opcion que desea: ")

        if opcion == "1":
            print("---Tus datos personales---")
            print("-----------------------------------------------")
            print(f"ID: {camper_actual['idCamper']}")
            print(f"Nombre: {camper_actual['nombre']}")
            print(f"Apellido: {camper_actual['apellido']}")
            print(f"Email: {camper_actual['gmail']}")
            print(f"Teléfono: {camper_actual['telefono']}")
            print(f"Dirección: {camper_actual['direccion']}")
            print(f"Acudiente: {camper_actual['acudiente']}")
            print(f"Jornada: {camper_actual['jornada']}")
            print(f"Grupo: {camper_actual['grupo']}")
            print(f"Estado General: {camper_actual['estado']}")
            print("-----------------------------------------------")

        elif opcion == "2":
            grupos = cargar_grupos()
            grupo_encontrado = False
            for grupo in grupos:
                if grupo["idGrupo"] == camper_actual["grupo"]:
                    grupo_encontrado = True
                    print("---Datos del grupo al que perteneces---")
                    print("-----------------------------------------------")
                    print(f"ID Grupo: {grupo['idGrupo']}")
                    print(f"Ruta: {grupo['ruta']}")
                    print(f"Salón: {grupo['salon']}")
                    print(f"Hora inicio: {grupo['hora_inicio']}")
                    print(f"Hora fin: {grupo['hora_fin']}")
                    print(f"Jornada: {grupo['jornada']}")
                    print(f"Fecha inicio: {grupo['fecha_inicio']}")
                    print(f"Fecha fin: {grupo['fecha_fin']}")
                    print("-----------------------------------------------")
                    break
            if not grupo_encontrado:
                print("No tienes un grupo asignado aún.")
                print("-----------------------------------------------")

        elif opcion == "3":
            print("---Tus notas de los modulos---")
            grupos = cargar_grupos()
            grupo_encontrado = False
            
            for grupo in grupos:
                for i in grupo["campers"]:
                    if i["idCamper"] == camper_actual["idCamper"]:
                        grupo_encontrado = True
                        print(f"Grupo: {grupo['idGrupo']} - Ruta: {grupo['ruta']}")
                        print("-----------------------------------------------")
                        
                        for modulo in grupo["modulos"]:
                            print(f"Módulo: {modulo['nombre']}")
                            encontrado_nota = False
                            
                            for evaluacion in modulo["evaluaciones"]:
                                if evaluacion["idCamper"] == camper_actual["idCamper"]:
                                    print("-----------------------------------------")
                                    print(f"Actividad: {evaluacion['actividad']}")
                                    print(f"Práctica: {evaluacion['practica']}")
                                    print(f"Teórica: {evaluacion['teorica']}")
                                    print(f"Definitiva: {evaluacion['definitiva']}")
                                    print(f"Estado: {evaluacion['estado']}")
                                    print(f"Riesgo: {evaluacion['riesgo']}")
                                    print("-----------------------------------------")
                                    encontrado_nota = True
                                    break
                            
                            if not encontrado_nota:
                                print(f" Sin calificaciones aún")
                            print()
                        break
            
            if not grupo_encontrado:
                print("No tienes un grupo asignado aún.")
            
            print("-----------------------------------------------")

        elif opcion == "4":
            print("---Estado actual de tus módulos---")
            grupos = cargar_grupos()
            grupo_encontrado = False
            
            for grupo in grupos:
                for i in grupo["campers"]:
                    if i["idCamper"] == camper_actual["idCamper"]:
                        grupo_encontrado = True
                        print(f"Grupo: {grupo['idGrupo']} - Ruta: {grupo['ruta']}")
                        print("-----------------------------------------------")
                        
                        for modulo in grupo["modulos"]:
                            print(f"Módulo: {modulo['nombre']}")
                            
                            for evaluacion in modulo["evaluaciones"]:
                                if evaluacion["idCamper"] == camper_actual["idCamper"]:
                                    print(f"Estado: {evaluacion['estado']}")
                                    print(f"Riesgo: {evaluacion['riesgo']}")
                                    print("-----------------------------------------")
                                    break
                            else:
                                print(f"  Estado: Pendiente de calificación")
                        
                        break
            
            if not grupo_encontrado:
                print(f"Estado General: {camper_actual['estado']}")
                print("Aún no tienes un grupo asignado.")
            
            print("-----------------------------------------------")

        elif opcion == "5":
            print("Saliendo del menu camper...")
            break

        else:
            print("Opcion invalida. Intente nuevamente.")