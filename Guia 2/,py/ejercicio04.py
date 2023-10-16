# Ejercicio 4

# Desarrollar algoritmo que permita calcular el promedio de 5 números introducidos por el teclado. 
# Valide que dichos números estén entre 10 y 70, presentando un mensaje de error en caso contrario.

while True:
    n = 5
    sum_num=0
    nums = []

    print(f"A continuación te pediré que ingreses {n} numeros entre 10 y 70 (estos 2 inclusive).")

    for i in range(n):
        while True:
            num = float(input(f"Indique el numero {i + 1}: "))
            if num>=10 and num<=70:
                nums.append(num)
                break
            else:
                print("El numero ingresado debe estar entre 10 y 70.")
    for num in nums:
        sum_num += num
        prom=(sum_num/n)
    break

print(f"El promedio de los {n} numeros ingresados es de: {prom}")