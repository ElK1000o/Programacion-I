# Listas 

# lista=[] -> lista vacía rango 0

lista_numeros=[10,50,60,70,80]

print(lista_numeros)
print(lista_numeros[1:3]) # Rango de lista

# añadir un dato al final

lista_numeros.append(15)
print(lista_numeros)

# Insertar dato en posición específica insert(posicion, dato)

lista_numeros.insert(2, 25)
print(lista_numeros)

# Eliminar un elemento de la lista

lista_numeros.remove(25)
print(lista_numeros)

lista_numeros.append(15)
lista_numeros.append(15)
print(lista_numeros)

lista_numeros.remove(15)
print(lista_numeros) # Borra solo uno

# Ordenar una lista

lista_ordenada=lista_numeros.sort(reverse=True)
print(lista_ordenada)

# lista con lista

listas_ = [["a", "b", "c", ["x", "y", "z"]], [1, 2, 3], lista_numeros, lista_ordenada]

print(listas_[0]) # Primera lista
print(listas_[0][2]) # Dato dentro de la primera lista
print(listas_[0][3][2]) # Dato dentro de la lista en la primera lista

# Imprimir elemento por elemento

for i in lista_numeros:
    print(i)
