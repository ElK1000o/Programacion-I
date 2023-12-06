# Esto es un comentario
# Los comentarios sirven para orientarse dentro del 
# codigo, y saber pa que sirve esto.

# Salida de datos o informacion
print("Hola mundo!")

#siempre antes de ejecutar, guardar!
#pa guardar Ctrl+S

#VARIABLES Y TIPOS DE DATOS

# Variable tipo int -> numeros enteros
numero = 1
# Variable tipo str -> string "cadena" almacena textos
texto = "Hola 1234"
# Variable tipo float -> numero decimal o punto flotante
temperatura = 23.1
# Variable tipo boolean -> True o False
pagado = True

print(numero)
print(f"El numero ingresado es: {numero}")
print(f"El numero es: {numero} y la temperatura es: {temperatura}")

#Operadores basicos
a = 3 + 2 #suma
b = 5 - 4 #resta
c = 2 * 3 #multiplicasound
d = 3 / 2 #division
e = 3 // 2 #division entera
f = 3 ** 4 # tres elevado a cuatro
g = 7 % 2 #modulo -> es el resto de la division
operacion = ((a + b) * (c - d)) / 2
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
print(f"d = {d}")
print(f"e = {e}")
print(f"f = {f}")
print(f"g = {g}")
print(f"operacion = {operacion}")

print(f"El resultado de a + b es: {a + b}")

# Las variables pueden cambiar su valor
print(f"Originalmente a vale: {a}")
a = a + 1
# a += 1
print(f"Ahora a vale: {a}")

#ENTRADA DE DATOS
nombre = input("Ingresa tu nombre: ")
print(f"Tu nombre es: {nombre}")

#Como pedir un numero y guardarlo como un numero
# es lo misma logica que hacer g(f(x))
valor = int(input("Ingrese un numero: "))
print(f"Valor + 1 es: {valor + 1}")

#pedir un numero decimal
decimal = float(input("Ingresa una nota: "))
print(f"El valor de la nota es: {decimal}")

edad = int(input("Ingresa tu edad: "))
#CONDICIONALES (if - elif - else)
if edad >= 18 and edad < 21:
    print("Eres mayor de edad en Chile pero no en USA")
    print("jeje")
elif edad >= 21:
    print("Eres mayor de edad en Chile y USA")
else:
    print("No eres mayor de edad.")
    print("Que sad.")

