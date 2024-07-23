# creando una lista (se pueden modificar)
lista = ['Lucas', 25, True, 1.85]

# creando una tupla (no pueden modificarse)
tupla = ('Lucas', 25, True, 1.85) # Invariable: no se puede modificar sus conjuntos de datos

# esto es válido
lista[3] = 'Master of poppets'

# esto no es valido
#tupla[3] = 'Master of poppets'

# print(lista[0])


# creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {'Lucas', 25, True, 1.85, 'Lucas'}
#conjunto = {'Hola, buenas tardes'}

# esto no funciona porque no se puede acceder como una lista
# print(conjunto[2])

# esto si funciona porque accede al set
# los conjuntos no imprimen los datos duplicados
#print(conjunto)


# creando un diccionario (dict)
diccionario = {
    'nombre': 'Yorel',
    'apellido': 'Acosta',
    'feliz': True,
    'altura': 1.85,
    'email': 'yorelacostabergonzoni@gmail.com'
}

print(diccionario['nombre'])
print(diccionario['altura'] + 2)