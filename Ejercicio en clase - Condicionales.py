""" Un instituto de inglés necesita un programa que le permita, cada día, procesar
observaciones sobre las clases de ese día. 

El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un 
día de la semana diferente: los lunes se dicta nivel inicial, los martes el nivel intermedio,
los miércoles el nivel avanzado, los jueves son para práctica hablada y los viernes se dicta inglés
 para viajeros.

Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato “día,
DD/MM”, donde [día] es un día de la semana, DD es el número de día y MM es el
número de mes.

Si el usuario ingresa un día de la semana inexistente o una fecha cuyo
día supere el número 31 o el mes supere el número 12, finalizar el programa indicando
que se produjo un error. Debe permitirse que ingrese el día de la semana en
minúsculas o mayúsculas indistintamente.

Como precondición se tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico], 
[numérico]/[numérico]>.
Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
que las prácticas habladas y el inglés para viajeros no tienen exámenes. 

Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
programa le mostrará el porcentaje de aprobados.

Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.

Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
imprimir el ingreso total en $."""

fecha=str(input("Ingrese la fecha actual en formato dia,DD/MM: ")).lower()
dia,ddmm=fecha.split(",")
dd,mm=ddmm.split("/")
dd=int(dd)
mm=int(mm)
if (dd < 1 or dd > 31) or ( mm < 1 or mm > 12):
    print("Error, reinicie el programa.")
else:
    if dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes" and (dd < 1 and dd >31) and (mm < 1 and mm > 12):
        print("Se produjo un error.")
    elif dia == "lunes" or dia == "martes" or dia == "miercoles":
        validador=str(input("¿Ese día se tomaron los exámenes? Si / No. ")).lower()
        if validador == "si":
            aprobados=int(input("¿Cuántos alumnos aprobaron? "))
            desaprobados=int(input("¿Cuantos desaprobaron? "))
            porcentaje= (aprobados /(aprobados+desaprobados))*100
            print(f"La cantidad de aprobados son del {porcentaje:.1f} % ")
    elif dia == "jueves":
        asistencia=int(input("Indique el porcentaje de asistencias: "))
        if asistencia > 50 and asistencia <= 100:
            print("Asistió la mayoria")
        elif asistencia >= 0 and asistencia <=50:
            print("No asistió la mayoria")   
        else:
            print("Porcentaje fuera de rango")     
    if dia == "viernes"and dd==1 and mm == 1 or mm == 7:
        print("Comienzo del nuevo ciclo: ")
        alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel=float(input("Ingrese el arancel por alumno en pesos: "))
        total=arancel*alumnos
        print(f"El ingreso total es: $ {total:.2f} .")





