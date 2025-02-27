#EL PROGRAMA INGRESA POLINOMIOS A Y B
#HACE SUMAS Y RESTAS DE POLINOMIOS
#MUESTRA EL RESULTADO FINAL

polinomioA = []
polinomioB = []


def Ingresar_Elementos(polinomio):
    cantidad = int(input("\nIngrese la Cantidad de Elementos que Desea Ingresar: "))
    for i in range(cantidad):
        polinomio.append((0, 0))


def Ingresar_Componentes(polinomio):
    for i in range(len(polinomio)):
        componente = int(input("\nIngrese el Componente del Elemento No.{}:".format(i + 1)))
        polinomio[i] = (componente, polinomio[i][1])


def Ingresar_Coeficientes(polinomio):
    for i in range(len(polinomio)):
        coeficiente = int(input("\nIngrese el Coeficiente del Elemento No.{}:".format(i + 1)))
        polinomio[i] = (polinomio[i][0], coeficiente)


def Ingreso_PolinomioA():
    print("\n Ingreso Polinomio A")
    Ingresar_Elementos(polinomioA)
    Ingresar_Componentes(polinomioA)
    Ingresar_Coeficientes(polinomioA)


def Ingreso_PolinomioB():
    print("\n Ingreso Polinomio B")
    Ingresar_Elementos(polinomioB)
    Ingresar_Componentes(polinomioB)
    Ingresar_Coeficientes(polinomioB)


def Suma_Polinomios(polinomioA, polinomioB):
    resultado = []
    max_len = max(len(polinomioA), len(polinomioB))
    for i in range(max_len):
        coeficienteA = polinomioA[i][0] if i < len(polinomioA) else 0
        coeficienteB = polinomioB[i][0] if i < len(polinomioB) else 0
        exponente = polinomioA[i][1] if i < len(polinomioA) else (polinomioB[i][1] if i < len(polinomioB) else 0)
        suma = coeficienteA + coeficienteB
        resultado.append((suma, exponente))
    return resultado


while True:
    print("\n\tMENÚ PRINCIPAL")
    print("1. Ingresar Componentes de un Polinomio")
    print("2. Adición y Sustracción")
    print("3. Evaluar Polinomios")
    print("4. SALIR")
    opcion = input("Ingrese el Número de la Opción que Desee: ")

    if opcion == "1":
        while True:
            print("\nIngreso de Componentes de Polinomios")
            print("1. Polinomio A")
            print("2. Polinomio B")
            print("3. Regresar al Menú Principal")
            opcion2 = input("Ingrese el Número de la Opción que Desee: ")

            if opcion2 == "1":
                Ingreso_PolinomioA()
            elif opcion2 == "2":
                Ingreso_PolinomioB()
            elif opcion2 == "3":
                break
            else:
                print("\n¡ERROR! Opción Inválida. Intente de Nuevo")

    elif opcion == "2":
        while True:
            print("\nOperaciones")
            print("1. Adición")
            print("2. Sustracción")
            print("3. Regresar al Menú Principal")
            opcion3 = input("Ingrese el Número de la Opción que Desee: ")

            if opcion3 == "1":
                resultado_suma = Suma_Polinomios(polinomioA, polinomioB)
                print("\nEl resultado de la suma es:", resultado_suma)
            elif opcion3 == "2":
                print("RESTA (Funcionalidad Pendiente)")
            elif opcion3 == "3":
                break
            else:
                print("\n¡ERROR! Opción Inválida. Intente de Nuevo")

    elif opcion == "3":
        print("El Resultado de la Operación del Polinomio es:")
        print(resultado_suma if 'resultado_suma' in locals() else "No se ha Realizado Ninguna Operacion aun")

    elif opcion == "4":
        print("Gracias por Utilizar mi Programa")
        print("Programa Hecho por: Armando Champet - 1662523")
        exit()
    else:
        print("\n¡ERROR! Opción Inválida. Intente de Nuevo")
