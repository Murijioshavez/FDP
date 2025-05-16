palabras_a_buscar = ["PAJARO", "GATO", "GATOS", "PERRO", "TIGRE", "RATON"]
encontradas = {}
lineas = []

# Leer la sopa
with open('sopa_de_letras.txt', 'r') as f:
    for linea in f:
        letras = linea.strip().split()
        lineas.append(letras)

counter = 0  
for fila in lineas:
    texto = ''.join(fila)
    for palabra in palabras_a_buscar:
        x = texto.find(palabra)
        if palabra in texto:
            print(f'{palabra} [{counter}, {x}]')
    counter += 1
