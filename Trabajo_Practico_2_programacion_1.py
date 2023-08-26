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

# 10)_Escribir un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 
# y si es mayor de 18 años, $1000.
edad=int(input("Ingrese su edad: "))
if edad < 4:
    print("Su entrada es gratis.")
elif edad >=4 and edad <=18:
    print("Usted debe pagar $ 500 ")
elif edad >18:
    print("Usted debe pagar $ 1000 ")
else:
    print("Dato incorrecto")
    
# 11)_La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta
# le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
ingredientes_vegetarianos= ["pimiento","tofu"]
ingredientes_no_vegetarianos=["peperoni","jamon","salmon"]
tipo_pizza=["vegetariana","no vegetariana"]
pizza=str(input("¿Desea una pizza vegetariana? Si / No: " )).lower()
if pizza=="si":
    print(f"Menú: {ingredientes_vegetarianos} (Sólo se permite añadir 1 ingrediente)")
    ingrediente=input("¿Cual desea?: ")
    print(f"Tipo de pizza: {tipo_pizza[0]}")
    print(f"Ingredientes: tomate,mozzarella,{ingrediente}")
elif pizza=="no":
    print(f"Menú: {ingredientes_no_vegetarianos} (Sólo se permite añadir 1 ingrediente)")
    ingrediente=input("¿Cual desea?: ")
    print(f"Tipo de pizza: {tipo_pizza[0]}")
    print(f"Ingredientes: tomate,mozzarella,{ingrediente}")

# 12)_Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado
# desde ese año o cuántos años faltan para llegar a ese año.
import math
anio_actual=int(input("Ingrese el año actual: "))
anio_cualquiera=int(input("Ingrese un año cualquiera: "))
rango=abs(anio_actual-anio_cualquiera)
if anio_actual > anio_cualquiera:
    print("Ha/n pasado ",rango," año/s desde ese año.")
elif anio_actual < anio_cualquiera:
    print("Falta/n",rango," año/s para ese año.")
else:
    print("Es el mismo año.")

# 13)_Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.
#  Haciendo que el programa avise cuando se escriben valores negativos o nulos.
num1=int(input("Ingrese un número entero: "))
num2=int(input("Ingrese otro número entero: "))
if num1>num2:
    if num1 % num2==0:
        print(num1," es múltiplo de ",num2) 
    else:
        print(num2," no es múltiplo de ",num1)
elif num2>num1:
    if num2%num1==0:
        print(num2," es múltiplo de ",num1)
    else:
        print(num2," no es múltiplo de ",num1)
elif num1==0 or num2==0:
    print("No se puede dividir por cero")

# 14)_Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números
# sean solución. Se recuerda que la fórmula de las soluciones es x = -b / a
a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
x= (-b) / a
if a !=0:
    print(f"Solución única: {x:.2f}")

if a ==0:
    print("No tiene solucion")

if a==0 and b==0:
    print("Tiene infinitas soluciones")

# 15)_Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir
#  entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo 
# (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
import math
triangulo_o_circulo=input("Ingrese el área que desea calcular (triangulo: 't'/ciculo: 'c'): ").lower()
if triangulo_o_circulo == "t":
    base=float(input("Ingrese la base: "))
    altura=float(input("Ingrese la altura: "))
    area= (base*altura)/2
    print(f"Area: {area:.2f}")
elif triangulo_o_circulo=="c":
    radio=float(input("Ingrese el radio: "))
    area= math.pi*(radio**2)
    print(f"Area: {area:.2f}")

# 16)_Haz una calculadora básica pida al usuario dos valores, a y b.
# Según la opción que desean, realizar la operación:
# Si operación es 1 entonces debemos ver el resultado de a + b
# Si operación es 2 entonces debemos ver el resultado de a * b
# Si operación es 3 entonces debemos ver el resultado de a - b
# Si operación es 4 entonces debemos ver el resultado de a / b
a=float(input("Ingrese el 1º valor: "))
b=float(input("Ingrese el 2º valor: "))
operacion_matematica=input("Indique la operación matemática (Suma / Resta / Multiplicacion / Division ): ")
if operacion_matematica=="suma":
    suma= a + b
    print(f"Suma: {suma:.2f} ")
elif operacion_matematica=="resta":
    resta= a - b
    print(f" Resta: {resta:.2f} ")
elif operacion_matematica=="multiplicacion":
    multiplicacion= a * b
    print(f" Multiplicacion: {multiplicacion:.2f} ")
elif operacion_matematica=="division":
    if b==0:
        print("No se puede dividir por cero)")
    else:
        division= a / b
        print(f"Division: {division:.2f} ")

# 17)_Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
# otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia_de_la_semana=str(input("Ingrese un dia de la semana: ")).lower()
if dia_de_la_semana == "lunes":
    print("Una nueva semana")
elif dia_de_la_semana == "viernes":
    print("Hoy se sale")
elif dia_de_la_semana == "sabado" or dia_de_la_semana == "domingo":
    print("Es fin de semana")

# 18)_Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
# La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas,
# si trabajó horas extras y mostrar esta cantidad.
# Mostrar su salario total, tomando en cuenta que las horas extras serán 
# pagadas un 10% más que las horas laborales comunes.
horas_trabajadas= int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
salario_por_hora=int(input("Ingrese su salario por hora: "))
if horas_trabajadas < 48:
    print(f"Su salario es de: {horas_trabajadas*salario_por_hora}")
else:
    print(f"Usted trabajó {horas_trabajadas - 48} hora/s extra/s")
    horas_extra = horas_trabajadas - 48
    salario_extra=( horas_extra * salario_por_hora ) + ( horas_extra * 0.1)
    print(f"Su salario base es de: {48 * salario_por_hora}")
    print(f"Las horas extra incluye un 10% más... Le corresponde: {salario_extra}")
    print(f"Su salario total es de: {salario_extra + 48 * salario_por_hora}")

# 19)_Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más,
# existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
cantidad_lapices=int(input("Ingrese la cantidad de lápices que desea llevar: "))
if cantidad_lapices >= 1000:
    print("Usted recibe un 7% de descuento")
    print(f"Monto total: $ {(cantidad_lapices * 60)-(cantidad_lapices * 60 * 0.07)}")
else:
    print(f"Monto total: $ {(cantidad_lapices * 60)}")

# 20)_Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas,
# es mayor o igual a 6; caso contrario saldrá desaprobado.  
nota1= int(input("Ingrese la 1º nota: "))
nota2= int(input("Ingrese la 2º nota: "))
nota3= int(input("Ingrese la 3º nota: "))
nota4= int(input("Ingrese la 4º nota: "))
if (nota1 or nota2 or nota3 or nota4)<=0 or (nota1 or nota2 or nota3 or nota4)> 10:
    print("Error, reinicie el programa.")
else:
    suma= nota1 + nota2 + nota3 + nota4
    promedio=suma/4
    if promedio >=6:
        print(f"Aprobó el curso. Promedio: {promedio:.1f}")
    else:
        print(f"Reprobó el curso. Promedio: {promedio:.1f}")