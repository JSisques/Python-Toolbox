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

'''
Este metodo comprueba si la palabra del usuario es igual a la elegida para adivinar
'''
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

'''
Este metodo comprueba letra a letra si coincide con la letra dada en el parametro, en el caso de que coincida se cambia el _ por la letra correspondiente
'''
def comprobarLetra(letra, palabra):
    palabra  = list(palabra)

    posicion = 0
    for letraAdivinar in palabraParaAdivinar:
        if letra == letraAdivinar:
            palabra[posicion] = letra
        posicion += 1

    return "".join(palabra)

'''
Este metodo convierte la palabra seleccionada a una palabra solo con guiones y devuelve esta ultima
'''
def convertirPalabraRespuesta(palabra):
    palabraRespuesta = ""

    for letra in palabra:
        palabraRespuesta += "_"

    return palabraRespuesta

'''
Este metodo pide una palabra al usuario y la devuelve en minusculas
'''
def pedirPalabra():
    palabraUsuario = input("Introduce la palabra: ")
    return palabraUsuario.lower()

jugar()