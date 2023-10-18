# Ejercicio 7

# Desarrollar algoritmo que permita imprimir en pantalla una secuencia de números, 
# la cual será dada por números que se incrementen de 2 en 2 hasta llegar al 20, además,
# al término de las iteraciones debe imprimir los siguientes promedios:
# Promedio de secuencia de números que sean mayores o iguales a 10.Promedio de secuencia de números que sean menores a 10.

bajo=0
sobre=0
men_10=[]
may_10=[]
num=[]

print("Frecuencia de numeros 2 al 20 (2 en 2): ")

for i in range(2, 21, 2):
        if i>=2 and i<10:
            men_10.append(i)
            print(f"{i}")
        elif i>=10 and i<=20:
            may_10.append(i)
            print(f"{i}")

for i in men_10:
     bajo+=i
     prom_men=(bajo/len(men_10))

for i in may_10:
     sobre+=i
     prom_may=(sobre/len(may_10))

print(f"El promedio de los numeros mayores o iguales a 10 en la secuencia es de: {prom_may}. ")
print(f"El promedio de los numeros menores a 10 en la secuencia es de: {prom_men}. ")
