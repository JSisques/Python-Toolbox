'''
Una sentencia condicional es aquella que dependiendo de una variable o de un dato escogerá ejecutar un trozo de codigo u otro
En Python existen 3 tipos diferentes de condicionales pero dos de ellas solo existen si una tercera presente en el codigo
Las diferentes sentencias son:
    1. If --> La sentencia if comprueba si la variable o dato es true y en ese caso ejecuta las intrucciones siguientes
    2. Else --> La sentencia else ejecuta un fragmento de codigo si la sentencia if es false
    3. Elif --> La sentencia elif ejecuta un fragmento de codigo siempre y cuando la condicion del if sea false y la condicion del elif sea true
'''

esCalvo = False

if esCalvo:
    print("Vete a Turquia")
else:
    print("Menudo pelazo tienes pareces John Travolta")

nota = int(input("Introduzca la nota del alumno: "))

if nota >= 0 and nota < 5:
    print("Estas suspenso")
elif nota >= 5 and nota < 7:
    print("Estas aprobado pero no te emociones") 
elif nota >=7 and nota <= 10:
    print("Notaza compañero")
else:
    print("Esa nota es imposible")

'''
Ejemplo discoteca
Somos un portero de una discote a la cual solo pueden entrar personas mayores de 17 años
Nuestra mision es pedir por pantalla la edad del usuario y validar su entrada
'''

edad = int(input("Introduzca su edad: "))

if edad >= 0 and edad <= 17:
    print("Te jodes mamon no pasas")
elif edad > 17:
    print("Tu si pasas")
else: 
    print("Esa edad es imposible")

'''
Ejemplo bombilla 1
Tenemos dos interruptores y una bombilla, la bombilla solo se encenderá si los dos interruptores estan dados, en cualquier otro caso la bombilla permanecera apagada
True == Encendido
False == Apagado
'''

bombilla = False
interruptor1 = bool(input("¿El interruptor 1 esta encendido? "))
interruptor2 = bool(input("¿El interruptor 2 esta encendido? "))

if interruptor1 == True and interruptor2 == True:
    bombilla = True
else:
    bombilla = False

if bombilla == True:
    print("La bombilla esta encendida")
else:
    print("La bombilla esta apagada")


'''
Ejemplo bombilla 2
Tenemos dos interruptores y una bombilla, la bombilla solo se encenderá si algun interruptor esta dado, en cualquier otro caso la bombilla permanecera apagada
True == Encendido
False == Apagado
'''

bombilla = False
interruptor1 = True
interruptor2 = False

if interruptor1 == True or interruptor2 == True:
    bombilla = True
else:
    bombilla = False

if bombilla == True:
    print("La bombilla esta encendida")
else:
    print("La bombilla esta apagada")

