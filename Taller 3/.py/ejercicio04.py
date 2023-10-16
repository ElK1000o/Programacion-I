# 4
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida.

while True:
    texto=input("Ingrese una palabra no mayor a 10 caracteres: ")
    if len(texto)>10:
        print("La palabra seleccionada no puede superar los 10 caracteres")
    elif len(texto)==0:
        print("No puede dejar el espacio vacío")
    else:
        break

for i in texto:
    print(i)