# Objetos para gestionar una lista de tareas pendientes

# Clase Tarea
class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre} - {self.prioridad}"
# Clase lista de tareas
class ListaTareas:
    # Agregar tarea
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    # Marcar tarea como completada
    def marcar_completada(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                self.tareas.remove(tarea)
                break
    # Mostrar tareas
    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea)
    # Eliminar tarea
    def eliminar_tarea(self, nombre):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                self.tareas.remove(tarea)
                break
    

