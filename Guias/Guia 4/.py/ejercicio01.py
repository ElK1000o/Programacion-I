# Ejercicio 01

lista=[]
f=True
n=3
print("A continuación deberás ingresar 3 números")
for i in range(n):
    while f:
        try:
            print(f"#{i+1}. ")
            numero=float(input("Ingrese el dato: "))
            lista.append(numero)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco/debe ser numérico. ")

for i in lista:
    print(i)

