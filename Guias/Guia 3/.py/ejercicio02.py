# Ejercicio 2

# Desarrollar programa que permita ingresar por pantalla los datos de N jugadores de voleibol (implemente try/except). 
# Defina funciones para la digitación de cada dato.Los datos a ingresar son: Posición De Juego : 
# 1-Delantero, 2-Zaguero, 3-Libero.Equipo Del Jugador : 1-Ciutadella, 2-Teruel. Edad Del Jugador : (Entre 14 y 28 años).
# Además, antes de terminar el programa debe imprimir los siguientes resultados: Cantidad De Jugadores Según Equipo:
# Cantidad De Jugadores Del Equipo Ciutadella. Cantidad De Jugadores De Equipo Teruel. Cantidad De Jugadores Según Posición:
# Cantidad De Jugadores Con Posición Delantero. Cantidad De Jugadores Con Posición Zaguero. Cantidad De Jugadores Con Posición Libero.
# Cantidad De Jugadores Según Equipo y Posición: Cantidad De Jugadores Con Posición Delantero De Ciutadella.
# Cantidad De Jugadores Con Posición Delantero De Teruel. Cantidad De Jugadores Con Posición Zaguero De Ciutadella.
# Cantidad De Jugadores Con Posición Zaguero De Teruel. Cantidad De Jugadores Con Posición Libero De Ciutadella.
# Cantidad De Jugadores Con Posición Libero De Teruel. Promedio General De Edades De Todos Los Jugadores.

del_1=[]
del_2=[]
zag_1=[]
zag_2=[]
lib_1=[]
lib_2=[]
edades=[]
suma_edades=0
f=True

while True:
    try:
        n=int(input("Indique cuantos jugadores de voleibol desea ingresar: "))
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
            posicion=int(input(f"1-Delantero, 2-Zaguero, 3-Libero: "))
            assert posicion==1 or posicion==2 or posicion==3
            break
        except ValueError:
            print("El espacio no puede quedar en blanco")
        except:
            print("Digito mal ingresado, pruebe nuevamente. ")
    while f:
        try:
            print(f"Ingrese el equipo del jugador {i+1}. ")
            equ=int(input("1-Ciutadella, 2-Teruel: "))
            assert equ==1 or equ==2
            if equ==1 and posicion==1:
                del_1.append(equ)
            elif equ==1 and posicion==2:
                zag_1.append(equ)
            elif equ==1 and posicion==3:
                lib_1.append(equ)
            elif equ==2 and posicion==1:
                del_2.append(equ)
            elif equ==2 and posicion==2:
                zag_2.append(equ)
            elif equ==2 and posicion==3:
                lib_2.append(equ)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco. ")
        except:
            print("Digito mal ingresado, intente nuevamente. ")
    while f:
        try:
            edad=int(input(f"Ingrese la edad del jugador {i+1} (debe ser entre 14 y 28): "))
            assert edad>=14 and edad<=28
            edades.append(edad)
            break
        except ValueError:
            print("El espacio no puede quedar en blanco")
        except:
            print("La edad debe ser entre 14 y 28 años. ")

for edad in edades:
    suma_edades += edad

prom=suma_edades/n
ciutadella=len(del_1)+len(zag_1)+len(lib_1)
teruel=len(del_2)+len(zag_2)+len(lib_2)
delanteros=len(del_1)+len(del_2)
zagueros=len(zag_1)+len(zag_2)
liberos=len(lib_1)+len(lib_2)

if ciutadella==0:
    print("No hay jugadores de Ciudatella. ")
else:
    print(f"La cantidad de jugadores del equipo Ciutadella es de: {ciutadella}")
    if len(del_1)==0:
        print("Ciudatella no tiene delanteros. ")
    else:
        print(f"La cantidad de jugadores con posición delantero de Ciudatella es de: {len(del_1)}")
    if len(zag_1)==0:
        print("Ciudatella no tiene zagueros. ")
    else:
        print(f"La cantidad de jugadores con posición zaguero de Ciudatella es de: {len(zag_1)}")
    if len(lib_1)==0:
        print("Ciudatella no tiene liberos. ")
    else:
        print(f"La cantidad de jugadores con posición libero de Ciudatella es de: {len(lib_1)}")
if teruel==0:
    print("No hay jugadores de Teruel. ")
else:
    print(f"La cantidad de jugadores del equipo Teruel es de: {teruel}")
    if len(del_2)==0:
        print("Teruel no tiene delanteros. ")
    else:
        print(f"La cantidad de jugadores con posición delantero de Teruel es de: {len(del_2)}")
    if len(zag_2)==0:
        print("Teruel no tiene zagueros. ")
    else:
        print(f"La cantidad de jugadores con posición zaguero de Teruel es de: {len(zag_2)}")
    if len(lib_2)==0:
        print("Teruel no tiene liberos. ")
    else:
        print(f"La cantidad de jugadores con posición libero de Teruel es de: {len(lib_2)}")

if delanteros==0:
    print("No hay jugadores delanteros en ningun equipo. ")
else:
    print(f"La cantidad de jugadores con posición delantero es de: {delanteros}")

if zagueros==0:
    print("No hay jugadores zagueros en ningun equipo. ")
else:    
    print(f"La cantidad de jugadores con posición zaguero es de: {zagueros}")

if liberos==0:
    print("No hay jugadores liberos en ningun equipo. ")
else:
    print(f"La cantidad de jugadores con posición libero es de: {liberos}")

print(f"El promedio general de edades de los jugadores es de: {prom}")
