#strings
print("Hola mundo")     #print aplica como funcion
print('Hola mundo')
print("""Hola mundo""")
print('''Hola mundo''')
#para saber que tipo de dato es, tecleamos (type)
type("Hola mundo")
#para imprimirlo y conocer el tipo de dato junto el codigo
print(type('Hola mundo'))
print(type(100))    #entero
print(type(100.5))      #flotante

#Esta es la forma de concatenar strings (tambien con variables)
print("Adios" + " mundo cruel")
print(3+3) #Si aplicamos el '+' en numero, estos se sumaran

#Boolean, para el interprete -bool
True
False
print(type(True))     #bool
        #Metodos para agrupar datos
#List
[10,20,30,32]
['Hola', 'Adios', 'equisde']
print(type([1,2,5]))   #list
[] #lista vacia o nula

#Tuples, para elementos fijos (inmutables)
(10, 20, 30, 45)
()  #tuple vacia
print(type((1,200)))      #tuple

#Dictionaries, par aagrupar datos de una misma entidad
#Estan conformados como     clave:nombre
{ 
    "name":"Erick",
    "last_name":"Garcia",    
    "nickname":"erickbgc"
}
print(type({ 
    "name":"Erick",
    "last_name":"Garcia",    
    "nickname":"erickbgc"
}))

#None type para variables con contenido Nulo no establecido
None
print(type(None))
