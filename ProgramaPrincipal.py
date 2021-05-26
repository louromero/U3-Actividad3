from ColeccionTalleres import ColeccionTaller
from ColeccionPersona import ColeccionPersona
from ColeccionInscripcion import ColeccionInscripcion
from Persona import Persona
from Inscripcion import Inscripcion
from TallerCapacitacion import TallerCapacitacion
from datetime import date

def imprimir():
    print("\n------------------MENU----------------")
    print("1. Registrar Inscripciones.")
    print("2. Consultar Inscripciones.")
    print("3. Consultar Inscriptos.")
    print("4. Registrar Pago.")
    print("5. Gruardar Inscripciones.")
    print("0. SALIR")
    print("--------------------------------------\n")

def menu():
    band=True
    imprimir()
    while band:
        opcion=int(input("Ingresar opcion: "))

        #-------------------------------------------------------OPCION 1
        if opcion==1:
            print("\n\t\t\tINSCRIPCION")
            bandera=True
            while bandera:
                nombre=input("\nNombre (0 para salir): ")
                if (nombre!=0):
                    dni=int(input("\nIngrese DNI: "))
                    direccion=input("\nIngrese direccion: ")
                    nuevaPersona=Persona(nombre,dni,direccion)
                    ColeccionPersona.agregar(nuevaPersona)
                    print("\t\tTalleres")
                    print("N° \tNombre\t\tCupo\t\t\tPrecio")
                    for x in manejadorT.getColeccion():
                        print("{}. {}\t\t\t{}\t\t\t${}".format(x.getIdTaller(),x.getNombre(),x.getVacantes(),x.getMontoInscripcion()))
                    op=1
                    b=False
                    while not b:
                        op=int(input("\nIngrese opcion: "))
                        b=op<=manejadorT.getColeccion()[-1].getIdTaller() and op>=manejadorT.getColeccion()[0].getIdTaller()
                        if not b:
                            print("\nIncorrecto, intente de nuevo.")
                    taller=manejadorT.getTaller(op)
                    manejadorT.actualizar(op)
                    manejadorI.agregar(Inscripcion(str(date.today()),nuevaPersona,taller))
                else:
                    b=False


        #-------------------------------------------------------OPCION 2
        #INSCRIPCIONES
        elif opcion==2:
            dni=int(input("\nIngrese DNI: "))
            manejadorI.consultarInscripciones(dni)


        #-------------------------------------------------------OPCION 3
        #BUSCAR INSCRIPTO
        elif opcion==3:
            band=False
            while not band:
                op=int(input("\nN° Taller: "))
                band=op<=manejadorT.getColeccion()[-1].getIdTaller() and op>=manejadorT.getColeccion()[0].getIdTaller()
                if not band:
                    print("\nIncorrecto, vuelva a intentar.")
            manejadorI.consultarInscriptos(op)


        #-------------------------------------------------------OPCION 4
        elif opcion==4:
            dni=int(input("\nIngrese DNI: "))
            manejadorI.registrarPago(dni)


        #-------------------------------------------------------OPCION 5
        elif opcion==5:
            manejadorI.guardarInscripciones()

        elif opcion==0:
            band=False
            print("\nChau :)")

        else:
            print("\nOpcion incorrecta, vuelva a ingresar.")


if __name__=='__main__':
    manejadorP=ColeccionPersona()
    manejadorT=ColeccionTaller()
    manejadorI=ColeccionInscripcion()
    menu()