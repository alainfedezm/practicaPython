class Alumno:

    #Constructora
    def __init__(self,nombre, nota):
        self.__nombre = nombre
        self.__nota = nota


    def __str__(self):
        aprob = "Aprobado"
        if int(self.__nota) < 5: aprob = "Suspendido"
        return str(f'{self.__nombre} ha obtenido la nota: {self.__nota}  {aprob}')
    

#Metodo Principal
if __name__ == "__main__":
    print(Alumno("Alain",10))