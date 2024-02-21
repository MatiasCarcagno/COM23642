def DoblarNúmeros(nros):
    for indice in range(len(nros)):
        nros[indice]=nros[indice]*2
    return nros    
MiNúmeros=[10,20,30]
print(DoblarNúmeros(MiNúmeros))
print(MiNúmeros)