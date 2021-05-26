import csv
import numpy as np
from TallerCapacitacion import TallerCapacitacion

class ColeccionTaller:
    __coleccion=None
    __actual=0
    __tope=0

    def __init__(self):
        self.setArreglo()

    def setArreglo(self):
        archivo = open("Talleres.csv")
        talleres = csv.reader(archivo,delimiter=",")
        for x in talleres:
            if talleres.line_num == 1:
                self.__tope = int(x[0])
                self.__coleccion = np.empty(self.__tope, dtype = TallerCapacitacion )
            else:
                self.agregar(TallerCapacitacion(int(x[0]),x[1],int(x[2]),float(x[3])))
        archivo.close()

    def agregar(self,unTaller):
        actual=self.__actual
        if actual<self.__tope:
            self.__coleccion[actual]=unTaller
            self.__actual+=1
        else:
            print("\nLimite de talleres en la coleccion alcanzado, no se puede agregar mas.")

    def getColeccion(self):
        return self.__coleccion