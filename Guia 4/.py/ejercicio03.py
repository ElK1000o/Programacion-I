# Ejercicio 03

lista=[]
f=True
n=10

print(f"A continuación deberás ingresar {n} números. ")
for i in range(n):
    while f:
        try:
            print(f"#{i+1}. ")
            numero=float(input("Ingrese el dato: "))
            lista.append(numero)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco/debe ser numérico. ")

lista.sort(reverse=True)

cant=0
try:
    buscar=int(input("Digite el número que desea buscar: "))
    if buscar>0:
        for i in lista:
            if i==buscar:
                cant=cant+1
except ValueError:
    print("El espacio no puede quedar en blanco/debe ser numérico. ")

print(f"El numero está en la lista {cant} veces.")