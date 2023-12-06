# Deberá desarrollar un programa que permita pedir por pantalla los datos de “N” Obras
# (Pinturas) de un museo: Precio, EsSlo y Especificación de Pintores. Considere que su programa
# debe:
# 1. Implementar while y try/except para validar.
# 2. Al ir ingresando los datos, indique la vuelta actual del ciclo.
# Los datos a ingresar son:
# • El precio de la pintura : Debe estar entre $1.000.000 y $10.000.000
# • Los Estilos De Pintura : 1-Realismo, 2-Surrealismo.
# • Los Pintores Son : 1-Van Gogh, 2-Salvador Dali, 3-Leonardo Da Vinci
# Debe generar las funciones para la digitación de los datos necesarios y para la presentación de
# los resultados:
# • digitarCantidadIngresos().
# • digitarPrecios().
# • digitarEstilos().
# • digitarPintores().
# • presentarResultados().

from os import system

def promedio(b):
    c=0
    for i in b:
        c+=i
    prom=c/len(b)
    return prom

def suma1(b):
    a=0
    for i in b:
        if i==1:
            a+=1
    return a

def suma2(b):
    a=0
    for i in b:
        if i==2:
            a+=1
    return a

def suma3(b):
    a=0
    for i in b:
        if i==3:
            a+=1
    return a

precio=0
pintor=[]
real=[]
surr=[]
precio_a=[]
precio_b=[]
precio_1=[]
precio_2=[]
precio_3=[]
f=True

print("A continuación, se le solicitarán los datos de la cantidad de obras que ud. elija. ")

while f:
    try:
        n=int(input("Digite la cantidad de personas que desea ingresar: "))
        assert n>0
        break
    except ValueError:
        print("El espacio no puede quedar en blanco. ")
    except:
        print("El número debe ser mayor que cero. ")

for i in range(n):
    while f:
        try:
            print(f"Ingrese el estilo de la pintura #{i+1}. ")
            est=int(input("1-Realismo, 2-Surrealismo: "))
            assert est==1 or est==2
            if est==1:
                real.append(est)
            elif est==2:
                surr.append(est)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco. ")
        except:
            print("Ingrese correctamente el número. ")
    system("cls")
    while f:
        try:
            print(f"Ingrese el pintor de la obra #{i+1}. ")
            pint=int(input("1-Van Gogh, 2-Salvador Dali, 3-Leonardo Da Vinci: "))
            assert pint==1 or pint==2 or pint==3
            pintor.append(pint)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco. ")
        except:
            print("Ingrese correctamente el número. ")
    system("cls")
    while f:
        try:
            prec=int(input("Digite el precio de la pintura. (debe ser entre $1.000.000 y $10.000.000): "))
            assert prec>=1000000 and prec<=10000000
            if pint==1:
                precio_1.append(prec)
            elif pint==2:
                precio_2.append(prec)
            elif pint==3:
                precio_3.append(prec)
            elif est==1:
                precio_a.append(prec)
            elif est==2:
                precio_b.append(prec)
            break   
        except ValueError:
            print("El espacio no puede quedar en blanco. ")
        except:
            print("Ingrese correctamente el precio. (debe ser entre $1.000.000 y $10.000.000)")
    system("cls")

if n==1:
    print("Se digitó una pintura. ")
else:
    print(f"La cantidad total de pinturas es: {n}. ")

if len(real)>0:
    print(f"La cantidad de pinturas con estilo realista son: {len(real)}. ")
else:
    print("No hay pinturas con estilo realista. ")

if len(surr)>0:
    print(f"La cantidad de pinturas con estilo surrealista son: {len(surr)}. ")
else:
    print("No hay pinturas con estilo surrealista. ")

if len(precio_a)>0:
    print(f"El promedio de precios de las obras estilo realistas es de: {promedio(precio_a)}. ")
else:
    print("No hay pinturas con estilo surrealista para promedio de precio. ")

if len(precio_b)>0:
    print(f"El promedio de precios de las obras estilo realistas es de: {promedio(precio_b)}. ")
else:
    print("No hay pinturas con estilo realista para promedio de precio. ")

if len(precio_1)>0:
    print(f"El promedio de precios de las obras de Van Gogh es de: {promedio(precio_1)}. ")
else:
    print("No hay pinturas de Van Gogh para promedio de precio. ")

if len(precio_2)>0:
    print(f"El promedio de precios de las obras de Salvador Dali es de: {promedio(precio_2)}. ")
else:
    print("No hay pinturas de Salvador Dali para promedio de precio. ")

if len(precio_3)>0:
    print(f"El promedio de precios de las obras de Leonardo Da Vinci es de: {promedio(precio_3)}. ")
else:
    print("No hay pinturas de Leonardo Da Vinci para promedio de precio. ")

if len(pintor)>0:
    if suma1(pintor)>0:
        print(f"La cantidad de obras de Van Gogh es de {suma1(pintor)}. ")
        if suma1(real)>0:
            print(f"La cantidad de obras con estilo realista de Van Gogh es de {suma1(real)}. ")
        else:
            print("No hay obras realistas de Van Gogh. ")
        if suma1(surr)>0:
            print(f"La cantidad de obras con estilo surrealista de Van Gogh es de {suma1(surr)}. ")
        else:
            print("No hay obras surrealistas de Van Gogh. ")
    else:
        print("No hay obras de Van Gogh. ")
        
    if suma2(pintor)>0:
        print(f"La cantidad de obras de Salvador Dali es de {suma2(pintor)}. ")
        if suma2(real)>0:
            print(f"La cantidad de obras con estilo realista de Salvador Dali es de {suma2(real)}. ") 
        else:
            print("No hay obras realistas de Salvador Dali. ")
        if suma2(surr)>0:
            print(f"La cantidad de obras con estilo surrealista de Salvador Dali es de {suma2(surr)}. ")
        else:
            print("No hay obras surrealistas de Salvador Dali. ")
    else:
        print("No hay obras de Salvador Dali. ")

    if suma3(pintor)>0:
        print(f"La cantidad de obras de Leonardo Da Vinci es de {suma3(pintor)}. ")
        if suma3(real)>0:
            print(f"La cantidad de obras con estilo realista de Leonardo Da Vinci es de {suma3(real)}. ")
        else:
            print("No hay obras realistas de Leonardo Da Vinci. ")
        if suma3(surr)>0:
            print(f"La cantidad de obras con estilo surrealista de Leonardo Da Vinci es de {suma3(surr)}. ")
        else:
            print("No hay obras surrealistas de Leonardo Da Vinci. ")
    else:
        print("No hay obras de Leonardo Da Vinci. ")

print("Programa terminado. ")
system("pause")
system("cls")
