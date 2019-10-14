# Con el attrib def se establecen las funciones
# despues de nombrar la funcion, se escribe el codigo que lleva en ella
# se suelen utilizar para encapsular codigo y reutilizarlo 
# para mostrarlo en pantalla solo bastara con llamar a esa funcion del mismo modo en que la creamos
def hello():
    print('Hello World')

hello()

# Dentro de los parentesis va el parametro de la funcion 
# si queremos mostrarlo en pantalla solo bastara con llamar la funcion y establecer el parametro
def hello(name):
    print('Hello '+ name)

hello('Erick')

# Tambien podemos establecer un parametro por defecto en caso de que no se establezca ninguna al llamarlo
def hello(name="Jhon Doe"):
    print('Hello ' + name)

hello('Brandon')
hello()

# Aplica con datos de los cuales necesitemos retornalos
def add(n1, n2):
    return n1 + n2

print(add(10,20))

# La funcion lamba nos puede servir para lo mismo pero suele hacerce uso para codigo mas especifico
# En este caso la variable -sum hace llamado a la funcion lambda que contiene 2 parametros(n1, n2), de los cuales retorna una suma entre ellos
sum = lambda n1, n2: n1 + n2
print(sum(25, 25))