tareas = []


def mostrar_menu():
    print("\nSISTEMA DE GESTIÓN DE TAREAS DEL EQUIPO")
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
    print("Tarea agregada correctamente.")


def listar_tareas():
    if len(tareas) == 0:
        print("No existen tareas.")
        return

    for tarea in tareas:
        print("Tarea:", tarea["nombre"])
        print("Completada:", tarea["completada"])


def mostrar_progreso():
    total = len(tareas)

    if total == 0:
        print("Sin tareas")
        return

    completadas = 0

    for tarea in tareas:
        if tarea["completada"]:
            completadas += 1

    porcentaje = completadas * 100 / total

    print("Progreso:", porcentaje, "%")


while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()

    elif opcion == "2":
        listar_tareas()

    elif opcion == "3":
        mostrar_progreso()

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida.")