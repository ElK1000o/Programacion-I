# 1
# Desarrollar algoritmo que permita pedir el ingreso del nombre, luego el apellido y por último la edad de una persona. 
# Imprima los datos generando la siguiente salida:“Daniel Pérez Tiene 34 Años”

while True:
    nombre=input("Ingrese su nombre: ")
    if len(nombre)>0:
        break
    elif len(nombre)==0:
        print("El espacio no puede quedar en blanco, ingrese su nombre: ")

while True:
    apellido=input("Ingrese su apellido: ")
    if len(apellido)>0:
        break
    elif len(apellido)==0:
        print("El espacio no puede quedar en blanco, ingrese su apellido: ")

edad=int(input("Ingrese su edad: "))

print(f"{nombre} {apellido} tiene {edad} años. ")