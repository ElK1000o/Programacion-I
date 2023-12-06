# 10
# Desarrollar Algoritmo que permita Ingresar las 4 notas de un alumno, junto con su respectiva ponderación o porcentaje de incidencia en el promedio. 
# Considere que la suma de las ponderaciones debe ser de un 100% para lograr realizar el cálculo del promedio, ya que, de no serasí, presente en pantalla un mensaje de error.
# Una vez obtenido el promedio, determine si el alumno debe rendir examen o no. Paraello debe asegurarse de que el promedio sea superior o igual 5.0, y además ninguna nota debe ser roja.
# En caso de que sí deba rendir examen, el promedio de presentación tiene unaponderación del 75%, mientras que la nota que obtenga del examen tendrá una ponderación del 25%.
# Imprima en pantalla el detalle completo del alumno como en el siguiente formato de ejemplo:
# Nota 1 (20%)Nota 2 (25%)Nota 3 (30%)Nota 4 (25%)Promedio: 3,6Nota Examen: 4,6 Situación Final: Reprobado Con Promedio 3,9

npe=.75
examen=.25

# Solicitud notas y porcentajes

while True:
    n = 4
    sum_prc=0
    sum_nts=0
    notas = []
    porcentajes = []

    print(f"A continuación te pediré que ingreses tus {n} notas y su respectivo porcentaje en el ramo.")

    for i in range(n):
        while True:
            try:
                nota = float(input(f"Indique la nota {i + 1}: "))
                assert nota>=1 and nota<=7
                notas.append(nota)
                break
            except AssertionError:
                print("La nota no puede ser menor a 1 ni mayor a 7.")
        while True:
            porcentaje = int(input(f"Indique el porcentaje de la nota {i + 1}: "))
            if porcentaje < 0 or porcentaje > 100:
                print("El porcentaje no puede ser menor a 0 ni mayor a 100.")
            else:
                porcentajes.append(porcentaje)
                break
    for porcentaje in porcentajes:
        sum_prc += porcentaje
    if sum_prc!=100:
        print("La suma de los porcentajes ingresados debe dar 100.")
        print("ingrese todo nuevamente asegurándose de colocar correctamente cada porcentaje. ")
    else:
        break   

# Calculos suma notas y promedio

for nota in notas:
    sum_nts += nota
prom=sum_nts/n
rojo=0

for nota in notas:
    if nota<4:
        rojo=rojo+1

# Comprobaciones rendición examen + Aprobado/Reprobado

while True:
    if prom>=5 and rojo==0:
        for nota, porcentaje in zip(notas, porcentajes):
            print(f"Nota {nota} ({porcentaje}%)")
        print(f"Situación final: Aprobado con promedio {prom} (100%). ")
        print("Felicidades, pasaste y te eximiste del examen. ")
        break
    elif prom>=5 and rojo>0:
        print(f"Tu promedio es {prom}, lo necesario para eximirte. ")
        print(f"Sin embargo tienes {rojo} notas rojas, debes dar examen. ")
        notaexamen=float(input("Ingrese la nota obtenida en el examen: "))
        final=(npe*prom)+(examen*notaexamen)
        if final>=4:
            for nota, porcentaje in zip(notas, porcentajes):
                print(f"Nota {nota} ({porcentaje}%)")
            print(f"Promedio: {prom} (75%)")
            print(f"Nota examen: {notaexamen} (25%)")
            print(f"Situación final: Aprobado con promedio {final} (100%). ")
            print("Felicidades, pasaste. ")
        elif final<4:
            for nota, porcentaje in zip(notas, porcentajes):
                print(f"Nota {nota} ({porcentaje}%)")
            print(f"Promedio: {prom} (75%)")
            print(f"Nota examen: {notaexamen} (25%)")
            print(f"Situación final: Reprobado con promedio {final} (100%). ")
            print("No pasaste. ")
        break
    elif prom<5:
        print(f"Tu promedio de presentación es {prom}. ")
        print("Debes rendir examen. ")
        notaexamen=float(input("Ingrese la nota obtenida en el examen: "))
        final=(npe*prom)+(examen*notaexamen)
        if final>=4:
            for nota, porcentaje in zip(notas, porcentajes):
                print(f"Nota {nota} ({porcentaje}%)")
            print(f"Promedio: {prom} (75%)")
            print(f"Nota examen: {notaexamen} (25%)")
            print(f"Situación final: Aprobado con promedio {final} (100%). ")
            print("Felicidades, pasaste. ")
        elif final<4:
            for nota, porcentaje in zip(notas, porcentajes):
                print(f"Nota {nota} ({porcentaje}%)")
            print(f"Promedio: {prom} (75%)")
            print(f"Nota examen: {notaexamen} (25%)")
            print(f"Situación final: Reprobado con promedio {final} (100%). ")
            print("No pasaste. ")
        break
