# Ejercicio 05

lista=[]
n=5
f=True

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

print(f"El número menor de la lista es {min(lista)}")
print(f"El número mayor de la lista es {max(lista)}")
