MiDicc={
    1:"Rios",
    2:"Ayala",
    3:"Juan",
    14:"Rodriguez",
    4:"Roque",
    16:"marcos"
}
...
for clave in MiDicc.keys():                             #Iteración por CLAVE 
    print(f"casaca n°: {clave} jugador {MiDicc[clave]}")
...
for nombre in MiDicc.values():                          #Iteración por VALOR 
    print(f"Nombre: {nombre}")
...
for clave,nombre in MiDicc.items():                     #Iteración por CLAVE Y VALOR
    print(f"Casaca N° {clave}, jugador {nombre}")