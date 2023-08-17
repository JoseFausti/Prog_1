# 1)_ Asignamos el valor 5 a la variable "numero1" y lo mostramos por pantalla y mostramos que tipo de dato es.
numero1=5 
print("El valor de la primer variable es: ",numero1)
print(type(numero1))
# 2)_ Asignamos el valor 7.2 a la variable "numero2" y lo mostramos por pantalla y mostramos que tipo de dato es.
numero2=7.2
print("El valor de la segunda variable es: ",numero2)
print(type(numero2))
# 3)_Creamos la variable "suma" que almacena la suma de dichas variables anteriores y la mostramos por pantalla 
# y su tipo de dato.
suma= numero1 + numero2
print("El valor de la suma entre ambas variables es: ",suma)
print(type(suma))
# 4)_Creamos tres variables más para las operaciones: "resta", "multiplicación" y "división" y repetimos el mismo
#  procedimiento.
resta= numero1-numero2
print("El valor de la resta entre ambas variables es: ",resta)
print(type(resta))
multiplicacion=numero1*numero2
print("El valor de la multiplicación entre ambas variables es: ",multiplicacion)
print(type(multiplicacion))
division=numero1/numero2
print("El valor de la división entre ambas variables es: ",division)
print(type(division))
# 5)_Creamos una variable llamada "nombre" y le asignamos el nombre propio como valor, luego lo mostramos por pantalla
# junto con su tipo de dato.
nombre="Jose"
print("El nombre del propietario del código es: ",nombre)
print(type(nombre))
# 6)_Creamos una variable llamada "precio", le asignamos un valor decimal y simulamos que representa el valor de un
# artículo ficticio, luego lo mostramos por pantalla junto con su tipo.
precio=550.0
print("El valor del precio de dicho artículo es: ",precio)
print(type(precio))
# 7)_Creamos una variable llamada "descuento" y le aplicamos un valor del 30%, luego lo mostramos por pantalla junto
# con su tipo
descuento=0.3
print("El valor del descuento aplicado es: ",descuento)
print(type(descuento))
# 8)_Calculamos el precio final aplicando el descuento al precio original y almacenamos el resultado en una nueva 
# variable llamada "precio_final", luego lo mostramos por pantalla e indicamos su tipo de dato.
precio_final= precio-(precio*descuento)
print("El valor del precio final es: ",precio_final)
print(type(precio_final))
# 9)_Creamos un string llamado "cadena" y le asignamos un texto, luego lo mostramos por pantalla e indicamos de que
# clase es.
cadena="Programadores Jr"
print("La cadena asignada es: ",cadena)
print(type(cadena))
# 10)_Creamos una variable llamada "longitud" y en ella almacenamos la longitud de la variable "cadena", luego la
# mostramos por pantalla e indicamos su tipo.
longitud=len(cadena)
print("El tamaño de la variable -cadena- es: ",longitud)
print(type(longitud))
# 11)_Reasignamos un nuevo valor a la variable "precio", lo convertimos en un numero entero y lo mostramos por 
# pantalla junto con su tipo de dato. 
precio=110.5
precio= int(precio)
print("El valor del nuevo precio es: ",precio)
print(type(precio))
# 12)_Reasignamos un nuevo nombre a la variable "nombre" y creamos una nueva variable llamada "apellido",luego las
# concatenamos en una variable llamada "nombre_completo", lo mostramos por pantalla e indicamos su tipo.
nombre="Emiliano"
apellido="Fausti"
nombre_completo= nombre + " " + apellido
print("El nombre completo es: ",nombre_completo)
print(type(nombre_completo))
# 13)_Escribimos la edad en una variable, la aumentamos en cinco y la disminuímos en diez, luego la mostramos por
# pantalla e indicamos su tipo.
edad=22
edad+=5
edad-=10
print("La edad del programador Jr es: ",edad)
print(type(edad))
# 14)_Creamos una variable llamada "altura" que contenga la altura expresada en metros, la multiplicamos por cuatro
# y la dividimos por tres, luego la mostramos por pantalla e indicamos su tipo.
altura=1.75
print("La altura del programador Jr es: ",altura)
print(type(altura))
altura*=4
altura/=3
print("El nuevo valor de la altura es: ",altura)
print(type(altura))
# 15)_Creamos una variable que contenga mi nombre completo en mayúsculas y la convertimos a minúsculas mediante
# algún método de python, la mostramos por pantalla e indicamos su tipo.
nombre_mayusculas="JOSE"
print("El nombre del programador Jr en mayúsculas es: ",nombre_mayusculas)
print(type(nombre_mayusculas))
nombre_minusculas=nombre_mayusculas.lower()
print("El nombre del programador Jr en minúsculas es: ",nombre_minusculas)
print(type(nombre_minusculas))
# 16)_Con la variable del nombre en mayúsculas aplicamos un método parecido para que se transforme todo en 
# minúsculas excepto la primer letra, la mostramos por pantalla e indicamos su tipo.
nombre_mayusculas=nombre_mayusculas.title()
print("El nombre convertido a minúsculas excepto la primer letra es: ",nombre_mayusculas)
print(type(nombre_mayusculas))
