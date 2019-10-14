foods = ['rice','cheese','beef','ham']
fruits = ['apple', 'pineapple', 'mango']
# for food in foods:
#     if food == 'beef':
#         print('Remember the beef')
#         continue
#     print(food)

dato = input('Elemento en la lista: ')
for x in fruits:
    if x == dato:
        print('El elemento esta en lista')
        break
else:
    print('El elemento no esta en la lista')

# Loop de una string
# for x in 'ERICK':
#     print(x)

# sentencia break
# for x in fruits:
#     if x == 'banana':
#         print(x)
#         break
#     print(x)

    # Escrito de otra manera...
# for x in fruits:
#     print(x)
#     if x == 'banana':
#         break

# for x in adj:
#     if x == 'yellow':
#         break
#     print(x)

# Continue statement, salta a la siguiente posicion de la lista
# Nested loops, un loop dentro de otro
# for x in fruits:
#     for y in adj:
#         if x == 'banana':
#             continue
#         print(x, y)
# For simple con continue statement
# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)

# Funcion de rango, nos muestra una secuencia de numeros empezando de 0
# for x in range(6):
#     print(x)
# Funcion de rango especificando el intervalo
# for x in range(2, 8):
#     print(x)
# Funcion de rango con intervalo y saltos
# Este ultimo digito nos indica cuantos saltos de numero dara
# for x in range(2, 31, 4): 
#     print(x)

# Else en loops, la sentencia else en un loop nos indica un bloque de codigo que sera ejecutado cuando este termine
# for x in adj:
#     print(x)
# else:
#     print('Colores')