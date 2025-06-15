'''
Clase:        Correlativo de clase
Tema:         matrices
Ejercicio:    10.2.1
Descripción:  Pues segui las indicaciones de la guia

Autor:        Mauricio ALejandro Chávez Funes
Fecha:        2025-06-14
Estado:       [ Terminado ]
'''
# Leer dimensiones
N = int(input())
M = int(input())

mat = []
for i in range(N):
    partes = input().split(',')  
    fila = []
    for num in partes:
        fila.append(int(num))
    mat.append(fila)

res = []
for i in range(N):
    fila = []
    for j in range(M):
        cnt = 0
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni = i + di
                nj = j + dj
                if ni >= 0 and ni < N and nj >= 0 and nj < M:
                    cnt = cnt + mat[ni][nj]
        fila.append(cnt)
    res.append(fila)
for fila in res:
    print(fila)

    
        