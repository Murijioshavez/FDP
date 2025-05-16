list = [5,2,3,80,47,45,61,7,8,8,90,9,10]

list.remove(list[-2])
print(list)

list.sort()
print(list)

list.sort(reverse=True) # reverse=True lista en reversa
print(list)

persona = {'nombre': 'mau', 'edad': 20}

for clave, valor in persona.items(): #items hace que lo itere como una lista y no como diccionario
    print(f'{clave}: {valor}')
    
print(persona.keys())
print(persona.values())


