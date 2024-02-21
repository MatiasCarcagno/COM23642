#crear un ejercicio donde podamos dar el presente de estudiantes
#utilizar una tupla
from datetime import datetime #libreria de datetime
legajo=int(input("Ingrese el número de legajo del alumno: "))
nombre=(input("Ingrese el nombre: "))
apellido=(input("Ingrese el apellido del alumno: "))
fecha=datetime.now()
presente=[False]
MiTupla=(legajo,nombre,apellido,fecha,presente)
print(MiTupla)
presente[0]=True
print(MiTupla)