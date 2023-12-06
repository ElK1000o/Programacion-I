print("Hola")

#variable

#int (enteros)
num = 1
#str (string/cadena, almacena texto letras numeros)
txt = "Asd wasd 123"
#float (decimales o punto flotante)
flt = 0.123
#boolean (T/F)
pg = True
print("La suma de num + flt es:", num+flt)
print(f"La suma de num + flt es: {num+flt}")

#Operadores basicos
a=3+2
b=1*5
c=1-3
d=3/2
e=3//2 #entero
f=2**2 #elevado
g=7%2 #modulo = resto de division
a
b
c
d
e
f
g
op=((a+b)*(c-d))/2
op

print("a={a}")
print("b={b}")
print("c={c}")
print("d={d}")
print("e={e}")
print("f={f}")
print("g={g}")
print("op={op}")
print("Originalmente a:", a)
#a=a+1
a+=1
print("Ahora a vale:", a)

#Entrada de datos

nombre = input("Ingresa tu nombre: ")
print("Tu nombre es: ", nombre)
edad = int(input("Ingresa tu edad: "))
print("Tu edad es: ", edad)

#Condicionales (if (si esto) - elif (o si no) - else (de lo contrario))
edad = int(input("Ingresa tu edad: "))
if edad>=18 and edad<21:
    print("Eres mayor de edad en Chile, pero no en USA.") #se ejecuta solo con if verdadero
elif edad>=21:
    print("Eres mayor de edad en Chile y en USA.") #se ejecuta con if falso
else: #Se ejecuta si todo lo anterior es falso
    print("No eres mayor de edad.")

