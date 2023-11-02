# 2)_Crea una clase llamada Cuenta que tendrá los siguientes atributos:

# titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio
# y la cantidad es opcional. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
# directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad 
# introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

class Acount:

    def __init__(self,account_holder = "Tony Stark", amount = 1000000000):
        self.__private_account_holder = account_holder
        self.__private_amount = amount

    @property # Decorador getter
    def private_account_holder(self):
        return self.__private_account_holder
    
    @private_account_holder.setter # Decorador setter
    def private_account_holder(self,account_holder):
        self.__private_account_holder = account_holder

    @property
    def private_amount(self):
        return self.__private_amount   
    
    @private_amount.setter
    def private_amount (self,amount):
        self.__private_amount = amount

    # Ingreso y Extraccion   
    def insertCash(self,amount):
        if amount >= 0:
            self.__private_amount = self.__private_amount + amount

    def extractCash(self,amount):
        if amount >= 0:
            self.__private_amount = self.__private_amount - amount

    def show(self):
        print(f"Titular de la cuenta: {self.__private_account_holder}, Monto: {self.__private_amount}")  