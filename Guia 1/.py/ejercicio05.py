# 5
# Desarrollar algoritmo que permita Pedir el ingreso de dos valores Numéricos y luego identificar cuál de ellos es mayor o si dichos números son iguales.

n=2

numeros=[]

for i in range(n):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    numeros.append(numero)

minimo=min(numeros)
maximo=max(numeros)

print(f"Los números ingresados son: {numeros}")
if maximo==minimo:
    print(f"Todos los números son iguales ({minimo}).")
elif maximo>minimo:
    print(f"El numero mayor es {maximo}. ")
