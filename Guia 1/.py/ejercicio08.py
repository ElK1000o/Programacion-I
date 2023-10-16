# 8
# Desarrollar Algoritmo que permita pedir el ingreso de 4 insumos de la compra en un supermercado, indicando el nombre, su precio y el día de la compra con números (1, 2,3, 4, 5, 6 y7). 
# Determine el total de la compra, pero recuerde aplicar el descuento sobre dicho total dependiendo del día.
# El día lunes tendrá descuento de 10%.El día miércoles tendrá descuento del 15%.El día viernes tendrá descuento del 20%

n = 4 
dcto_lun=.9
dcto_mie=.85
dcto_vie=.8
sum_prec = 0

print(f"A continuación te pediré que ingreses los {n} insumos de la compra de supermercado.")

# Solicitud Insumos y Precio

while True:
    insumos = []
    precios = []
    for i in range(n):
        while True:
            insumo = input(f"Indique el insumo {i + 1}: ")
            if len(insumo) == 0:
                print("El insumo no puede quedar en blanco.")
            else:
                insumos.append(insumo)
                break
        while True:
            precio = int(input("Indique el precio del insumo: "))
            if precio <= 0:
                print("El precio debe ser un número mayor a 0.")
            else:
                precios.append(precio)
                break
    break

# Calculo precio total de productos

for precio in precios:
    sum_prec += precio

# Solicitud día de compra

while True:
    print("ingrese numéricamente el día de la compra.")
    dia=int(input("Siendo 1.Lunes 2.Martes, 3.Miercoles 4.Jueves 5.Viernes 6.Sabado 7.Domingo: "))
    if dia==1 or dia==2 or dia==3 or dia==4 or dia==5 or dia==6 or dia==7:
        break
    else:
        print("El día está mal ingresado, hágalo de nuevo. ")

# Calculo de precio total según día de compra

if dia==1:
    total=(sum_prec*dcto_lun)
    print(f"Insumos ingresados: {insumos}")
    print(f"Precios ingresados: {precios}")
    print(f"El valor de sus productos es de: {sum_prec}")
    print("Por comprar el lunes tiene 10% de dcto")
    print(f"El total de su la lista es: {total}")
elif dia==3:
    total=(sum_prec*dcto_mie)
    print(f"Insumos ingresados: {insumos}")
    print(f"Precios ingresados: {precios}")
    print(f"El valor de sus productos es de: {sum_prec}")
    print("Por comprar el miercoles tiene 15% de dcto")
    print(f"El total de su la lista es: {total}")
elif dia==5:
    total=(sum_prec*dcto_vie)
    print(f"Insumos ingresados: {insumos}")
    print(f"Precios ingresados: {precios}")
    print(f"El valor de sus productos es de: {sum_prec}")
    print("Por comprar el viernes tiene 20% de dcto")
    print(f"El total de su la lista es: {total}")
elif dia==2 or dia==4 or dia==6 or dia==7:
    print(f"Insumos ingresados: {insumos}")
    print(f"Precios ingresados: {precios}")
    print(f"El total de su la lista es: {sum_prec}")
