'''
Clase:        Correlativo de clase
Tema:         matrices
Ejercicio:    10.3.1
Descripción:  Pues segui las indicaciones de la guia

Autor:        Mauricio ALejandro Chávez Funes
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
dimension_de_matriz = int(input())

matriz_entrada = []
for indice_de_fila in range(dimension_de_matriz):
    texto_de_fila = input().split(',')  
    fila_de_enteros = []
    for texto_de_valor in texto_de_fila:
        fila_de_enteros.append(int(texto_de_valor))
    matriz_entrada.append(fila_de_enteros)

matriz_es_simetrica = True
for indice_de_fila in range(dimension_de_matriz):
    for indice_de_columna in range(dimension_de_matriz):
        valor_en_posicion = matriz_entrada[indice_de_fila][indice_de_columna]
        valor_transpuesto = matriz_entrada[indice_de_columna][indice_de_fila]
        if valor_en_posicion != valor_transpuesto:
            matriz_es_simetrica = False
            break
    if not matriz_es_simetrica:
        break

if matriz_es_simetrica:
    print("La matriz es simétrica")
else:
    print("La matriz no es simétrica")
