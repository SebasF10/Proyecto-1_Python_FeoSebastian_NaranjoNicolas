import json
from crearGrupos import crearGrupos

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
                estado = camper.get("estado", "").lower()
                if estado in ["proceso de ingreso", "proceso de inscripcion", "proceso de inscripción"]:
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
                    camper["estado"] = "Agendada para evaluacion"
                    print("evaluacion agendada correctamente")
                    found = True
                    break
            if not found:
                print("camper no encontrado")
            guardar_campers(campers)
        
        elif opcion == "2":
            print("estudiantes para evaluacion")
            if camper["estado"]== "proceso de ingreso" or camper["Estado"]== "proceso de inscripcion":
                print(camper["Idcamper"], camper["Nombre"])
                print("fecha:", camper["nombre"])

        elif opcion =="3":
            print("asignar grupos a activos")
            if camper ["Estado"]== "activo":
                print(camper["Idcamper"],camper["Nombre"],"grupo:", camper["Grupo"])
                id_buscar= int(input("ingrese el Id del camper:"))
                grupo= input("ingrese el grupo")

            for camper in campers:
                if camper["idCamper"] == id_buscar and camper["estado"] == "Activo":
                    camper["grupo"] = grupo
                    print("Grupo asignado correctamente")

            guardar_campers(campers)

        elif opcion =="4":
            print("editar estado del camper")
            


        elif opcion == "9":
            crearGrupos()

        elif opcion == "10":
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menuCoordinador()
