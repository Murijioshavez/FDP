# num = int(input('entra el numero XD'))
# for i in range(num+1):
#     print(i*'*')

# def celsius_to_farenheit(celcius):
#     return (celcius *9/5) +32
# for i in range(0, 101):
#     print(f'{i}°C = {celsius_to_farenheit(i)}°F ')

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'no se puede dividir entre 0'
    
print(divide(10,2))
print(divide(10,0))  # imprime 'no se puede dividir entre