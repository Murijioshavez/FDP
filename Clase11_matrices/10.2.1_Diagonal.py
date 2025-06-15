'''
Clase:        Correlativo de clase
Tema:         matrices
Ejercicio:    10.2.1
Descripción:  Pues segui las indicaciones de la guia

Autor:        Mauricio ALejandro Chávez Funes
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
numero = int(input('Entre el numero'))
matriz = []   
salidas = []
temp_list = []
for i in range(numero):
    fila = input(f"Entre los valores para la fila {i+1} ")
    matriz.append(fila.split(','))


for index in range(len(matriz)):
    temp_list.append(matriz[index][index])
salidas.append(temp_list)
temp_list = []
for index in range(len(matriz)):
    index_reversed = (index+1)*-1
    temp_list.append(matriz[index][index_reversed])
salidas.append(temp_list)
temp_list = []

for i in salidas:
    print(salidas, end='\n')
    
        