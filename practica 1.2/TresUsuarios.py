
# Escribe un programa simple Java que incorpore las sentencias necesarias para leer los datos de tres personas
# (nombre, apellidos, nif y direcciÃ³n postal) desde el teclado, los guarde y los muestre, en pantalla; se deben
# mostrar en orden inverso, primero los datos de la Ãºltima persona.
#
# Autor: Adrian Penalver Fernandez
# 22/09/23

print("Escriba el nombre de la persona nº 1: ", end="")
nombre1 = input()
print("Escriba los apellidos de la persona nº 1: ", end="")
apellido1 = input()
print("NIF de la persona nº 1: ", end="")
nif1 = input()
print("Dirección postal de la persona nº 1: ", end ="")
direccion1 = input()
print()

print("Escriba el nombre de la persona nº 2: ", end="")
nombre2 = input()
print("Escriba los apellidos de la persona nº 2: ", end="")
apellido2 = input()
print("NIF de la persona nº 2: ", end="")
nif2 = input()
print("Dirección postal de la persona nº 2: ", end ="")
direccion2 = input()
print()

print("Escriba el nombre de la persona nº 3: ", end="")
nombre3 = input()
print("Escriba los apellidos de la persona nº 3: ", end="")
apellido3 = input()
print("NIF de la persona nº 3: ", end="")
nif3 = input()
print("Dirección postal de la persona nº 3: ", end ="")
direccion3 = input()
print()
       
      
print(f"El nombre de la persona nº3 es: {nombre3} {apellido3} ,NIF: {nif3} ,Dirección: {direccion3}")

print("El nombre de la persona nº2 es: " + nombre2 + apellido2 + " ,NIF: " + nif2 + " ,DirecciÃ³n: " + direccion2)

print("El nombre de la persona nº1 es: " + nombre1 + apellido1 + " ,NIF: " + nif1 + " ,DirecciÃ³n: " + direccion1)