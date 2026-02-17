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

with open ("jsons/Trainers.json", "r", encoding="utf-8") as file:
    trainers = json.load(file)


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

            grupo_encontrado["estado"] = "activo"

            guardar_campers(campers)
            guardar_grupos(grupos)
            print("grupo asignado correctamente")


        elif opcion == "4":
            print("Editar estado de estudiantes activos")
            hay_activos = False
            for camper in campers:
                if camper["estado"] == "cursando":
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

        elif opcion == "7":
            print("Lista de calificaciones de los cursos")
            with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
                grupos = json.load(file)

            for grupo in grupos:
                print("-----------------------------------")
                print(grupo.get("idGrupo"), grupo.get("ruta"))

                hay_calificaciones = False

                for modulo in grupo.get("modulos", []):
                    for ev in modulo.get("evaluaciones", []):
                        hay_calificaciones = True
                        print("Módulo:", modulo.get("nombre"))
                        print("  Camper ID:", ev.get("idCamper"),
                            "| Definitiva:", ev.get("definitiva"),
                            "| Estado:", ev.get("estado"),
                            "| Riesgo:", ev.get("riesgo"))

                if not hay_calificaciones:
                    print("No hay calificaciones registradas para este grupo.")
        elif opcion == "8":
            with open("jsons/Trainers.json", "r", encoding="utf-8") as file:
                trainers = json.load(file)
            
            print("-----------------------------------")
            print("1.campers y trainers que se encuentren asociados a una ruta")
            print("2.Mostrar cuantos campers perdieron y aprobaron cada uno de los " \
            "módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado ")
            print("3.ver los estudiantes en alto riesgo puntaje en modulo < 60 ")
            print("4.un llamado de atencion al estudiante por su puntaje en ese modulo ")
            print("5.Crear Trainers nuevos")
            print("6.cambio de estado de  estudiantes")
            print("7.salir del modulo de reportes-")
            print("-----------------------------------")
            opcion_reportes = input("Ingrese el numero de la opcion que desea: ")

            if opcion_reportes == "1":
                with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
                    grupos = json.load(file)
                with open("jsons/Trainers.json", "r", encoding="utf-8") as file:
                    trainers = json.load(file)
            
                for grupo in grupos:
                    print("-----------------------------------")
                    print("Grupo ID:", grupo.get("idGrupo"))
                    print("Ruta:", grupo.get("ruta"))
                    trainer_nombre = "No asignado"
                    for trainer in trainers:
                        if trainer["id"] == grupo.get("trainer_id"):
                            trainer_nombre = trainer["nombre"]
                            break

                    print("Trainer:", trainer_nombre)

                    print("Campers asociados:")
                    for camper in grupo.get("campers", []):
                        print(f"  - {camper['nombre']} (ID: {camper['idCamper']})")

            elif opcion_reportes == "2":
                with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
                    grupos = json.load(file)
                for grupo in grupos:
                    print("-----------------------------------")
                    print("Grupo ID:", grupo.get("idGrupo"))
                    print("Ruta:", grupo.get("ruta"))
                    aprobados = 0
                    reprobados = 0
                    for modulo in grupo.get("modulos", []):
                        for ev in modulo.get("evaluaciones", []):
                            if ev.get("definitiva", 0) >= 60:
                                aprobados += 1
                            else:
                                reprobados += 1
                    print(f"Aprobados: {aprobados} | Reprobados: {reprobados}")

            elif opcion_reportes == "3":
                with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
                    grupos = json.load(file)
                print("Estudiantes en alto riesgo (definitiva < 60):")
                for grupo in grupos:
                    for modulo in grupo.get("modulos", []):
                        for ev in modulo.get("evaluaciones", []):
                            if ev.get("definitiva", 0) < 60:
                                print(f"Camper ID: {ev.get('idCamper')} | Módulo: {modulo.get('nombre')} | Definitiva: {ev.get('definitiva')}")
           
            elif opcion_reportes == "4":
                with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
                    grupos = json.load(file)
                
                print("Estudiantes en alto riesgo (definitiva < 60):")
                print("-----------------------------------")
                
                estudiantes_riesgo = []
                for grupo in grupos:
                    for modulo in grupo.get("modulos", []):
                        for ev in modulo.get("evaluaciones", []):
                            if ev.get("definitiva", 0) < 60:
                                estudiantes_riesgo.append({
                                    "idCamper": ev.get("idCamper"),
                                    "modulo": modulo.get("nombre"),
                                    "definitiva": ev.get("definitiva"),
                                    "grupo": grupo.get("idGrupo")
                                })
                
                if not estudiantes_riesgo:
                    print("No hay estudiantes en alto riesgo.")
                else:
                    for i, est in enumerate(estudiantes_riesgo, 1):
                        print(f"{i}. Camper ID: {est['idCamper']} | Módulo: {est['modulo']} | Definitiva: {est['definitiva']}")
                    
                    try:
                        opcion_est = int(input("Seleccione el número del estudiante para crear el reporte: "))
                        if opcion_est < 1 or opcion_est > len(estudiantes_riesgo):
                            print("Opción inválida")
                        else:
                            est_seleccionado = estudiantes_riesgo[opcion_est - 1]
                            
                            for camper in campers:
                                if camper["idCamper"] == est_seleccionado["idCamper"]:
                                    fecha = input("Ingrese la fecha del reporte (ej: 17/02/2026): ")
                                    asunto = f"Llamado de atención - Módulo {est_seleccionado['modulo']}"
                                    descripcion = f"El estudiante obtuvo una calificación de {est_seleccionado['definitiva']} en el módulo {est_seleccionado['modulo']}. Se recomienda mejorar el desempeño para evitar riesgos académicos. "
                                    observaciones = input("Ingrese observaciones adicionales: ")
                                    
                                    descripcion_final = f"Calificación en {est_seleccionado['modulo']}: {est_seleccionado['definitiva']}. Observaciones: {observaciones}"
                                    
                                    nuevo_reporte = {
                                        "fecha": fecha,
                                        "asunto": asunto,
                                        "descripcion": descripcion_final,
                                        "coordinador": "Coordinador",
                                        "tipo": "Llamado de atención"
                                    }
                                    
                                    if "reportes" not in camper:
                                        camper["reportes"] = []
                                    
                                    camper["reportes"].append(nuevo_reporte)
                                    guardar_campers(campers)
                                    print(f"Reporte de atención creado exitosamente para Camper ID: {camper['idCamper']}")
                                    break
                    except ValueError:
                        print("Entrada inválida. Ingrese un número válido.")
            
            elif opcion_reportes == "5":
                print("Crear Trainers nuevos")
                print("------------------------------------------------------------------------------------------")
                nombre = input("Ingrese el nombre del nuevo trainer: ")
                gmail = input("Ingrese el correo electrónico del nuevo trainer: ")
                contraseña = input("Ingrese la contraseña del nuevo trainer: ")
                hora_inicio = input("Ingrese la hora de inicio de disponibilidad (Horario militar de (0 a 24)): ")
                hora_fin = input("Ingrese la hora de fin de disponibilidad (Horario militar de (0 a 24)): ")
                repito = int(input("Cuantas especialidades tiene el trainer? "))
                for i in range(repito):
                    especialidad = input("Ingrese la especialidad del nuevo trainer: ")
                rol = "Trainer"

                nuevo_trainer = {
                    "id": len(trainers) + 1,
                    "nombre": nombre,
                    "gmail": gmail,
                    "contraseña": contraseña,
                    "hora_inicio": hora_inicio,
                    "hora_fin": hora_fin,
                    "especialidad": [especialidad],
                    "rol": rol
                }
                trainers.append(nuevo_trainer)
                with open("jsons/Trainers.json", "w", encoding="utf-8") as file:
                    json.dump(trainers, file, indent=4, ensure_ascii=False)

                print("Trainer creado exitosamente")
                print("-------------------------------------------------------------------------------------------")
                
            elif opcion_reportes == "6":
                print("Cambio de estado de estudiantes")
                print("-----------------------------------")
                
                # Mostrar lista numerada de estudiantes
                print("Seleccione el estudiante:")
                for index, camper in enumerate(campers, 1):
                    print(f"{index}. {camper['nombre']} (ID: {camper['idCamper']}) - Estado: {camper['estado']}")
                
                try:
                    opcion_estudiante = int(input("Ingrese el número del estudiante: "))
                    if opcion_estudiante < 1 or opcion_estudiante > len(campers):
                        print("Opción inválida")
                        continue
                    
                    camper_seleccionado = campers[opcion_estudiante - 1]
                    
                    # Mostrar lista de estados posibles
                    print("Seleccione el nuevo estado:")
                    estados_disponibles = ["proceso de ingreso", "inscrito", "aprobado", "cursando", "egresado", "retirado","Expulsado"]
                    for index, estado in enumerate(estados_disponibles, 1):
                        print(f"{index}. {estado}")
                    
                    opcion_estado = int(input("Ingrese el número del estado: "))
                    if opcion_estado < 1 or opcion_estado > len(estados_disponibles):
                        print("Opción de estado inválida")
                        continue
                    
                    nuevo_estado = estados_disponibles[opcion_estado - 1]
                    
                    # Actualizar estado
                    camper_seleccionado["estado"] = nuevo_estado
                    guardar_campers(campers)
                    print(f"Estado actualizado correctamente a '{nuevo_estado}' para {camper_seleccionado['nombre']}")
                    
                except ValueError:
                    print("Entrada inválida. Ingrese un número válido.")

            elif opcion_reportes == "7":
                print("Saliendo del módulo de reportes...")
                break
            

        elif opcion == "9":
            print("------------------------------------")
            crearGrupos()
        
        elif opcion == "10":
            print("Saliendo del programa...")
            break


        


