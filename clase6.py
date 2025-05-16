from functools import reduce
students = [{'nombre':'Dennis', 'edad':'19','carrera':'computacion'},{'nombre':'Yajaira', 'edad':'19','carrera':'computacion'},{'nombre':'Alfredo', 'edad':'19','carrera':'computacion'},{'nombre':'Julio', 'edad':'18','carrera':'computacion'},{'nombre':'Mauricio', 'edad':'18','carrera':'computacion'}]

# print(students.get('nota', 'No aplica'))
nums = [1,2,3,4,5,6,7,8,30,40,50]
# list = list *2
# print(list)

squared = list(map(lambda x:x*x,nums))
print(squared)

filtered = list(filter(lambda x:x >25, nums))
print(filtered)

result = reduce(lambda x,y:x*y,nums)
print(result)


with open('doc_importante.txt', 'w') as archivo:
    archivo.write('holaaaaaa, con esto borro todo y escribo esto, con "w"')
    print(archivo)
with open('doc_importante.txt', 'r') as archivo:
    contenido = archivo.read()
    words = contenido.split()
    pares = 0
    for word in words:
        if len(word) %2 == 0:
            pares+=1
    print(pares)



with open('doc_importante.txt', 'a') as archivo:
    archivo.write('esto se agrega al final del archivo, con "a"')
    print(archivo)
file = open('doc_importante.txt', 'r')
file.close
try:
    with open('doc_importante.txt', 'x') as archivo:
        archivo.write('esto se agrega al final del archivo, con "x"')
except:
    print('el archivo ya existe')
finally:
    file = open('doc_importante.txt', 'r')
    file.close


