diccionario = {
    'nombre' : 'yorel',
    'acosta' : 'acosta',
    'subs' : 30
}

#recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print(f'La clave es: {key}')

# recorriendo el diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]

    print(f'La clave es: {key} y el valor es: {value}')