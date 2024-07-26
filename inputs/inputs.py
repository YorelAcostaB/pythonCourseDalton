# pedirle un dato al usuario
nombre = input('Dime como te llamas: ')
numero = input('Dame un numero pa: ')

# cuento la cantidad de caracteres del nombre
cant_caracteres = len(nombre)

# convierte el numero a entero y lo multiplico por 2
producto = int(numero) * 2

# convierte el numero a float y lo multiplico por 2
producto_f = float(numero) * 2

print(f'Tu nombre tiene {cant_caracteres} caracteres')
print(f'INT Resultado del producto: {producto}')
print(f'FLOAT Resultado del producto: {producto_f}')