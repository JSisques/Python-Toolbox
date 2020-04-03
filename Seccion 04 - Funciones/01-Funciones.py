'''
Una funcion en programación es un tipo de sentencia que puede o no tener valores de entrada (parametros) y que puede devolver o no un valor de retorno
La sintaxis de los metodos o funciones es la siguiente: nombreMetodo(parametros separados por comas)
Ejemplos:
    1. comprobarLetra(letra)
    2. comprobarResultado(palabra)
    3. pintarCoordenada(x, y)
    3. pintarCubo(x, y, z)

Existen dos tipos de funciones, las que devuelven un valor y las que no devuelven ningun valor
Para indicar si una funcion devuelve un valor usaremos la palabra return seguido de la variable o valor que queramos devolver, si no queremos devolver nada no pondremos un return
'''
miString = "Hola"
miString.count("a")

'''
Tomando como ejemplo la funcion o metodo count(valor) vemos que podemos diferenciar 2 partes:
    1. Nombre de la funcion --> En este caso corresponde a count
    2. Parametros --> Son todo lo que vaya entre () y en este caso es el valor que queremos buscar

En este caso la funcion count() devuelve el numero de letras encontradas que coincidan con la letra del parametro
'''

numeroLetras = miString.count("a")
#print(numeroLetras)

'''
Se pueden crear funciones personalizadas y programarlas para que hagan lo que uno quiera.
Al definir una funcion podemos encontrar varias partes:
    1. La palabra clave def --> Esta palabra indica a Python que se va a definir una funcion
    2. El nombre de la función --> El nombre que le queremos dar a nuestra funcion
    3. () --> Obligatorio ponerlos al definir y al llamar a una función
    4. Valores dentro de los parentesis (Parametros) --> Opcionales, si tenemos valores dentro de los parentesis indicamos que la función necesita datos de entrada, pueden infinitos
    5. : --> Obligatorio al final de la linea donde se define la función
'''

def contarHastaDiez():
    #Codigo
    lista = []
    for i in range(1, 11):
        lista.append(i)
    return lista

contarHastaDiez() #[1,2,3,4,5,6,7,8,9,10]
variableLista = [1,2,3,4,5,6,7,8,9,10]
variableFuncion = contarHastaDiez()

variable3 = contarHastaDiez()
variable4 = contarHastaDiez()

print(str(variableLista))
print(str(variableFuncion))
print(str(variable3))
print(str(variable4))

def saludar(nombre):
    return "Hola " + str(nombre)

saludo = saludar("Sara")
print(saludo)

def comprobacionEdad(edad):
    if edad >= 18:
        print("Puedes pasar a la discoteca")
    else:
        print("No puedes pasar")

comprobacionEdad(5)

def sumarDosDigitos(num1, num2):
    return num1 + num2

suma = sumarDosDigitos(6,10)
print(suma + 10)
 
lista = []
def addElementoLista(lista, elemento):
    lista.append(elemento)

print(str(lista))
addElementoLista(lista, "Patata")
print(str(lista))
addElementoLista(lista, 1)
print(str(lista))
addElementoLista(lista, True)
print(str(lista))