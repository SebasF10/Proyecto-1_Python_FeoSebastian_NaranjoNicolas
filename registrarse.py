import json

def registrarse():
    with open("jsons/Campers.json", "r", encoding="utf-8") as file:
        campers = json.load(file)  
    while True:
        print("-------------------------------------------------")
        print("Registro de nuevo Camper")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        gmail = input("Ingrese su  gmail: ")
        
        email_existe = any(camper["gmail"] == gmail for camper in campers)
        if email_existe:
            print(f"Error: El email {gmail} ya está registrado")
            continue
        
        contraseña = input("Ingrese su contraseña: ")
        acudiente = input("Ingrese el nombre del acudiente: ")
        telefono = input("Ingrese su teléfono: ")
        direccion = input("Ingrese su dirección: ")
        grupo = None
        
        if len(campers) == 0:
            nuevo_id = 1
        else:
            ultimo_id = campers[-1]["idCamper"]
            nuevo_id = ultimo_id + 1

        
        # Crear nuevo camper
        nuevo_camper = {
            "idCamper": nuevo_id,
            "rol": "camper",
            "nombre": nombre,
            "apellido": apellido,
            "acudiente": acudiente,
            "gmail": gmail,
            "contraseña": contraseña,
            "telefono": telefono,
            "direccion": direccion,
            "estado": "Proceso de inscripción",
            "riesgo": None,
            "grupo": grupo
        }
        campers.append(nuevo_camper)
        
        # Guardar permanentemente en el archivo JSON
        with open("jsons/Campers.json", "w", encoding="utf-8") as file:
            json.dump(campers, file, indent=2, ensure_ascii=False)
        
        print("--------------------------------------------------")
        print(f"¡Registro exitoso! Bienvenido {nombre} {apellido}")
        print(f"Su ID de camper es: {nuevo_id}")
        print("--------------------------------------------------")
        
        break

    