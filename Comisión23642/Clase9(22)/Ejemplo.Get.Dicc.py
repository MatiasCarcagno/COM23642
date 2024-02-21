MiDicc={
    1:"Rios",
    2:"Ayala",
    3:"Juan",
    14:"Rodriguez",
    4:"Roque",
    16:"marcos"
}
for clave in MiDicc.keys():
    print(f"Casaca N° {clave}")
casaca=int(input("Ingrese un número de casaca: "))
print(MiDicc.get(casaca))           #Método .get(), para ubicar dentro del Diccionario
