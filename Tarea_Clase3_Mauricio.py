class Libro:
    def __init__(self, titulo, autor, anio_publicacion, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.cantidad_paginas = cantidad_paginas
        
class Biblioteca:
    def __init__(self, libros=None):
        self.libros = libros if libros is not None else []
    def ordenar_libros_por_autor(self):
        obras_autores = {}
        for libro in self.libros:
            if libro.autor not in obras_autores:
                obras_autores[libro.autor] = [libro.titulo]
            elif libro.autor in obras_autores:
                obras_autores[libro.autor].append(libro.titulo)
            else:
                print('es posible que veas esto?')
        for autor in obras_autores.keys():
            print(f'{autor} publico las siguientes obras:')
            for obras in obras_autores[autor]:
                print(f'- {obras}')
                            
    def libros_masde_400pags(self):
        libros_grandes = []
        for libro in self.libros:
            if libro.cantidad_paginas >= 400:
                libros_grandes.append([libro.titulo, libro.cantidad_paginas])
        
        print('Los libros mas grandes son:')
        for titulo, pags in libros_grandes:
            print(f"- {titulo} con {pags} paginas")
            
aventuras_sherlock = Libro('Las Aventuras de Sherlock Holmes', 'Arthur Conan Doyle', 1892, 300)
estudio_escarlata = Libro('El Estudio de la Escarlata', 'Arthur Conan Doyle', 1891, 250)
sabueso_baskerville = Libro('El sabueso de los Baskerville', 'Arthur Conan Doyle', 1902, 320)
harry_filosofal = Libro('Harry Potter y la piedra filosofal', 'J.K. Rowling', 1997, 500)
harry_camara = Libro('Harry Potter y la camara secreta', 'J.K. Rowling', 1998, 350)
harry_prisionero = Libro('Harry Potter y el prisionero de Azkaban', 'J.K. Rowling', 1999, 400)
biblia = Libro('La Biblia', 'Dios', 4000, 1000)
abundance = Libro('Abundance', 'Peter Diamandis', 2012, 480)
biblioteca = Biblioteca([aventuras_sherlock, estudio_escarlata, sabueso_baskerville, harry_filosofal, harry_camara, harry_prisionero, biblia, abundance])
biblioteca.ordenar_libros_por_autor()
biblioteca.libros_masde_400pags()

