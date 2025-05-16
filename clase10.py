class Persona:
    def __init__(self, nombre, edad, altura): #cuando hay una funcion dentro de un objeto es un metodo, afuera solo una funcion.
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    
    def saludar(self):
        print("Hola soy " + self.nombre + " y tengo " + str(self.edad))
    
    def cumpleanos(self):
        self.edad = self.edad +1 
        

juan = Persona("juan", 10, 170)
rafa = Persona('Rafael', 18, 182)
oliver = Persona('Oliver',18,170)
mau = Persona('Mauricio',18,165)
personas = [juan, rafa, oliver, mau]


for pene in personas:
    print(pene.nombre)
    #fin de iteracion



class Auto:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def mostrar_detalle(self):
        print(f"El auto es un {self.marca} {self.modelo} del año {self.anio}")
carro1 = Auto('Chevrolet', 'Camaro', 2020)
# print(carro1.marca)


class CuentaBancaria:
    def __init__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance
        
    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Se ha depositado {cantidad} y el nuevo balance es {self.balance}")
        
    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
        else:
            print("No tienes suficiente dinero puto pobre")
    
    def mostrar_detalle(self):
        print(f"El propietario de la cuenta es {self.propietario}")
        print(f"El balance de la cuenta es {self.balance}")




# class Libro:
#     def __init__(self, titulo, autor, anio_publicacion, paginas):


#class Biblioteca:
#debe cumplir con devolver todos los libros d eun autor
#debe tener que devuelve el libro con mas paginas