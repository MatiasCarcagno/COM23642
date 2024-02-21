listaalumno=[]
nombre=""
legajo=0
nota1=0.0

while True:
    print("1) Para ingresar Alumno")
    print("2) Para listar Alumnos")
    print("3) Para salir")
    op=input("Ingrese una opción: ")
    if op == "1":
        nombre=input("Ingrese el nombre del alumno: ")
        legajo=int(input("Ingrese el número de legajo: "))
        nota1=float(input("Ingrese la nota: "))
        listaalumno.append({"nombre":nombre, "Legajo":legajo, "Nota1":nota1})
    elif op=="2":
        for dic in listaalumno:
            print(f"nombre: {dic['nombre']}, legajo: {dic['Legajo']}, nota1: {dic['Nota1']}")
    elif op=="3":
        break        
    