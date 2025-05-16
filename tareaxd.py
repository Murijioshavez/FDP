import csv

with open('database.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)

def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    apellido = input("Ingrese el apellido del estudiante: ").strip().lower()
    identificador = nombre + apellido  
    with open('database.csv', 'r', newline="") as file:
        reader = csv.reader(file)
        estudiantes = list(reader)
    for row in estudiantes:
        if row[0].strip().lower() == identificador:
            print("Ya existe un estudiante con ese nombre y apellido.")
            return
    if len(estudiantes) > 1:
        ultimo_id = int(estudiantes[-1][1])
    else:
        ultimo_id = 0  
    nuevo_id = ultimo_id + 1  
    with open('database.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([identificador, nuevo_id, '0', '0', '0', '0', '0'])  
    print("Estudiante agregado con éxito")
    print('<', '-' * 50, '>')

def ver_todo_estudiante():
    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            print('nombre', row['name'], 'calculo:', row['calculo'], 'fisica:', row['fisica'], 'dp:', row['dp'], 'Introduccion a la ingeneria:', row['intro'], 'programacion:', row['programacion'])
    print('<', '-'*50, '>')

def ver_estudiante_especifico():
    criterio = input("Ingrese el ID o el nombre completo del estudiante: ").strip().lower()
    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            identificador = row['name'].strip().lower()
            if row['id'] == criterio or identificador == criterio.replace(" ", ""):
                print(f"Nombre: {row['name']}, ID: {row['id']}, Cálculo: {row['calculo']}, Física: {row['fisica']}, DP: {row['dp']}, Introducción a la ingeniería: {row['intro']}, Programación: {row['programacion']}")
                return
    print("Estudiante no encontrado.")
    print('<', '-' * 50, '>')

def actualizar_notas():
    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        estudiantes = list(data)
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    materias = {'calculo': 'c', 'fisica': 'f', 'dp': 'd', 'intro': 'i', 'programacion': 'p'}
    materia = input("Ingrese la materia a actualizar (Cálculo, Física, DP, Intro, Programación): ").strip().lower()
    materia = [key for key, value in materias.items() if materia == key or materia == value]
    if not materia:
        print("Materia no encontrada.")
        return
    materia = materia[0]
    nota = input("Ingrese la nueva nota (1-100): ").strip()
    if not nota.isdigit() or not (1 <= int(nota) <= 100):
        print("Nota inválida. Debe ser un número entre 1 y 100.")
        return
    for row in estudiantes:
        if row['name'].strip().lower() == nombre:
            row[materia] = nota
            print("Nota actualizada para", row['name'], "en", materia, "a", nota)
            break
    else:
        print("No se encontró al estudiante.")
        return  
    with open('database.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(estudiantes)
    print('<', '-'*50, '>')

def calcular_promedio():
    with open('database.csv', 'r') as file:
        data = csv.reader(file)
        estudiantes = list(data)
        nombre = input("Ingrese el nombre del estudiante: ").strip().lower()  
        for row in estudiantes[1:]: 
            if row[0].strip().lower() == nombre: 
                notas = list(map(int, row[2:]))  
                promedio = sum(notas) / len(notas)
                print('El promedio del estudiante es:', promedio)
                return  
        print('No se encontró el estudiante')
    print('<', '-'*50, '>')

def el_mejor_de_todos():
    with open('database.csv', 'r') as file:
        data = csv.reader(file)
        estudiantes = list(data)
        cums = {}
        for row in estudiantes[1:]:
            notas = list(map(int, row[2:]))
            promedio = sum(notas)/len(notas)
            cums[row[0]] = promedio
        mejor_cum = max(cums, key=cums.get)
        print('El mejor de todos es', mejor_cum, 'con un cum de', cums[mejor_cum])
    print('<', '-'*50, '>')

while True:
    option = input('Ingrese el número o nombre de la opción:\n1. agregar estudiante\n2. ver todos los estudiantes\n3. actualizar notas\n4. calcular promedio5. encontrar el mejor estudiante\n6. encontrar el mejor de todos\n7. ver estudiante específico\n8. salir\n').strip().lower()
    
    if option in ['1', 'agregar estudiante']:
        agregar_estudiante()
    elif option in ['2', 'ver todos los estudiantes']:
        ver_todo_estudiante()
    elif option in ['3', 'actualizar notas']:
        actualizar_notas()
    elif option in ['4', 'calcular promedio']:
        calcular_promedio()
    elif option in ['5', 'encontrar el mejor estudiante']:
        mejor_dela_clase()
    elif option in ['6', 'encontrar el mejor de todos']:
        el_mejor_de_todos()
    elif option in ['7', 'ver estudiante específico']:
        ver_estudiante_especifico()
    elif option in ['8', 'salir']:
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")