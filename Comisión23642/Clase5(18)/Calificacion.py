nota=int(input("ingrese su calificación: "))
if nota>=1 and nota<=6:
    print("ha sido desaprobado")
elif nota>=7 and nota<=8:
    print("usted ha aprobado")
elif nota==9 or nota==10:
    print("usted ha aprobado distinguidamente")
else:
    print("la nota ingresada es errónea")
print("hasta luego")