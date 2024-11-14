#Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

from itertools import cycle
class Persona():
    def __init__(self,nombre="",edad=0,rut=""):
        self.nombre =  nombre
        self.edad =  edad
        self.rut = rut

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def rut(self):
        return self.__rut

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    def validar_rut(self):
        self.__rut= str(self.__rut.replace("-", ""))
        aux = self.__rut[:-1]
        dv=self.__rut[-1]
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
        if str(res) == dv:
            return self.__rut
        elif dv=="K" and res==10:
            return self.__rut
        else:
            self.__rut=""
            return self.__rut

    @rut.setter
    def rut(self,rut):
        self.__rut=rut
        self.__rut=self.validar_rut()

    @edad.setter
    def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad

    def mostrar(self):
        print("Nombre:", self.nombre ,"\nedad: ",self.edad,"\nRut: ",self.rut)

    def esmayordeedad(self):
        if self.edad >= 18 :
            return True  
        else:
            return False


