'''
Clase:        Tipos de datos
Tema:         Tema de la clase
Ejercicio:    Identificador de la clase
Descripción:  Filtro de contrasenias seguras, impuestos según consumo y números mágicos
Autor:        Mauricio Alejandro Chávez Funes
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
password = input('Ingrese su contrasenia:')
longitud = False
mayus = False
digit = False
for c in password:
    if len(password) >= 8:
        longitud = True
        continue
    if c.isupper():
        mayus = True
        continue
    if c.isdigit():
        digit = True
            
if longitud and mayus and digit:
    print('La contra es segura')
else:
    print('La contra no es segura')
    
#<------------------------------------------->
consumido = int(input('Ingrese la cantidad consumida'))
impuesto = 0
if consumido <0:
    print('No se puede consumir menos de 0')
elif consumido >= 0 and consumido <= 100:
    print('Sin impuestos')
elif consumido >= 101 and consumido <= 200:
    for i in range(consumido+1):
        impuesto += 0.05
    print('Su impuesto es:', impuesto)
    print(f'el total es ${consumido + impuesto}')
elif consumido >= 201:
    for i in range(consumido+1):
        impuesto += 0.07
    print('Su impuesto es:', impuesto)
    print(f'el total es ${consumido+impuesto}')
    
#<----------------------------------------------->
numero = int(input('Ingrese un numero:'))
if numero % 7 == 0 and numero % 5 != 0:
    print('El numero es magico')
    