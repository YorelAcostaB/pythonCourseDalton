ingreso_mensual = 72000
gasto_mensual = 8000

# if anidados y else if (elif)


if (ingreso_mensual >= 10000):
    print('Estas bien economicamente en cualquier parte del mundo')

    if (gasto_mensual - gasto_mensual < 0):
        print('Estas en deficit')
    elif ingreso_mensual - gasto_mensual > 3000:
        print('Tus finanzas son correctas')
    else:
        print('Estas gastando una banda para tus ahorros')


elif (ingreso_mensual >= 1000):
    print('Estas bien economicamente en LATAM')

elif (ingreso_mensual >= 500):
    print('Estas bien economicamente en Argentina')

elif (ingreso_mensual >= 200):
    print('Estas bien economicamente en Venezuela')

else:
    print('sos pobre')