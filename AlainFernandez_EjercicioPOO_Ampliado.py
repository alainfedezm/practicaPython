#Clase Singleton
class Clase (object):
    __instance = None
    __alumnos = None
    __profesor = None

    #Constructora
    def __new__(cls):
        if Clase.__instance is None:
            Clase.__instance = object.__new__(cls)
            Clase.__alumnos = {}
            Clase.__profesor = {}
        return Clase.__instance
    
    #Anadir un alumno al dicc
    def anadirAlumno(self,alumno):
        self.__alumnos[alumno.id] = alumno

    #Anadir lista de Alumnos al dicc
    def anadirListaAlumnos(self,lista):
        for alumno in lista:
            self.anadirAlumno(alumno)

    #Añadir el Profesor de la clase
    def anadirProfesor(self, profesor):
        self.__profesor = profesor

    #Imprimir todos los alumnos de la clase
    def printData(self):
        print(f'Para la asignatura {self.__profesor.getAsignatura()} impartida por {self.__profesor.getNombre()} estan matriculados los alumnos: ' )
        for alumno in self.__alumnos: print(self.__alumnos[alumno])

class Persona():
    #Constructora
    def __init__(self,nombre, identificador):
        self.__nombre= nombre
        self.id = identificador

    def getNombre(self): return self.__nombre

class Profesor(Persona):
    #Constructora
    def __init__(self,nombre, identificador,asignatura):
        Persona.__init__(self, nombre, identificador)
        self.__asignatura = asignatura

    def getAsignatura(self): return self.__asignatura

class Alumno(Persona):
    #Constructora
    def __init__(self,nombre, identificador, nota):
        Persona.__init__(self, nombre, identificador)
        self.__nota = nota

    def __str__(self):
        aprob = "Aprobado"
        if int(self.__nota) < 5: aprob = "Suspendido"
        return str(f'{self.getNombre()} ha obtenido la nota: {self.__nota}  {aprob}')
    
    def getNota(self): return self.__nota

#Metodo Principal
if __name__ == "__main__":
    Clase().anadirListaAlumnos([Alumno("Alain","id01", 10), Alumno("Diego","id02", 10), Alumno("Izaro","id03",10)])
    Clase().anadirProfesor(Profesor("Koldo", "id00", "pooJava"))
    Clase().printData()
