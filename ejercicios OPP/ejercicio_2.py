# Desarrollar un programa con tres clases:
#La primera debe ser Universidad, 
#con atributos nombre (Donde se almacena el nombre de la Universidad). 
#La segunda llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
#Y por último, una llamada Estudiante, que tenga como atributos su nombre y edad. 
#El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.


class universidad():

     def __init__(self , Nombre):
        self.Nombre = Nombre

class carrera():

    def carrera(self,especialidad):
        self.especialidad = especialidad

class estudiante(universidad,carrera):

    def datos(self,nombre,edad):
        self.nombre = nombre
        self.edad =  edad

    def imprimir(self):
        print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nUniversidad: ",self.Nombre,"\nCarrera: ",self.especialidad)


persona1=estudiante("los lagos")
persona1.carrera("Ingenieria en informatica")
persona1.datos("Marco",20)

persona1.imprimir()