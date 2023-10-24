# Ejercicio 1

# Desarrollar programa que permita ingresar por pantalla los datos de N jugadores de fútbol (implemente try/except). 
# Defina funciones para la digitación de cada dato.Los datos a ingresar son: Posición De Juego : 
# 1-Delantero, 2-Mediocampista, 3-Defensa, 4.Portero. Edad Del Jugador : (Entre 10 y 50).
# Los jugadores serán clasificados y dicha clasificación dependerá de la edad:De tener una edad entre 10 y 17, será clasificado como juvenil.
# De tener una edad entre 18 y 50 será clasificado como adulto.Antes de terminar el programa debe imprimir los siguientes resultados:
# Cantidad Total De Jugadores. Promedio De Edad De Todos Los Jugadores. Cantidad Total De Jugadores Juveniles. Promedio De Edad De Jugadores juveniles.
# Cantidad De Jugadores Adulto. Promedio De Edad De Jugadores Adulto. Cantidad De Delanteros. Promedio De Edad De Delanteros. Cantidad De Mediocampistas.
# Promedio De Edad De Mediocampistas. Cantidad De Defensas. Promedio De Edad De Defensas. Cantidad De Porteros. Promedio De Edad De Porteros.

delanteros=[]
defensas=[]
medio=[]
porteros=[]
edades=[]
adultos=[]
juveniles=[]
suma_edades=0
f=True

while f:
    try:
        n=int(input("Indique cuantos jugadores de futbol desea ingresar: "))
        assert n>0
        break
    except ValueError:
        print("El espacio no puede quedar en blanco. ")
    except:
        print("El número debe ser mayor que cero. ")

for i in range(n):
    while f:
        try: 
            print(f"Ingrese numéricamente la posición del jugador {i+1}. ")
            posicion=int(input(f"1-Delantero, 2-Mediocampista, 3-Defensa, 4.Portero: "))
            assert posicion==1 or posicion==2 or posicion==3 or posicion==4
            break
        except ValueError:
            print("El espacio no puede quedar en blanco")
        except:
            print("Digito mal ingresado, pruebe nuevamente. ")
    while f:
        try:
            edad=int(input(f"Ingrese la edad del jugador {i+1} (debe ser entre 10 y 50): "))
            assert edad>=10 and edad<=50
            edades.append(edad)
            if edad>=10 and edad<=17 and posicion==1:
                juveniles.append(edad)
                delanteros.append(edad)
            elif edad>17 and edad<=50 and posicion==1:
                adultos.append(edad)
                delanteros.append(edad)
            elif edad>=10 and edad<=17 and posicion==2:
                juveniles.append(edad)
                medio.append(edad)
            elif edad>17 and edad<=50 and posicion==2:
                adultos.append(edad)
                medio.append(edad)
            elif edad>=10 and edad<=17 and posicion==3:
                juveniles.append(edad)
                defensas.append(edad)
            elif edad>17 and edad<=50 and posicion==3:
                adultos.append(edad)
                defensas.append(edad)
            elif edad>=10 and edad<=17 and posicion==4:
                juveniles.append(edad)
                porteros.append(edad)
            elif edad>17 and edad<=50 and posicion==4:
                adultos.append(edad)
                porteros.append(edad)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco")
        except:
            print("La edad debe ser entre 10 y 50 años. ")


for edad in edades:
    suma_edades += edad
prom=suma_edades/len(edades)

print(f"La cantidad total de jugadores es de: {n}")
print(f"El promedio general de edades es de: {prom}")

suma_edades=0
for edad in juveniles:
    suma_edades += edad

if len(juveniles)==0:
    print("No hay jugadores juveniles. ")
else:
    prom=suma_edades/len(juveniles)
    print(f"La cantidad de jugadores juveniles es de: {len(juveniles)}")
    print(f"El promedio general de edad en juveniles es de: {prom}")

suma_edades=0
for edad in adultos:
    suma_edades += edad

if len(adultos)==0:
    print("No hay jugadores adultos. ")
else:
    prom=suma_edades/len(adultos)
    print(f"La cantidad de jugadores adultos es de: {len(adultos)}")
    print(f"El promedio general de edad en adultos es de: {prom}")

suma_edades=0
for edad in delanteros:
    suma_edades+=edad

if len(delanteros)==0:
    print("No hay delanteros. ")
else:
    print(f"La cantidad de delanteros es de: {len(delanteros)}")
    print(f"El promedio de edades de los delanteros es de: {suma_edades/len(delanteros)}")

suma_edades=0
for edad in medio:
    suma_edades+=edad

if len(medio)==0:
    print("No hay mediocampistas. ")
else:
    print(f"La cantidad de mediocampistas es de: {len(medio)}")
    print(f"El promedio de edades de los mediocampistas es de: {suma_edades/len(medio)}")

suma_edades=0
for edad in defensas:
    suma_edades+=edad

if len(defensas)==0:
    print("No hay defensas. ")
else:
    print(f"La cantidad de defensas es de: {len(defensas)}")
    print(f"El promedio de edades de los defensas es de: {suma_edades/len(defensas)}")

suma_edades=0
for edad in porteros:
    suma_edades+=edad

if len(porteros)==0:
    print("No hay porteros. ")
else:
    print(f"La cantidad de porteros es de: {len(porteros)}")
    print(f"El promedio de edades de los porteros es de: {suma_edades/len(porteros)}")
