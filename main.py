tareas = []

def mostrar_menu():
    print("\nGESTOR DE TAREAS")
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