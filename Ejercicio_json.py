import json
# Esto es para evitar mucha indentación y que no nos confundamos Ish
def cargar_datos():
    with open('database.json', 'r') as file:
        return json.load(file)

def guardar_datos(data):
    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4) #indent lo vimos en clase y lo hace más legible
#<---------------------------------------------------------------------------------------------------->
#Ahora ponemos las funciones que importan Ish
#<---------------------------------------------------------------------------------------------------->
def agregar_estudiante():
    data = cargar_datos()
    nombre = input("Ingrese el nombre del estudiante: ")
    data["students"].append({"name": nombre, "calculo": 0, "fisica": 0, "dp": 0, "intro": 0, "programacion": 0})
    guardar_datos(data)
    print("¡Estudiante agregado con éxito!\n")
    print('<------------------------------>')
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def ver_todos():
    data = cargar_datos()
    for student in data["students"]:
        print(student)
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def actualizar_notas():
    data = cargar_datos()
    nombre = input("Ingrese el nombre del estudiante: ")
    for student in data["students"]:
        if student["name"].lower() == nombre.lower():
            materia = input("Ingrese el nombre de la materia (calculo, fisica, dp, intro, programacion): ").lower()
            if materia in student:
                student[materia] = int(input(f"Ingrese la nueva nota para {materia}: "))
                guardar_datos(data)
                print("\n")
                print("¡Nota actualizada con éxito!\n")
                return
    print("Estudiante o materia no encontrados")
    print('<------------------------------>')
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def calcular_promedio():
    data = cargar_datos()
    nombre = input("Ingrese el nombre del estudiante: ")
    print("\n")
    for student in data["students"]:
        if student["name"].lower() == nombre.lower():
            promedio = float(sum(student[materia] for materia in student if materia != "name") / 5)
            print("\n")
            print(f"El promedio de {nombre} es: {promedio}\n")
            return
    print("Estudiante no encontrado")
    print('<------------------------------>')
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def mejor_dela_clase():
    data = cargar_datos()
    materia = input("Ingrese la materia (calculo, fisica, dp, intro, programacion): ").lower()
    if not data["students"]:
        print("No hay estudiantes registrados")
    mejor = max(data["students"], key=lambda x: x.get(materia, 0))
    print("\n")
    print(f"El mejor en {materia} es {mejor['name']} con una calificación de {mejor[materia]}\n")
    print('<------------------------------>')
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
def el_mejor_de_todos():
    data = cargar_datos()
    if not data["students"]:
        print("No hay estudiantes registrados")
    mejor = max(data["students"], key=lambda x: sum(x[materia] for materia in x if materia != "name") / 5)
    promedio = sum(mejor[materia] for materia in mejor if materia != "name") / 5
    print("\n")
    print(f"El mejor estudiante es {mejor['name']} con un promedio de {promedio:.2f}\n")
    print('<------------------------------>')
#<---------------------------------------------------------------------------------------------------->

#<---------------------------------------------------------------------------------------------------->
#Aquí empieza el programa Ish con el menú
print("Hola! Bienvenido a la base de datos de los estudiantes de Key Institute, ¿qué deseas hacer hoy?")
while True:
    option = input("1. Agregar estudiante\n2. Ver todos los estudiantes\n3. Actualizar notas\n4. Calcular promedio\n5. Mejor estudiante en una materia\n6. Mejor estudiante\n7. Salir\n")
    if option == '1':
        agregar_estudiante()
    elif option == '2':
        ver_todos()
    elif option == '3':
        actualizar_notas()
    elif option == '4':
        calcular_promedio()
    elif option == '5':
        mejor_dela_clase()
    elif option == '6':
        el_mejor_de_todos()
    elif option == '7':
            break
    else:
        print("Opción no válida")