print('Bienvenido a mi primera tarea de fundamentos de programacion.\nPor favor, seleccione una acción por hacer')
def factorial_con_bucle_for():
    print('Vamos a sacar el factorial de un número con bucle for')
    num = int(input('Entra un número entero para sacar su factorial(recuerda que los negativos no tienen factorial)'))
    if num <0:
        print('Los negativos no tienen factorial')
    else:
        for i in range (1, num):
            num *=i    
        print(num)
        print('Ahí tienes el factorial')
def factorial_con_bucle_while():
    print('Vamos a sacar el factorial de un número con bucle while')
    num = int(input('Entra un número entero para sacar su factorial(recuerda que los negativos no tienen factorial)'))
    if num <0:
        print('Los negativos no tienen factorial')
    else:
        fact = num
        while num > 1:
            fact = fact * (num - 1)
            num-=1
        print(fact)
        print('Ahi tienes el factorial')
def invertir_cadenas_de_texto():
    word = input('entra la palabra para invertir')
    reversedWord = ''
    for i in reversed(word):
        reversedWord+=i
    print('La palabra invertida es:', reversedWord)

def secuencia_de_Fibonacci():
    print('Vamos a sacar la secuencia de Fibonacci')
    num = int(input('Entra un número entero para sacar la secuencia de Fibonacci'))
    a, b = 0, 1
    while a < num:
        a, b = b, a+b
        print(a, end=' ')
    print('Aqui tienes la secuencia de Fibonacci')

while True:
    ans = input('1.Factorial con bucle for\n2.Factorial con bucle while\n3.Invertir cadena de texto\n4.Secuencia de Fibonacci\nPara salir entre cualquier otra cosa')
    if ans == '1':
        factorial_con_bucle_for()
    elif ans == '2':
        factorial_con_bucle_while()
    elif ans == '3':
        invertir_cadenas_de_texto()
    elif ans == '4':
        secuencia_de_Fibonacci()
    else:
        print('Hasta luego')
        break