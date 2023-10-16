# 3
# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10 de un número entregado por el usuario.

numero=0

while True: #ciclo infinito
    numero=int(input("Ingresa un número entero mayor a 0: "))
    if numero>0 and numero%1==0:
        break
    else:
        print("El número debe ser entero (sin decimales) y positivo (mayor a 0)")


# Forma 1

for i in range(1, 11):
     print(f"{i*numero}, ", end="")

# Forma 2

for i in range(1, 11):
    if i==1:
        print(f"{i} X {numero} = {i*numero}")
    elif i==2:
        print(f"{i} X {numero} = {i*numero}")
    elif i==3:
        print(f"{i} X {numero} = {i*numero}")
    elif i==4:
        print(f"{i} X {numero} = {i*numero}")
    elif i==5:
        print(f"{i} X {numero} = {i*numero}")
    elif i==6:
        print(f"{i} X {numero} = {i*numero}")
    elif i==7:
        print(f"{i} X {numero} = {i*numero}")
    elif i==8:
        print(f"{i} X {numero} = {i*numero}")
    elif i==9:
        print(f"{i} X {numero} = {i*numero}")
    elif i==10:
        print(f"{i} X {numero} = {i*numero}")

# El orden de los factores "numero" e "i" se pueden invertir a gusto de cada quien