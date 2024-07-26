
import math

# Promedio de duración (horas)
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duracion de Crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duracion
diferencia_con_min = 100 - math.floor(dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - math.floor(dalto_curso / otros_cursos_promedio * 100)

# Mostrando las diferencias de duracion ( Ejercicio A)
print('Ejercicio A:')
print('El curso de Dalto dura:')
print(f' - un {diferencia_con_min}% menos que el más rápido')
print(f' - un {diferencia_con_max}% menos que el más lento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print('------------')

# Calculando el porcentaje de tiempo vacio eliminado
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto    = 100 - dalto_curso * 1000 // crudo_dalto / 10

# Mostrando la cantidad de espacios vacios que se eliminan (Ejercicio B)
print('Ejercicio B:')
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío')
print(f'Este curso Dalto elimina un {tiempo_vacio_dalto}% de tiempo vacío')
print('------------')


# Mostrando diferencias si los cursos duraran 10 horas (Ejercicio C)
print('Ejercicio C:')
print(f'Ver 10h de este curso equivale a ver {otros_cursos_promedio * 1000 // dalto_curso / 100} horas de otros cursos')
print(f'Ver 10h de otros cursos equivale a ver {dalto_curso * 1000 // otros_cursos_promedio / 100} horas de este curso')