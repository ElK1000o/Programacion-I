# Ejercicio 02

lista=[]
f=True

while f:
    try:
        n=int(input("Digite la cantidad de numeros que desea ingresar: "))
        assert n>0
        break
    except ValueError:
        print("El espacio no puede quedar en blanco. ")
    except:
        print("El número debe ser mayor que cero. ")

print(f"A continuación deberás ingresar {n} números mayores que 0. ")
for i in range(n):
    while f:
        try:
            print(f"#{i+1}. ")
            numero=float(input("Ingrese el dato: "))
            assert numero>0
            lista.append(numero)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco/debe ser numérico. ")

lista.sort()

try:
    buscar=int(input("Digite el número que desea buscar: "))
    if buscar>0:
        for i in lista:
            if i==buscar:
                print(f"El numero está en la lista, ubicado en la posición #{lista.index(buscar)}")
            else:
                print("El numero no está en la lista. ")
except ValueError:
    print("El espacio no puede quedar en blanco/debe ser numérico. ")
   

