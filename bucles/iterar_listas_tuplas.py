animales = ['gatos', 'perros', 'papagallo', 'tiburon', 'pez']
numeros = [52, 16, 14, 72, 28]

# recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

# recorriendo lista de numeros y multiplicando el valor por 10
for num in numeros:
    print(f'{num} * 10 = {num * 10}')

# iterando mas de 2 listas al mismo tiempo del mismo tamaño
for numero, animal in zip(animales,numeros):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}')

for num in range(5,10):
    print(num)
    
# forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor  = num[1]
    print(f'Indice: {indice} || Valor: {valor}')
    
# usando el for:else
for num in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {num}')
else:
    print('el bucle termino')
    

