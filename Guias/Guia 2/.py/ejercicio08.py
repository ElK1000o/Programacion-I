# Ejercicio 8

# Desarrollar algoritmo que permita pedir por pantalla la categoría de entradas 
# (1.Platea, 2.Galería, 3.Palco) y cantidad de entradas vendidas. Realizar este proceso N veces e imprimir 
# finalmente la siguiente estadística:Suma Total De Entradas Vendidas.Suma De Entradas Vendidas De Platea.
# Suma De Entradas Vendidas De Galería.Suma De Entradas Vendidas De Palco.

while True:
    cant_platea=0
    cant_galeria=0
    cant_palco=0

    print("A continuación podrás solicitar las entradas que quieras comprar: ")

    while True:
        n=int(input("Ingrese la cantidad de entradas que desea: "))
        if n<=0:
            print("La cantidad debe ser mayor a 0. ")
        else:
            break
    for i in range (n):
        while True:
            print(f"Digite numericamente la categoria de entrada {i+1} que desea. ")
            cat=int(input("1. Platea 2. Galeria 3. Palco. "))
            if cat==1:
                cant_platea=cant_platea+1
                break
            elif cat==2:
                cant_galeria=cant_galeria+1
                break
            elif cat==3:
                cant_palco=cant_palco+1
                break
            else:
                print("El número ingresado no es válido. ")
    break

if n==1:
    print("Se vendió 1 entrada.")
else:
    print(f"El total de entradas vendidas es de {n}. ")

if cant_platea==0:
    print("No se vendieron entradas para Platea")
elif cant_platea==1:
    print(f"Para Platea se vendió {cant_platea} entrada.")
elif cant_platea>1:
    print(f"Para Platea se vendieron {cant_platea} entradas. ")

if cant_galeria==0:
    print("No se vendieron entradas para Galeria")
elif cant_galeria==1:
    print(f"Para Galeria se vendió {cant_galeria} entrada.")
elif cant_galeria>1:
    print(f"Para Galeria se vendieron {cant_galeria} entradas. ")

if cant_palco==0:
    print("No se vendieron entradas para Palco")
elif cant_palco==1:
    print(f"Para Palco se vendió {cant_palco} entrada.")
elif cant_palco>1:
    print(f"Para Palco se vendieron {cant_palco} entradas. ")
