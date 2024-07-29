# creando un diccionario con dict()
diccionario = dict(nombre='yorel', apellido='acosta')

# las listas no pueden ser claves y usamos frozenset para hacer conjuntos inmutables
diccionario = {frozenset(['dato1', 'dato2']) : 'valor1'}

# creando un diccionario con fromkeys() 1
#-> Crea iterando el primer parametro (ABCDE) en keys y le asigna a cada key el vaue 'Valor'
diccionario = dict.fromkeys('ABCDE', 'valor')

# creando un diccionario con fromkeys() 2
# -> Crea la cantidad de keys mencionadas en la lista y les deja a cada entrada el value en 'None'
diccionario = dict.fromkeys(['nombre', 'apellido', 'seguidores'])

# creando un diccionario con fromkeys() 3
# -> Crea la cantidad de keys mencionadas en la lista y les deja a cada entrada el value en 'valorX'
diccionario = dict.fromkeys(['nombre', 'apellido', 'seguidores'], 'valorX')

print(diccionario)