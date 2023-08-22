# 1)_Calcular el perímetro y área de un rectángulo dada su base y su altura.
base= float(input("Ingrese la base  del rectángulo: "))
altura= float(input("Ingrese la altura del rectángulo: "))
perimetro= 2*(base + altura)
area= base * altura
print("Perímetro: ",perimetro,", Área: ",area)
print(type(base,altura))

# 2)_Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1=float(input("Ingrese el 1º cateto del triangulo: "))
cateto2=float(input("Ingrese el 2º cateto del triangulo: "))
hipotenusa=((cateto1**2+cateto2**2)**(1/2))
print("Cateto 1: ",cateto1,", Cateto 2: ",cateto2,", Hipotenusa: ",hipotenusa)
print(type(cateto1,cateto2,hipotenusa))

# 3)_Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
num1=float(input("Ingrese el 1º número: "))
num2=float(input("Ingrese el 2º número: "))
print("Suma: ",num1+num2)
print("Resta: ",num1-num2)
if num2 > 0:
    print("División: ",num1/num2)
else:
    print("No es posible dividir un número por cero")    
print("Multiplicación: ",num1*num2)

# 4)_Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
grados_farenheit=float(input("Ingrese la temperatura en ºFarenheit: "))
grados_celcius=(1.8*grados_farenheit)+32
print("Su temperatura en ºCelcius es: ",grados_celcius)
 
# 5)_¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?
"""a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)
c)	edad = int(input(“Edad: “))
print(tu edad es, edad)
d)	edad = int(input(“Edad: “))
print(“Veamos si tu edad es 18…”, edad=18)"""

""""a)_ No se asigna ningun valor a la variable nombre y nos sale error por pantalla
b)_No se imprime el valor de salida por pantalla, falta parte de codigo: [print("Total: ",total)]
c)_Cuando se incita a mostrar por pantalla, ---tu edad es---debe ir entre comillas ya que sino pasa a ser
una variable que no toma ningun valor y nos sale error por pantalla
d)_Cuando se incita a mostrar por pantalla, a la variable edad, en vez de llamarla se le asigna un nuevo
valor y nos sale error por pantalla"""

# 6)_Calcular la media de tres números pedidos por teclado.
n1=float(input("Ingrese el 1º número: "))
n2=float(input("Ingrese el 2º número: "))
n3=float(input("Ingrese el 3º número: "))
media=(n1+n2+n3)/3
print("Los números ingresados fueron: ",n1," , ",n2," , ",n3)
print("La media de dichos números es: ",media)

# 7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y 
# minutos corresponde.Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
x=float(input("Ingrese la cantidad de tiempo deseada en minutos: "))
horas=int(x/60)
minutos=int(x%60)
print("La cantidad de ",x," minutos es equivalente a ",horas," horas y ",minutos," minutos")

# 8)_Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor 
# desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes
#  y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
sueldo_base=float(input("Por vafor, ingrese su sueldo base: "))
comicion_ventas=0.1
total=sueldo_base+(sueldo_base*comicion_ventas)
print("Su sueldo total: $ ",total)

# 9)_Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
# cuanto deberá pagar finalmente por su compra.
valor_compra=float(input("Ingrese el valor de su compra: "))
descuento=0.15
total_compra=valor_compra-(valor_compra*descuento)
print("Su total con descuento es: $ ",total_compra)

# 10)_Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# Dicha calificación se compone de los siguientes porcentajes:
#•	    55% del promedio de sus tres calificaciones parciales.
#•	    30% de la calificación del examen final.
#•	    15% de la calificación de un trabajo final.


# Inicializamos los porcentajes de la materia con su total por tramo correspondiente
porcentaje_parciales=0.55
porcentaje_examen_final=0.3
porcentaje_trabajo_final=0.15
# Pedimos el valor de las notas y los asignamos a una lista
nota1=float(input("Ingrese la 1º nota del parcial: "))
nota2=float(input("Ingrese la 2º nota del parcial: "))
nota3=float(input("Ingrese la 3º nota del parcial: "))
# Calculamos el promedio y el porcentaje obtenido en los parciales 
promedio_parciales=(nota1+nota2+nota3)/3
porcentaje_parciales=(promedio_parciales*porcentaje_parciales)/10
# Realizamos el mismo procedimiento con el exámen final 
examen_final=float(input("Ingrese la nota obtenida en el exámen final: "))
porcentaje_examen_final=(examen_final*porcentaje_examen_final)/10
# Y con el trabajo final...
trabajo_final=float(input("Ingrese la nota obtenida en el tabajo final: "))
porcentaje_trabajo_final=(trabajo_final*porcentaje_trabajo_final)/10
# Expresamos el porcentaje total final asignándolo a una variable
porcentaje_total=(porcentaje_parciales+porcentaje_examen_final+porcentaje_trabajo_final)
# Finalmente imprimimos las notas por pantalla
print(f"Porcentaje obtenido en los parciales: {porcentaje_parciales*100:.0f} %")
print(f"Porcentaje obtenido en el exámen final:  {porcentaje_examen_final*100:.0f} %")
print(f"Porcentaje obtenido en el trabajo final:  {porcentaje_trabajo_final*100:.0f} %")
print(f"Porcentaje total Final:{porcentaje_total*100 } %")

# 11)_Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
num1=float(input("Ingrese el 1º número: "))
num2=float(input("Ingrese el 2º número: "))
distancia=abs(num1-num2)
print(f"La distancia entre los dos números es: {distancia:.1f}")

# 12)_Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
num=float(input("Ingrese un número para conocer su raíz cuadrada y su cúbica: "))
rcuadrada= num**(1/2)
rcubica= num**(1/3)
print(f"Raíz cuadrada: {rcuadrada:.3f}")
print(f"Raíz cúbica: {rcubica:.3f}")

# 13)_Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
# Ejemplo, si se introduce 23 que muestre 32.
num=int(input("Ingrese un número de dos cifras: "))
if num > 100:
    operador=False
    while operador==False:
       num=int(input("Incorrecto; Ingrese un número de dos cifras: "))
       if num <= 100:
           operador=True
a= int ( num / 10)
b= num % 10
print(f"Su número invertido es: {b}{a}")

# 14)_Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo
# que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.
A=float((input("Ingrese el 1º número: ")))
B=float((input("Ingrese el 2º número: ")))
print(f"Valor antes del intercambio: A:{A} ; B:{B} .")
C=A
A=B
B=C
print(f"Valores después del intercámbio: A:{A} ; B:{B} .")

# 15)_Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.

#Suponemos que el recorrido del viaje es en avion
# Tomamos como parámetro que en un avión se recorren 13 km aprox por minuto
S=13/60
T=float(input("Ingrese la distancia a recorrer (km): "))
while T > 13:
    T=input("Incorrecto, la distancia para llegar a tiempo ha de ser menor a los 13 km")
    if T <= 13:
        break
T/=S
print(f"Usted llegará en {T:.2f} segundos aproximadamente...")

# 16)_Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre=str(input("Ingrese su nombre: "))
apellido_1=str(input("Ingrese su primer apellido: "))
apellido_2=str(input("Ingrese su segundo apellido: "))
n=nombre.upper()
a1=apellido_1.upper()
a2=apellido_2.upper()
print("Inicial del nombre: ",n[0])
print("Inicial del 1º apellido: ",a1[0])
print("Inicial del 2º apellido: ",a2[0])

# 17)_Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada 
# usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”.
usuario=str(input("Ingrese su nombre: "))
print("Ahora estás en la matrix, ",usuario)

# 18)_Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. 
# A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina.
#  Imprimir en pantalla el monto final a pagar.
valor_cena=float(input("¿Cuanto costó su cena?: "))
monto_final=valor_cena+(valor_cena*0.062)+(valor_cena*0.1)
print("Monto final: ",monto_final)

# 19)_Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos
#  en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa.
dia=int(input("Ingrese el dia de su nacimiento: "))
mes=int(input("Ingrese el mes de su nacimiento: "))
ano=int(input("Ingrese el año de su nacimiento: "))
if mes < 10:
    print("Fecha de nacimiento: ",dia," / 0",mes," / ",ano)
else:
    print("Fecha de nacimiento: ",dia," / ",mes," / ",ano)

# 20)_Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA.
dia=int(input("Ingrese el dia de su nacimiento: "))
mes=int(input("Ingrese el mes de su nacimiento: "))
ano=int(input("Ingrese el año de su nacimiento: "))
ddmmaaa=[dia,mes,ano]
print("Fecha de nacimiento: ",ddmmaaa[0])

# 21)_Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto,
# para saber cuántos tanques de combustible consumirá el viaje entero.
# Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, 
# qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
# Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.
km_l=float(input("Ingrese: ¿Cuantos km puede recorrer su moto con 1 litro de combustible? "))
l_tanque=float(input("¿Cual es la capacidad total del tanque de combustible? "))
km_total=float(input("¿Cuantos km totales va a recorrer? "))

l_total= km_total / km_l
tanques_l_totales= l_total / l_tanque

print(f"El gasto total de combustible será de: {l_total} litros.")
print(f"Usted consumirá {tanques_l_totales} tanques de combustible para su viaje.")