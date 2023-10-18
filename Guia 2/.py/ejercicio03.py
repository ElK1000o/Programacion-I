# Ejercicio 3

# Desarrollar algoritmo que permita pedir por pantalla 5 números y muestre la suma de ellos. 
# Valide que los números sean positivos, es decir, mayores a cero, presentando un mensaje de error en caso contrario.

while True:
    n = 5
    sum_num=0
    nums = []

    print(f"A continuación te pediré que ingreses {n} numeros positivos.")

    for i in range(n):
        while True:
            num = float(input(f"Indique el numero {i + 1}: "))
            if num<=0:
                print("El numero ingresado debe ser positivo (mayor a 0).")
            else:
                nums.append(num)
                break
    for num in nums:
        sum_num += num
    break

print(f"La suma de los {n} numeros ingreasdos es de: {sum_num}")