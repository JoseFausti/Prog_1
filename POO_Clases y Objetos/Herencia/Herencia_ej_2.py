# 2.1)_Crea una clase base llamada "Animal" con los siguientes atributos y métodos:
# a)_ Atributos: nombre, edad, género.
# b)_ Un constructor (__init__) para inicializar los atributos.
# c)_ Métodos:
# d)_ hacer_sonido(): Este método imprimirá "El animal hace un sonido genérico

# 2.2)_Crea al menos tres clases derivadas que representen diferentes tipos de animales (por
# ejemplo, "Perro", "Gato" y "Pájaro"). Cada una de estas clases debe heredar de la clase
# "Animal" y tener atributos y métodos específicos para ese tipo de animal:
# a)_ Agrega atributos adicionales que sean específicos para cada tipo de animal,
# como "raza" para el perro o "especie" para el pájaro.
# b)_ Define el método hacer_sonido() para cada clase derivada de manera que
# imprima un sonido característico del animal (por ejemplo, "El perro ladra" para
# la clase "Perro").
# c)_ Crea un método adicional llamado informacion() que imprimirá la información
# sobre el animal, incluyendo los atributos específicos del tipo de animal

# 2.3)_Crea instancias de las clases derivadas, configura sus atributos y llama a los métodos
# hacer_sonido() e informacion() para comprobar el funcionamiento de la herencia y los
# métodos específicos de cada tipo de animal

# CLASES

class Animal:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def hacer_sonido(self):
        print("El animal hace un sonido genérico")

class Perro(Animal):
    def __init__(self, nombre, edad, genero, raza):
        super().__init__(nombre, edad, genero)
        self.raza = raza

    def hacer_sonido(self):
        print("El perro ladra")

    def informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Raza: {self.raza}")

class Gato(Animal):
    def __init__(self, nombre, edad, genero, color):
        super().__init__(nombre, edad, genero)
        self.color = color

    def hacer_sonido(self):
        print("El gato maulla")

    def informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Color: {self.color}")

class Pajaro(Animal):
    def __init__(self, nombre, edad, genero, especie):
        super().__init__(nombre, edad, genero)
        self.especie = especie

    def hacer_sonido(self):
        print("El pájaro canta")

    def informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Especie: {self.especie}")

# Crear instancias de las clases derivadas
perro = Perro("Buddy", 3, "Macho", "Labrador")
gato = Gato("Whiskers", 2, "Hembra", "Atigrado")
pajaro = Pajaro("Tweety", 1, "Macho", "Canario")

# Llamar a los métodos hacer_sonido() e informacion() para cada instancia
print("Perro:")
perro.hacer_sonido()
perro.informacion()
print("\n")

print("Gato:")
gato.hacer_sonido()
gato.informacion()
print("\n")

print("Pájaro:")
pajaro.hacer_sonido()
pajaro.informacion()
