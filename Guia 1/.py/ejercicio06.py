# 6
# Desarrollar algoritmo que permita pedir el ingreso de 4 números e imprima cuál de elloses el menor (considere que los 4 números ingresados son diferentes).

while True:
    n=4
    numeros=[]
    print("A continuación te pediré que ingreses distintos números. ")
    for i in range(n):
        numero = float(input(f"Ingresa el número {i+1}: "))
        numeros.append(numero) 
    minimo=min(numeros)
    maximo=max(numeros)
    num_rev=set(numeros)
    if len(numeros)==len(num_rev):
        print(f"Los números ingresados son: {numeros}")
        print(f"El numero menor es {minimo}. ")
        break
    else:
        print("Hay números duplicados en la lista, vuelve a intentar. ")
