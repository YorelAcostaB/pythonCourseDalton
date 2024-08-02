# falto el profe y los pibes van a armar la clase.

#pedir el nombre y la edad de los compañeros que vinieron hoy a clase.

def obtener_compañeros(cantidad):
    # creando la lista con los compañeros
    compañeros = []

    # ejecutando un for para pedir la info de c/compañero
    for i in range(cantidad):
        print('---')
        nombre = input('ingrese el nombre del compañero: ')
        edad   = input('ingrese la edad del compañero: ')
        compañero = (nombre, edad)

        # agrego la info a la lista
        compañeros.append(compañero)

    # ordeno los compas de menor a mayor segun su edad
    compañeros.sort(key = lambda x : x[1])

    # compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    # para definir el asistente y al profesor
    asistente = compañeros[0][0]
    profesor  = compañeros[-1][0] # el -1 nos devuelve el último elemento

    # retornamos una tupla
    return (asistente, profesor)

# proceso de desempaquetacion
asistente,profesor = obtener_compañeros(5)

print('---')
print(f'El Asistente es: {asistente}')
print(f'El Profesor es: {profesor}')