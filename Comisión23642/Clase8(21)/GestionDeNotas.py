#...
#se ingresaron notas de los alumnos de un curso
#1.mostrar las notas ingresadas
#2.mostrar el promedio de las notas ingresadas
#3.mostrar la nota maxima
#4.mostrar la nota minima
#5.mostrar cuantas notas estan por encima del promedio
#...
import os #LLAMA A LA FUNCIÓN "LIMPIAR PANTALLA" DE LA LIBRERÍA SYSTEM
notas=[]
while True:
    print("*******gestión de notas******")
    print("1. Para ingresar notas")
    print("2. Para listar notas")
    print("3. Para ver el promedio de notas")
    print("4. Para mostrar nota máxima")
    print("5. Para mostrar la nota mínima")
    print("6. Para ver notas por encima del promedio")
    print("7. Para salir")
    op=input("Selecione una opción")
    if op=="1":
        print("1. Para cargar notas")
        print("2. Para volver al menú principal")
        resp=input("ingrese una opcion")
        if resp=="1":
            nota=float(input("ingrese una calificacion"))
            notas.append(nota)
        elif resp=="2":
            break   
    elif op=="2":
        print("1. Para listar notas")
        print("2. Para volver al menú principal")
        resp=input("ingrese una opción")
        if resp=="1":
            print("listando notas...")
            for n in notas: 
                print(n)   
    elif op=="3":
        print("1) Para hallar el promedio de notas")
        print("2) Para volver al menú principal")
        resp=input("Ingrese una opción")
        if resp==1:
            sumatoria=0
            for n in notas:
                sumatoria+=n
            print(f"El promedio de notas es {sumatoria/len(notas)}")
            input("Presione Enter para continuar...")
        elif op=="7":
                print("Adios!!!")
                break