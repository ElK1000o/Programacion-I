#Ejercicio 1
#Generar script en Python que a partir de un número cualquiera(ingreso por teclado), determine el área de un triangulo ((base * altura) / 2).

#variables
base = 0
altura = 0
area = 0

#Pedir datos

base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
area=((base*altura)/2)

print(f"El área del triángulo cuya base es {base} y cuya altura es {altura} da como resultado : {area}")
