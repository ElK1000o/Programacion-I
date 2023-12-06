# Ejercicio 2
# Generar script en Python que a partir de una deuda y de un monto a pagar por un cliente, determine cuanto recibe de vuelto o si es 0 o si falto dinero para pagar.

deuda=0
pago=0

deuda=int(input("Ingrese el monto de la deuda: "))
pago=int(input("Ingrese el monto que pagará: "))

saldo=pago-deuda

if saldo>0:
    print(f"Tienes de vuelto: ${saldo}")
elif saldo==0:
    print(f"Pagaste lo justo, tu vuelto es: ${saldo}")
else:
    print(f"No completaste el pago de tu deuda.")
    print(f"Te faltan por pagar ${deuda-pago}")
