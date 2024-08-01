numeros = [4, 7, 1, 42 ,15]

# encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# redondeando a 6 decimales
numero = round(12.351235125154567, 1)
print(numero)

# retorna False -> 0, vacio, False, ninguno
resultado_bool = bool([])
print(resultado_bool)

# retorna True, si todos los valores son verdaderos
resultado_all = all([123, 'true', None, [344, 23]])
print(resultado_all)

# suma todos los valores de un iterable
sum_total = sum(numeros)
print(sum_total)