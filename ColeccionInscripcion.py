from Persona import Persona
import csv
class ColeccionInscripcion:
    __coleccion=[]

    def __init__(self):
        self.__coleccion=[]

    def getColeccion(self):
        return self.__coleccion

    def agregar(self,unaInscripcion):
        self.__coleccion.append(unaInscripcion)

    def consultarInscripciones(self,dni):
        identificacion=0
        band=False
        coleccion=self.getColeccion()
        while identificacion<len(coleccion) and not band:
            i=coleccion[identificacion]
            persona=i.getPersona()
            if persona.getDNI()==dni:
                if i.getPago()==True:
                    print("\nEl inscripto no adeuda monto.")
                else:
                    print("\nInscripcion N° {}".format(identificacion+1))
                    print("\nTaller: {}".format(i.getTaller().getNombre()))
                    print("\nMonto adeudado: ${}".format(i.getTaller().getMonto()))
                band=True
            identificacion+=1
        if band==False:
            print("\nLa persona no se encuentra inscripta.")

    def consultarInscriptos(self,id):
        alumnos=[]
        coleccion=self.getColeccion()
        for inscriptos in coleccion:
            taller=inscriptos.getTaller()
            if taller.getIdTaller()==id:
                persona=inscriptos.getPersona()
                alumnos.append(persona)
        if len(alumnos)!=0:
            print("\n\t\t\tDATOS DE ALUMNOS")
            print("NOMBRE\t\tDNI\t\t\tDIRECCION")
            for a in alumnos:
                print("{}\t"+ a.__str__())
        else:
            print("\nEl alumno no se encontro en el taller.")

    def registrarPago(self,dni):
        band=False
        identificacion=0
        coleccion=self.getColeccion()
        while not band and identificacion < len(coleccion):
            persona=coleccion[identificacion].getPersona()
            if persona.getDNI()==dni:
                print("\nPago registrado.")
                coleccion[identificacion].setPago()
                band=True
            identificacion+=1
        if band==False:
            print("\nNo se encontro DNI.")

    def guardarInscripciones(self):
        coleccion=self.getColeccion()
        with open("Inscripciones.csv", "w", newline="") as archivo:
            writer = csv.writer(archivo)
            for ins in coleccion:
                dni = ins.getPersona().getDNI()
                id  = ins.getTaller().getIdTaller()
                fecha = ins.getFecha()
                writer.writerow([dni,id,fecha])
        print("\nSe guardó con exito.")