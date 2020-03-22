'''
Las variables sirven para almacenar cualquier tipo dato para luego poder usarlo en otra funcion o lo que sea necesario
Para asignar un valor a una variable debemos de escribir el nombre de la variable que queramos seguido de un = y el valor
'''

miVariable = 5 

'''
Los nombres de las variables deben de seguir unas reglas basicas y unas convenciones.
Reglas:
    1. Ninguna variable puede empezar por un numero, pero si contener numeros dentro del nombre. Ejemplo: num1
    2. Ninguna variable puede contener caracteres especiales
    3. Ninguna variable puede contener espacios en su nombre

Convenciones:
    1. Las variables deberán de empezar en MINUSCULA
    2. Se debe de usar Camel Case o separar las palabras por guiones bajos para su correcta lectura. 
    Ejemplo: 
    nombredejuan --> Se entiende poco a primera vista
    numbreDeJuan --> Se entiendde mucho mejor a primera vista ya que se detectan las palabras mas facilmente
    nombre_de_juan --> Tambien se entiende mucho mejor
'''

#Variable que almacena un numero entero
numEntero = 0

#Variable que define un String
miString = "Hola"

'''
Como vemos no hace falta definir el tipo de datos, se puede hacer pero no es obligatorio
Para definir el tipo de datos usamos lo siguiente:
    1. Enteros --> int(valor)
    2. Float --> float(valor)
    3. String --> str(valor)
'''

numPersonas = 15
numRegalosPorPersona = 2
numRegalosTotales = numPersonas * numRegalosPorPersona
print("Mi numero de la mala suerte es el " + str(numRegalosTotales))

nombre = "Javi"
edad = "21"
print("Me llamo " + nombre + " y tengo " + edad + " años")