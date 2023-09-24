# Escribe un programa simple en Java, que lea un nÃºmero correspondiente a una edad e indique lo siguiente:
# Menor, edad de trabajar, jubilado o numero no valido.
# Autor: Adrian Penalver Fernandez
# 22/09/23

print("Escriba su edad: ")
num1 = int(input())

if (num1 < 18 and num1 > 0): # comprobamos si es menor de 18 y mayor que 0
    print("Menor de edad.")
elif (num1>=18 and num1 < 65): # comprobamos si es mayor o igual a 18 y menor de 65
    print("Adulto en edad de trabajar.")
elif (num1>=65): # comprobamos si es mayor o igual de 65
    print("Jubilado.")
else:
    print("Número incorrecto")