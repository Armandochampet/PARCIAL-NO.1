import random

class Nodo:
    def __init__(self, id, tiempo):
        self.id = id
        self.tiempo = tiempo
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def ingresar_un_nuevo_proceso(self, tiempo):
        id = random.randint(1000, 9999)
        nuevo_nodo = Nodo(id, tiempo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        print(f"Proceso {id} agregado con {tiempo} segundos")
        self.mostrar_estado()

    def atender_proceso(self):
        if not self.cabeza:
            print("\n¡ERROR!")
            return
        print(f"Atendiendo Proceso {self.cabeza.id} ({self.cabeza.tiempo} Segundos Restantes)")
        if self.cabeza.tiempo <= 2:
            self.eliminar_principio()
        else:
            self.cabeza.tiempo -= 2
            self.rotar()
        self.mostrar_estado()

    def ejecutar_la_planificacion(self):
        rotaciones = 0
        procesos_atendidos = 0
        tiempo_total = 0
        while self.cabeza:
            self.atender_proceso()
            rotaciones += 1
            tiempo_total += 2
            procesos_atendidos += 1
        print("Planificación Ejecutada Correctamente")
        print(f"Procesos Atendidos: {procesos_atendidos}")
        print(f"Tiempo Total: {tiempo_total} segundos")
        print(f"Rotaciones Necesarias: {rotaciones}")

    def eliminar_principio(self):
        if not self.cabeza:
            return
        print(f"Proceso {self.cabeza.id} Finalizado Correctamente!")
        if self.cabeza.siguiente == self.cabeza:
            self.cabeza = None
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente

    def rotar(self):
        self.cabeza = self.cabeza.siguiente

    def mostrar_estado(self):
        if not self.cabeza:
            print("Lista de Procesos Vacía")
            return
        temp = self.cabeza
        procesos = "Procesos:\n"
        procesos_activos = 0
        tiempo_restante = 0
        while True:
            procesos += f"{temp.id} - {temp.tiempo} segundos\n"
            procesos_activos += 1
            tiempo_restante += temp.tiempo
            temp = temp.siguiente
            if temp == self.cabeza:
                break
        print(procesos)
        print(f"Procesos activos: {procesos_activos}")
        print(f"Tiempo restante: {tiempo_restante} segundos")

lista = ListaCircular()
opcion = 0

def obtener_entrada(mensaje):
    return input(mensaje)

def mostrar_menu():
    global opcion
    print("\n1. Ingresar un nuevo proceso")
    print("2. Atender proceso")
    print("3. Ejecutar la planificación")
    print("4. Salir")
    opcion = int(obtener_entrada("Seleccione una opción: "))
    if opcion == 1:
        tiempo = int(obtener_entrada("Ingrese el tiempo del proceso: "))
        lista.ingresar_un_nuevo_proceso(tiempo)
    elif opcion == 2:
        lista.atender_proceso()
    elif opcion == 3:
        lista.ejecutar_la_planificacion()

while opcion != 4:
    mostrar_menu()
