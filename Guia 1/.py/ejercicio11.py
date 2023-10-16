# 11
# Desarrollar Algoritmo que permita ingresar un “Código de departamento”, un “Precio de Compra” y Una “Cantidad” de productos comprados. 
# A partir del código ingresado, el programa debe permitir Calcular el valor total final aplicando el descuento correspondiente según el código
# CODIGO NOMBRE DEPTO DESCUENTO
# 1 Deporte 30%
# 2 Tecnología 5%
# 3 Electrodomésticos 20%
# 4 Niños 15%
# La impresión final de resultados debe aparecer como muestra a continuación:
# Nombre Depto. : “Depende del código digitado” Precio Compra. : “Ingresado por el usuario” Cantidad: “Ingresado por el usuario” Total: “Valor Calculado: Precio * cantidad” 
# Descuento: “Valor Calculado: Porcentaje de descuento según el código”Total Final:“Valor Calculado: Total - Descuento

dcto_1=.7
dcto_2=.95
dcto_3=.8
dcto_4=.85

print("A continuación deberá elegir una categoria de compra. ")
print("Siendo:")

while True:
    while True:
        print("1. Deporte")
        print("2. Tecnologia")
        print("3. Electrodomésticos")
        print("4. Niños")
        cat=int(input("Ingrese el número correspondiente: "))
        if cat==1 or cat==2 or cat==3 or cat==4:
            break
        else:
            print("El código ingresado no es válido. ")
    while True:
        precio=int(input("Digite el precio del producto que desea comprar: "))
        if precio<=0:
            print("El precio debe ser mayor a 0. ")
        else:
            break
    while True:
        cant=int(input("Coloque la cantidad de productos que llevará: "))
        if cant<=0:
            print("La cantidad de productos debe ser mayor a 0. ")
        else:
            break
    break

total=cant*precio

if cat==1:
    depto="Deporte"
    dcto=total*(1-dcto_1)
    final=total*dcto_1
elif cat==2:
    depto="Tecnologia"
    dcto=total*(1-dcto_2)
    final=total*dcto_2
elif cat==3:
    depto="Electrodomesticos"
    dcto=total*(1-dcto_3)
    final=total*dcto_3
elif cat==4:
    depto="Niños"
    dcto=total*(1-dcto_4)
    final=total*dcto_4

print(f"Nombre del departamento: {depto}.")
print(f"Llevas {cant} de productos de ${precio} c/u. ")
print(f"Su precio total es de: {int(total)}.")
print(f"El descuento obtenido por la categoría de compra es: {int(dcto)}")
print(f"Su total final es de: {int(final)}")
