#******************************************
# Segundo commit Calculadora
# Hacer una calculadora basica
# calc-index
# ejecutable.exe
# release: 11/11/2022
# Developer: H. Leandro Mangicavalli
#******************************************

x = int(input("Ingrese el valor de X para la operacion: "))

y = int(input("Ingrese el valor de Y para la operacion: "))

seleccion = 0

while seleccion != 5:
    print("""Seleccione el tipo de operacion:
    1) x + y
    2) x * y
    3) x - y
    4) x / y
    5) Salir""")

    seleccion = int(input("Elija una opcion: "))

    if seleccion == 1:
        print(" ")
        print("El resultado es ", x, "+", y, "=", x+y)
        print(" ")
    elif seleccion == 2:
        print(" ")
        print(x, "x", y, "=", x*y)
        print(" ")
    elif seleccion == 3:
        print(" ")
        print(x, "-", y, "=", x-y)
        print(" ")
    elif seleccion == 4:
        print(" ")
        print(x, "/", y, "=", x/y)
        print(" ")
    elif seleccion == 5:
        print(" ")
        print("Ha salido de la calculadora")
        print(" ")
        

