# Escribe un programa simple Java, basado en Saludos.java, que lea un nÃºmero e indique si es par o impar.
# Autor: Adrian Penalver Fernandez
# 22/09/23

print("Escriba el número: ")
numero1 = int(input())

if numero1 % 2 == 0: # esta funcion modulo devuelve el resto, por lo que si es 0, se trata de un numero par
    print("El numero es par.")
else:
    print("El numero es impar.")
