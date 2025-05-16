import csv
import json

def csv_to_json(csv_filename, json_filename):
    data = {}
    with open(csv_filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Nombre']
            if name not in data:
                data[name] = {"Edad": int(row['Edad'])}
            data[name][row['Materia']] = float(row['Nota'])
    
    with open(json_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"CSV convertido a JSON y guardado en {json_filename}")

def json_to_csv(json_filename, csv_filename):
    with open(json_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    subjects = set()
    for student in data.values():
        subjects.update(student.keys())
    subjects.discard("Edad")
    
    fieldnames = ['Nombre', 'Edad'] + sorted(subjects)
    with open(csv_filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for name, student_data in data.items():
            row = {'Nombre': name, 'Edad': student_data['Edad']}
            row.update({subject: student_data.get(subject, '') for subject in subjects})
            writer.writerow(row)
    print(f"JSON convertido a CSV y guardado en {csv_filename}")

def create_sample_files():
    sample_csv = """Materia,Nombre,Edad,Nota
Matemáticas,Juan Pérez,16,8.5
Física,Juan Pérez,16,7.8
Historia,Juan Pérez,16,9.0
Matemáticas,Ana López,17,9.0
Historia,Ana López,17,8.2
Física,Ana López,17,8.5
"""
    with open('materias.csv', 'w', encoding='utf-8') as file:
        file.write(sample_csv)
    print("Archivo materias.csv creado.")
    
    sample_json = {
        "Juan Pérez": {
            "Edad": 16,
            "Matemáticas": 8.5,
            "Física": 7.8,
            "Historia": 9.0
        },
        "Ana López": {
            "Edad": 17,
            "Matemáticas": 9.0,
            "Historia": 8.2,
            "Física": 8.5
        }
    }
    with open('materias.json', 'w', encoding='utf-8') as file:
        json.dump(sample_json, file, indent=4, ensure_ascii=False)
    print("Archivo materias.json creado.")

if __name__ == "__main__":
    create_sample_files()
    choice = input("¿Quieres convertir CSV a JSON (1) o JSON a CSV (2)? ")
    if choice == '1':
        csv_to_json('materias.csv', 'materias.json')
    elif choice == '2':
        json_to_csv('materias.json', 'materias.csv')
    else:
        print("Opción inválida.")
