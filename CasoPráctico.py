# Objetos para gestionar una lista de tareas pendientes

# Clase Tarea

class Tarea:
    def __init__(self, id_tarea, nombre):
        self.id_tarea = id_tarea
        self.nombre = nombre
    

    def __str__(self):
        return f"{self.nombre} - {self.id_tarea}"

# Clase GestorTareas

class GestorTareas:
    def __init__(self):
        self.tareas = {}

        # Agregar tareas

    def agregar_tarea(self, tarea):
        self.tareas[tarea.id_tarea] = tarea
        print(f"Tarea agregada - ID: {tarea.id_tarea}, Nombre: {tarea.nombre}")
        # Imprime Tarea agregada - ID: x , Nombre: xxx

        # Marcar tarea como completada

    def marcar_completada(self, id_tarea):
        if id_tarea in self.tareas:
            self.tareas[id_tarea].completada = True
            print(f"Tarea con ID {id_tarea} marcada como completada.") # Imprime Tarea con ID x marcada como completada.
        else:
            print("No se encontró la tarea con ese ID.") # Imprime No se encontró la tarea con ese ID.

        # Mostrar todas las tareas
    def mostrar_tareas(self):
            print("Tareas:") # Imprime Tareas:
            for id_tarea, tarea in self.tareas.items():
                print(tarea) # Imprime tarea
          
        # Borrar tareas

    def borrar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            del self.tareas[id_tarea]
            print(f"Tarea con ID {id_tarea} borrada.") # Imprime Tarea con ID x borrada.
        else:
            print("No se encontró la tarea con ese ID.") # Imprime No se encontró la tarea con ese ID.

    

# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()
    
    # Agregar tareas
    print("Tareas agregadas:")
    tarea1 = Tarea(1, "Pasear")
    tarea2 = Tarea(2, "Comprar pan")
    tarea3 = Tarea(3, "Tomar aperitivo")
    tarea4 = Tarea(4, "Comer")
    tarea5 = Tarea(5, "Recoger")
    tarea6 = Tarea(6, "Jugar coches")
   

    gestor.agregar_tarea(tarea1)
    gestor.agregar_tarea(tarea2)
    gestor.agregar_tarea(tarea3)
    gestor.agregar_tarea(tarea4)
    gestor.agregar_tarea(tarea5)
    gestor.agregar_tarea(tarea6)

    # Marcar tarea como completada
    print("\nTareas completadas:")  
    gestor.marcar_completada(2)
    gestor.marcar_completada(4)
    gestor.marcar_completada(6)
  
    



    









