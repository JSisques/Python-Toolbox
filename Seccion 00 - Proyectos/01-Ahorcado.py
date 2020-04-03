'''
Proyecto sobre el juego del ahorcado
'''

'''
Función principal que controlará todo el juego
'''

#Aqui importamos una libreria que nos permite usar funciones aleatorias
import random

listadoPalabras = ["hospital", "gato", "elefante", "tortuga"]
palabraParaAdivinar = random.choice(listadoPalabras)

def jugar():

    palabraRespuesta = convertirPalabraRespuesta(palabraParaAdivinar)

    opcion = 99
    while opcion != 0:
        print(list(palabraRespuesta))
        print("----------------------------")
        print("[1] ==> Introducir una letra")
        print("[2] ==> Resolver")
        print("[0] ==> Salir")
        opcion = int(input("Introduzca la opcion: "))

        if opcion == 1:
            letra = pedirLetra()
            palabraRespuesta = comprobarLetra(letra, palabraRespuesta)
        elif opcion == 2:

            palabraUsuario = pedirPalabra()
            comprobacion = comprobarResultado(palabraUsuario)
            
            if comprobacion:
                print("Enhorabuena, has ganado")
                opcion = 0
            else:
                print("Sigue intentandolo")
                
        elif opcion == 0:
            opcion = 0
        else:
            print("Error, no es una opción valida")

def comprobarResultado(palabra):
    if  palabra == palabraParaAdivinar:
        return True
    else:
        return False

'''
Esta funcion pide al usuario una letra y la devuelve
'''
def pedirLetra():
    letra = input("Introduce la letra: ")
    return letra.lower()

def comprobarLetra(letra, palabra):
    palabra  = list(palabra)

    posicion = 0
    for letraAdivinar in palabraParaAdivinar:
        if letra == letraAdivinar:
            palabra[posicion] = letra
        posicion += 1

    return "".join(palabra)

def convertirPalabraRespuesta(palabra):
    palabraRespuesta = ""

    for letra in palabra:
        palabraRespuesta += "_"

    return palabraRespuesta

def pedirPalabra():
    palabraUsuario = input("Introduce la palabra: ")
    return palabraUsuario.lower()

jugar()