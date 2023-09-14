# 2)_Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50
# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos
# Ejemplo de una entrada:
# D 200
# D 200
# R 100
# D 50
# Introducir una línea vacía indica que ha finalizado la bitácora.
# La salida de éste programa sería:
# 350
total=0
print("Deje un espacio en blanco para salir")
operator = ""
amount = 0
while True:
    print("Saldo Disponible: $",total)
    print("Ingrese su operacion (D:deposito / R:retiro) y luego el monto: ")
    operation=str(input()).upper()
    if operation == "":
        print("Gracias por su visita.")
        break
    else:
        operator,amount=operation.split()
        amount=int(amount)
        if operator:
            if operator == "R" or operator== "D":
                if amount >= 0:
                    if operator == "R":
                        if total >= amount:
                            total -= amount
                            print("Usted retiro: $",amount)
                            print("-----------------------------")
                        else:
                            print("Fondos insuficientes.")
                    if  operator == "D":
                        total += amount
                        print("Usted deposito: $",amount)
                        print("-----------------------------")
                else:
                    print("No se puede ingresar valores negativos o numeros con coma...")            
                    continue
        else:
            break                
    print("Resumen final: Usted posee $",total,". Gracias por su visita.")     