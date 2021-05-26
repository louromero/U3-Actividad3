class Inscripcion:
    __fechaInscripcion = ''
    __pago = True
    __taller = None
    __persona = None

    def __init__(self,fechaInscripcion,persona,taller,pago=False):
        self.__fechaInscripcion=fechaInscripcion
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller
        
    def getFecha(self):
        return self.__fechaInscripcion

    def getPago(self):
        return self.__pago

    def getTaller(self):
        return self.__taller

    def getPersona(self):
        return self.__persona

    def setPago(self):
        self.__pago=True