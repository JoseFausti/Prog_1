# 1)_Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
# Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos

import time
import os

def validator(dni):
    if len(dni)== 7 or len(dni) == 8 :
        return True
    else:
        return False

dni = input("Ingrese su DNI: ")
if dni.isnumeric():
    operator = validator(dni)
    if operator == True:
        print("Su DNI es: {}".format(dni)) 
    else:
       print("DNI incorrecto, reinicie el programa..")
else:
    print("DNI incorrecto, reinicie el programa..")    
    
time.sleep(3)    
os.system("cls")    
    

# 2)_Escribir una función que, dado un string, retorne la longitud de la última palabra.
# Se considera que las palabras están separadas por uno o más espacios. También podría haber espacios 
# al principio o al final del string pasado por parámetro.

def length(sentence):
    words = sentence.split()
    # Verificamos si la lista de palabras está vacía
    if not words:  
        return 0
    last_word = len(words[-1])
    return last_word

sentence = str(input("Ingrese una palabra: "))
 # Verificamos si la cadena no está vacía
if sentence.strip(): 
    print("La longitud de la última palabra de su oración es:", length(sentence))
else:
    print("Oración incorrecta, reinicie el programa.")

time.sleep(3)    
os.system("cls")


# 3)_Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
# Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso 
# de un nombre vacio.

# Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será:
# nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, el usuario solo ingresará uno.

# Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario
# en un bucle hasta que ingrese un DNI correcto.

# Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras
# del apellido y los 3 primeros dígitos de su DNI.
# Ejemplo:
# Nombre: María Ines Rosales
# DNI: 25469648
# ID -> Maria7254
import os
import time

def name_validator(completed_name):
    name1 , name2 = "" , ""
    name_parts = completed_name.split()
    
    if len(name_parts) == 1:
        name1 = name_parts[0]
    elif len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        name1, name2 = name_parts[0], name_parts[1]
    return name1, name2

def validator_dni(dni):
    if len(dni) in [7, 8] and dni.isdigit():
        return dni
    else:
        return False

def validator_dni2():
    dni_verified = ""
    while not dni_verified:
        os.system("cls")
        print("Incorrecto, intente de nuevo..")
        dni_verified = input("Ingrese correctamente el DNI: ")
        if len(dni_verified) in [7, 8] and dni_verified.isdigit():
            return dni_verified

while True:
    os.system("cls")
    completed_name = input("Ingrese su o sus nombres completos en Formato: (nombre1 nombre2): ").strip()
    dni = input("Ingrese su DNI: ")

    try:
        name1 , name2 = name_validator(completed_name)
    except ValueError:
        name1 = name_validator(completed_name)

    dni = validator_dni(dni)
    if dni is False:
        dni = validator_dni2()

    surname = input("Ingrese su apellido: ")
    if not surname.isalpha():
        print("El apellido debe contener solo letras. Intente de nuevo...")
        continue

    print(f"ID: {name1} {len(surname)} {dni[-3:]}")

    again_code = input("Desea continuar? SI/NO: ").upper()
    if again_code != "SI":
        break

time.sleep(3)
os.system("cls")

# 4.Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. 
# Crea una función que reciba los dos números, y devuelve si el primero es múltiplo del segundo.

def is_multiple_number(number1,number2):
    if number1 % number2 == 0:
        print(f"{number1} es múltiplo de {number2}")
    elif number2 % number1 == 0:    
        print(f"{number2} es múltiplo de {number1}")
    else:
        print("No son múltiplos entre si...")


number1 = None
number2 = None

while (number1 and number2) != None:
    try:
        numbers = input("Ingrese dos numeros entreros separados por coma: ").isalnum()
        number1 , number2 = numbers.split(",")
        number1 = int(number1)
        number2 = int(number2)
        
        multiple = is_multiple_number(number1 , number2)
    except ValueError():
        print("Hubo un error , intentelo de nuevo..")
        continue
    

time.sleep(3)
os.system("cls")


# 5.Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día 
# y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

# 6.Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra.
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

# 7.Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.
# Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.

# 8.Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal
# que lea el radio de una circunferencia y muestre su área y perímetro.

# 9.Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre
# de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no
# se ha podido hacer login incremente este valor.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente
# tenemos tres oportunidades para intentarlo.

# 10.Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios
# y porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.

# 11.Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar
# la función dada a cada uno de los elementos de la lista.

# 12.Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.

#13.Escribir una función que calcule el módulo de un vector.

# 14.Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.

# 15.Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad
# total de números leídos en total. Utilizar una o más funciones, según sea necesario.

# 16.Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número,
# utilizando para ello una función que calcule la frecuencia.

# 17.Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo.
# Por cada número, mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces
# que aparece en el número (frecuencia). Al finalizar el programa, mostrar el factorial del mayor número ingresado.
