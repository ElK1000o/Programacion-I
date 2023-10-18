# Ejercicio 5

# Desarrollar algoritmo que permita mostrar en pantalla de manera automática, 
# valores que se sumen de 5 en 5, hasta llegar al valor 50. 
# Ejemplo: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50 (un número debajo de otro).

print("Secuencia de números 5 al 50 (5 en 5): ")

for i in range(5, 51, 5):
        if i>=5:
            print(f"{i}")