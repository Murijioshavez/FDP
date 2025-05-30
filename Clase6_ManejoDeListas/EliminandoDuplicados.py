entrada = input('Ingrese los numeros separados por espacios: ')
lista = entrada.split()
unicos = []
for i in lista:
    if i in unicos:
        continue
    else:
        unicos.append(i)

print(" ".join(unicos))