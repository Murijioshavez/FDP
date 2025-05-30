'''
Clase:        Correlativo de clase
Tema:         Listas
Ejercicio:    Adivina el numero
Descripción:  Pues segui las indicaciones de la guia

Autor:        Mauricio ALejandro Chávez Funes
Fecha:        2025-05-28
Estado:       [ Terminado ]
'''

import random
num_secreto = random.randint(1,100)

while True:
    x = int(input('Adivina un numero del 1 al 100'))
    if x < num_secreto:
        print('El numero secreto es mayor')
    elif x > num_secreto:
        print('El numero secreto es menor')
    elif x== num_secreto:
        print('Felicidades, adivinaste el numero secreto')
        break
    else:
        print('No es un numero del 1 al 100')