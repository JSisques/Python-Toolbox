'''
Hacer un programa que cumpla los siguientes requisitos:
El programa deberá tener un menú con 4 opciones: 
    1. Calcular los numeros pares en un rango que nos indique el usuario
    2. Mostrar la longitud, el numero de letras "A" que tiene un texto independientemente de si estan en mayusculas o en minusculas
    3. Calcular la probabilidad de que en un numero de N personas dadas por el usuario 2 cumplan años el mismo dia.
    4. Salir
'''

opcion = 99

while opcion != 0:
    print("[1] ==> Calcular los numeros pares en un rango que nos indique el usuario")
    print("[2] ==> Mostrar la longitud, el numero de letras A que tiene un texto independientemente de si estan en mayusculas o en minusculas")
    print("[3] ==> Calcular la probabilidad de que en un numero de N personas dadas por el usuario 2 cumplan años el mismo dia.")
    print("[0] ==> Salir")
    opcion = int(input("Introduzca la opcion: "))

    if opcion == 1:
        rango = int(input("Introduce el rango: "))
        for i in range(0, rango, 2):
            print(i)
    elif opcion == 2:
        texto = input("Introduce el texto: ")
        print("La longitud es " + str(texto.__len__()) + " y el numero de letras A es" + str(texto.upper().count("A")))
    elif opcion == 3:
        numeroPersonas = int(input("Introduzca el numero de personas: "))
        casosPosibles = float(365) #Constante de dias del año
        casosFavorables = float(365) 
        resultadoDivisones = float(1)
        porcentajeFinal = float(0)

        for i in range(0, numeroPersonas):
            print(i)
            resultadoDivisones *= (casosFavorables - i) / casosPosibles
            print(resultadoDivisones)
        
        #Se puede usar la funcion round(numero, decimales a redondear) para obtener un valor redondeado
        porcentajeFinal = (1 - resultadoDivisones)
        print("El porcentaje de que en un grupo con " + str(numeroPersonas) + " numero de personas haya 2 que cumplan el mismo dia es del " + str(round(porcentajeFinal * 100, 2)) + "%")
    else:
        print("Has elegido salir")