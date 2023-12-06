# Crear programa de menu con opciones

# Opcion 1. Agregar marca automoviles.
# Opcion 2. Listar marcas agregadas.
# Opcion 3. Buscar una marca.
# Opcion 4. Salir.

from os import system

def Menu():

    lista_marcas=[]

    while True:
        op=0
        system("cls")
        print("----------------------")
        print("    MENU PRINCIPAL   ")
        print("----------------------")
        print()
        print("1. Agregar marca. ")
        print("2. Listar marca. ")
        print("3. Buscar marca. ")
        print("4. Salir. ")
        print()
        
        try:
            op=int(input("Ingrese numérciamente la opcion del menu: "))   
            if op==1:
                lista_marcas = Agregar(lista_marcas)
            elif op==2:
                Listar(lista_marcas)        
            elif op==3:
                Buscar(lista_marcas)
            elif op==4:
                Salir() 
        except ValueError:
            print("El espacio no puede quedar en blanco / El valor debe ser numérico y corresponder. ")
            system("pause")

def Agregar(lista_marcas):

    system("cls")
    print("----------------------")
    print("    AGREGAR MARCAS   ")
    print("----------------------")
    print()
    marca=input("Ingrese una marca: ")
    lista_marcas.append(marca.upper())
    return lista_marcas

def Listar(lista_marcas):
    system("cls")
    print("---------------------")
    print("    LISTAR MARCAS   ")
    print("---------------------")
    print()
    for i in lista_marcas:
        print(f"Marca: {i}")
    system("pause")
    return


def Buscar(lista_marcas):
    system("cls")
    print("---------------------")
    print("    BUSCAR MARCAS   ")
    print("---------------------")
    print()
    marca=input("Ingrese la marca a buscar: ")
    marca=marca.upper()
    if marca in lista_marcas:
        print(f"La marca está en la lista. ")
    else:
        print("La marca no está en la lista. ")
    system("pause")
    return

def Salir():
    exit(0)

# Iniciar Programa

Menu()