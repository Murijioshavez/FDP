'''
Clase:        Correlativo de clase
Tema:         Listas
Ejercicio:    Sumador de posicion
Descripción:  Pues segui las indicaciones de la guia

Autor:        Mauricio ALejandro Chávez Funes
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''
numero = input('Ingrese el numero a sumar ')
x = numero
while True:
    y = x   
    if len(x) > 1:
        lista = []
        for j in x:
            lista.append(int(j))       
    x = str(sum(lista))
    if len(x) == 1:
        print(f"{y} = {x}")
        break
    print(f"{y} = {x}")
    
print('El resultado final es:', x)