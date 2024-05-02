# Autor: Isidro M. @imoca06
# Fecha: 2024/05/02

# POO que gestionará una lista de tareas pendientes
# Cada tarea tendrá un ID y un nombre

import os

# Clase Tarea

class Tarea:
    def __init__(self, id_tarea, nombre):
        self.id_tarea = id_tarea
        self.nombre = nombre
        self.completada = False
    
    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.nombre} - {estado}"

# Clase GestorTareas

class GestorTareas:
    def __init__(self):
        self.tareas = {}
                   
        # Agregar tareas
    def agregar_tarea(self, tarea):        
        self.tareas[tarea.id_tarea] = tarea

        # Marcar tarea como completada
    def marcar_completada(self, id_tarea):
        tarea = self.tareas.get(id_tarea)
        if tarea:
            if not tarea.completada:
                tarea.completada = True
                print(f"Tarea con ID {id_tarea} marcada como completada.")
            else:
                print(f"Tarea con ID {id_tarea} ya estaba completada.")
        else:
            print("No se encontró la tarea con ese ID.")

        # Mostrar todas las tareas
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.") # Imprime No hay tareas. 
        else:
            for tarea_id, tarea in self.tareas.items():
                print(f"ID: {tarea_id}, {tarea}") # Imprime tarea

        # Borrar tareas
    def borrar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            del self.tareas[id_tarea]
            print(f"Tarea con ID {id_tarea} borrada.") # Imprime Tarea con ID x borrada.
        else:
            print("No se encontró la tarea con ese ID.") # Imprime No se encontró la tarea con ese ID.

# Funcion para mostrar el menu

def mostrar_menu():
    print("1. Agregar tarea") # Imprime 1. Agregar tarea
    print("2. Completar tarea") # Imprime 2. Completar tarea
    print("3. Mostrar tareas") # Imprime 3. Mostrar tareas
    print("4. Eliminar tarea") # Imprime 4. Eliminar tarea
    print("5. Limpiar pantalla") # Imprime 5. Limpiar pantalla y se borra la pantalla
    print("6. Salir") # Imprime 6. Salir

# Ejemplo de uso

if __name__ == "__main__":
    gestor = GestorTareas()

    while True: # Mientras sea verdadero
        mostrar_menu() # Muestra el menu
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            id_tarea = int(input("Introduce el ID de la tarea: "))
            nombre = input("Introduce la descripción de la tarea: ")
            tarea = Tarea(id_tarea, nombre)
            gestor.agregar_tarea(tarea)
        elif opcion == "2":
            id_tarea = int(input("Introduce el ID de la tarea que quieres marcar como completada: "))
            gestor.marcar_completada(id_tarea)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            id_tarea = int(input("Introduce el ID de la tarea que quieres eliminar: "))
            gestor.borrar_tarea(id_tarea)
        # Si la opcion es 5 # limpia la pantalla
        elif opcion == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
        # Si la opcion es 6 # Salir
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        # Si la opcion no es ninguna de las anteriores
        else:
            print("Opción no válida. Inténtelo de nuevo")

# Fin del programa