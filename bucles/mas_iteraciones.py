# creando las listas
frutas = ['banana', 'manzana', 'naranja,' 'pera', 'ciruelas', 'granada']
cadena = 'Hola Yorel!'
bitcoins = [10, 7, 99, 51]

# evitando que se coma una naranja con sentencia continue (skip) 
for fruta in frutas:
    if(fruta == 'naranja'):
        continue
    print(f'Me voy a comer una {fruta}')
    
# evitar que el bucle siga ejecutandose (break)
for fruta in frutas:
    if (fruta == 'ciruela'):
        break
    else: # no se 
        print('terminado')

# recorrer cadena
for letra in cadena:
    print(letra)

# for en una sola linea de codigo (duplicamos los numeros)
bitcoins_duplicados = [x*2 for x in bitcoins]
print(bitcoins_duplicados)