frase = input('Decime una frase, y te calculo cuánto tardarías si tuvieras que decirla: ')

palabras_separadas = frase.split(' ')

cantidad_palabras = len(palabras_separadas)

print('Dijiste:')
print(f'- {cantidad_palabras} palabras')
print(f'=> Tú tardarías: {cantidad_palabras / 2}s en decirlo')
print(f'=> Dalto tardaría: {cantidad_palabras * 1000 // 2 * 1.3 / 100}s en decirlo')
if (cantidad_palabras > 120):
    print('Para flaco, tampoco te pedí un testamento')
print('------------')
