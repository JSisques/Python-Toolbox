'''
El bucle while se diferencia del for en que no crea una variable por cada iteracion, simplemente por cada vuelta evalua una condicion y repite el codigo dentro del mismo hasta que la condicion sea False.
Hay que tener cuidado de no hacer un bucle infinito, el caso comun de este error es no cambiar la variable de la condicion una vez dentro del bucle
'''

condicion = ""

while condicion != "salir":
    condicion = input("Para salir escriba salir: ")

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

#Ejemplo de menu
opcion = 99

while opcion != 0:
    print("[1] ==> Decir buenos dias")
    print("[2] ==> Decir buenas tardes")
    print("[3] ==> Decir buenas noches")
    print("[0] ==> Salir")
    opcion = int(input("Introduzca la opcion: "))

    if opcion == 1:
        print("Buenos dias")
    elif opcion == 2:
        print("Buenas tardes")
    elif opcion == 3:
        print("Buenas noches")
    else:
        print("Has elegido salir")



