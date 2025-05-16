
#Genera una lista que contiene listas de todas las palabras por renglón (info del estudiante)
def hacer_listas(documento):
    try:    
        with open(documento, "r") as file:

            lista_completa = []

            for line in file:
                lista_palabras = line.split()
                renglon = []
                
                for palabra in lista_palabras:
                    renglon.append(palabra)

                lista_completa.append(renglon)
    
    finally:
        file.close()
    
    return lista_completa

#Transformar la variedad de nombres posibles para una materia a un único término (con el fin de usarlo en el resto de funciones)
def confirmador_de_materias(materia):

    materialow = materia.lower()
    confirmador = False

    carnet = ["carné", "carne", "carnet", "id"]

    calculo = ["matemática", "matemáticas", "mate", "matematica", "matematicas", "calculo", "cálculo",
               "matemática 1", "matemáticas 1", "mate 1", "matematica 1", "matematicas 1", "calculo 1", "cálculo 1",
               "matemática i", "matemáticas i", "mate i", "matematica i", "matematicas i", "calculo i", "cálculo i",
               "cálculo diferencial", "calculo diferencial", "cálculo diferencial de una variable",
               "calculo diferencial de una variable", "caluclo", "mates", "calc", "calcu", "cal"]
    
    dp = ["desarrollo personal", "desarrollo", "dp", "personal"]

    introing = ["introducción", "introduccion", "intro", "intro a la ingeniería", "intro a la ingenieria", 
                "introduccion a la ingenieria", "intro ingenieria", "intro ingeniería", "ingenieria", "ingeniería",
                "intro a la ing", "ing", "solidworks", "solid works", "laboratorio de mecánica", "laboratorio de mecanica",
                "lab de mecánica", "lab de mecanica", "laboratorio mecánica", "laboratorio mecanica", "lab mecánica",
                "lab mecanica", "lab de meca", "lab meca", "introing"]
    
    fisica = ["física", "fisica", "física 1", "fisica 1", "física i", "fisica i", "física aplicada", "fisica aplicada",
              "física aplicada 1", "fisica aplicada 1", "física aplicada i", "fisica aplicada i"]
    
    fundeprogra = ["fundeprogra", "fundamentos de programación", "fundamentos de programacion", "programación", "programacion",
                   "fundamentos programación", "fundamentos programacion", "fundamentos", "funda", "python", "pyton", "progra"]
    
    posibles_nombres_categorias = {"carnet": carnet, "calculo": calculo, "dp": dp, "introing": introing, "fisica": fisica, 
                                   "fundeprogra": fundeprogra}
 
    for key_materia in (posibles_nombres_categorias):
        if materialow in posibles_nombres_categorias[key_materia]:
            materialow = key_materia
            confirmador = True
            break

    if confirmador == False:
        print(f"{materia} no es una materia válida. Por favor intente de nuevo e ingrese un término válido.")
        return None
    else:
        return materialow

def confirmar_nombre_en_lista(nombre, documento):

    masterlist = hacer_listas(documento)

    nombrelow = nombre.lower()
    nombrelow = nombrelow.replace(" ", "_")

    confirmador = False

    if len(masterlist) <= 1:
        print(f"La lista no tiene ningún nombre, por lo tanto {nombre} no se encuentra en ella.")
        return None
    
    length = len(masterlist)

    num_de_categorias_noname = (len(masterlist[1])-1)

    if num_de_categorias_noname == 0:
        print("Ha ocurrido un error inminente, el documento no ha sido preparado para la base de datos. ")
        print("Reininice el programa y oprima la opción 'Limpiar base de datos'")
        print("")
        quit()

    for line in masterlist[1:(length):num_de_categorias_noname]:
        if nombrelow in line:
            confirmador = True
            
    if confirmador == True:
        return(nombrelow)
    else:
        print(f"{nombre} no se encuentra en la lista. Escriba un nombre válido.")
        return None

def agregar_estudiante(nombre, documento):

    nombre = nombre.lower()
    nombre = nombre.replace(" ","_")
    masterlist = hacer_listas(documento)
    categorias = masterlist[0]

    try:    
        with open(documento, "a") as file:

            file.write(nombre)

            for i in range((len(categorias)) - 1):
                file.write(" None")

            file.write("\n")

            for categoria in (categorias[1:]):
                if categoria != "carnet":
                    file.write(nombre + "_" + categoria)
                    file.write("\n")
    
    finally:
        file.close()

def todos_estudiantes(documento):
    
    masterlist = hacer_listas(documento)
    length = len(masterlist)

    if (len(masterlist)) == 0:
        print("El documento no ha sido preparado para la base de datos. Reinicie el programa y oprima la opción 'Limpiar base de datos'")
        quit()
    elif (len(masterlist)) == 1:
        print("La lista no posee el nombre de ningún estudiante.")
        return None

    num_de_categorias_noname = (len(masterlist[1])-1) #Siempre se omite la categoría "Carnet"

    if num_de_categorias_noname == 0:
        print("Ha ocurrido un error inminente, el documento no ha sido preparado para la base de datos. ")
        print("Reininice el programa y oprima la opción 'Limpiar base de datos'")
        print("")
        quit()

    print(masterlist[0])
    for line in masterlist[1:(length):num_de_categorias_noname]:
        print(line)
    
def promedio_materia(nombre, materia, documento):

    masterlist = hacer_listas(documento)

    nombrefin = confirmar_nombre_en_lista(nombre, documento)
    materiafin = confirmador_de_materias(materia)

    if nombrefin == None:
        return None
    elif materiafin == None:
        return None

    name_of_location = (nombrefin + "_" + materiafin)
    
    subtotal = 0
    contador = 1

    for line in masterlist:
        
        if name_of_location == line[0]:
            
            if len(line) <= 1:
                print(f"No hay notas guardadas en el expediente de {nombre} en relación a la materia {materia}.")
                return None
            
            else:
                for notas in range(len(line)-1):
                    siguiente = float(line[contador])
                    subtotal = subtotal + siguiente
                    contador = contador + 1
    
    promedio = (subtotal/(contador-1))

    return promedio

def agregar_datos_stu(student, materia, neonota, documento):

    masterlist = hacer_listas(documento)

    student_c = confirmar_nombre_en_lista(student, documento)
    materia_c = confirmador_de_materias(materia)

    categorias = masterlist[0]

    if student_c == None:
        return None
    elif materia_c == None:
        return None

    if materia_c != "carnet":
        try:
            neonota = float(neonota)
        except:
            print(f"{neonota} no es una nota válida, coloque una nota válida por favor (número)")
            return None
        
        if neonota < 0:
            print(f"{neonota} no es una nota válida, coloque una nota válida por favor (número)")
            return None
    
    stu_materia = (student_c + "_" + materia_c)

    if materia_c == "carnet":
        try:
            with open(documento, "w") as file:
                for line in masterlist:
                    if student_c == line[0]:
                        posicion_carnet = categorias.index(materia_c)
                        line[posicion_carnet] = neonota
                    for item in line:
                        file.write(item)
                        file.write(" ")
                    file.write("\n")

        finally:
            file.close()

    else:    
        try:    
            with open(documento, "w") as file:
                for line in masterlist:
                    if stu_materia == line[0]:
                        line.append(neonota)
                    for item in line:
                        palabra = str(item)
                        file.write(palabra)
                        file.write(" ")
                    file.write("\n")
        
        finally:
            file.close()
    
    print(f"La nota/carnet ({neonota}) ha sido agregada exitosamente al expediente de {student} en relación a la materia {materia}.")

    if materia_c != "carnet":

        for line in masterlist:
            if student_c == line[0]:
                posicion = categorias.index(materia_c)
                line[posicion] = promedio_materia(student_c, materia_c, documento)

        try:
            with open(documento, "w") as file:
                for line in masterlist:
                    for item in line:
                        palabra = str(item)
                        file.write(palabra)
                        file.write(" ")
                    file.write("\n")
        
        finally:
            file.close()

def setear_documento(base_de_datos):
    try:
        with open(base_de_datos, "w") as file:
            file.write("name_of_student carnet calculo dp introing fisica fundeprogra \n")
    
    finally:
        file.close()

def quitar_espacios_costados(un_input):
    if un_input == "":
        print("No ha colocado un término válido. Intente colocarlo de nuevo.")
        return un_input
    elif un_input[-1] == " ":
        un_input = un_input[:-1]
        return quitar_espacios_costados(un_input)
    elif un_input[0] == " ":
        un_input = un_input[1:]
        return quitar_espacios_costados(un_input)
    else:
        return un_input
    
def mejor_en_clase(materia, documento):
    
    masterlist = hacer_listas(documento)
    materiafin = confirmador_de_materias(materia)

    if materiafin == "carnet":
        print("Esta función no puede utilizarse con la categoría de CARNET")
        return None
    
    if len(masterlist) <= 1:
        print("La lista no posee ningún dato en este momento, por lo tanto, no puede obtenerse al mejor promedio.")
        return None

    categorias = masterlist[0]
    posicion_de_materia = categorias.index(materiafin)

    nombres_y_notas = {}
    ganadores = []

    length = len(masterlist)

    num_de_categorias_noname = (len(masterlist[1])-1)

    if num_de_categorias_noname == 0:
        print("Ha ocurrido un error inminente, el documento no ha sido preparado para la base de datos. ")
        print("Reininice el programa y oprima la opción 'Limpiar base de datos'")
        print("")
        quit()

    for line in masterlist[1:(length):num_de_categorias_noname]:
        if line[posicion_de_materia] != "None":
            nombres_y_notas[line[0]] = float(line[posicion_de_materia])

    maximo = max(nombres_y_notas.values())

    for key, value in nombres_y_notas.items():
        if value == maximo:
            ganadores.append(key)

    if len(ganadores) == 1:
        print(f"La mejor nota en {materia} fue {maximo}, y fue obtenida por {ganadores[0]}.")
    else:
        print(f"La mejor nota en {materia} fue {maximo}, y fue obtenida por: ")
        print(ganadores)

    return None 

def goat(documento):

    masterlist = hacer_listas(documento)

    length = len(masterlist)

    promedios = {}

    ganadores = []

    if len(masterlist) <= 1:
        print("La lista no posee ningún dato en este momento, por lo tanto, no puede obtenerse al mejor promedio.")
        return None

    num_de_categorias_noname = (len(masterlist[1])-1)

    if num_de_categorias_noname == 0:
        print("Ha ocurrido un error inminente, el documento no ha sido preparado para la base de datos. ")
        print("Reininice el programa y oprima la opción 'Limpiar base de datos'")
        print("")
        quit()

    for line in masterlist[1:(length):num_de_categorias_noname]:
        numeros = line[2:]
        sumando = 0
        contador = 0
        floats_list = []

        for number in numeros:
            try:
                floats = float(number)
                floats_list.append(floats)

            except:
                continue

        if len(floats_list) == 0:
            return None
            
        for number in floats_list:
            sumando = sumando + number
            contador = contador + 1

        promedios[line[0]] = (sumando/contador)

    maximo = max(promedios.values())

    for key, value in promedios.items():
        if value == maximo:
            ganadores.append(key)

    if len(ganadores) == 1:
        print(f"El mejor promedio fue {maximo}, y fue obtenida por {ganadores[0]}.")
    else:
        print(f"El mejor promedio fue {maximo}, y fue obtenida por: ")
        print(ganadores)
    
    return None

print("Buen día, bienvenido a la interfaz de registro de notas.")
base_de_datos = input("Introduzca el path de su documento '.txt'. ")
print("")
base_de_datos = quitar_espacios_costados(base_de_datos)
continuar = True

if base_de_datos[-4:] == ".txt":
    try:
        with open(base_de_datos) as file:
            print("")
            file.close()

    except FileNotFoundError:
        print("No se ha encontrado la base de datos solicitada. Inténtelo de nuevo.")
        print("")
        quit()

else:
    print("Ha introducido un tipo de archivo inválido.")
    print("Asegúrese de que la extensión del archivo sea '.txt'.")
    print("Inténtelo de nuevo")
    print("")
    quit()

hay_base = input("¿Es necesario limpiar la base de datos? (Sí = 1, No = 0) ")
print("")

try:
    hay_base = int(hay_base)
except:
    print("Ha colocado un dato inválido. Reinicie el programa.")
    print("")
    quit()

if hay_base == 1:
    print(base_de_datos)
    setear_documento(base_de_datos)

while continuar == True:

    print("¿Qué acción le gustaría tomar en este momento?")
    print("Sus opciones son:")
    print("1. Agregar un el nombre de un estudiante.")
    print("2. Ver los nombres y promedios de todos los estudiantes.")
    print("3. Actualizar los datos de un estudiante (agregar una nueva nota a la materia)")
    print("4. Calcular el promedio de un estudiante en referencia a una materia.")
    print("5. Encontrar al mejor promedio de una materia determinada.")
    print("6. Encontrar al mejor promedio de todas las materias.")
    print("7. Terminar el programa")

    opciones = input("Escriba el NÚMERO de su opción. ")
    print("")
    opciones = quitar_espacios_costados(opciones)
    
    if opciones == "1":
        estudiante = input("¡Perfecto! ¿Cuál es el nombre del estudiante al que desea agregar? ")
        estudiante = quitar_espacios_costados(estudiante)
        try:
            agregar_estudiante(estudiante, base_de_datos)
            print(f"El estudiante de nombre {estudiante} fue agregado con éxito a la base de datos.")
            print("")
            print("-------------------------------------------------------------------------")
            
        except:
            print(TypeError)
            print("Ha ocurrido un error, notifique al desarrollador.")
            print("")
            print("-------------------------------------------------------------------------")
            quit()
           
    elif opciones == "2":
        print("¡Perfecto! Acá están los estudiantes y sus correspondientes promedios.")
        print("")
        todos_estudiantes(base_de_datos)
        print("")
        print("-------------------------------------------------------------------------")

    elif opciones == "3":
        estudiante = input("¡Perfecto! Ingrese el nombre del estudiante cuyos datos desea actualizar. ")
        categoria = input("¿Cuál es la categoría o materia que desea actualizar? ")
        nuevo_dato = input("¿Cuál es el nuevo dato que ingresará a la categoría mencionada? ")
        print("")

        estudiante = quitar_espacios_costados(estudiante)
        categoria = quitar_espacios_costados(categoria)
        nuevo_dato = quitar_espacios_costados(nuevo_dato)

        agregar_datos_stu(estudiante, categoria, nuevo_dato, base_de_datos)
        print("")
        print("-------------------------------------------------------------------------")
        
    elif opciones == "4":
        estudiante = input("¡Perfecto! Ingrese el nombre del estudiante cuyos promedio desea calcular. ")
        categoria = input("¿Cuál es la categoría o materia de la que desea el promedio? ")

        estudiante = quitar_espacios_costados(estudiante)
        categoria = quitar_espacios_costados(categoria)

        if categoria == "carnet":
            print("No puede obtenerse el promedio de una identificación. Inténtelo de nuevo.")
            print("")
            print("-------------------------------------------------------------------------")
            continue

        if promedio_materia(estudiante, categoria, base_de_datos) != None:
            print(f"El promedio de {estudiante} en la materia {categoria} fue de {promedio_materia(estudiante, categoria, base_de_datos)} puntos.")
        print("")
        print("-------------------------------------------------------------------------")

    elif opciones == "5":
        categoria = input("¿De qué materia desea conocer el mejor promedio? ")
        print("")

        categoria = quitar_espacios_costados(categoria)

        mejor_en_clase(categoria, base_de_datos)
        print("")
        print("-------------------------------------------------------------------------")

    elif opciones == "6":
        print("¡Muy bien!")
        (goat(base_de_datos))
        print("")
        print("-------------------------------------------------------------------------")

    elif opciones == "7":
        print("Fue un gusto poder ayudarle. Hasta la próxima.")
        print("")
        print("-------------------------------------------------------------------------")
        continuar = False

    else:
        print("Ha ingresado un número de opción inválido. Por favor ingrese un ingrese un número de la lista.")
        print("-------------------------------------------------------------------------")
    
                  