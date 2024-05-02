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

    def agregar_tarea(self, tarea):
        self.tareas[tarea.id_tarea] = tarea

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

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            for tarea_id, tarea in self.tareas.items():
                print(f"ID: {tarea_id}, {tarea}")

    def borrar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            del self.tareas[id_tarea]
            print(f"Tarea con ID {id_tarea} borrada.")
        else:
            print("No se encontró la tarea con ese ID.")

# Función para mostrar el menú
def mostrar_menu():
    print("1. Agregar tarea")
    print("2. Completar tarea")
    print("3. Mostrar tareas")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("6. Limpiar pantalla")

# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()

    while True:
        mostrar_menu()
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
        elif opcion == "5":
            print("¡Hasta luego!")
        elif opcion == "6":
            import os
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
