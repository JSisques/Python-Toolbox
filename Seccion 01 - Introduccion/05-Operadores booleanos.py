'''
Al igual que con otros tipos de datos se pueden hacer operaciones logicas con datos de tipo booleano
Estas operaciones son:
    1. and --> Se traduce como y
    2. or --> Se traduce como o
    3. == --> Se traduce como igual a
    4. != --> Se traduce como diferente de
    5. < --> Se traduce como menor estricto que
    6. > --> Se traduce como mayor estricto que
    7. <= --> Se traduce como menor o igual que
    8. >= --> Se traduce como mayor o igual que
'''
#Operacion and
#True and True dara igual a True
print(True and True)
#True and False dara igual a False
print(False and False)
#False and True dara igual a False
print(False and False)
#False and False dara igual a False
print(False and False)

#Operacion or
#True or True dara igual a True
print(True or True)
#True or False dara igual a True
print(True or False)
#False or True dara igual a True
print(False or True)
#False or False dara igual a False
print(False or False)


interruptor = False
preguntaEncendido = False
bombillaEncendida = False
#Operador ==
#Si True == True devolvera True
bombillaEncendida = interruptor == preguntaEncendido
print("¿La bombilla esta encendida? " + str(bombillaEncendida))

num1 = 10
num2 = 10
print(num1 == num2)
print(num1 != num2)

print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)





