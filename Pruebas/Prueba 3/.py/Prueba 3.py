# Prueba 3

from os import system

f=True
diccionario={}

def Menu():

    lista_pizzas=[]

    while True:
        op=0
        system("cls")
        print("----------------------")
        print("    MENU PRINCIPAL   ")
        print("----------------------")
        print()
        print("1. Agregar pizza. ")
        print("2. Listar todas las pizzas. ")
        print("3. Eliminar pizzas medianas. ")
        print("4. Eliminar pizzas familiares. ")
        print("5. Listar estadística. ")
        print("6. Buscar venta. ")
        print("7. Salir. ")
        print()
        
        try:
            op=int(input("Ingrese numérciamente la opcion del menu: "))
            assert op>=1 and op<=7   
            if op==1:
                lista_pizzas = Agregar(lista_pizzas)
            elif op==2:
                Listar(diccionario)        
            elif op==3:
                eliminar_mediana(diccionario)
            elif op==4:
                eliminar_familiar(diccionario)
            elif op==5:
                estadistica(diccionario)
            elif op==6:
                Buscar(diccionario)
            elif op==7:
                Salir() 
        except ValueError:
                print("El espacio no puede quedar en blanco / El valor debe ser numérico. ")
                system("pause")
                system("cls")
        except AssertionError:
                print("Ingrese correctamente el valor. ")
                system("pause")
                system("cls")   

def Agregar(lista_pizzas):
    lista_pizzas=[]
    pedido=(len(diccionario))+1
    system("cls")
    print("-----------------------")
    print("    AGREGAR PIZZA/S   ")
    print("-----------------------")
    print()
    print("A continuacion armaremos tu pizza. ")
    while f:
        print()
        print("1. MASA NORMAL - Valor: $6.000. ")
        print("2. MASA A LA PIEDRA - Valor: $7.500. ")
        try:
            masa=int(input("Ingrese el tipo de masa que desea: "))
            assert masa==1 or masa==2
            if masa==1:
                masa="MASA NORMAL ($6.000)"
                precio1=6000
                lista_pizzas.append(masa)
                break
            elif masa==2:
                masa="MASA A LA PIEDRA ($7.500)"
                precio1=7500
                lista_pizzas.append(masa)
                break
        except ValueError:
                print("El espacio no puede quedar en blanco / El valor debe ser numérico. ")
        except AssertionError:
                print("Ingrese correctamente el valor. ")
        system("pause")
        system("cls")
    while f:    
        print()
        print("1. MEDIANA - Valor: $6.000. ")
        print("2. FAMILIAR - Valor: $8.000. ")       
        try:
            tam=int(input("Ingrese el tamaño de pizza que desea: "))
            assert tam==1 or tam==2
            if tam==1:
                tam="MEDIANA ($6.000)"
                precio2=6000
                lista_pizzas.append(tam)
                break
            elif tam==2:
                tam="FAMILIAR ($8.000)"
                precio2=8000
                lista_pizzas.append(tam)
                break
        except ValueError:
                print("El espacio no puede quedar en blanco / El valor debe ser numérico. ")
        except AssertionError:
                print("Ingrese correctamente el valor. ")
        system("pause")
        system("cls")
    precio=precio1+precio2
    lista_pizzas.append(precio)
    diccionario[pedido]=(lista_pizzas)
    return

def Listar(diccionario):
    system("cls")
    print("----------------------")
    print("    LISTAR PIZZA/S   ")
    print("----------------------")
    print()
    if len(diccionario)==0:
        print("No hay pedidos para mostrar. ")
        print()
    else:
        for i in diccionario:
            print(f"Pedido: {i}, Orden = {diccionario[i]}")
    system("pause")
    return


def Buscar(diccionario):
    system("cls")
    print("---------------------")
    print("    BUSCAR VENTAS   ")
    print("---------------------")
    print()
    if len(diccionario)==0:
        print("No hay pedidos para buscar. ")
        print()
        system("pause")
        system("cls")
    else:
        try:
            pedido=int(input("Ingrese el número de pedido a buscar: "))
            assert pedido>0
            if pedido in diccionario:
                print(f"El pedido es el siguiente. ")
                if pedido in diccionario:
                    print(f"Pedido: {pedido} -> Orden = {diccionario[pedido]}")
                system("pause")
            else:
                print("El pedido no existe. ")
                system("pause")
        except ValueError:
            print("El espacio no puede quedar en blanco / El valor debe ser numérico. ")
            system("pause")
            system("cls")
        except AssertionError:
            print("Ingrese correctamente el valor. ")
            system("pause")
            system("cls")         
        return

def eliminar_mediana(diccionario):
    elimina=[]
    for k, val in diccionario.items():
        if "MEDIANA ($6.000)" in val:
            elimina.append(k)
    for k in elimina:    
        del diccionario[k]             
    system("cls")
    print("--------------------------------------------")
    print("    SE HAN ELIMINADO LAS PIZZAS MEDIANAS   ")
    print("--------------------------------------------")
    print()
    system("pause")

def eliminar_familiar(diccionario):
    elimina=[]
    for k, val in diccionario.items():
        if "FAMILIAR ($8.000)" in val:
            elimina.append(k)
    for k in elimina:    
        del diccionario[k]  
    system("cls")
    print("----------------------------------------------")
    print("    SE HAN ELIMINADO LAS PIZZAS FAMILIARES   ")
    print("----------------------------------------------")
    print()
    system("pause")

def estadistica(diccionario):
    total = sum(val[2] for val in diccionario.values())
    system("cls")
    print("-----------------------------")
    print("    ESTADISTICA DE VENTAS   ")
    print("-----------------------------")
    print()
    if len(diccionario)>0:     
        print(f"La cantidad total de pizzas vendidas es de: {len(diccionario)}")
        print()
        print(f"El precio de las pizzas vendidas es de: {total}")
        print()
    else:
        print("No existen pedidos para estadística actualmente.")
        print()
    system("pause")

def Salir():
    exit(0)

# Iniciar Programa

Menu()
