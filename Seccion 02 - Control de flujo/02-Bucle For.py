'''
Un bucle es un fragmento de codigo que se repite hasta que una condicion sea falsa, existen 2 tipos de bucles en Python, los bucles for y los bucles while
El bucle for funciona de la siguiente manera:
    1. El bucle necesita una variable interna y una variable a iterar
    2. El bucle asigna a la variable interna el primer valor de la variable a iterar
    3. El bucle ejecuta el codigo correspondiente
    4. El bucle compara o revisa si queda algo por iterar, si queda algo el bucle sigue funcionando, si no el bucle se acaba
'''

name = "Pepe"

for letter in name:
    print(letter)

'''
Podemos iterar o recorrer distintos tipos de datos:
    1. Strings --> El bucle for creará internamente una lista con los caracteres del string a iterar
    2. Listas --> El bucle for recorrerá cualquier tipo de lista
    3. Rangos --> El bucle for podrá recorrer listas generadas con la función range() que contendran los numeros que se hayan definido
'''

'''
Ejemplo: range(numMinimo, numeroMaximo, saltos)
Para usar la funcion range tendremos que tener en cuenta varios que puede tener:
    1. Se puede definir simplemente el numero de iteraciones que queramos hacer con nuestro bucle utilizando range(numIteraciones)
    2. Se puede definir el inicio del numero de las iteraciones asi como el final de las mismas utilizando range(numMinimo, numMaximo)
    3. Se puede definir un tercer parametro el cual indica los saltos que debe de hacer la funcion utilizando range(numMinmo, numMaximo, saltos)

'''

numeroMaximo = int(input("Introduce hasta que numero quieres saber los pares: "))
numeroMinimo = int(input("Introduce el numero de comienzo: "))

for numero in range(numeroMinimo, numeroMaximo, 2):
    print(numero)