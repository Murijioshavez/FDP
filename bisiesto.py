'''
Clase:        Condicionales
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción: saber si un anio es biciesto
Autor:        Mauricio Alejandro Chávez Funes
Fecha:        2025-05-15
Estado:       [ Terminado ]
Este ejercicio ya lo habia hecho en hacker rank
'''
def is_leap(year): 
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap
year = int(input()) 
print(is_leap(year))