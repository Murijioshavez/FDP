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
    impuesto = consumido * 0.5
    print('Su impuesto es:', impuesto)
    print(f'el total es ${consumido + impuesto}')
elif consumido >= 201:
    impuesto = consumido * 0.7
    print('Su impuesto es:', impuesto)
    print(f'el total es ${consumido+impuesto}')
    
#<----------------------------------------------->
numero = int(input('Ingrese un numero:'))
if numero % 7 == 0 and numero % 5 != 0:
    print('El numero es magico')
    