# Ejercicio 2

# Desarrollar algoritmo que a partir de un número digitado por el usuario, 
# permita mostraren pantalla la secuencia de números hasta llegar al valor 1. 
# Ejemplo: Si digita elnúmero 5, deberá mostrar en pantalla “5, 4, 3, 2, 1” (un número debajo de otro). 
# Valide que sólo se puedan ingresar números positivos, presentando un mensaje de error encaso contrario.

while True:
    n = int(input("Ingrese un número positivo: "))
    if n>0 and n%1==0:
        break
    else:
        print("El número debe ser positivo (mayor a 0)")

for i in range(n, 0, -1):
    if i<=n:
        print(f"{i}")