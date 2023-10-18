# Taller 4

# Sin manejo de excepciones

# x=10
# y=0
# division=x/y
# print(division)

# try - except

try:
    x=10
    y=0
    division=x/y
    print(division)
except: #Se colocan todos los comandos a ejecutar en caso de fallo
    print("No se puede dividir entre cero. ")

# try - except - ciclo

# try:
#     x=float(input("Ingrese valor de X: "))
#     while True: #??
#         y=float(input("Ingrese valor de y: ")) #??
#         if y==0: #??
#             print("El numero no puede ser 0. ") #??
#         else: #??
#             break #??
#     division=x/y
#     print(f"La división es: {division}")
# except: 
#     print("No se puede dividir entre cero. ")

# Opcion clase

while True:
    try:
        x=float(input("Ingrese valor de X: "))
        y=float(input("Ingrese valor de y: "))
        division=x/y
        print(f"La división es: {division}")
        break
    except ValueError:
        print("No se puede dividir entre cero. ")

# Uso de assert - Validacion de datos (se usa con try - except)

# try:
#     x=int(input("Ingrese valor de x: "))
#     assert x>0
# except AssertionError:
#     print("Fallo el assert. ")

try:
    x=int(input("Ingrese su nota: "))
    assert x>=1 and x<=7
except AssertionError:
    print("La nota debe ser entre 1 y 7. ")

# Metodos con strings

nombre="juan"
apellido="pEreZ"

# Convertir todo a mayúsculas
print(f"El nombre es: {nombre.upper()} {apellido.upper}")

datos="123,juan,santiago,chile"
print(datos.split(","))

# Listas

lista=datos.split(",")

# Acceder a elementos por posición

print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
