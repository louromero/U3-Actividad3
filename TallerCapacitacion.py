class TallerCapacitacion:
    __idTaller=0
    __nombre=''
    __vacantes=0
    __montoInscripcion=0

    def __init__(self,idTaller,nombre,vacantes,montoInscripcion):
        self.__idTaller=idTaller
        self.__nombre=nombre
        self.__vacantes=vacantes
        self.__montoInscripcion=montoInscripcion

    def getIdTaller(self):
        return self.__idTaller

    def getNombre(self):
        return self.__nombre

    def getVacantes(self):
        return self.__vacantes

    def getMontoInscripcion(self):
        return self.__montoInscripcion

    def actualizarVacantes(self):
        self.__vacantes-=1