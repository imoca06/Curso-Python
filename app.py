#  Copyright (c) 2024. Walter Cervini Colli
import os

class Task:
    # Clase para manejo de tareas
    def __init__(self, description: str):
        # Constructor de la clase Task
        # Esta clase es un objeto para almacenar tareas de forma individual
        # Sera usada por la clase tasks
        # @param description: str
        # @param description: str
        # @return None
        # ------------------------------------
        # Atributos
        # description: Descripcion de la tarea a realizar
        # completed: Estado de la tarea (completada o no completada)
        self.description = description
        self.completed: bool = False

    def __str__(self):
        if self.completed:
            state = "[✔]"
        else:
            state = "[ ]"
        return f"{state} {self.description}"


"""
Clase para el almacenamiento de las clases
"""
class TaskList:
    def __init__(self):
        #constructor de la clase TaskList
        # es un arreglo vacio para almacenar las tareas
        self.tasks = []

    def add_task(self, description):
        #metodo para agregar una tarea
        # @param description: str
        # en este punto se crea una instancia de la clase Task y se agrega al arreglo de tareas
        self.tasks.append(Task(description))

    def mark_completed(self, position):
        #metodo para marcar una tarea como completada
        # verificamos si la posicion es valida y cambiamos el estado de la tarea
        # en caso de que no sea valida la posicion se lanza una excepcion
        # @param position: int 
        if position >= 0 and position < len(self.tasks):
            self.tasks[position].completed = True
        elif position < 0:
            raise ValueError("Posición inválida")   
        else:
            raise ValueError("Posición inválida")

    def __str__(self):
        # este metodo se encarga de mostrar todas las tareas
        # si la longitud del arreglo de tareas es 0 se muestra un mensaje
        # indicando que no hay tareas pendientes en caso contrario se muestra
        # el listado de tareas
        # @param None
        # @return str
        if len(self.tasks) == 0:
            return "No hay tareas pendientes"
        else:
            output = ""
            #en esta parte se recorre el arreglo de tareas y se muestra el listado
            # usamos f-string para contatenar un numero con una tarea destro de un string
            for i, task in enumerate(self.tasks):
                output += f"{i+1}. {task}\n"
            return output

    def delete_task(self, position):
        # metodo para eliminar una tarea segun la posicion indicada
        # en caso que la posicion no sea valida se lanza una excepcion
        # con el mensaje "Posicion invalida"
        if position >= 0 and position < len(self.tasks):
            del self.tasks[position]
        else:
            raise ValueError("Posición inválida")



def show_menu():
    # funcion para mostrar el menu de opciones de la aplicacion
    
    print("Lista de tareas")
    print("1. Agregar una nueva tarea")
    print("2. Marcar una tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar una tarea")
    print("5. Salir")
    print("6. Borrar pantalla")


def main():
    # Inicializacion le la lista de tareas con un nuevo objeto TaskList
    task_list = TaskList()
    # Bucle principal de la aplicacion que finaliza cuando el usuario selecciona la opcion 5
    while True:
    
        show_menu()
        try:
            # se captura la opcion seleccionada por el usuario
            option = int(input("Ingrese una opción: "))
            # se ejecuta la opcion seleccionada por el usuario
            if option == 1:
                description = input("Ingrese una tarea: ")
                # La opcion se agregara a la lista de tareas
                task_list.add_task(description)
            elif option == 2:
                #esta opcion cambia el estado de una tarea a completada
                position = int(
                    input(
                        "Ingrese la posición de la tarea que desea marcar como completada: "
                    )
                )
                #es requerido restar uno a la posicion ya que los indices inician e cero
                task_list.mark_completed(position - 1)
            elif option == 3:
                #esta opcion muestra todas las tareas
                print(task_list)
            elif option == 4:
                # esta opcion elimina una tarea
                position = int(
                    input("Ingrese la posición de la tarea que desea eliminar: ")
                )
                task_list.delete_task(position - 1)
            elif option == 5:
                # esta opcion finaliza la ejecucion del programa
                break
            elif option == 6:
                os.system("clear")
            else:
                # en caso de que la opcion seleccionada no sea valida se lanza una excepcion
                raise ValueError("Opción inválida")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Punto de entrada de la aplicacion
    main()
