lista1=[1,2,3]
lista1.extend([4,5,6])
lista2=[7,8,9]
lista1.extend(lista2)
for elemento in lista1:
    print(elemento)
print(f"{lista1[4]} muestro el elemento del indice 4")
print(f"{lista1.index(5)} el indice del elemento cinco")
otralista=lista1[2:4]
print(otralista)