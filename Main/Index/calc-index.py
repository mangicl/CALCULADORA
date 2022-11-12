#******************************************
# Segundo commit Calculadora
# Hacer una calculadora basica
# calc-index
# ejecutable.exe
# release: 11/11/2022
# Developer: H. Leandro Mangicavalli
#******************************************

import math

x = float(input("Ingrese el valor de X para la operacion: "))

y = float(input("Ingrese el valor de Y para la operacion: "))

seleccion = 0

while True:
    if seleccion != 6:
        print("""Seleccione el tipo de operacion:
        1) x + y
        2) x * y
        3) x - y
        4) x / y
        5) RESET
        6) SALIR""")

    seleccion = int(input("Elija una opcion: "))

    if seleccion == 1:
        print(" ")
        print("Resultado ", x, "+", y, "=", x+y)
        print(" ")
    elif seleccion == 2:
        print(" ")
        print("Resultado ", x, "x", y, "=", x*y)
        print(" ")
    elif seleccion == 3:
        print(" ")
        print("Resultado ", x, "-", y, "=", x-y)
        print(" ")
    elif seleccion == 4:
        if x == 0:
            print("""El cero no es un numero divisible.
            Elija otra opcion...""")
            break
        print(" ")
        print("Resultado ", x, "/", y, "=", x/y)
        print(" ")
    elif seleccion == 5:
        del x, y,
        x = float(input("Ingrese un nuevo valor de X para la operacion: "))
        y = float(input("Ingrese un nuevo valor de Y para la operacion: "))
    elif seleccion == 6:
        print(" ")
        print("Ha salido de la calculadora")
        print(" ")
        

