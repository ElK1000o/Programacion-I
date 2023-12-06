# Ejercicio 04

from os import system

n=5
lista=[]
f=True

def SumaTodo(a):
    b=0
    for i in a:
        b+=i
    return b

def SumaMas18(a):
    b=0
    for i in a:
        if i>=18:
            b+=i
    return b

def SumaMen18(a):
    b=0
    for i in a:
        if i <18:
            b+=i
    return b

print(f"A continuación deberás ingresar {n} edades. ")
for i in range(n):
    while f:
        try:
            print(f"#{i+1}. ")
            numero=float(input("Ingrese la edad: "))
            assert numero>0
            if numero>0:
                lista.append(numero)
            else:
                print("La edad no puede ser menor que 1. ")
            break
        except ValueError:
            print("El espacio no puede quedar en blanco/debe ser numérico. ")

print("Qué desea hacer con estos datos?")

while f:
        try:
            print("1-Sumar todas las edades, 2-Sumar edades mayores o iguales a 18, ")
            est=int(input("3- Sumar edades menores a 18, 4- Salir: "))
            assert est>=1 and est<=4
            if est==1:
                print(f"La suma de todas las edades es de: {SumaTodo(lista)}. ")
            elif est==2:
                print(f"La suma de edades mayores o iguales a 18 es de: {SumaMas18(lista)}. ")
            elif est==3:
                print(f"La suma de edades menores a 18 es de: {SumaMen18(lista)}. ")
            else:
                print("Fin del programa")
                system("pause")
                system("cls")
            break
        except ValueError:
            print("El espacio no puede quedar en blanco. ")
        except:
            print("Ingrese correctamente el número. ")
