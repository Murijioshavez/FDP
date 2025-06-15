matriz = [[1,2,3],[4,5,6],[7,8,9]]

for lista in matriz:
    for elemento in lista:
        print(elemento, end=' ')
        
        

for i in range(len(matriz)):
    print(i)
    print(matriz[i])
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=' ')
