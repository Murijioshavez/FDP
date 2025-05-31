entrada = input('Ingrese los numeros separados por espacios: ')
lista = entrada.split()
unicos = []
for i in lista:
    if i not in unicos:
        unicos.append(i)
print(" ".join(unicos))