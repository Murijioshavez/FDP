print('Bienvenido a mi calculadora basica')
while True:
    num1 = int(input('entra tu primer numero'))
    num2 = int(input('entra el segundo numero '))
    print('Selecciona con el numero o signo la operacion por hacer')
    operacion = input('1. Suma(+) \n2. Resta(-) \n3. Multiplicacion(*) \n4. Division(/)\n5. Apagar calculadora')
    if operacion == '1' or operacion == '+':
        print('El resultado es', num1+num2)
    elif operacion == '2' or operacion == '-':
        print('El resultado es', num1-num2)
    elif operacion == '3' or operacion == '*':
        print('El resultado es', num1*num2)
    elif operacion == '4' or operacion == '/':
        if num2 < 0:
            print('no se puede dividir entre 0 XD')
            continue
        print('El resultado es', num1/num2)
    elif operacion == '5':
        print('gracias por usar mi calculadora')
        break
    else:
        print('entrada no valida, asi que ingresa numeros de nuevo')