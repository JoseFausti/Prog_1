# 3)_Desarrollar un programa que cargue los datos de un triángulo.

# Implementar una clase con los métodos para inicializar los atributos,
# imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo
# que es (equilátero, isósceles o escaleno).

class Triangle:

    def __init__(self,side_1 = 0,side_2 = 0,side_3 = 0):
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    # Lados:
    @property # Getter
    def side_1(self):    
        return self.__side_1
    
    @side_1.setter # Setter
    def side_1(self,side_1):
        if side_1 >= 0:
            self.__side_1 = side_1
        else:
            print("El numero ingresado debe ser mayor o igual a 0")    

    @property # Getter
    def side_2(self):    
        return self.__side_2
    
    @side_2.setter # Setter
    def side_2(self,side_2):
        if side_2 >= 0:
            self.__side_2 = side_2
        else:
            print("El numero ingresado debe ser mayor o igual a 0")    

    @property # Getter
    def side_3(self):    
        return self.__side_3
    
    @side_3.setter # Setter
    def side_3(self,side_3):
        if side_3 >= 0:
            self.__side_3 = side_3
        else:
            print("El numero ingresado debe ser mayor o igual a 0")         

    # Método:
    def biggerSide(self):
        if (self.__side_1 > self.__side_2) and (self.__side_1 > self.__side_3):
            print(f"El Lado mas grande es el Lado 1: {self.__side_1}")

        elif (self.__side_2 > self.__side_1) and (self.__side_2 > self.__side_3 ):   
            print(f"El Lado mas grande es el Lado 2: {self.__side_2}")

        else:
            print(f"El Lado mas grande es el Lado 3: {self.__side_3}")   

    def typeOfTriangle(self):
        if (self.__side_1 == self.__side_2) and (self.__side_1 == self.__side_3):
            print("Tipo de Triángulo: Equilátero")
            print(f"Los tres lados poseen el mismo valor: {self.__side_1}")

        elif (self.__side_1 == self.__side_2) or (self.__side_1 == self.__side_3) or (self.__side_2 == self.__side_3):
            print("Tipo de Triángulo: Isóceles")
            self.biggerSide()   

        else:
            print("Tipo de Triángulo: Escaleno")
            self.biggerSide()
            
     