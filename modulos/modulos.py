# importando un modulo y asignandole el nombre "ms" como namespace
import modulos.buenas_funciones.modulo_saludar as ms

# accede al método de la clase/modulo ms mediante nombre_modulo.nombre_metodo
# saludo = ms.saludar('Agustin')

# desde ese modulo, importamos las funciones unicamente mencionadas y les cambiamos el nombre
from modulos.buenas_funciones.modulo_saludar import saludar as s, saludo_gangoso as sg

# mala practica para importar todos los recursos de un modulo
#from modulo_saludar import *


# mostramos los resultados
saludo = s('Agustin')
saludo_raro = sg('ElManitas')
print(saludo)
print(saludo_raro)

# para ver las propiedades y metodos de el namespace
print(dir(ms))

# accedemos al nombre de este modulo
print(__name__)

# accedemos al nombre del modulo llamado
#print(ms.__name__)