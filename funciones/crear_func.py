# creando una funcion simple
def saludar():
    print('Hola pa! ¿Todo bien?')
    
# ejecutando una funcion simple
saludar()

# crear una funcion con parametro
def saludo_2o(nombre, sexo):
    sexo.lower()
    adjetivo = ''

    if sexo == 'f':
        adjetivo = 'reina'
    elif sexo == 'm':
        adjetivo = 'rey'
    else:
        adjetivo = 'amor'

    print(f'Hola {nombre}, mi {adjetivo}. ¿Cómo andás?')
    
saludo_2o('Agus', 'm')
saludo_2o('Cami', 'F')
saludo_2o('Sandra', 'z')

# crear una funcion que nos retorne valores
def crear_contrasena_random(num):
    chars = 'abcdefghij'
    num_entero = str(num)
    num = int(num_entero[0])

    c1 = num - 2
    c2 = num
    c3 = num - 5

    passwd = f'{chars[c1]}{chars[c2]}{chars[c3]}{num_entero * 2}'

    return passwd


mi_paswd = crear_contrasena_random(7)
print(f'Tu nueva contraseña generada es: \"{mi_paswd}\"')





# forma no optima de sumar valores
def suma_simple(lista):
    numeros_sumados = 0

    for num in lista:
        numeros_sumados = numeros_sumados + num

    return numeros_sumados

resultado_suma_simple = suma_simple([5, 3, 9, 10, 20, 3])
print(f'Suma simple = {resultado_suma_simple}')


def suma_pro(*numeros):
    return sum(numeros)

resultado_suma_pro = suma_pro(5, 3, 9, 10, 20, 3)
print(f'Resultado de la Suma Pro = {resultado_suma_pro}')