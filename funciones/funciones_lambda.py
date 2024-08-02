numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 20]

# creando una funcion lambda para multiplicar por 2
multiplicar_por_2 = lambda x : x*2  # noqa: E731

# creando una funcion comun que diga si num es par o impar
""" def es_par(num):
    if num%2 == 0:
        return True
    else:
        return False

numeros_pares = filter(es_par, numeros) """

# creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero : numero%2 == 0, numeros)

print(list(numeros_pares))