# 4
# Desarrollar algoritmo que permita Pedir por Pantalla El Número de Personas que fueron a un recital y luego el número de entradas vendidas en la Preventa.
# Compare los valores para identificar si fueron todas las personas al Recital, si dejaron de asistir, o si asistieron de más (sin entradas).


while True:
    cant=int(input("Ingrese el número de personas que fueron al recital: "))
    if cant<=0:
        print("La cantidad de personas debe ser mayor a 0. ")
    else:
        break

while True:
    ent=int(input("Ingrese el número de entradas vendidas: "))
    if ent<=0:
        print("La cantidad de entradas debe ser mayor a 0.")
    else:
        break

mas=cant-ent
menos=ent-cant

if (cant-ent)==1:
    print(f"Asistió {mas} persona más que entradas vendidas. ")
elif (cant-ent)>=2:
    print(f"Asistieron {mas} personas más que entradas vendidas. ")
elif (ent-cant)==1:
    print(f"Asistió {menos} persona menos que entradas vendidas. ")
elif (ent-cant)>=2:
    print(f"Asistieron {menos} personas menos que entradas vendidas")
elif cant==ent:
    print("Todas las personas que compraron entradas asistieron al recital. ")