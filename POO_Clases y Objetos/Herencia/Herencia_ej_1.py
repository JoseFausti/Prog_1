# 1)_Realiza la siguiente implementación
# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
# Realiza una función llamada catalogar() que reciba la lista de vehiculos y los
# recorra mostrando el nombre de su clase y sus atributos.

# Modifica la función catalogar() para que reciba un argumento optativo ruedas,
# haciendo que muestre únicamente los que su número de ruedas concuerde con el
# valor del argumento.
# También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:
# "únicamente si se envía el argumento ruedas. Ponla a
# prueba con 0, 2 y 4 ruedas como valor.


# CLASES

class Vehicle:
    def __init__(self,color,wheels):
        self.color = color
        self.wheels = wheels

class Car(Vehicle):
    def __init__(self, color, wheels,speed_km_h,displacement_cc):
        super().__init__(color, wheels)
        self.speed = speed_km_h
        self.displacement = displacement_cc

class Van(Car):
    def __init__(self, color, wheels, speed_km_h, displacement_cc,load_kg):
        super().__init__(color, wheels, speed_km_h, displacement_cc)        
        self.load = load_kg

class Bicycle(Vehicle):
    def __init__(self, color, wheels,type_urban_sport):
        super().__init__(color, wheels)
        self.type_ = type_urban_sport

class Motorcycle(Bicycle):
    def __init__(self, color, wheels, type_urban_sport,speed_km_h,displacement_cc):
        super().__init__(color, wheels, type_urban_sport)
        self.speed_km_h = speed_km_h
        self.displacement_cc = displacement_cc

# ALGORITMO PRINCIPAL

# Funcion catalogar
def catalogue(vehicles_list):
    for object_ in vehicles_list:
        # Nombre de la clase:
        class_name = object_.__class__.__name__
        # Atributos
        attribute = object_.__dict__
        # Impresion
        print(f'Nombre de la Clase: {class_name}\nAtributos: {attribute}')
    return    
# Funcion catalogar modificada
def modifyied_catalogue(vehicles_list, ruedas ): # El valor del argumento debe coincidir para ser mostrado por pantalla
    list_object_vehicles = [] 
    for object_ in vehicles_list:   
        # Verificar si se proporciona el argumento ruedas y si el número de ruedas coincide
        if hasattr(object_, 'wheels') and object_.wheels != ruedas:
            continue
        list_object_vehicles.append(object_)
        # Nombre de la clase:
        class_name = object_.__class__.__name__
        # Atributos (excluyendo métodos)
        attributes = {key: value for key, value in object_.__dict__.items() if not callable(value)}
        # Impresion
        print(f'Nombre de la Clase: {class_name}\nAtributos: {attributes}')
        if ruedas is not None:
            print(f"Se han encontrado {len(list_object_vehicles)} vehículos con {ruedas} ruedas.")
    return

# Creacion de Objetos
car_1 = Car('Rojo',4,160,1400)
van_1 = Van('Azul',5,180,1500,500)
bicycle_1 = Bicycle('Verde',2,'Urban')
motorcycle_1 = Motorcycle('Negro',2,'Sport',250,1200)
# Lista de Vehiculos
vehicles_list = [car_1,van_1,bicycle_1,motorcycle_1]
# Llamado a la funcion
catalogue(vehicles_list)
# LLamado a la fincion modificada
modifyied_catalogue(vehicles_list,0)
modifyied_catalogue(vehicles_list,2)
modifyied_catalogue(vehicles_list,4)