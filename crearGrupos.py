import json

def crearGrupos():
    print("----- CREAR GRUPO -----")

    with open("jsons/Trainers.json", "r", encoding="utf-8") as file:
        trainers = json.load(file)

    with open("jsons/Grupos.json", "r", encoding="utf-8") as file:
        grupos = json.load(file)

    print("\nProfesores disponibles:")
    for i in range(len(trainers)):
        print(i+1, ".", trainers[i]["nombre"],
              "Horario:", trainers[i]["hora_inicio"],
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

        for i in grupos:
            if i["trainer_id"] == trainer["id"] and i["hora_inicio"] == inicio:
                ocupado = True

        if ocupado == False:
            print(contador, ".", inicio, "-", fin)
            bloques.append((inicio, fin))
        else:
            print(contador, ".", inicio, "-", fin, "(OCUPADO)")

        inicio += 4
        contador += 1

    bloque_hora = int(input("Seleccione bloque: "))
    hora_inicio = bloques[bloque_hora-1][0]
    hora_fin = bloques[bloque_hora-1][1]

    letra = trainer["nombre"][0].upper()
    nombre_grupo = letra + str(bloque_hora)

    print("Rutas disponibles:")
    for i in range(len(trainer["especialidad"])):
        print(i+1, ".", trainer["especialidad"][i])

    ruta_op = int(input("Seleccione ruta: "))
    ruta = trainer["especialidad"][ruta_op-1]

    # Abrir salones
    with open("jsons/Salones.json", "r", encoding="utf-8") as file:
        salones = json.load(file)

    print("\nSalones disponibles:")
    for i in range(len(salones)):
        print(i+1, ".", salones[i]["nombre"])

    salon_op = int(input("Seleccione salon: "))
    salon = salones[salon_op-1]["nombre"]

    # Verificar si salon está ocupado
    for g in grupos:
        if g["salon"] == salon and g["hora_inicio"] == hora_inicio:
            print("Ese salon ya esta ocupado en ese horario.")
            return

    # Crear módulos según ruta
    modulos = []

    modulos.append({"nombre": "Fundamentos", "notas": {}})
    modulos.append({"nombre": "Web", "notas": {}})
    modulos.append({"nombre": "Bases de Datos", "notas": {}})

    if ruta.upper() == "JAVA":
        modulos.append({"nombre": "Backend Java", "notas": {}})
    elif ruta.upper() == "NODEJS":
        modulos.append({"nombre": "Backend NodeJS", "notas": {}})
    elif ruta.upper() == "NETCORE":
        modulos.append({"nombre": "Backend NetCore", "notas": {}})

    print("------------------------------------------------------")

    # Crear grupo
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

    # Guardar cambios
    with open("jsons/Grupos.json", "w", encoding="utf-8") as file:
        json.dump(grupos, file, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")

    print("Grupo creado correctamente!")
    print("Nombre grupo:", nombre_grupo)
    print("Ruta:", ruta)
    print("Horario:", hora_inicio, "-", hora_fin)
    print("Salon:", salon)
    print("_------------------------------------------------------")
