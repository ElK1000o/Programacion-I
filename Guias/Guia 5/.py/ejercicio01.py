# Escribe un programa python que pida un número por teclado y que cree un diccionario 
# cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.

f=True

diccionario={}

print("A continuación se le solicitará un número para definir la cantidad de elementos de un diccionario. ")

while f:
    try:
        x=int(input("Ingrese un número: "))
        assert x>0
        diccionario = {i: i**2 for i in range(1,x+1)}
        break
    except ValueError:
        print("El espacio no puede quedar en blanco/El valor no puede ser texto. ")
    except AssertionError:
        print("El valor debe ser un número entero mayor que 0.")

print(f"El diccionario es el siguiente")

for k in diccionario.keys():
    print(f"Clave = {k} -> valor = {diccionario[k]}. ")