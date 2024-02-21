Estaciones=["Paso De Los Libres","La Cruz","Santo Tomé","Gobernador Virasoro","A"]
while True:     
    print("1)Listar estaciones de ida")
    print("2)Listar estaciones intermedias")
    print("3)Listar estaciones de regreso")
    print("4)Listar estaciones intermedias")
    print("5)Salir")
    opcion=input("Seleccione la opción deseada: ")
    if opcion=="1":
        print("*****Estaciones de ida*****")
        for estacion in Estaciones:
            print(estacion)
            print("*****************************")    
    elif opcion=="2":
        print("*****Estaciones Intermedias*****")
        for estacion in Estaciones:
            print(Estaciones)        
    elif opcion=="3":
        print("*****Estaciones de regreso*****")
        Estaciones.reverse()
        for estacion in Estaciones:
            print(estacion)
            print("*****************************")
        Estaciones.reverse()
    elif opcion=="5":
        print("Gracias!!! Hasta luego!!!")
        print("*****************************")
        break  


