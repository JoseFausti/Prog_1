"""1)_El siguiente programa debería imprimir el número 2 si se le ingresan como 
    valores x=5, y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?""" 

# Lo qu hay que corregir es dentro de la funcion. Nos devuelve el valor de las
# variables la cual no se modifican y lo que realmente debe devolver son los 
# valores de los parametros... El codigo quedaria de la siguiente forma:

# def most(a,b):
#    if(a>b):
#       return a
#    else:
#       return b
#
# def least(a,b):
#    if(a<b):
#       return a
#    else:
#       return b
#
# x = int(input('Un numero'))
# y = int(input('Otro numero'))
#
# print(most( x-3 , least( x=2 , y-5 )))