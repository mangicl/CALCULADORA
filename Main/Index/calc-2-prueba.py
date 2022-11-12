import os

def ingresarValores():
    x = float(input("Ingrese el valor de X para la operacion: "))
    y = float(input("Ingrese el valor de Y para la operacion: "))
    os.system("cls")
    return x, y
def suma(x,y):
    return x+y
def multimplicacion(x,y):
    return x*y
def resta(x,y):
    return x-y
def division(x,y):
    return x/y            
def menu(x,y):
    while True:
        print(f"""Seleccione el tipo de operacion con X={x} y con Y={y}:
        s) x + y
        m) x * y
        r) x - y
        d) x / y
        0) RESET
        6) SALIR""")
        seleccion = input()
        if seleccion == 's':
            print(f"Resultado ", x, "+", y, "=", x+y)
        elif seleccion == 'm':
            print(f"Resultado ", x, "x", y, "=", x*y)
        elif seleccion == 'r':
            print(f"Resultado ", x, "-", y, "=", x-y)
        elif seleccion == 'd':
            print(f"Resultado ", x, "/", y, "=", x/y)
            if x == 0:
                print("""El cero no es un numero divisible.
            Elija otra opcion...""")
                break
        if seleccion == 0:
            del x,y
        if seleccion == 6:
            print(f"Ha salido de la calculadora")
            break
        input("Presione cualquier tecla para continuar")
        os.system("cls")

a,b = ingresarValores()
menu (a,b)            
        


