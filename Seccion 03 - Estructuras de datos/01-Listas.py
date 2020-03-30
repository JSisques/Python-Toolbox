'''
Una lista es una variable que contiene varios datos o variables de cualquier tipo
Se puede crear una lista vacia utilizando []
Los elementos de las tienen posiciones, siendo la primera posicion la 0 y la ultima la longitud de la lista menos 1
'''

miLista = ["Javi", "Perro", 6, True, 7.5]
listaVacia = []

'''
Para recorrer listas lo mejor es usar un bucle for aunque se puede utilizar cualquier tipo de bucle
Para acceder a un valor de la lista ponemos el nombre de la variable seguido de dos [] y dentro la posicion del elemento a acceder
lista[0] --> Sacamos el primer elemento de la lista
'''

posicion2 = miLista[2]
print("El elemento que hay en la posicion 2 es: " + str(posicion2))

#Ejemplo while
print("Ejemplo bucle while")
contador = 0
while contador < miLista.__len__():
    print(miLista[contador])
    contador += 1

#Ejemplo for
print("Ejemplo bucle for")
for elemento in miLista:
    print(elemento)

'''
Se pueden usar varios metodos para trabajar con listas:
    1. append() --> Añadir elementos a la lista
    2. remove() --> Eliminar un elemento de la lista
    3. sort() --> Ordenar una lista
    4. index() --> Obtiene el indice del primer valor encontrado
'''

pares = [] 
print("La lista antes del bucle: " + str(pares))

for i in range(0,10, 2):
    pares.append(i)

print("La lista despues del bucle: " + str(pares))

pares.remove(4)

print("La lista despues del borrado: " + str(pares))

valoresRepetidos = [0,2,4,4,6,8]
print("La lista antes del borrado: " + str(valoresRepetidos))
valoresRepetidos.remove(4)
print("La lista despues del borrado: " + str(valoresRepetidos))

listaDesordenada = [1,6,3,2,9,4,5,7,20]
print("La lista antes del ordenado: " + str(listaDesordenada))
listaDesordenada.sort()
print("La lista despues del ordenado: " + str(listaDesordenada))

listaIndex = ["Pepe", "Juan", "Elisa", "Kyle"]
print("Pepe se encuentra en la posicion: " + str(listaIndex.index("Elisa")))

'''
Ejercicio lista de la compra.

Hacer un menu que tenga las siguientes opciones:
    1. Añadir elemento a la lista de la compra
    2. Quitar un elemento de la lista de la compra
    3. Mostrar todo lo que haya en la lista de la compra

Requisitos:
La lista de la compra cuando se muestre se mostrará ordenada alfabeticamente y al principio en una linea se mostrará la longitud de la misma
Ejemplo:
Tu lista de la compra tiene 3 productos los cuales son:
Leche 
Galletas
Mantequilla
'''