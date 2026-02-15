import json
from crearGrupos import crearGrupos

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


def menuCoordinador():
    campers = cargar_campers()
    while True:
        print("-----------------------------------------------")
        print("Bienvenido que es lo que quieres hacer?")
        print("1.Agendar estudiantes a evaluacion de ingreso")
        print("2.Estudiantes para evalucion de ingreso")
        print("3.Asignar grupos a estudiantes Activos")
        print("4.Editar estado de estudiantes Activos")
        print("5.Resultados de examenes de ingreso ")
        print("6.Agregar rutas nuevas a trainer")
        print("7.Lista de calificaciones de los cursos")
        print("8.Modulo de reportes")
        print("9.Crear Grupo")
        print("10. Salir")
        print("-----------------------------------------------")
        opcion = input("Ingrese el numero de la opcion que desea: ")

        if opcion == "1":
            print("Agendar estudiantes a evaluacion de ingreso")
            for camper in campers:
                estado = camper.get("estado")
                if estado in ["proceso de ingreso"]:
                    print(camper.get("idCamper"), camper.get("nombre"), camper.get("estado"))

            try:
                id_buscar = int(input("ingrese id del camper: "))
            except ValueError:
                print("ID inválido")
                continue

            found = False
            for camper in campers:
                if camper.get("idCamper") == id_buscar:
                    fecha = input("ingrese fecha de evaluacion: ")
                    jornada = input("ingrese jornada de evaluacion: ")
                    if not camper.get("evaluacionIngreso"):
                        camper["evaluacionIngreso"] = {"fecha": None, "nota": None, "resultado": None, "jornada": None}
                    camper["evaluacionIngreso"]["fecha"] = fecha
                    camper["evaluacionIngreso"]["jornada"] = jornada
                    camper["estado"] = "inscrito"
                    print("evaluacion agendada correctamente")
                    found = True
                    break
            if not found:
                print("camper no encontrado")
            guardar_campers(campers)
        
        elif opcion == "2":
            print("estudiantes para evaluacion")
            for camper in campers:
                if camper["estado"] == "inscrito":
                    print(camper["idCamper"], camper["nombre"])
                    print("fecha:", camper["evaluacionIngreso"]["fecha"])

            id_buscar=int(input("ingrese el id del esrudiante:"))
            for camper in campers:
                if camper["idCamper"] == id_buscar:

                    nota=int(input("ingresa la puntuacion que obtuvo el estudiante (0-100)"))

                    camper["evaluacionIngreso"]["nota"]=nota

                    if nota >40:
                        print("El estudiante aprobo la prueba")
                        camper["evaluacionIngreso"]["resultado"]="aprobado"
                        camper["estado"] = "aprobado"
                    else:
                        print("El estudiante reprobo la prueba")
                        print("El estudiante tendra que volver a presentarla")
                        camper["evaluacionIngreso"]["resultado"]="reprobado"




        elif opcion == "3":
            print("Asignar grupos a activos")

            grupos = cargar_grupos()

            aprobados = [i for i in campers if i.get("estado") == "aprobado"]
            if not aprobados:
                print("No hay campers aprobados.")
                continue

            for i in aprobados:
                print(i.get("idCamper"), i.get("nombre"), "grupo:", i.get("grupo"))
            if not grupos:
                print("No hay grupos creados.")
                continue

            print("Grupos disponibles:")
            for g in grupos:
                print(g.get("idGrupo"), "-", g.get("ruta"), "-", g.get("estado"))
            try:
                id_buscar = int(input("ingrese el Id del camper: ").strip())
            except ValueError:
                print("ID inválido")
                continue

            grupo = input("ingrese el grupo: ").strip()
            if grupo == "":
                print("grupo invalido (vacio)")
                continue

            grupo_encontrado = None
            for i in grupos:
                if i.get("idGrupo") == grupo:
                    grupo_encontrado = i
                    break

            if grupo_encontrado is None:
                print("no existe ese grupo con ese id")
                continue

            camper_encontrado = None
            for camper in campers:
                if camper.get("idCamper") == id_buscar:
                    camper_encontrado = camper
                    break

            if camper_encontrado is None:
                print("camper no encontrado")
                continue

            if camper_encontrado.get("estado") != "aprobado":
                print("el id existe, pero el camper no esta aprobado")
                continue
                

            # asignar grupo
            camper_encontrado["grupo"] = grupo_encontrado.get("idGrupo")
           
            camper_encontrado["estado"] = "cursando"

            guardar_campers(campers)
            guardar_grupos(grupos)
            print("grupo asignado correctamente")


        elif opcion == "4":
            print("Editar estado de estudiantes activos")
            hay_activos = False
            for camper in campers:
                if camper["estado"] == "cursando ":
                    print(camper["idCamper"], camper["nombre"], "estado:", camper["estado"])
                    hay_activos = True
            if not hay_activos:
                print("No hay campers activos.")
            else:
                    try:
                        id_buscar = int(input("ingrese el Id del camper: ").strip())
                    except ValueError:
                        print("id invalido")
                        continue
                    nuevo_estado = input("ingrese el nuevo estado: ").strip()
                    if nuevo_estado == "":
                        print("estado invalido (vacio)")
                    else:
                        camper_encontrado = None
                        for camper in campers:
                            if camper.get("idCamper") == id_buscar:
                                camper_encontrado = camper
                            break
                    if camper_encontrado is None:
                        print("camper no encontrado")
                    else:
                        camper_encontrado["estado"] = nuevo_estado
                        guardar_campers(campers)
                        print("estado actualizado correctamente")

        elif opcion == "5":
            print("resultados de examenes de ingreso")
            for camper in campers:
                if camper.get("evaluacionIngreso"):
                    print(camper["idCamper"], camper["nombre"])
                    print("fecha:", camper["evaluacionIngreso"]["fecha"])
                    print("nota:", camper["evaluacionIngreso"]["nota"])
                    print("resultado:", camper["evaluacionIngreso"]["resultado"])
                    print("-----------------------------------")
                    
        elif opcion == "6":
            print("agregar especialidad nueva a trainer")
            with open("jsons/Trainers.json", "r", encoding="utf-8") as file:
                trainers = json.load(file)
                for trainer in trainers:
                    print(trainer["id"], trainer["nombre"])
                id_trainer = input("Ingrese el ID del trainer al que desea agregar la especialidad: ")
                trainer_encontrado = None
                for trainer in trainers:
                    if str(trainer["id"]) == id_trainer:
                        trainer_encontrado = trainer
                        break
                if trainer_encontrado is None:
                    print("Trainer no encontrado.")
                else:
                    nueva_ruta = input("Ingrese el nombre de la nueva especialidad: ")
                    if "especialidad" not in trainer_encontrado:
                        trainer_encontrado["especialidad"] = []
                    trainer_encontrado["especialidad"].append(nueva_ruta)
                    with open("jsons/Trainers.json", "w", encoding="utf-8") as file:
                        json.dump(trainers, file, indent=4, ensure_ascii=False)
                    print("especialidad agregada correctamente al trainer.")

        elif opcion == "8":
            print("-----------------------------------")
            print("1. ")
            print("2. ")
            print("3. ")
            print("4. ")
            print("-----------------------------------")
            opcion_reportes = input("Ingrese el numero de la opcion que desea: ")

        elif opcion == "9":
            print("------------------------------------")
            crearGrupos()
        
        elif opcion == "10":
            print("Saliendo del programa...")
            break


        


