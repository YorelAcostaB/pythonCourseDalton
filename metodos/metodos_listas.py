# creando una lista con list()
lista = list(['hola', 'Yorel', 34, 75, 1,85, True])
lista_2 = list([13, 51, 55, True, 91, True, 265, 11, False])

# agregando un elemento a la lista
lista.append('Acosta')

# agregando un elemento a la lista en un indice especifico
lista.insert(2, 'A casa')

# agregando varios elementos a la lista
lista.extend([False, 2002])

# eliminando un elemento de la lista por su indice
lista.pop(0) #-1 para el ultimo elemento / -2 para el penultimo / -3 antepenultimo ...

# removiendo un elemento de la lista por su valor
lista.remove('A casa')

# eliminando todos los elementos de la lista
lista.clear()

# ordenando la lista ASC (si usamos el paramatro reverse=True lo ordena DESC)
#lista_2.sort()

# invierte los elementos de una lista
lista_2.reverse()

print(lista)
print(lista_2)