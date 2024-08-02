# creando una funcion que muestre la serie fibonacci entre 0 y el numero dado

def fibonacci(num):
    a,b = 0,1
    fibonacci_list = []
    for i in range(num):
        if b > num:
            return fibonacci_list
        else:
            fibonacci_list.append(b)
            a,b = b,a+b

    return fibonacci_list

resultado = fibonacci(20)
print(resultado)