while True:
    try:#PERMITE HACER PRUEVAS!!
        x=int(input("ingrese un numero: "))
    except ValueError:#PERMITE MANEJAR EL ERROR!
        print("ha ocurrido un erro, ingrese un numero entero valido: ")    
    else:#EJECUTA CUANDO NO HAY ERRORES!
        print("el resultado es {resultado}")   
    finally:#EJECUTA CODIGO INDEPENDIENTEMENTE DE FORMA SIMULTÁNEA!!!
        print("ejecutando la clausula finally")                