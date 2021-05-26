class Persona:
    __nombre=''
    __direccion=''
    __dni=0

    def __init__(self,nombre,dni,direccion):
        self.__nombre=nombre
        self.__dni=dni
        self.__direccion=direccion

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getDNI(self):
        return self.__dni

    def __str__(self):
        return "\t{}\t\t{}\t\t\t{}".format(self.getNombre(),self.getDNI(),self.getDNI())