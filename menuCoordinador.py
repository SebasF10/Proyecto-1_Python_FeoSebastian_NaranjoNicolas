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
        print("1. Agendar estudiantes a evaluacion de ingreso")
        print("2. Estudiantes para evalucion de ingreso")
        print("3. Asignar grupos a estudiantes Activos")
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

                    camper["evaluacion de ingreso"]["nota"]=nota

                    if nota >40:
                        print("El estudiante aprobo la prueba")
                        camper["evaluacion de ingreso"]["resultado"]="aprobado"
                        camper["estado"] = "aprobado"
                    else:
                        print("El estudiante reprobo la prueba")
                        print("El estudiante tendra que volver a presentarla")
                        camper["evalucion de ingreso"]["resultado"]="reprobado"




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

            # buscar camper por id
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

            # asignar grupo y agregar al grupo si no está ya
            camper_encontrado["grupo"] = grupo_encontrado.get("idGrupo")
            if "campers" not in grupo_encontrado or grupo_encontrado["campers"] is None:
                grupo_encontrado["campers"] = []

            existe_grupo = any(c.get("idCamper") == camper_encontrado.get("idCamper") for c in grupo_encontrado["campers"])
            if not existe_grupo:
                grupo_encontrado["campers"].append({
                    "idCamper": camper_encontrado.get("idCamper"),
                    "nombre": camper_encontrado.get("nombre")
                })

            guardar_campers(campers)
            guardar_grupos(grupos)
            print("grupo asignado correctamente")

        


