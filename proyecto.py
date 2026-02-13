import json
from pathlib import Path
import getpass
import bcrypt

BASE_DIR = Path(__file__).resolve().parent
USERS_PATH = BASE_DIR / "users.json"


ROLE_MENUS = {
    "camper": [
        ("1", "Ver usuarios"),
        ("2", "Crear usuario"),
        ("3", "Eliminar usuario"),
        ("0", "Salir"),
    ],
    "coordinador": [
        ("1", "Agregar producto"),
        ("2", "Quitar producto"),
        ("3", "Ver menú"),
        ("0", "Salir"),
    ],
    "trainer":[
        (""),
        (""),
        (""),
        ("")
        




    ]
}


def load_users() -> dict:
    if not USERS_PATH.exists():
        return {}
    return json.loads(USERS_PATH.read_text(encoding="utf-8"))


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), password_hash.encode("utf-8"))


def login(users: dict) -> tuple[str, dict] | None:
    usuario = input("Usuario: ").strip()
    password = getpass.getpass("Contraseña: ")

    info = users.get(usuario)
    if not info:
        print("⛔ Usuario o contraseña incorrectos")
        return None

    if not verify_password(password, info["password_hash"]):
        print("⛔ Usuario o contraseña incorrectos")
        return None

    print(f"✅ Bienvenido/a, {usuario} (rol: {info['role']})")
    return usuario, info


def mostrar_menu(role: str) -> str:
    opciones = ROLE_MENUS.get(role)
    if not opciones:
        print("⛔ Rol no tiene menú configurado")
        return "0"

    print("\n=== MENÚ ===")
    for k, label in opciones:
        print(f"{k}. {label}")
    return input("Elige una opción: ").strip()


def ejecutar_opcion(role: str, opcion: str):
    # Aquí conectas tu lógica real
    if role == "admin":
        if opcion == "1":
            print(" (admin) Listando usuarios...")
        elif opcion == "2":
            print(" (admin) Crear usuario...")
        elif opcion == "3":
            print(" (admin) Eliminar usuario...")
    elif role == "coordinador":
        if opcion == "1":
            print("(coord) Agregar producto...")
        elif opcion == "2":
            print(" (coord) Quitar producto...")
        elif opcion == "3":
            print(" (coord) Ver menú...")


def main():
    users = load_users()

    auth = login(users)
    if not auth:
        return

    _, info = auth
    role = info["role"]

    while True:
        opcion = mostrar_menu(role)
        if opcion == "0":
            print("👋 Saliendo...")
            break
        ejecutar_opcion(role, opcion)


if __name__ == "__main__":
    main()






##listado 
ruta= [



]

estado=[




]

horario=[


]

jornada = [

]

campers_en_riesgo=[ ]



from enum import StrEnum
class permiso(StrEnum ):
    agregar_rutas_trainers = "ruta"
    ver_menu = "ver menu"
    cambiar_estado_camper= "estado"
    designar_jornada_camper= "jornada"
    designar__horario_camper= "horario"

##modulo de reportes planta de administracion
    campers_inscritos= "estado registro"
    listado_trainers= "trainers"
    campers_aprobados_EI= ""
#" en base a los modulos si el camper tiene un puntaje <60 esta en alto riesgo"
    campers_alto_riesgo= ""
    advertencia_camper_en_riego= ""

boleanito = True
while boleanito:
    print()
    print()
    print()
    print




