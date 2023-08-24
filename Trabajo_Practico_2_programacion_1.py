# 1)_Crear un programa que reciba el número de años que tiene nuestra computadora y muestre 
# en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo
# si es mayor a 2 años.
anios=int(input("Ingrese la antiguedad de su computadora: "))
if anios <= 2 and anios>=0:
    print("Su ordenador es nuevo")
elif anios > 2:
    print("Su ordenador es viejo")
# 2)_Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.    
else:
    print("Rango no válido")
    
# 3)_Solicitar al usuario que ingrese los nombres de dos personas, 
# los cuales se almacenarán en dos variables. A continuación. 
# Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. 
# Si no es así, imprimir ‘no hay coincidencia’.
nombre_1=str(input("Ingrese un nombre: "))
nombre_2=str(input("Ingrese otro nombre: "))
if nombre_1[0]==nombre_2[0]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
    
# 4)_Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: 
# candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
# #Según el candidato elegido (A, B o C) se debe imprimir el mensaje: 
# ‘Usted ha votado por el partido [color del candidato elegido].
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles,
# indicar ‘Opción errónea.’
candidato=str(input("Ingrese el candidato que desea votar: (A: rojo / B: verde / C: azul) ")).upper()
if candidato=="A" or candidato=="B" or candidato=="C":
    if candidato=="A":
        print("Usted ha votado por el partido rojo")
    elif candidato=="B":
        print("Usted ha votado por el partido verde")
    elif candidato=="C":
        print("Usted ha votado por el partido azul")
else:
    print("Opción erronea")
            
# 5)_Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
# informarle que no se puede procesar el dato.
letra=input("Ingrese una letra: ")
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("Es vocal")
elif len(letra)>1:
   print("No se puede prosecar el dato..") 
else: 
    print("No es vocal")

# 6)_Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible
# por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
anio=int(input("Ingrese un año: "))
if anio % 4 ==0 and anio % 100 != 0 or anio % 400== 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")

# 7)_Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.  
num1=int(input("Ingrese el 1º numero: "))
num2=int(input("Ingrese el 2º numero: "))
num3=int(input("Ingrese el 3º numero: "))
if num1<=num2 and num1<=num3:
    menor=num1
elif num2<=num1 and num2<=num3:
    menor=num2
elif num3<=num1 and num3<=num2:
    menor=num3
print(f"El número menor es {menor}")

# 8)_Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
# Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña 
# correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
usuario=input("Ingrese un usuario: ")
contrasenia=input("Ingrese su contraseña: ")
if usuario=="Gwenevere" and contrasenia=="excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

# 9)_Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
# posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla 
# el grupo que le corresponde

# A1 son las mujeres y A2 son los hombres pertenecientes al grupo "A"
A1=["A","B","C","D","E","F","G","H","I","J","K","L"]
A2=["Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# B1 son las mujeres y B2 son los hombres pertenecientes al grupo "B"
B1=["M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
B2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
sexo=input("Indique si es hombre o mujer: ").lower()
nombre=input("Indique su nombre: ").upper()
if sexo=="hombre":
    if nombre[0]== A2:
        print("Usted pertenece al grupo 'A'")
    else:
        print("Usted pertenece al grupo 'B'")
elif sexo=="mujer":
    if nombre[0]== A1:
        print("Usted pertenece al grupo 'A'")
    else:
        print("Usted pertenece al grupo 'B'")













