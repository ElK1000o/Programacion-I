# Funciones Python

# Calculadora
# suma - resta - multiplicacion - divison

# f(x) = x + 1

def mensaje():
    print("funcion mensaje")

print("ejecución prueba")

mensaje()

# Función parámetros

def suma(a,b):
    print(f"la suma es: {a+b}")

suma(5,3)

# A traves de variable

num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))

suma(num1, num2)


# Por defecto

def saludar(nombre="Camilo", edad="22"): #Si no se le dan los parámetros se asumen los ingresados (1)
    print(f"Hola, tu nombre es {nombre} y tu edad es {edad}")

saludar() # (1)
saludar("Alex", 100) # (2)
saludar("Carlos", ) # (3)
saludar(nombre="Jose") # (4)
saludar(edad=23) # (5)

# Retornar valor desde una funcion

def suma(a,b):
    c=a+b
    return c

num1=int(input("Ingrese el numero 1: "))
num2=int(input("Ingrese el numero 2: "))

resultado=suma(num1, num2)

print(f"El valor de la suma es {resultado}")
