
# Autor: Isidro M. @imoca06
# Fecha: 2024/05/03

# POO que gestionará una lista de tareas pendientes
# Cada tarea se podrá agregar, marcar como completada, mostrar y eliminar

import os
import funciones 

# Bucle principal
while True:
    
    # Menu de opciones
    print("\n ***** Bienvenido al Sistema de Gestión de Tareas *****\n")
    print("1. Agregar tarea")
    print("2. Marcar como completada")
    print("3. Mostrar tareas")
    print("4. Eliminar tarea")
    print("5. Limpiar pantalla")
    print("6. Salir")



    print("\n")

    # Entrada de datos para seleccionar una opción
    opcion = input("Introduzca una opción: ")
    print("\n")

    # Menu de opciones
    if opcion == "1":
        funciones.agregar_tarea(funciones.tareas)
    elif opcion == "2":
        funciones.marcar_como_completada(funciones.tareas)
    elif opcion == "3": 
        funciones.mostrar_tareas(funciones.tareas)
    elif opcion == "4": 
        funciones.eliminar_tarea(funciones.tareas)
    elif opcion == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nPantalla limpiada correctamente\n")
    elif opcion == "6":
        print("\nGracias por utilizar el sistema de gestión de tareas. ¡Hasta pronto!\n")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo")

# Fin del programa