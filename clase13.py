'''
Clase:        Tipos de datos
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Calculadora de totales
Autor:        Mauricio Alejandro Chávez Funes
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
subtotal = float(input('Ingrese el subtotal de la cuenta'))
propina = subtotal *0.1
total = subtotal + propina
print(f'Subtotal: ${subtotal:.2f}\nPropina: ${propina:.2f}\nTotal de la cuenta: ${total:.2f}')