# Tuplas y Diccionarios

# Tuplas: una vez creadas NO son modificables (Datos estáticos)

# Tupla vacía ()

tupla=()
tupla=tuple()

# Tupla con valores ()

tupla=(10,20,30,40,50)
print(tupla)

# Acceder a elementos []

tupla=[0] # Posicion 0
print(tupla[0])

# Tuplas a partir de tuplas

# -5 -4 -3 -2 -1 (ultimo elemento siempre es -1)
tp1=(1,2,3,4,5)
# 0 1 2 3 4 (primer elemento siempre es 0)

tp2=tp1[:] # Todos los elementos
tp3=tp1[0:] # Todos los elementos
tp4=tp1[0:4] # 1 al 3 de la tupla
tp5=tp1[:-2] # Todo hasta el -2
tp6=tp1[-4:-2] # Del -4 hasta el -2
tp7=tp1[-3:-4] # Si el 2do negativo es menor al primero obtenemos tupla vacía

# Diccionarios: Identifican un elemento asociandolo a una clave (key)
# Cada clave debe ser unica.
# Las claves pueden ser enteros, flotantes o cadenas.
# Un diccionario NO es una lista, este almacena pares de valores (clave/valor).
# La función len regresa la cantidad de pares (clave/valor) en el diccionario.

# Crear diccionario {} "    , "":""    "

DicAnimales={"gato":"cat", "perro":"dog", "caballo":"horse", "pez":"fish"}

DicTelefonos={"jefe":94546545, "hermano":56498468, "x":45577856}

DicVacio={}

print(DicAnimales)
print(DicTelefonos)
print(DicVacio)

print(DicAnimales["gato"]) # Devuelve "cat"
print(DicTelefonos["jefe"]) # Devuelve numero

# print(DicTelefonos["presidente"]) # Devuelve "KeyError", no se pueden buscar claves inexistentes

# Agregar informacion a diccionarios

DicTelefonos["presidente"] = 65415325
print(DicTelefonos)

# Crear a partir de solicitudes

DicSabores={}

for i in range(0, 4):
    nombre=input("Ingrese su nombre: ")
    sabor=input("Ingrese el sabor de helado favorito: ")
    DicSabores[nombre]=sabor

print(DicSabores)

# Recorrer diccionario por claves

for k in DicSabores.keys():
    print(f"clave = {k} -> valor = {DicSabores[k]}")

# Recorrer diccionario por ITEMS

for i in DicSabores.items():
    print(k)
    print(f"La clave es: {i[0]}") # Valor 0 de la tupla


# Diccionarios mas complejos

DicNotas={"Juan":[1.0, 5.3, 4.2, 3.7], "Daniela":[2.0, 4.3, 6.2, 2.7]}

for k in DicNotas.keys():
    notas=DicNotas[k]
    print(f"Las notas de {k} son {notas}") # Devuelve lista de notas

def promedio(notas):
    sum_not=0
    for i in notas:
        sum_not=sum_not+i
        prom=sum_not/len(notas)
    return prom

# Calcular promedio

# Forma 1
for k in DicNotas.keys():
    notas=DicNotas[k]
    prom=promedio(notas)
    print(f"Las notas de {k} son {notas} y su promedio es {prom}")

# Forma 2
for k in DicNotas.keys():
    notas=DicNotas[k]
    print(f"Las notas de {k} son {notas} y su promedio es {promedio(notas)}")
