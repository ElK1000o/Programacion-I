# 3
# Desarrollar algoritmo que permita pedir el ingreso de datos de una moto, los cuales son:Patente, Marca (1.Kawasaki, 2.Ducati, 3.Harley Davidson).
# Descripción, Precio y Año. Muestre todos los datos de la moto, junto con el cálculo del kilometraje aproximado,para ello considere que cada mes se han recorrido 1000 kilómetros. 
# Además, al momento deimprimir la marca, no presente el número, sino más bien, lo que representa.

# Marca

while True:
    marca=int(input("Ingrese la numéricamente la marca de la moto (1.Kawasaki, 2.Ducati, 3.Harley Davidson): "))
    if marca==1 or marca==2 or marca==3:
        break
    else:
        print("El valor ingresado no corresponde, vuelva a introducir (1.Kawasaki, 2.Ducati, 3.Harley Davidson): ")

if marca==1:
    marca_="Kawasaki"
elif marca==2:
    marca_="Ducati"
elif marca==3:
    marca_="Harley Davidson"

# Año

while True:
    año=int(input("Ingrese el año de la moto: "))
    año_=str(año)
    if len(año_)==4:
        break
    else:
        print("El año deben ser 4 dígitos. Ingrese nuevamente. ")

# Patente

while True:
    while True:
        letras=input("ingrese las letras (EN MAYUSCULAS) presentes en la patente de la moto: ")
        if len(letras)>=2 and len(letras)<=3:
            break
        else:
            print("La cantidad de letras (EN MAYUSCULAS) no puede ser menor a 2, ni mayor a 3. Ingreselas nuevamente: ")

    while True:
        numero=int(input("ingrese las numeros presentes en la patente de la moto: "))
        numeros=str(numero)
        if numero<0:
            print("Los números de la patente no pueden ser negativos")
        elif len(numeros)>=2 and len(numeros)<=3:
            break
        else:
            print("la cantidad de numeros no puede ser menor a 2, ni mayor a 3. Ingreselos nuevamente: ")
    if (len(letras)+len(numeros))==5:
        break
    else:
        print("La patente debe contener exactamente 5 caracteres en total. Asegúrese de ingresar correctamente los datos. ")


patente=str(f"{letras}°{numeros}")

# Descripcion

while True:
    desc=input("Presente una breve descripción de la moto (no más de 100 caracteres): ")
    if len(desc)>0 and len(desc)<=100:
        break
    elif len(desc)==0:
        print("La descripción no puede quedar vacía. ")
    elif len(desc)>100:
        print("El limite son 100 caracteres. Resuma la descripción. ")

# Meses de uso y kilometraje

while True:
    meses=int(input("Ingrese numéricamente la cantidad de meses de uso que tiene la moto: "))
    meses_=str(meses)
    if len(meses_)==0:
        print("No puede dejar el espacio en blanco. ")
    if meses<=0:
        print("La moto no puede tener menos de 0 meses de uso. Ingrese otra vez. ")
    else:
        break

kilometraje=(meses*1000)

# Precio

while True:
    precio=int(input("Ingrese el precio de la moto: "))
    if precio<=0:
        print("El precio debe ser mayor a $0. Ingrese nuevamente. ")
    else:
        break

# Prints

print(f"Moto marca: {marca_}, año: {año_}, patente: {patente}, meses de uso: {meses}.")
print(f"{desc}")
print(f"Kilometraje: {kilometraje} kms.")
print(f"Precio: ${precio}.")
