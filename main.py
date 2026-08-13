tareas = []

def mostrar_menu():
    print("SISTEMA DE GESTIÓN DE TAREAS DEL EQUIPO")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Mostrar progreso")
    print("4. Salir")


def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    tarea = {
        "nombre": nombre,
        "completada": False
    }
    tareas.append(tarea)

def listar_tareas():
    for tarea in tareas:
        print("Tarea:", tarea["nombre"])
        print("Completada:", tarea["completada"])

