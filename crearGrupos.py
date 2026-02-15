import json

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

    profe = int(input("Seleccione profesor: "))
    trainer = trainers[profe-1]

    print("Bloques disponibles:")

    bloques = []
    inicio = trainer["hora_inicio"]
    contador = 1

    while inicio < trainer["hora_fin"]:
        fin = inicio + 4
        ocupado = False

        for g in grupos:
            if g["trainer_id"] == trainer["id"] and g["hora_inicio"] == inicio:
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

    for g in grupos:
        if g.get("idGrupo") == nombre_grupo:
            print("Ya existe un grupo con ese id:", nombre_grupo)
            return

    # validar especialidades
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

    for g in grupos:
        if g["salon"] == salon and g["hora_inicio"] == hora_inicio:
            print(" Ese salon ya esta ocupado en ese horario.")
            return

    modulos = [
    {"nombre": "Fundamentos", "evaluaciones": []},
    {"nombre": "Web", "evaluaciones": []},
    {"nombre": "Bases de Datos", "evaluaciones": []}
    ]

    nombre_backend = f"Backend {ruta.strip().title()}"
    modulos.append({"nombre": nombre_backend, "evaluaciones": []})

    nuevo_grupo = {
        "idGrupo": nombre_grupo,
        "trainer_id": trainer["id"],
        "ruta": ruta,
        "salon": salon,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
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
