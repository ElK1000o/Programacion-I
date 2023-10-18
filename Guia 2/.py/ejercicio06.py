# Ejercicio 6

# Desarrollar algoritmo que permita pedir por pantalla el ingreso de N notas de un alumno. 
# Valide que las notas estén entre 1 y 7. Imprima la siguiente estadística:
# Promedio General De Notas. Promedio De Notas Rojas. Promedio De Notas Azules.

while True:
    sum_not=0
    sum_roj=0
    sum_az=0
    rojo=0
    azul=0
    notas = []
    azules = []
    rojos = []

    print("A continuación te pediré que ingreses tus notas.")

    while True:
        n=int(input("Cuantas notas tienes actualmente en el ramo? "))
        if n==0:
            print("No tienes notas, no necesitas sacar tu promedio. ")
            break
        elif n<0:
            print("Tu cantidad de notas no puede ser negativa. ")
        else:
            for i in range(n):
                while True:
                    nota = float(input(f"Indique la nota {i + 1}: "))
                    if nota < 1 or nota > 7:
                        print("La nota no puede ser menor a 1 ni mayor a 7.")
                    elif nota>=1 and nota<4:
                        rojos.append(nota)
                        notas.append(nota)
                        break
                    elif nota>=4:
                        azules.append(nota)
                        notas.append(nota)
                        break
            for nota in notas:
                sum_not += nota
                if nota<4:
                    rojo=rojo+1
                elif nota>=4:
                    azul=azul+1
                prom=(sum_not/n)
            for nota in rojos:
                sum_roj += nota
                prom_roj=(sum_roj/rojo)
            for nota in azules:
                sum_az += nota
                prom_az=(sum_az/azul)
            print(f"Tu promedio general de notas es de: {prom}. ")
            print(f"Tu promedio de notas rojas es de: {prom_roj}. ")
            print(f"Tu promedio de notas azules es de: {prom_az}. ")
            break
    break
        