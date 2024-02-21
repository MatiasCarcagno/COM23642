nomAnimal=input("ingrese el nombre del animal: ")
if nomAnimal.lower()=="perro":
    print("es un canino")
    peso=float(input("ingrese el peso: "))
    if peso<7:
        print("es un perro pequeño")
    if peso>=7 and peso<13:
        print("es un perro mediano")
    if peso>=13:
        print("es un perro grande")
else:
    print("el animal no esta contemplado")
print("adios!")                    