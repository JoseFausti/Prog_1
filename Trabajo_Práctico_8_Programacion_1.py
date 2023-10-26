from gettext import find
import random
"""1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene."""
def f(n):
    s=str(n)
    return len(s)
while True:
    try:
        n=int(input("ingrese un valor positivo: "))
        if n:   
            result = f(n)
            break
    except(ValueError,TypeError,KeyError):
        print("hubo un error")
        continue
print(result)
"""2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b."""
def f(n,b):
    if n % b == 0 :
        return True
    else: 
        return False    
while True:
    try:
        b=int(input("ingrese un numero: "))
        n=int(input("ingrese un numero que crea que es potencia del primero: "))
        break
    except(ValueError,KeyError,TypeError):
        print("hubo un error")
        continue
if f(n,b) == True:
    print("n es potencia de b")
else:
    print("n no es potencia de b")


# # 3-Escribir una funcion recursiva que reciba como parámetros dos strings a y b, 
# # y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:


def internity(a, b, c=[], start=0):
     aux_1 = a.find(b, start)
     if aux_1 != -1:
         c.append(aux_1)
         return internity(a, b, c, aux_1 + 1)
     else:
         return c

print(internity("Un tete a tete con Tete", "te"))

#  -4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
#  •	1 es impar.
#  •	Si un número es impar, su antecesor es par; y viceversa.

def impar (number):
    
    if number == 1 :   
        return 1
    elif number == 0 :
        return 0
    else :
        if impar(number-2) == 1:
            return True
        
if impar(random.randint(1 , 10)) :
    print("el numero es impar !!!!!!!!!") 

def par (number):
    
     if number == 1 :
         return 1
     elif number == 0 :
         return 0
     else :
         if par(number-2) == 0:
             return True
if par(random.randint(1 , 10)) :
    print("el numero es par !!!!!!!!!")      

# 7)_Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# El programa debe pedir al usuario que ingrese un número n, y un número d,
# Luego debe calcular el valor de K(n, p) usando una función recursiva,
# Debe imprimir el resultado de K(n, p)

def K(n,p):

    if n == 1:
        return p
    else:
        return p*n + K(n-1,p)

while True:
    try:
        number_n = int(input("Ingrese un numero positivo: "))
        number_d = int(input("Ingrese otro numero positivo: "))
        if number_n >= 0 and number_d >= 0:
            result = K(number_n,number_d)
            break
        else:
            print("Ingrese numeros possitivos..")
            continue    

    except(ValueError,TypeError,KeyError):
        print("Hubo un error, intente de nuevo")
        continue

print("Resultado de la sumatoria de productos: ",result)


# 8)_El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente
# manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila
# se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes
# del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos
# de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se
# encuentra en la fila n y la columna k.
