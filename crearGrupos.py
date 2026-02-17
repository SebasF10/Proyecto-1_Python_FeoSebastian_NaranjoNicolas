import json
from datetime import datetime, date
import calendar


def crearGrupos():
    print("----- CREAR GRUPO -----")

    with open("jsons/Trainers.json", "r", encoding="utf-8") as file:
        trainers = json.load(file)

    with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
        grupos = json.load(file)

    print("Profesores disponibles:")
    for i in range(len(trainers)):
        print(i+1, ".", trainers[i]["nombre"],
              "Horario: ", trainers[i]["hora_inicio"], 
              "-", trainers[i]["hora_fin"])

    profe_input = input("Seleccione profesor: ")
    try:
        profe = int(profe_input)
    except (ValueError, TypeError):
        print("Selección inválida. Operación cancelada.")
        return

    if profe < 1 or profe > len(trainers):
        print("Profesor inválido.")
        return

    trainer = trainers[profe-1]

    print("Bloques disponibles:")

    bloques = []
    inicio = trainer["hora_inicio"]
    contador = 1

    while inicio < trainer["hora_fin"]:
        fin = inicio + 4
        ocupado = False

        for i in grupos:
            if i["trainer_id"] == trainer["id"] and i["hora_inicio"] == inicio:
                ocupado = True
                break

        if not ocupado:
            print(contador, ".", inicio, "-", fin)
            bloques.append((inicio, fin))
        else:
            print(contador, ".", inicio, "-", fin, "(OCUPADO)")

        inicio += 4
        contador += 1

    if len(bloques) == 0:
        print("Este profesor no tiene horarios disponibles.")
        return

    bloque_hora = int(input("Seleccione bloque disponible: "))

    if bloque_hora < 1 or bloque_hora > len(bloques):
        print("Bloque inválido.")
        return

    hora_inicio = bloques[bloque_hora-1][0]
    hora_fin = bloques[bloque_hora-1][1]

    if "especialidad" not in trainer or not trainer["especialidad"]:
        print("Este profesor no tiene especialidades registradas.")
        return
    

    letra = trainer["nombre"][0].upper()
    nombre_grupo = letra + str(bloque_hora)

    print("Rutas disponibles:")
    for i in range(len(trainer["especialidad"])):
        print(i+1, ".", trainer["especialidad"][i])

    ruta_op = int(input("Seleccione ruta: "))
    ruta = trainer["especialidad"][ruta_op-1]


    with open("jsons/Salones.json", "r", encoding="utf-8") as file:
        salones = json.load(file)

    print("Salones disponibles:")
    for i in range(len(salones)):
        print(i+1, ".", salones[i]["nombre"])

    salon_op = int(input("Seleccione salon: "))
    salon = salones[salon_op-1]["nombre"]

    for i in grupos:
        if i.get("idGrupo") == nombre_grupo:
            print("Ya existe un grupo con ese id:", nombre_grupo)
            return

    modulos = [
    {"nombre": "Fundamentos", "evaluaciones": []},
    {"nombre": "Web", "evaluaciones": []},
    {"nombre": "Bases de Datos", "evaluaciones": []}
    ]

    nombre_backend = f"Backend {ruta.strip().title()}"
    modulos.append({"nombre": nombre_backend, "evaluaciones": []})

    if hora_inicio < 12:
        jornada = "Mañana"
    else:
        jornada = "Tarde"

    fecha_inicio_str = input("Ingrese fecha de inicio (año/mes/dia): ")
    try:
        fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y/%m/%d").date()
    except ValueError:
        print("Formato de fecha inválido. Use año/mes/dia (ej: 2026/02/16).")
        return

    def add_10_months(d: date) -> date:
        m = d.month + 10
        y = d.year + (m - 1) // 12
        m = (m - 1) % 12 + 1
        day = min(d.day, calendar.monthrange(y, m)[1])
        return date(y, m, day)

    fecha_fin = add_10_months(fecha_inicio)
    # Guardar fechas como strings para que json.dump las serialice correctamente
    fecha_inicio1 = fecha_inicio.strftime("%Y-%m-%d")
    fecha_fin1 = fecha_fin.strftime("%Y-%m-%d")

    

    nuevo_grupo = {
        "idGrupo": nombre_grupo,
        "trainer_id": trainer["id"],
        "ruta": ruta,
        "salon": salon,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "jornada": jornada,
        "fecha_inicio": fecha_inicio1,
        "fecha_fin": fecha_fin1,
        "estado": "Planeado",
        "campers": [],
        "modulos": modulos
    }

    grupos.append(nuevo_grupo)

    with open("jsons/Grupos.json", "w", encoding="utf-8") as file:
        json.dump(grupos, file, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print("Grupo creado correctamente!")
    print("Nombre grupo:", nombre_grupo)
    print("Ruta:", ruta)
    print("Horario:", hora_inicio, "-", hora_fin)
    print("Salon:", salon)
    print("------------------------------------------------------")
