# Escribe un programa simple Java, basado en Saludos.java, que pida y visualice el nombre y la edad de dos personas en dos lÃ­neas diferentes.
# Autor: Adrian Penalver Fernandez
# 22/09/23

print("Escriba el nombre de la persona nº 1: ", end="")
nombre1 = input()
print("Edad la persona nº 1: ", end="")
a = int(input())

print("Escriba el nombre de la persona nº 2: ", end="")
nombre2 = input()
print("Edad la persona nº 2: ", end="")
b = int(input())

print(f"El nombre de la persona nº1 es: {nombre1} y su edad es: {a} años.")
print(f"El nombre de la persona nº1 es: {nombre2} y su edad es: {b} años.")