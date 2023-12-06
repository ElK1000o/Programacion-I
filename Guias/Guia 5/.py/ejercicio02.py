# Escribe un programa que lea una string y devuelva un diccionario con la cantidad de apariciones de cada carácter en el string.

f=True
diccionario={}

print("A continuación te pediré que escribas lo que quieras. ")

while f:
    try:
        texto=str(input("Digite texto de máximo 30 caracteres: "))
        assert len(texto)>0 and len(texto)<31
        for i in texto:
            if i == " ":
                i = "espacio"
            if i in diccionario:
                diccionario[i] += 1
            else:
                diccionario[i] = 1
        break
    except ValueError:
        print("Digite correctamente")
    except:
        print("El texto no puede tener más de 30 caracteres")

print(f"El diccionario es el siguiente")

for k in diccionario.keys():
    print(f"Clave = {k} -> valor = {diccionario[k]}. ")