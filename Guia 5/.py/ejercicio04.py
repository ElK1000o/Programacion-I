# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase 
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la 
# información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán 
# listas con las notas de cada alumno.El programa pedirá el número de alumnos que vamos a introducir, 
# pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el 
# programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
# Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

from os import system

f=True
diccionario={}

def prom(x):
    a=0
    for i in x:
        a+=i
    if len(x)<1:
        print("Estudiante no tiene notas. ")
    else:
        prom=a/len(x)
    return prom

def promedio(x):
    for k in x.keys():
        print(f"Nombre = {k} -> Promedio de notas = {prom(x[k])}. ")
while f:
    while f:
        try:
            cant=int(input("Ingrese la cantidad de estudiantes que desea registrar: "))
            assert cant>0
            system("cls")
            break
        except ValueError:
            print("El espacio no puede quedar en blanco / Debe ser un numero. ")
        except AssertionError:
            print("La cantidad debe ser mayor que 0. ")
    print("A continuación se le solicitará el nombre del estudiante y posteriormente sus notas. ")
    while f:
        try:
            for i in range(cant):
                notas=[]
                while f:
                    nombre=input(f"Ingrese el nombre del estudiante {i+1}: ")
                    nombre=nombre.upper()
                    if nombre in diccionario:
                        print("Estudiante ya está en la lista. ")
                    else:
                        break
                nota=float(input("Ingrese nota. Una vez quiera terminar, sólo ingrese un número negativo (Ej. -1): "))
                while nota>0:
                    notas.append(nota)
                    nota=float(input("Ingrese nota. Una vez quiera terminar, sólo ingrese un número negativo (Ej. -1): "))
                diccionario[nombre]=notas
                system("cls")
            break
        except ValueError:
            print("El espacio no puede quedar en blanco / Debe ser un numero. ")
    break

print("Los promedios respectivos de cada estudiante son los siguientes: ")

promedio(diccionario)
