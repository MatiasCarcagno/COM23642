import os 
def menu():
    os.system("cls")
    print(" ****** MENÚ PRINCIPAL ***** ")
    print("1) Para SUMAR")
    print("2) Para RESTAR")
    print("3) Para MULTIPLICAR")
    print("4) Para DIVIDIR")
    print("5) Para SALIR")
    op=int(input("INGRESE UNA OPCIÓN: "))
    return op
def sumar(pn,sn):
    res=pn+sn
    return res
def restar(pn,sn):
    res=pn-sn
    return res
def multiplicar(pn,sn):
    res=pn*sn
    return res
def dividir(pn,sn):
    try:
        res=pn/sn
        return res
    except:
         print("NO SE PUEDE DIVIDIR POR 0!!!")
         n1=float(input("Ingrese Un Número: "))
         n2=float(input("Ingrese Otro Número: "))
         print(f"EL RESULTADO DE DIVIDIR {n1} Y {n2} ES: {dividir(n1,n2)} ")
         input("***PRESIONE ENTER PARA CONTINUAR***")
         return
#INICIA EL PROGRAMA
while True:
    op=menu()
    if op==1:
        n1=float(input("Ingrese Un Número: "))
        n2=float(input("Ingrese Otro Número: "))
        print(f"EL RESULTADO DE SUMAR {n1} Y {n2} ES: {sumar(n1,n2)} ")
        input("***PRESIONE ENTER PARA CONTINUAR***")
    elif op==2:
        n1=float(input("Ingrese Un Número: "))
        n2=float(input("Ingrese Otro Número: "))
        print(f"EL RESULTADO DE RESTAR {n1} Y {n2} ES: {restar(n1,n2)} ")
        input("***PRESIONE ENTER PARA CONTINUAR***")
    elif op==3:
        n1=float(input("Ingrese Un Número: "))
        n2=float(input("Ingrese Otro Número: "))
        print(f"EL RESULTADO DE MULTIPLICAR {n1} Y {n2} ES: {multiplicar(n1,n2)} ")
        input("***PRESIONE ENTER PARA CONTINUAR***")
    elif op==4:
        n1=float(input("Ingrese Un Número: "))
        n2=float(input("Ingrese Otro Número: "))
        print(f"EL RESULTADO DE DIVIDIR {n1} Y {n2} ES: {dividir(n1,n2)} ")
        input("***PRESIONE ENTER PARA CONTINUAR***")
    elif op==5:
        break    