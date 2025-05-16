# def trans_texto(texto):
#     #escribe el codigo
#     a = texto.split()
#     print(a)
#     e = a[::-1]
#     print(e)
#     e = " ".join(e)
#     print(e)
#     i = e.swapcase()
#     print(i)
#     return i


class Pene:
    def __init__(self, texto):
        self.texto = texto
        
    def __str__(self):
        print(self)

a = Pene('hola')
a.__str__()