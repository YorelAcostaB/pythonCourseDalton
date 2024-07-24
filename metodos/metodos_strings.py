cadena1 = 'Hola,soy,el,mismisimo,Agus'
cadena2 = 'Bienvenido fiera'
cadena3 = '12731980237891723'
cadena4 = 'ASD12asd73198asd023asd7891723'

# convierte a mayyusculas
mayus = cadena1.upper()

# convierte a minuscula
minus = cadena1.lower()

# primera letra en mayuscula
primer_letra_mayus = cadena1.capitalize()

# buscar una cadena en otra cadena / Si no hay coincidencias devuelve -1
busqueda_find = cadena1.find('d')

# buscar una cadena en otra cadena. / Si no hay coincidencias lanza excepcion
busqueda_index = cadena1.index('a')

# si es numerico, devolvemos true, si no false
es_num = cadena3.isnumeric()

# si es alfanumerico, devolvemos true, si no false
es_alfanum = cadena4.isalpha()

# contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count('soy')

# contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es así devuelve True
empieza_con = cadena1.startswith('Hol')

# verificamos si una cadena termina con otra cadena dada, si es así devuelve True
termina_con = cadena1.endswith('s')

# remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace('la', 'lu')

# serparar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(',')
resultado = cadena_separada
print(resultado)