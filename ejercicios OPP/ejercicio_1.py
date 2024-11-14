#Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno.
#Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class estudiante():
    def __init__(self , nombre , nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:", self.nombre ,"\nNota: ",self.nota)

    def resul(self):
        if self.nota >= 7:
            print("APROBADO")
        else:
            print("NO APROBADO")
           

estudiante1 = estudiante("Angel",4)

estudiante1.imprimir()
estudiante1.resul()


