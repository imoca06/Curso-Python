# Lista de tareas
tareas = []

# Funciones del sistema de gestión de tareas

# Función para agregar una tarea
def agregar_tarea(lista):
    tarea = input("Introduzca la tarea que desea agregar: ")
    lista.append(tarea)
    print("\nTarea agregada correctamente.\n")
    print(f"La tarea {tarea} ha sido agregada correctamente")
    print(f"Tarea agregada correctamente en la posición {len(lista)}\n")

# Función para marcar una tarea como completada
def marcar_como_completada(lista):
    mostrar_tareas(lista)
    tarea = int(input("Introduzca el número de la tarea que desea marcar como completada: "))
    lista[tarea - 1] = lista[tarea - 1] + " (completada)"
    print("Tarea marcada como completada correctamente")

# Función para mostrar las tareas
def mostrar_tareas(lista):
    if len(lista) == 0:
        print("No hay tareas en la lista")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista):
            print(str(i + 1) + ". " + tarea)

# Función para limpiar la pantalla
def limpiar_pantalla(lista):
    lista.clear()
    print("Pantalla limpiada correctamente")

# Función para eliminar una tarea
def eliminar_tarea(lista):
    mostrar_tareas(lista)
    tarea = int(input("Introduzca el número de la tarea que desea eliminar: "))
    del lista[tarea - 1]
    print("Tarea eliminada correctamente")
    


    

