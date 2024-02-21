cadena="hola Juan"
car=input("ingrese un caracter: ")
for letra in cadena:
    if letra==car:
        print(f"Letra encontrada {letra}")
        break
else:
    print("No se encontró {letra}")