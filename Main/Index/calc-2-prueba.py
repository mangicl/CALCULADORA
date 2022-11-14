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
            0) RESET DE VALORES
            1) GUARDAR EL RESULTADO EN MEMORIA
            2) Asignar MEMORIA a: X
            3) Asignar MEMORIA a: Y
            e) SALIR""")
            
            seleccion = input()
            if seleccion == 'c':
                x = float(input("Ingrese un nuevo valor de X para la operacion: "))
                y = float(input("Ingrese un nuevo valor de Y para la operacion: "))
                print("Se han reseteado los valores")
            if seleccion == 's':
                print(f"Resultado: {x} + {y} = {suma(x,y)}")
            elif seleccion == 'm':
                print(f"Resultado: {x} x {y} = {multimplicacion(x,y)}")
            elif seleccion == 'r':
                print(f"Resultado: {x} - {y} = {resta(x,y)}")
            elif seleccion == 'd':
                print(f"Resultado: {x} / {y} = {division(x,y)}")
            elif seleccion == "e":
                print(f"Ha salido de la calculadora")
                break
            
            input("Presione cualquier tecla para continuar operando con los mismos valores")
            os.system("cls")
        
a,b = ingresarValores()
menu (a,b)            
        


