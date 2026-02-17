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

def menuTrainer(trainer):
    while True:
        print("-----------------------------------------------")
        print("Que es lo que quieres hacer?")
        print("1. Ver grupos asignados y sus campers")
        print("2. Visualizar datos del sus grupos")
        print("3. Calificar modulos")
        print("4. Salir")
        print("-----------------------------------------------")
        opcion = input("Ingrese el numero de la opcion que desea: ")

        if opcion == "1":
            print("---Visualizar grupos asignados y sus campers---")
            grupos = cargar_grupos()
            
            print("Grupos asignados:")
            for grupo in grupos:
                if grupo["trainer_id"] == trainer["id"]:
                    print("-----------------------------------------------")
                    print(f"ID Grupo: {grupo['idGrupo']}")
                    print(f"Ruta: {grupo['ruta']}")
                    print("------------------------------------------------")
                    print("Campers asignados:")
                    for camper in grupo["campers"]:
                        print(f" {camper['nombre']} (ID: {camper['idCamper']})")
                    print("-----------------------------------------------")

        elif opcion == "2":
            for grupo in grupos:
                if grupo["trainer_id"] == trainer["id"]:
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

            print("-------- Calificar los modulos --------")

            grupos = cargar_grupos()
            print("¿A que grupo quieres calificar?")
            encontrado = False

        
            for i in range(len(grupos)):
                if grupos[i]["trainer_id"] == trainer["id"]:

                    encontrado = True
                    print("-----------------------------------")
                    print("ID Grupo:", grupos[i]["idGrupo"])
                    print("Ruta:", grupos[i]["ruta"])
                    print("Horario:", grupos[i]["hora_inicio"], "-", grupos[i]["hora_fin"])
                    print("-----------------------------------")

            if encontrado == False:
                print("No tienes grupos para calificar.")

            else:
                opcionG = input("Escribe el ID del grupo:  (Escribe en mayus la primera letra)")
                grupo_sel = None

                for i in range(len(grupos)):
                    if grupos[i]["trainer_id"] == trainer["id"]:
                        if grupos[i]["idGrupo"] == opcionG:
                            grupo_sel = grupos[i]

                if grupo_sel == None:
                    print("Grupo no encontrado.")

                else:

                    if len(grupo_sel["campers"]) == 0:
                        print("No hay estudiantes en este grupo.")

                    else:
                        print("Estudiantes del grupo:")
                        for i in range(len(grupo_sel["campers"])):
                            camper = grupo_sel["campers"][i]
                            print("ID:", camper["idCamper"],
                                "Nombre: ", camper["nombre"])


                            id_camper = int(input("Escribe el ID del camper a calificar: "))

                            camper_sel = None

                            for i in range(len(grupo_sel["campers"])):
                                if grupo_sel["campers"][i]["idCamper"] == id_camper:
                                    camper_sel = grupo_sel["campers"][i]

                            if camper_sel == None:
                                print("Camper no encontrado.")

                            else:
                                print("Selecciona el modulo:")

                                for i in range(len(grupo_sel["modulos"])):
                                    print(i+1, ".", grupo_sel["modulos"][i]["nombre"])

                                op_mod = int(input("Seleccione modulo: "))
                                modulo_sel = grupo_sel["modulos"][op_mod-1]

                                print("Ingrese las notas:")

                                actividad = float(input("Actividad (10%): "))
                                practica = float(input("Evaluacion practica (60%): "))
                                teorica = float(input("Evaluacion teorica (30%): "))

                                definitiva = (actividad * 0.1) + (practica * 0.6) + (teorica * 0.3)

                                if definitiva >= 80:
                                    riesgo = "BAJO"
                                elif definitiva >= 40:
                                    riesgo = "MEDIO"
                                else:
                                    riesgo = "ALTO"

                                if definitiva >= 60:
                                    estado = "APROBADO"
                                else:
                                    estado = "DESAPROBADO"

                                registro = {
                                    "idCamper": id_camper,
                                    "actividad": actividad,
                                    "practica": practica,
                                    "teorica": teorica,
                                    "definitiva": definitiva,
                                    "riesgo": riesgo,
                                    "estado": estado
                                }

                                modulo_sel["evaluaciones"].append(registro)

                                print("Nota final:", definitiva)
                                print("Riesgo:", riesgo)
                                print("Estado:", estado)

                                guardar_grupos(grupos)


                            print("Nota final:", definitiva)
                            with open("jsons/Grupos.json", "w", encoding="utf-8") as file:
                                json.dump(grupos, file, indent=2, ensure_ascii=False)

                            print("Notas guardadas correctamente.")
        elif opcion == "4":
            print("Saliendo del menu trainer...")
            break
        
        else:
            print("Opcion invalida. Intente nuevamente.")





