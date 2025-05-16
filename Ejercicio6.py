#Ejercicio de la clase 6

with open('doc_importante.txt', 'r') as archivo:
    contenido = archivo.read()
    words = contenido.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
print(word_count)