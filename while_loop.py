count = 0
list = ['red', 'green', 'blue']
print('Adivina un color de la lista. Solo tienes 3 oportunidades/n')

while count < 3:
    dato = input('Dime un elemento en la lista: ')
    for color in list:
        if color == dato:
            print(f'Bien hecho el color {dato} esta en la lista')
            break
        else:
            continue
    if color == dato:
        print('Haz ganado el juego!')
        break
    elif count == 2:
        print('Haz perdido el juego, reinicia el programa.')
        break
    elif count != dato:
            print(f'El color {dato}, no esta en la lista. Te quedan {2-count} oportunidades')
            count += 1

# Los while loops necesitan tener un iterador para romper con su ciclo, encambio los for rompen con su ciclo una vez hayan cumplido con su condicion
# En el for se establece la condicion continue para que siga buscando dentro de el sin repetir el ciclo while