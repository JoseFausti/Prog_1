
# 1)_ Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.
# Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Person:
    def __init__(self,name,age,dni):
        self.__private_name = name
        self.__private_age = age
        self.__private_dni = dni
        
    @property # Decorador
    def private_name(self):
        return self.__private_name    
    
    @private_name.setter # Decorador - propiedad setter
    def private_name(self,name):
        self.__private_name = name

    @property 
    def private_age(self):
        return self.__private_age
    
    @private_age.setter
    def private_age(self,age):
        if age >= 0:
            self.__private_age = age
        else:
            print("La edad no puede tomar valores negativos")

    @property
    def private_dni(self):
        return self.__private_dni 

    @private_dni.setter
    def private_dni(self,dni):
        if 7 <= len(dni) <= 8:    
            self.__private_dni = dni
        else:
            print("Número de dni incorrecto")     

    def show(self):
        print(f"Nombre: {self.__private_name}, Edad: {self.__private_age}, DNI: {self.__private_dni}")              

    def isOlder(self):        
        if self.__private_age >= 18:
            return True
        else:
            return False


