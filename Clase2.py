
actual = 2025
while True:
    print('escoge una de las opciones con el numero')
    respuesta = input('1. Correr programa \n2. Salir del programa')
    if respuesta == '2':
        break
    edad = int(input('Cual es tu edad?'))
    anio = int(input('anio que quieres saber tu edad'))
    prediccion = edad + (anio - actual)
    if edad < 0:
        print('El anio que pusiste ni siquiera habias nacido')
        continue
    print('tu edad en', anio, 'sera', prediccion)
