# 2
# Desarrollar algoritmo que permita pedir el ingreso del precio de un producto y la cantidad comprada del mismo. 
# Debe obtener el valor neto (precio * cantidad), calcular el iva (neto * 19%) y luego determinar el total (Valor Neto + Iva). Imprima todos los datos.

iva=.19

while True:
    precio=int(input("Indique el precio del producto deseado: "))
    if precio>0:
        break
    elif precio<=0:
        print("El precio debe ser mayor a 0, indique el valor nuevamente: ")

while True:
    cantidad=int(input("Indique la cantidad del producto deseado: "))
    if cantidad>0:
        break
    elif cantidad<=0:
        print("La cantidad debe ser mayor a 0, indique el valor nuevamente: ")

neto=int(precio*cantidad)
iva_=int(neto*iva)
bruto=neto+iva_

print(f"El monto neto de tu compra es de ${neto}. ")
print(f"El iva total de tu compra es de ${iva_}. ")
print(f"El monto bruto o total de tu compra es de ${bruto}. ")