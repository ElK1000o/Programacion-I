# Modulos

# Su principal objetivo es poder reutilizar funcionalidades del proyecto
# En un modulo existen clases, funciones y variables (identidades)
# Se importan

# Modulo math
import math

radio=float(input("Ingrese el radio de un círculo: "))

area = math.pi * (math.pow(radio, 2))

print(f"El area del circulo es: {area}")

ang=float(input("Ingrese angulo en radianes: "))

print(f"Valor seno = {math.sin(ang)}, Valor coseno = {math.cos(ang)}")
print(f"Radianes a Grados = {math.degrees(ang)}")

# Modulo random
import random

print(random.random()) # un número aleatorio entre 0 y 1

for i in range(1,10):
    print(random.randint(1,9)) # Numeros aleatorios entre 1 y 9

# O también

for i in range(1,10):
    print(f"Iteracion {i}, numero generado: {random.randint(1,9)}")

# Modulo system
# Aplicable unicamente en windows
from os import system

# cls / pause

for i in range(1,15):
    print(f"Iteracion: {i}")

system("pause") # Solicita tecla para continuar el programa
system("cls") # Limpia la pantalla

print("Programa terminado")
