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
