'''
Un String es una cadena de caracteres que puede tener tantas letras o caracteres como se quiera
Simplificando es cualquier texto
'''

miString = "Hola mundo!"

'''
Se pueden usar funciones para cualquier String como por ejemplo contar el numero de caracteres que tiene a parte de otras muchas mas
Para llamar a cualquier funcion debemos de escribir el string o la variable que lo contiene seguido de un . y el metodo o funcion
'''

#Saber el numero de veces que se repite un string o caracter dentro de otro
#Ejemplo: Quiero saber cuantas veces aparece la letra o
numCaracteres = miString.count("o")
print("La letra o aparece " + str(numCaracteres) + " veces")

#Saber cuantos caracteres tiene un texto
numCaracteres = miString.__len__()
print("El texto " + miString + " tiene " + str(numCaracteres) + " caracteres")

#Convertir a mayusculas o minusculas
textoMayusculas = miString.upper()
textoMinusculas = miString.lower()
print("El texto original era " + miString)
print("El texto en mayusculas es " + textoMayusculas)
print("El texto en minusculas es " + textoMinusculas)