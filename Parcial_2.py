# Examen parcial

# Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.
#Te ha contratado a ti para que desarrolles un programa que detecte si un humano es mutante basándose
# en su secuencia de ADN.

# Para eso te ha pedido crear un programa con un método o función booleana, llamada is_mutant(dna),
# que recibe como parámetro un arreglo de Strings que representan cada fila de una matriz 6x6 con la
# secuencia de ADN.

# Las letras de los Strings solo pueden ser: A,T,C,G; las cuales representan cada base nitrogenada del ADN.
# Sabrás si un humano es mutante, si encuentras más de una secuencia de cuatro letras iguales, estas
# pueden aparecer de forma oblicua, horizontal o vertical.

# Ejemplo de matrices válidas:
# En el caso de la matriz de la derecha,
# adn = [‘ATGCGA’,’CAGTGC’,’TTATGT’,’AGAAGG’,’CCCCTA’,’TCACTG’]
# la función devolverá True.

# Desarrolla el algoritmo de forma más eficiente posible.
# El ingreso de los valores de la matriz debe ser pedido por teclado. Ten en cuenta casos para que sea
# mutante y casos en los que no lo sea.

# Una vez cargada correctamente la misma (esto debe verificarse), aplique la función que verifica si hay
# presencia de genes mutantes o no y mostrar el resultado por pantalla al usuario.
# Subir a Github el proyecto con los casos de prueba.

import random

# Función
def is_mutatnt(dna):
    # Contador para Verificar si es mutante
    mutant_counter = 0

    # Filas Horizontales
    for rows in dna:
        # Contador de filas
        row_counter = 0
        for i in range(0,6,1):
            if rows[i] == rows[i+1]:
                row_counter += 1
            # Posible mutante    
            if row_counter >= 4:  
                mutant_counter += 1  
    
    # Filas 

    return 

# Inicializamos la matriz
matrix = [
    [],
    [],
    [],
    [],
    [],
    [],
]
# Bucle
while True:
    try:
        # Ingreso de Datos:
        for row in matrix:
            dna = str(input("Ingrese una secuencia de Aminoácidos (A,T,G,C), Ejemplo: 'ACTGCG'")).upper()
            # Validador
            if len(dna) > 6 or not dna.isalpha():
                print("Ingreso incorrecto")
                continue
            # Insercion de datos en la matriz
            if all(letter in "ATCG" for letter in dna):
                row.append(list(dna))
            
        # Llamada de la Función
        print(matrix)
        is_mutatnt(matrix)   

    except(ValueError,KeyError,TypeError):
        print("Algun valor ingresado fue incorrecto, intente de nuevo..")
        continue

