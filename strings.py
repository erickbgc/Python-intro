#Formas de operar con un string
myStr = 'Hola Mundo tarados'
print('respuesta: ' + myStr)    #Otras fornas de
print(f'respuesta: {myStr}')    #concatenar
print('respuesta: {0}'.format(myStr))

""" 
-dir sirve para saber todo 
lo que se pueda hacer con una string 
"""

#   print(dir(myStr))

    #El print es solo para mostrarlo en pantalla,
    #realmente solo ocupamos myStr.EQUIS()
# print(myStr.upper())
# print(myStr.lower())
# print(myStr.swapcase()) 
# print(myStr.capitalize())

#     Tambien podemos poner otro metodo despues de aplicar
#     el metodo anterior.
#     Estos se llaman, 'metodos encadenados'
# print(myStr.replace('Hola', 'Adios').upper())
# print(myStr.count('o'))
# print(myStr.count(' '))

#     Para 'startswith' tiene que concordar con la string
#     Utiliza operacion booleana
# print(myStr.startswith('Hola'))
# print(myStr.endswith('Hola'))

# print(myStr.split('o'))
# print(myStr.find(' '))

#     len() -con esto sabemos la longitud de nuestra string
# print(len(myStr))
# print(myStr.index('a'))

# print(myStr.isnumeric())
# print(myStr.isalpha())

# print(myStr[5])
# print(myStr[-4])
