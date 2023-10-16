# 7
# Desarrollar Algoritmo que permita pedir el ingreso de 5 números. 
# Luego realice una búsqueda a partir de un número cualquiera que el usuario digite en ese momento eindique a través de un mensaje si dicho número se encuentra almacenado o no.

n=5
numeros=[]

print(f"A continuación te pediré que ingreses {n} números. ")
for i in range(n):
    numero = float(input(f"Ingresa el número {i+1}: "))
    numeros.append(numero)

num_sol=float(input("Ingrese ahora un número cualquiera. A continuación se indicará si se encuentra o no almacenado. "))

if num_sol in numeros:
    print(f"El número {num_sol} está en la lista.")
else:
    print(f"El número {num_sol} no está en la lista.")