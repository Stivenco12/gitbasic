dinero = int(input("ingrse un numero "))
dinero2 = int(input("ingrese un numero "))

eleccion = 0

while eleccion != 6:
    print("""
    indique la operacion
          
    1) suma
    2) resta
    3) multiplicasion
    4) division
    5) cambio de valores
    6) salir
    """)

    eleccion = int(input())

    if eleccion == 1:
        print(" ")
        print("resultado: ", dinero,"+",dinero2,"=",dinero+dinero2)

    if eleccion == 2:
        print(" ")
        print("resultado: ", dinero,"-",dinero2,"=",dinero--dinero2)                                   

    if eleccion == 3:
        print(" ")
        print("resultado: ", dinero,"*",dinero2,"=",dinero*dinero2)        

    if eleccion == 4:
        print(" ")
        print("resultado: ", dinero,"/",dinero2,"=",dinero/dinero2)    

    if eleccion == 5:
        dinero = int(input("ingrse un numero "))
        dinero2 = int(input("ingrese un numero "))

    if eleccion == 6:
        print("GRACIAS POR UTILIZAR LA CALCULADORA")                 