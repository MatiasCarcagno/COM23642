#DECLARAMOS LA FUNCIÓN PARA SUMAR:
def suma (Pn,Sn):
    res=int(Pn)+int(Sn)
    return res
#DECLARAMOS OTRA FUNCIÓN PARA MULTIPLICAR
def multi(pn,sn):
    res=int(pn)*int(sn)
    return res
#ACÁ COMIENZA A CORRER EL PROGRAMA
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: "))
print("el resultado de la suma es: ",suma(n1,n2))
print("el resultado de la multiplicacion es : ",multi(n1,n2))