import csv
# Sacamos encabezados
with open('database.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    file.close()
#<---------------------------------------------------------------------------------------------------->
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    apellido = input("Ingrese el apellido del estudiante: ").strip().lower()
    identificador = nombre + apellido  # ID único basado en nombre y apellido
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

    # Agregar nuevo estudiante al archivo CSV
    with open('database.csv', 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([identificador, nuevo_id, '0', '0', '0', '0', '0'])  

    print("Estudiante agregado con éxito")
    print('<', '-' * 50, '>')

#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def ver_todo_estudiante():
    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            print('nombre',row['name'], 'calculo:', row['calculo'], 'fisica:', row['fisica'], 'dp:', row['dp'],'Introduccion a la ingeneria:', row['intro'], 'programacion:', row['programacion'])
    file.close()
    print('<', '-'*50, '>')
#<---------------------------------------------------------------------------------------------------->

def ver_estudiante_especifico():
    criterio = input("Ingrese el ID o el nombre completo del estudiante: ").strip().lower()

    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            identificador = row['name'].strip().lower()  # Asegurar formato de comparación
            if row['id'] == criterio or identificador == criterio.replace(" ", ""):  
                print(f"Nombre: {row['name']}, ID: {row['id']}, Cálculo: {row['calculo']}, "
                      f"Física: {row['fisica']}, DP: {row['dp']}, "
                      f"Introducción a la ingeniería: {row['intro']}, Programación: {row['programacion']}")
                return
    print("Estudiante no encontrado.")
    print('<', '-' * 50, '>')
#<---------------------------------------------------------------------------------------------------->   
def actualizar_notas():
    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        estudiantes = list(data)

    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    materia = input("Ingrese la materia a actualizar (Cálculo, Física, DP, Intro, Programación): ").strip().lower()
    if materia.startswith('c') or materia.startswith('m'):
        materia = 'calculo'
    elif materia.startswith('f'):
        materia = 'fisica'
    elif materia.startswith('d'):
        materia = 'dp'
    elif materia.startswith('i'):
        materia = 'intro'
    elif materia.startswith('p'):
        materia = 'programacion'      
    else:  
        print("Materia no encontrada.")
        return
    
    nota = input("Ingrese la nueva nota (1-100): ").strip()
    if int(nota) >=1 or int(nota) <= 100:
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
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def calcular_promedio():
    with open('database.csv', 'r') as file:
        data = csv.reader(file)
        estudiantes = list(data)
        nombre = input("Ingrese el nombre del estudiante: ").strip().lower()  
        promedio = 0
        for row in estudiantes[1:]: 
            if row[0].strip().lower() == nombre: 
                notas = list(map(int, row[2:]))  
                promedio = sum(notas) / len(notas)
                print('El promedio del estudiante es:', promedio)
                return  

        print('No se encontró el estudiante')

    print('<', '-'*50, '>')
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def mejor_dela_clase():
    with open('database.csv', 'r') as file:
        data = csv.DictReader(file)
        estudiantes = list(data)
        mejor_dela_clase = None
        mejor_dela_clase_nota = 0
        ans = input('Escriba la materia donde quiere encontrar al mejor estudiante:\n1.Calculo'
                        '\n2.Fisica\n3.DP\n4.Intro\n5.Programacion\n')
        ans = ans.lower()
        if ans.startswith('c') or ans.startswith('m') or ans =='1':
            ans = 'calculo'
        elif ans.startswith('f') or ans =='2':
            ans = 'fisica'
        elif ans.startswith('d') or ans =='3':
            ans = 'dp'
        elif ans.startswith('i') or ans =='4':
            ans = 'intro'
        elif ans.startswith('p') or ans =='5':
            ans = 'programacion'
        else:
            print('Materia inválida. Por favor, entre el nombre de una de las materias.')
            print('<', '-'*50, '>')
            return
        for nota in estudiantes:
            if mejor_dela_clase == None:
                mejor_dela_clase = nota['name']
                mejor_dela_clase_nota = nota[ans]
            elif int(nota[ans]) > int(mejor_dela_clase_nota):
                mejor_dela_clase = nota['name']
                mejor_dela_clase_nota = nota[ans]
            elif int(nota[ans]) == int(mejor_dela_clase_nota):
                print('los mejores de la clase son:', mejor_dela_clase, 'y', nota['name'], 'con una calificacion de:', nota[ans])
        
        print('El mejor de la clase es:', mejor_dela_clase, 'con una calificacion de:',mejor_dela_clase_nota )
        print('<', '-'*50, '>')
#<---------------------------------------------------------------------------------------------------->
       
#<---------------------------------------------------------------------------------------------------->
def el_mejor_de_todos():
    with open('database.csv', 'r') as file:
        data = csv.reader(file)
        estudiantes = list(data)
        cums = {}
        for row in estudiantes[1:]:
            promedio = 0
            notas = list(map(int, row[2:]))
            promedio = sum(notas)/len(notas)
            cums[row[0]] = promedio
        mejor_cum = max(cums, key=cums.get)
        print(cums)
        print('El mejor de todos es', mejor_cum, 'con un cum de', cums[mejor_cum])
    print('<', '-'*50, '>')
#<---------------------------------------------------------------------------------------------------->

while True:
    option = input('Ingrese por número o nombre la actividad que quiere hacer:\n1. agregar estudiante (agregar)\n2.ver todos los estudiantes (ver)\n3.actualizar notas de los estudiantes (actualizar)'
                   '\n4. calcular el promedio (promedio)\n5. encontrar el mejor de cada clase (mejor)\n6.encontrar al mejor de todos (mejor_todos)\n7. Ver estudiante especifico (estudiante_especifico)\n8. salir (salir)\n').strip().lower()
    
    if option == '1' or option == 'agregar' or option.startswith('ag'):
        agregar_estudiante()
    elif option == '2' or option == 'ver' or option.startswith('v'):
        ver_todo_estudiante()
    elif option == '3' or option == 'actualizar' or option.startswith('ac'):
        actualizar_notas()
    elif option == '4' or option == 'promedio' or option.startswith('p'):
        calcular_promedio()
    elif option == '5' or option == 'mejor' or option.startswith('m'):
        mejor_dela_clase()
    elif option == '6' or option == 'mejor_todos' or option.__contains__('t'):
        el_mejor_de_todos()
    elif option == '7' or option == 'estudiante_especifico' or option.__contains__('es'):
        ver_estudiante_especifico()
    elif option == '8' or option == 'salir' or option.startswith('s'):
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")