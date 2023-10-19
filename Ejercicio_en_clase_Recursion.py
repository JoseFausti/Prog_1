# 1)_Escribir una función que simule el siguiente experimento: 
# Se tiene una rata en una jaula con 3 caminos, entre los cuales elige al azar
# (cada uno tiene la misma probabilidad), si elige el 1 luego de 3 minutos vuelve
# a la jaula, si elige el 2 luego de 5 minutos vuelve a la jaula, en el caso de 
# elegir el 3 luego de 7 minutos sale de la jaula. La rata no aprende, siempre 
# elige entre los 3 caminos con la misma probabilidad, pero quiere su libertad,
# por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula.

import random,time

def rat_way(rat,total_time):
    way = random.choice(rat)
    if way == 1:
        time.sleep(3)
        print("La rata ha vuelto a la jaula luego de 3 minutos")
        return rat_way(rat,total_time + 3)
    elif way == 2:
        time.sleep(5)
        print("La rata ha vuelto a la jaula luego de 5 minutos")
        return rat_way(rat,total_time + 5)
    else:
        time.sleep(7)
        print("La rata ha salido de la jaula luego de 7 minutos")
        total_time += 7
        return total_time
    
rat = (1,2,3)
total_time = 0
total_time = rat_way(rat,total_time)
print("----------------------------------")
print("El tiempo total que tardo la rata en salir fueron ",total_time," minutos.")
    


# 2)_Escribir una consigna apropiada para la siguiente función. Asumir que n es un número
#entero.

def f(n): # Creamos la funcion
    s = str(n) # Convertimos a string el numero
    if len(s) <= 1: # Si la longitud de la cadena es menor o igual a 1 retornamos la varible
        return s
# De otro modo retornamos la ultima posicion y llamamos de forma recursiva
# la variable restandole un valor y transformandolo en entero.
    return s[-1] + f(int(s[:-1]))
    
# Crea una funcion que ingresado un numero entero lo retorne al reves, por ejemplo:
# El nùmero 234 sera retornado como 432
