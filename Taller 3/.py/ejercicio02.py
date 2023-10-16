# Ejercicio 2
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

while True:
    numero = int(input("Ingrese un número entero positivo: "))
    if numero >=0 and numero%1==0:
        break
    else:
        print("El número debe ser entero (sin decimales) y positivo (mayor a 0)")

for i in range(numero, -1, -1):
        print(f"{i}, ", end="")
