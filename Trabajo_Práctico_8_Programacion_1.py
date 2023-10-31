# 1)_Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene

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

# 2)_Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b

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

def pascal(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# Ejemplo de uso
n = 4  # Fila 4
k = 2  # Columna 2
resultado = pascal(n, k)
print(f'El valor en la fila {n} y columna {k} es: {resultado}')

# 9)_ Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, 
# y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres 
# dados (permitiendo caracteres repetidos).

def combinations(listt, k):
    def prefix_combinations(prefix):
        if len(prefix) == k:
            print(prefix)
            return
        for character in listt:
            prefix_combinations(prefix + character)
    
    if k <= 0 or not listt:
        return
    
    prefix_combinations("")

caracteres = ["A", "B", "C","D"]
k = 3
combinations(caracteres, k)
