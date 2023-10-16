# 9
# Desarrollar Algoritmo que permita Ingresar la edad de una persona y determine la fase de vida enla que encuentra bajo las siguientes consideraciones de rango de edad:
# Entre 1 y 6 años está en fase de “Infancia”.
# Entre 7 y 12 años está en fase de “Niñez”.
# Entre 13 y 15 años está en fase de “Preadolescencia”.
# Entre 16 y 21 años está en fase de “Adolescencia”.
# Entre 22 y 35 años está en fase de “Adultez Joven”.
# Entre 36 y 60 años está en fase de “Adultez Madura”.
# Más de 60 años está en fase de “Adultez Mayor”

while True:
    edad=int(input("Ingrese su edad (debe ser mayor a 0): "))
    if edad<=0:
        print("La edad debe ser mayor que 0. ")
    else:
        break

if edad>=1 and edad<=6:
    print("Usted se encuentra en la fase de Infancia. ")
elif edad>=7 and edad<=12:
    print("Usted se encuentra en la fase de Niñez. ")
elif edad>=13 and edad<=15:
    print("Usted se encuentra en la fase de “Preadolescencia”. ")
elif edad>=16 and edad<=21:
    print("Usted se encuentra en la fase de “Adolescencia”. ")
elif edad>=22 and edad<=35:
    print("Usted se encuentra en la fase de Adultez Joven. ")
elif edad>=36 and edad<=60:
    print("Usted se encuentra en la fase de Adultez Madura. ")
elif edad>60:
    print("Usted se encuentra en la fase de Adultez Mayor. ")
