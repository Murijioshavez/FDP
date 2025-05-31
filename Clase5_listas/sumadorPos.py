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

while True:
    y = numero   
    if len(numero) > 1:
        lista = []
        for j in numero:
            lista.append(int(j))       
    numero = str(sum(lista))
    print(f"{y} = {numero}")
    if len(numero) == 1:
        break
    
print('El resultado final es:', numero)