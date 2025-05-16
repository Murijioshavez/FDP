import re
students = [{'nombre':'Dennis', 'edad':'19','carrera':'computacion'},{'nombre':'Yajaira', 'edad':'19','carrera':'computacion'},{'nombre':'Alfredo', 'edad':'19','carrera':'computacion'},{'nombre':'Julio', 'edad':'18','carrera':'computacion'},{'nombre':'Mauricio', 'edad':'18','carrera':'computacion'}]

x = input('Ingrese el nombre')
for i in students:
    if i['nombre'] == x:
        print(f'El estudiante {i["nombre"]} tiene {i["edad"]} años y estudia la carrera de {i["carrera"]}.')