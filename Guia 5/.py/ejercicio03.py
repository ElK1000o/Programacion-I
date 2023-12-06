# Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
# El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a 
# partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa 
# nos preguntará si queremos hacer otra consulta.

from os import system

f=True
diccionario={"MANZANA":300,"PLATANO":750,"FRUTILLA":150,"MANGO":1500,"DURAZNO":450,"DAMASCO":500,"PIÑA":1800,"MELON":2500,"SANDIA":3000}

def Buscar():
    while f:
        system("cls")
        fruta=input("Ingrese la fruta: ")
        fruta=fruta.upper()
        try: 
            cant=int(input("Ingrese la cantidad que se ha vendido: "))
            assert cant>0
            if fruta in diccionario:
                if fruta in diccionario:
                    precio= diccionario[fruta] * cant
                    print(f"Fruta: {fruta} - Precio Unitario: {diccionario[fruta]} - Cantidad: {cant} - Precio Final: {precio}")
                system("pause")
                Consulta()
            else:
                print("La fruta no está en la lista. ")
                system("pause")
                Consulta()
        except ValueError:
            print("El espacio no puede quedar en blanco / Debe ser un numero. ")
            system("pause")
        except AssertionError:
            print("La cantidad debe ser mayor que 0. ")
            system("pause")
    return

def Consulta():
    system("cls")
    while f:
        print("Desea buscar otra vez? ")
        print()
        print("1. Si, ealizar otra busqueda. ")
        print("2. No, salir. ")
        print()
        try:
            opcion=int(input("Ingrese la opción: "))
            assert opcion==1 or opcion==2
            if opcion==1:
                Buscar()
            elif opcion==2:
                Salir()
        except ValueError:
            system("cls")
            print("El espacio no puede quedar en blanco / Debe ser un numero. ")
            system("pause")
        except AssertionError:
            system("cls")
            print("Ingrese correctamente el valor. ")
            system("pause")

def Salir():
    exit(0)

Buscar()