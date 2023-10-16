# CLASE CICLOS

# Funcion len

texto = "Tengo un texto con varias letras"
print(f"El texto tiene {len(texto)} caracteres")

#Ciclo WHILE
numero=0

while True: #ciclo infinito
    afp=int(input("Ingresa tu AFP 1. Habitat 2. Capital: "))
    #Como salir?
    if afp!=1 or afp!=2:
        print("1 o 2")
    else:
        break

# Otra forma

#    if afp==1 or afp==2:
#        break
#    else:
#        print("1 o 2")

# CICLO FOR

for i in range(10): #(1,10)
	print(f"El valor de i actualmente es {i}")

# Ejercicios nuevos

# 1
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

while True:
    numero = int(input("Ingrese un número positivo: "))
    if numero >=0:
        break
    else:
        print("El número debe ser positivo (mayor a 0)")

for i in range(1, numero+1):
    if i%2!=0: #impar
        print(f"{i}, ", end="") #end es para mostrar todo en una linea
for i in range (10, 0, -1): #Cuenta regresiva
   print(i)
