#Cuando NO sabemos de antemano la cantidad de ARGUMENTOS
def hijos(*hijos):
    for hijo in hijos:
        print("Nombre de los hijos: ",hijo)
hijos("Daniel","Ana","Dario")    