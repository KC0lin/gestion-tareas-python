class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "✔️" if self.completada else "❌"
        return f"{estado} {self.descripcion}"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def añadir_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)
        print(f"Tarea añadida: {descripcion}")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea_eliminada = self.tareas.pop(indice)
            print(f"Tarea eliminada: {tarea_eliminada.descripcion}")
        else:
            print("Índice de tarea no válido.")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def marcar_tarea_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].marcar_completada()
            print(f"Tarea marcada como completada: {self.tareas[indice].descripcion}")
        else:
            print("Índice de tarea no válido.")


def main():
    gestor = GestorTareas()
    
    while True:
        print("\nGestor de Tareas")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Listar tareas")
        print("4. Marcar tarea como completada")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            descripcion = input("Descripción de la tarea: ")
            gestor.añadir_tarea(descripcion)
        elif opcion == '2':
            indice = int(input("Índice de la tarea a eliminar: "))
            gestor.eliminar_tarea(indice)
        elif opcion == '3':
            gestor.listar_tareas()
        elif opcion == '4':
            indice = int(input("Índice de la tarea a marcar como completada: "))
            gestor.marcar_tarea_completada(indice)
        elif opcion == '5':
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            
if __name__ == "__main__":
    main()
 