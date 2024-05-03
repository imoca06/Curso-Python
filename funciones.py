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
    try:
        tarea = int(input("Introduzca el número de la tarea que desea marcar como completada: "))
        if tarea > len(lista):
            print("Número de tarea no válido")
            return
        if tarea <= 0:
            print("Número de tarea no válido")
            return
        if lista[tarea - 1] == "Completada":
            print("La tarea ya está completada")
            return
        lista[tarea - 1] = "Completada"
        print("Tarea marcada como completada correctamente")
    except ValueError:
        print("El número de tarea a modificar debe ser un número entero mayor de 0")
        return
    
# Función para mostrar las tareas
def mostrar_tareas(lista):
    if len(lista) == 0:
        print("No hay tareas en la lista")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista):
            print(str(i + 1) + ". " + tarea)

# Función para eliminar una tarea
def eliminar_tarea(lista):
    mostrar_tareas(lista)
    if len(lista) == 0:
        print("No hay tareas en la lista")
        return
    try:
        tarea = int(input("Introduzca el número de la tarea que desea eliminar: "))
        if tarea > 0 and tarea <= len(lista):
            lista.pop(tarea - 1)
            print("Tarea eliminada correctamente")
        else:
            print("Número de tarea no válido")
    except ValueError:
        print("El número de tarea a borrar debe ser un número entero mayor de 0")
        

# Función para limpiar la pantalla
def limpiar_pantalla(lista):
    lista.clear()
    print("Pantalla limpiada correctamente")

# Fin del módulo funciones.py

# Fin del programa