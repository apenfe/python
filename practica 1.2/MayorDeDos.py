# Escribe un programa simple Java, basado en Saludos.java, que pida y visualice el nombre y la edad de dos personas en dos lÃ­neas diferentes.
# Autor: Adrian Penalver Fernandez
# 22/09/23

print("Escriba el número 1: ", end="")
num1 = int(input())
print("Escriba el número 2: ", end="")
num2 = int(input())
print()

if (num1 > num2):
    print("El numero 1 es el mayor: ", num1)
else:
    print("El numero 2 es el mayor: ", num2)
