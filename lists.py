demo_list = [1, 'Hola', 1.34, True]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
# print(type(numbers_list))

# r = list(range(1, 10))
# print(r)
# print(dir(colors)) para saber que puedo hacer con las listas
# print(len(demo_list))
# print(colors[-2])
# print('green' in colors) asi accedemos a los elementos
# print(colors) siempre y cuando los conozcamos

    # Asi accedemos a la lista y alteramos un elemento de ella
# colors[1] = 'yellow'    Tmb asi podemos diferenciar
# print(colors)    de otro tipo de dato

#Con -append podemos agregar un elemento mas a nuestra lista
# colors.append('violet')  

# como solo podemos agregar un elemento, para agregar mas
# los metemos en una tuple
# colors.append(['violet','yellow'])    Si usamos este formato
# se mostrara la tupla en la lista, para eso llamamos a extend
# colors.extend(['violet','yellow'])
# a (colors) extiende basado en la tuple
# print(colors)
# colors.insert(1, 'black')
# print(colors)
# colors.insert(-1, 'orange')
# colors.insert(len(colors), 'orange')
# print(colors)

#Quitar elementos
#con -pop quita el ultimo elemento o uno cualquiera, si especificamos el indice
#con -remove se remueve un elemento tal cual
# colors.pop()
# colors.remove('blue')   
# colors.pop(1)
#colors.clear() elimina todos los elementos de la lista

#  ordena la lista
# con colors.sort(reverse=True) ordena la lista de Z a A
# con print(colors.index('blue')) imprime el indice de blue

colors.sort()
print(colors.index('red'))
print(colors.count('red'))
print(colors)
