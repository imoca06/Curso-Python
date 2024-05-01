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

        # Lista de tareas
    def lista_tareas(self, tarea):
        self.tareas[tarea.id_tarea] = tarea
        print(f"ID: {tarea.id_tarea}, Nombre: {tarea.nombre}") # Imprime ID: x , Nombre: xxx

        # Agregar tareas

    def agregar_tarea(self, tarea):        
        self.tareas[tarea.id_tarea] = tarea
        print(f"ID: {tarea.id_tarea}, Nombre: {tarea.nombre}") # Imprime ID: x , Nombre: xxx

        # Marcar tarea como completada

    def marcar_completada(self, id_tarea):
        if id_tarea in self.tareas:
            self.tareas[id_tarea].completada = True
            print(f"Tarea con ID {id_tarea} marcada como completada.") # Imprime Tarea con ID x marcada como completada.
        else:
            print("No se encontró la tarea con ese ID.") # Imprime No se encontró la tarea con ese ID.

        # Mostrar todas las tareas
    def mostrar_tareas(self):            
            for id_tarea, tarea in self.tareas.items():
                print(tarea) # Imprime tarea
          
        # Borrar tareas

    def borrar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            del self.tareas[id_tarea]
            print(f"Tarea con ID {id_tarea} borrada.") # Imprime Tarea con ID x borrada.
        else:
            print("No se encontró la tarea con ese ID.") # Imprime No se encontró la tarea con ese ID.

        # Buscar tareas borradas

    def buscar_tareas_borradas(self):
              for id_tarea, tarea in self.tareas.items():
                print(tarea) # Imprime tarea


    

# Ejemplo de uso

if __name__ == "__main__":
    gestor = GestorTareas()

    # Lista de tareas
    print("\nLista de tareas:") # Imprime Lista de tareas:
    tarea1 = Tarea(1, "Pasear")
    tarea2 = Tarea(2, "Comprar pan")
    tarea3 = Tarea(3, "Comer")
    tarea4 = Tarea(4, "Recoger")
    tarea5 = Tarea(5, "Jugar coches")
    tarea6 = Tarea(6, "Parquear")
    tarea7 = Tarea(7, "Duchar")
    tarea8 = Tarea(8, "Cenar")
    tarea9 = Tarea(9, "Jugar")
    tarea10 = Tarea(10, "Dormir")

    
    gestor.lista_tareas(tarea1)
    gestor.lista_tareas(tarea2)
    gestor.lista_tareas(tarea3)
    gestor.lista_tareas(tarea4)
    gestor.lista_tareas(tarea5)
    gestor.lista_tareas(tarea6)
    gestor.lista_tareas(tarea7)
    gestor.lista_tareas(tarea8)
    gestor.lista_tareas(tarea9)
    gestor.lista_tareas(tarea10)





    # Agregar tareas

    print("\nTareas agregadas:") # Imprime Tareas agregadas:
    tarea1 = Tarea(1, "Pasear")
    tarea2 = Tarea(2, "Comprar pan")
    tarea3 = Tarea(3, "Comer")
    tarea4 = Tarea(4, "Recoger")
    tarea5 = Tarea(5, "Jugar coches")
    tarea6 = Tarea(6, "Parquear")
    tarea7 = Tarea(7, "Duchar")
    tarea8 = Tarea(8, "Cenar")
    tarea9 = Tarea(9, "Jugar")
    tarea10 = Tarea(10, "Dormir")
    
   
    gestor.agregar_tarea(tarea8)
    gestor.agregar_tarea(tarea9)
    gestor.agregar_tarea(tarea10)

    

    # Marcar tarea como completada

    print("\nTareas completadas:")  
    gestor.marcar_completada(1)
    gestor.marcar_completada(2)

    # Mostrar todas las tareas

    print("\nTodas las tareas:") # Imprime Todas las tareas:
    gestor.mostrar_tareas()

    # Borrar tareas

    print("\nTareas borradas:") # Imprime Tareas borradas:
    gestor.borrar_tarea(1)
    gestor.borrar_tarea(2)
   

    #buscar tarea borrada
    print("\nTodas las tareas pendientes:") # Imprime Todas las tareas pendientes:
    gestor.buscar_tareas_borradas()


  
   
    



    









