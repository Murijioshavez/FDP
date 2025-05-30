a=5
b=3
c = a/b
decimales = 10

def truncar(numero,decimales):
    factor = 10**decimales
    print(int(numero*factor)/factor)

truncar(c,decimales)