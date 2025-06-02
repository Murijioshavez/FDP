'''
Clase:        Correlativo de clase
Tema:         Listas
Ejercicio:    Numeros lideres
Descripción:  Pues segui las indicaciones de la guia

Autor:        Mauricio ALejandro Chávez Funes
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''
entrada = input('Entre su lista de numeros separados por espacios: ')
lista_numeros = entrada.split()
lista_numeros = [int(x) for x in lista_numeros]
lideres = []
for i in range(len(lista_numeros)):
    if i == len(lista_numeros)-1:
        break
    elif lista_numeros[i] > lista_numeros[i+1]:
        lideres.append(lista_numeros[i])

en_str = list(map(str, lideres))
en_str.append(str(lista_numeros[-1]))    
print(" ".join(en_str))