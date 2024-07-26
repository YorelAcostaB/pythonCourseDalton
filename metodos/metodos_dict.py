diccionario = {
    'nombre'    : 'Yorel',
    'apellido'  : 'Acosta',
    'followers' : 16
}

# devuelve las claves (sirve para iterar) (dict_item)
claves = diccionario.keys

# obtenindo un elemento del dict usando un get()
item_especifico = diccionario.get('nombre') # => Controla la excepcion
# item_especifico = diccionario.['asdasd'] => Lanza excepcion.


# elimino todo del diccionario
# diccionario.clear()

# eliminando un elemento del dict
diccionario.pop('nombre')

# obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)