# color = input("Color: ")

decision = input('User or Admin(lowercase): ')

#Se puede escribir un if dentro de otro if, respetando los espacios
if decision == 'admin':
    password = input('Passowrd: ')
    if password == '123':
        print('Access granted')
    else:
        print('Access denied')
else:
    print('Save your info to register into the database')
    prof_name= input('Profile name: ')
    prov_pass= input('Provisional password: ')

# Quita los commits para probar con el ejemplo de abajo
# Hay que respetar la estructura del condicional, marcando con dos puntos(:) despues de escribir la sentencia
# Siempre hay que dejar espacios despues de haber establecido la sentencia del condicional
# Condicional dentro de un else(si no)
# if color == 'red':
#     print(color)
#     print(color.replace('red', 'blue'))
# else: 
#     if color == 'blue':
#         print(color)
#         print(color.replace('blue','red'))
#     else:
#         print('Tu color no esta en la lista')

# if color == 'red':
#     print(color.replace('red','blue'))
# elif color == 'blue':
#     print(color.replace('blue','red'))
# else:
#     print('Tu color no esta en la lista')
