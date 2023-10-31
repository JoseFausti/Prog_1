
# 1)_ Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.



class Person:

    def __init__(self,name,age,dni):
        self.name = name
        self.age = age
        self.dni = dni

    def gettername(self):
        return self.name    
    
    def settername(self,name):
        self.name = name

    def getterage(self):
        return self.age    
    
    def setterage(self,age):
        if age >= 0:
            self.age = age
        else:
            print("La edad no puede tomar valores negativos")

    def getterdni(self):
        return self.dni  

    def setterdni(self,dni):
        if 7 <= len(dni) <= 8:    
            self.dni = dni
        else:
            print("Número de dni incorrecto")           

    def EsMayorDeEdad(self):        
        if self.age >= 18:
            return True
        else:
            return False


