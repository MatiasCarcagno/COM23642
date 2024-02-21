mitupla=("hola",1.4,78,[10,20,30],False,78)
print(mitupla)
for elemento in mitupla:
    print(elemento)
mitupla[3].append(40)
print(mitupla)
CantEle=len(mitupla)
print(f"mitupla tiene {CantEle} de elementos")    
OtraTupla=mitupla[0:3]
mitupla=mitupla+OtraTupla
print(mitupla)