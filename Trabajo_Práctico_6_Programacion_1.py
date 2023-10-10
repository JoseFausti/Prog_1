# 9_Escribir un programa que simule el juego clásico de Memoria (Memotest)
# utilizando matrices. El juego consiste en un tablero de cartas boca abajo y el objetivo es 
# encontrar todas las parejas de cartas iguales.

import os,time

memotest = [
    ["rojo", "verde", "azul", "amarillo"],
    ["naranja", "violeta", "negro", "blanco"],
    ["azul", "verde", "rojo", "amarillo"],
    ["negro", "blanco", "naranja", "violeta"]
]

empty_table = [
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""]
]

print("Tablero 4x4")
time.sleep(3)

while True:
    os.system("cls")

    try:
        option_1 = input("Ingrese la 1º posicion en formato (posicion 1 x posicion2): ")
        position_1, position_2 = map(int, option_1.split("x"))

        if position_1 < 0 or position_1 >= 4 or position_2 < 0 or position_2 >= 4:
            print("Ingresó algún valor incorrecto, intente de nuevo...")
            time.sleep(3)
            continue

        option_2 = input("Ingrese la posición en formato (posicion 1 x posicion2): ")
        position_3, position_4 = map(int, option_2.split("x"))

        if position_3 < 0 or position_3 >= 4 or position_4 < 0 or position_4 >= 4:
            print("Ingresó algún valor incorrecto, intente de nuevo...")
            time.sleep(3)
            continue

        if memotest[position_1][position_2] == memotest[position_3][position_4]:
            print("Ha encontrado un par!")
            time.sleep(2)
            empty_table[position_1][position_2] = memotest[position_1][position_2]
            empty_table[position_3][position_4] = memotest[position_3][position_4]

        if empty_table == memotest:
            os.system("cls")
            print("Ha completado el juego!")
            print(empty_table)
            time.sleep(7)

    except (ValueError, TypeError, KeyError, IndexError):
        print("Hubo un error, intente de nuevo.")
        time.sleep(3)
        continue


# 10)_Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
# a)_la diagonal principal.
# b)_la diagonal inversa.

# 11)_Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},pregunte al usuario por una divisa y muestre su símbolo
#  o un mensaje de aviso si la divisa no está en el diccionario.

# 12)_Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
# guarde en un diccionario.Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> 
# años, vive en <dirección> y su número de teléfono es <teléfono>’.

# 13)_Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#  pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
# de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
# mensaje informando de ello.
