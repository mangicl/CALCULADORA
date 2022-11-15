#************************************************************
# Segundo commit Calculadora
# - Creación de repositorios
# - Importación a la computadora
# - Generación del .py
# - Una calculadora sencilla con la sintaxis
# - Aprender a buscar información de experiencias anteriores
# - Aprender a trabajar solos como desarrolladores
# calc-index
# ejecutable.exe
# release: 11/11/2022
# Developer: H. Leandro Mangicavalli
#************************************************************

import math

x = float(input("Ingrese el valor de X para la operacion: "))
y = float(input("Ingrese el valor de Y para la operacion: "))
seleccion = 0

while True:
    if seleccion != 9:
        print("""Seleccione el tipo de operacion:
        1) x + y
        2) x * y
        3) x - y
        4) x / y
        5) RESET
        6) Asignar el resultado a X y seguir operando
        7) Asignar el resultado a Y y seguir operando
        8) SALIR""")
    seleccion = float(input("Elija una opcion: "))
    if seleccion == 1:
        print(" ")
        print("Resultado ", x, "+", y, "=", x+y)
        resultado = x+y
        print(" ")
    elif seleccion == 2:
        print(" ")
        print("Resultado ", x, "x", y, "=", x*y)
        resultado = x*y
        print(" ")
    elif seleccion == 3:
        print(" ")
        print("Resultado ", x, "-", y, "=", x-y)
        resultado = x-y
        print(" ")
    elif seleccion == 4:
        if y == 0:
            print("""El cero no es un numero divisible.
            Elija otra operacion...""")
            continue
        print(" ")
        print("Resultado ", x, "/", y, "=", x/y)
        resultado = x/y
        print(" ")
    elif seleccion == 5:
        x = float(input("Ingrese un nuevo valor de X para la operacion: "))
        y = float(input("Ingrese un nuevo valor de Y para la operacion: "))
    elif seleccion == 6:
        x = resultado
        y = float(input("Ingrese un nuevo valor de Y para la operacion: "))
    elif seleccion == 7:
        x = float(input("Ingrese un nuevo valor de X para la operacion: "))
        y = resultado
    elif seleccion == 8:
        print(" ")
        print("Ha salido de la calculadora")
        print(" ")
        break

