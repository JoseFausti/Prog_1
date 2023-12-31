# Bucle For:

# Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos equipos de 6
# integrantes cada uno, donde un integrante de cada equipo es el “jefe” y los otros 5 son sus “oficiales”.
# La regla más importante del juego es que sólo se comunicarán mediante un canal común, por lo que
# deben buscar la forma de ocultar el contenido de sus mensajes. Uno de los equipos decide utilizar un
# método antiguo de encriptación llamado “la cifra del césar”, que consiste en correr cada letra del
# mensaje –considerando la posición de cada una en el alfabeto– una determinada cantidad de lugares.
# Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma en “CVCSWG”.
# Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus oficiales.
# Escribir un programa que permita encriptar los 5 mensajes. El corrimiento (cantidad de lugares que se
# correrán las letras) será dado por el usuario antes de comenzar a encriptar. Los 5 mensajes usarán el
# mismo corrimiento.
# Nota: si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a
# comenzar desde la letra “a”.
# Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en “HAWUD”. Utilizando el alfabeto
# español, de 27 letras, el siguiente cálculo matemático permite volver a comenzar por el principio una
# vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
# Sólo se encriptarán las letras de los mensajes, dejando al resto de caracteres sin modificación.

from ast import Str
from asyncio.base_futures import _FINISHED


abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
jugadores=["jugador1","jugador2","jugador3","jugador4","jugador5"]
palabra_cesar=""
corrimiento= int(input("Ingrese el corrimiento: "))

for i in jugadores:
    mensaje=str(input(f"{i}: Ingrese una palabra: ")).upper()
    for n in mensaje:
        letra=abecedario.find(n)
        letra_cesar= abecedario[(letra + corrimiento % 27)]
        palabra_cesar = palabra_cesar + letra_cesar
    print(f"Palabra encriptada: {palabra_cesar}")
    
# Bucle While:

# 2)_Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
# 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

num="0"
digito_par=0
digito_impar=0
pares_totales=0
impares_totales=0
while num != 0: 
    digito_par=0
    digito_impar=0
    num=str(input("Ingrese un numero entero positivo: "))
    for i in num:
        digito = i
        if digito != "0":
            digito=int(digito)
            if digito % 2 == 0:
                digito_par+=1
                pares_totales += 1
            else:
                digito_impar+=1
                impares_totales += 1
        else:
            num=0
            break        
    print(f"La cantidad de dígitos pares son {digito_par} y los digitos impares son {digito_impar}") 
print(f"La cantidad de dígitos pares totales son {pares_totales} y los digitos impares totales son {impares_totales}")     
        
