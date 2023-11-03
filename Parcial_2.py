# Examen parcial

# Magneto quiere reclutar la mayor cantidad de mutantes para poder luchar contra los X-Mens.
# Te ha contratado a ti para que desarrolles un programa que detecte si un humano es mutante basándose
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

# FUNCIONES

# Funcion Para verificar si es mutante
def is_mutant(dna):
    # Contador para Verificar si es mutante
    mutant_counter = 0

    # Horizontales
    for rows in dna:
        # Contador de filas
        row_counter = 1
        for i in range(5):
            if rows[i] == rows[i+1]:
                row_counter += 1
                # Posible mutante    
                if row_counter >= 4:  
                    mutant_counter += 1  
    # Verticales
    for columns in range(5): # Toma la longitud de la primer fila de la lista
        # Contador de columnas
        column_counter = 1
        for j in range(5):
            if dna[columns][j] == dna[columns+1][j]:
                column_counter +=1
                # Posible mutante
                if column_counter >= 4:
                    mutant_counter += 1
    # Diagonales                
    #----------------------------------#
    # Diagonal Principal
    for i in range(3):
        # Contador de diagonales
        diagonal_counter = 1
        for j in range(3):
            if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                diagonal_counter +=1
                # Posible mutante    
                if diagonal_counter >= 4:  
                    mutant_counter += 1  
    #----------------------------------# 
    # Diagonal Opuesta 
    for i in range(3):
        # Contador de diagonales
        diagonal_counter = 1
        for j in range(3,6):
            if dna[i][j] == dna[i + 1][j - 1] == dna[i + 2][j - 2] == dna[i + 3][j - 3]:
                diagonal_counter +=1  
                # Posible mutante    
                if diagonal_counter >= 4:  
                    mutant_counter += 1      
    #----------------------------------#       
    # Retorno
    if mutant_counter >= 2:
        return True
    else:
        return False
    
# Funcion Para Imprimir matrices 
def show_result(matrix):
    is_mutant_result = is_mutant(matrix)
    
    print("----------------------------------")
    for row in matrix:
        print(row)   
    print()
    
    if is_mutant_result == True:
        print("Es mutante")
    else:
        print("No es mutante")  
    print("----------------------------------")

# ALGORITMO PRINCIPAL

# 1º Prueba: Mutante
# Inicializamos la matriz
mutant_matrix = []
# Bucle
while True:
    # Inicializamos el contador
    i = 0
    print("----------------------------------")
    print("1º PRUEBA")
    print("----------------------------------")
    # Ingreso de Datos:
    while i < 6:
        dna = str(input("Ingrese una secuencia de Aminoácidos (A,T,G,C), Ejemplo: 'ACTGCG': " )).upper()
        # Validador
        if len(dna) != 6 or not dna.isalpha() or not all(letter in "ATCG" for letter in dna):
            print("Ingreso incorrecto")
            continue
        # Insercion de datos en la matriz
        dna_row = list(dna)
        mutant_matrix.append(dna_row)
        i += 1    
    break
# 2º Prueba  
# Inicializamos la matriz  
no_mutant_matrix = []
# Bucle
while True:
    # Inicializamos el contador
    i = 0
    print("----------------------------------")
    print("2º PRUEBA")
    print("----------------------------------")
    # Ingreso de Datos:
    while i < 6:
        dna = str(input("Ingrese una secuencia de Aminoácidos (A,T,G,C), Ejemplo: 'ACTGCG': ")).upper()
        # Validador
        if len(dna) != 6 or not dna.isalpha() or not all(letter in "ATCG" for letter in dna):
            print("Ingreso incorrecto")
            continue
        # Insercion de datos en la matriz
        dna_row = list(dna)
        no_mutant_matrix.append(dna_row)
        i += 1   
    break     
# Llamada de la Función y Resultado Final
# 1º Prueba
show_result(mutant_matrix)
# 2º Prueba
show_result(no_mutant_matrix)
