import os
estaciones=[
    {"id":1,"nombre":"Paso De Los Libres","horaSalida":"08:00","horaLlegada":"19:00","precioIda":0,"precioVuelta":1000,"estado":"habilitado"},
    {"id":2,"nombre":"Guaviraví","horaSalida":"08:45","horaLlegada":"18:15","precioIda":100,"precioVuelta":900,"estado":"Deshabilitado"},
    {"id":3,"nombre":"La Cruz","horaSalida":"09:30","horaLlegada":"17:30","precioIda":200,"precioVuelta":800,"estado":"habilitado"},
    {"id":4,"nombre":"Las Palmitas","horaSalida":"10:15","horaLlegada":"16:45","precioIda":300,"precioVuelta":700,"estado":"Deshabilitado"},
    {"id":5,"nombre":"Colonia Arrocera","horaSalida":"11:00","horaLlegada":"16:00","precioIda":400,"precioVuelta":600,"estado":"Deshabilitado"},
    {"id":6,"nombre":"Cuay Chico","horaSalida":"11:45","horaLlegada":"15:15","precioIda":500,"precioVuelta":500,"estado":"Deshabilitado"},
    {"id":7,"nombre":"Cuay grande","horaSalida":"12:30","horaLlegada":"14:30","precioIda":600,"precioVuelta":400,"estado":"Deshabilitado"},
    {"id":8,"nombre":"Santo Tomé","horaSalida":"13:15","horaLlegada":"13:45","precioIda":700,"precioVuelta":300,"estado":"habilitado"},
    {"id":9,"nombre":"Tareirí","horaSalida":"14:00","horaLlegada":"13:00","precioIda":800,"precioVuelta":200,"estado":"Deshabilitado"},
    {"id":9,"nombre":"Virasoro","horaSalida":"14:45","horaLlegada":"12:15","precioIda":900,"precioVuelta":100,"estado":"habilitado"},
]
def menu():
    print("*****MENU DE OPCIONES*****")
    print("1) Para listar estaciones de ida")
    print("2) Para listar estaciones de regreso")
    print("3) Para agregar estaciones intermedias")
    print("4) Para vender pasajes")
    print("5) Para salir")
    op=int(input("INGRESE UNA OPCIÓN: "))
    os.system("cls")
    return op
def listarEstaciones(estaciones,tipo="ida"):
    print(f"listar estaciones de {tipo}")
    if tipo=="ida":
        for estacion in estaciones:
            if estacion["estado"]=="habilitado":
                print(f"id: {estacion['id']} estacion: {estacion['nombre']}")
    elif tipo=="vuelta":
        estaciones.reverse()
        for estacion in estaciones:
            if estacion["estado"]=="habilitado":
                print(f"id: {estacion['id']} estacion: {estacion['nombre']}")
                break
        estaciones.reverse()        
def habilitarEstacion(estaciones):
    print("Habilitar Estacion")
    listarEstaciones(estaciones)
    id=int(input("Ingrese el ID de la estacion"))
    for estacion in estaciones:
        if estacion["estacion"]==id:
            estacion["estado"]="habilitado"
            print("Estación habilitada")
            return
    print(f"no se encontró la estación con id {id}")
def venderPasaje(estaciones):
    print("venta de pasajes")
    listarEstaciones(estaciones)
    estacionSalida=int()       

    #INICIA EL PROGRAMA PRINCIPAL
op=menu()
while op!=5:
    if op==1:
        print(listarEstaciones(estaciones,tipo="ida"))
    elif op==2:
        print(listarEstaciones(estaciones,tipo="vuelta"))
    elif op==3:
        print()
    elif op==4:
        print()
    else:         
        print("Adios!") 