class mascotas:
    def __init__(self,nombre,tipo,dni_propietario,sonido):
        self.nombre=nombre
        self.tipo=tipo
        self.dni_propietario=dni_propietario
        self.sonido=sonido
    def comunicarse(self):
        print(f"{self.nombre} está {self.sonido}")
mi_mascota=mascotas("coca","perro","38274653","ladrando")
mascotaJuan=mascotas("felpita","gato","")