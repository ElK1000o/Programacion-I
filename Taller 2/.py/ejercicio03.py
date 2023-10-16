# Ejercicio 3
# Generar script en Python que a partir del sueldo base se logre obtener el sueldo líquido, pero debe tener en cuenta los descuentos de salud y AFP.
# Descuento De Afp     => Habitat(11%), Capital (13%).
# Descuento De Salud => Fonasa(7%), Isapre(13%).
# Impuesto A La Renta=> 5% Si el Sueldo Base supera el $1.200.000.
# Sueldo Líquido          => Sueldo Base – Descto.Afp – Descto. Salud – Impuesto.

base=0
fonasa=.07
isapre=.13
habitat=.11
capital=.13
impuesto=.05
dcto_afp=0
dcto_prev=0

base=int(input("Ingrese su sueldo base: "))
if base>=1200000:
    imp=(base*impuesto)
elif base<1200000:
    imp=0


while True:
    afp=int(input("Ingresa tu AFP 1. Habitat 2. Capital: "))
    if afp==1 or afp==2:
        break
    else:
        print("Ingrese correctamente el número de la previsión que posees (1. Habitat 2. Capital): ")

if afp==1:
   dcto_afp=(base*habitat)
elif afp==2:
   dcto_afp=(base*capital)

while True:
    prevision=int(input("Ingresa tu previsión 1. Fonasa 2. Isapre: "))
    if prevision==1 or prevision==2:
        break
    else:
        print("Ingrese correctamente el número de la previsión que posees (1. Fonasa 2. Isapre): ")

if prevision==1:
    dcto_prev=(base*fonasa)
elif prevision==2:
    dcto_prev=(base*isapre)

print(f"El descuento por AFP es de: {dcto_afp}")
print(f"El descuento previsional es de: {dcto_prev}")
print(f"Por impuestos se descuentan: {imp}")

print(f"Tu sueldo líquido es: {base - dcto_afp - imp - dcto_prev}")