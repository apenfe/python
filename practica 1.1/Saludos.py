# Saludos.py
# Programa simple que muestra varios mensajes en la consola del sistema.
# apf - 2023.09.24

nombre = ""		# Variable de texto, se declara pero no se inicializa.

# Configura y muestra mensajes de bienvenida.
numOrden = 1  # Se inicializa la variable.
print("Hola,")
print("Soy un modesto ",end="")
print("programa de ordenador...")
print("Bienvenido al Curso.\t" "Este es el saludo nº ", numOrden)  # \t crea un tabulado
numOrden=numOrden +1 # se aumenta en una unidad el valor de la variable. no vale numOrden++
print(f"Bienvenido a Java.\t" f"Este es el saludo nº {numOrden}") # si no pongo f delante saldra impreso el codigo literalmente
print("\nFin programa...")    # \n antes del texto, salta una linea antes de escribir

# SALIDA ESPERADA:
#
#  Hola,
#  Soy un modesto programa de ordenador...
#  Bienvenido al curso.    Este es el saludo nÂº 1
#  Bienvenido a Java.      Este es el saludo nÂº 2
#  
#  Fin programa...