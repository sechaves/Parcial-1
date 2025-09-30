#Autor: Sergio Gabriel Chaves Mosquera
#Asignación: Parcial 1
#Objetivo del programa: simulador de operaciones básicas de una biblioteca universitaria.

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self._categoria = categoria
        self._isbn = int(isbn)

    def obtener_isbn(self):
        return self._isbn
    
    def obtener_info_libro(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Categoria: {self._categoria} | ISBN: {self._isbn}"

class Usuario:
    def __init__(self, nombre, documento, programa):
        self._nombre = nombre
        self._numerodocumento = int(documento)
        self._programa = programa

    def obtener_documento(self):
        return self._numerodocumento

    def obtener_info(self):
        return f"Usuario: {self._nombre} | Numero Documento: {self._numerodocumento} | Programa: {self._programa}"

class Biblioteca:
    def __init__(self, nombrebiblio):
        self.nombrebiblio = nombrebiblio
        self._catalogo = {}
        self._usuarios = {}

    def registrar_libro(self, libronuevo):
        isbn = libronuevo.obtener_isbn()
        if isbn in self._catalogo:
            return False, f"ERROR: El libro con ISBN {isbn} ya existe."
        self._catalogo[isbn] = libronuevo 
        return True, f"Libro registrado con exito: {libronuevo.obtener_info_libro()}"

    def registrar_usuario(self, usuarioNuevo):
        doc = usuarioNuevo.obtener_documento()
        if doc in self._usuarios:
            return False, f"ERROR: Usuario con documento {doc} ya existe."
        self._usuarios[doc] = usuarioNuevo
        return True, f"Usuario registrado con exito: {usuarioNuevo.obtener_info()}"

def menu_principal():
    biblio = Biblioteca("Biblioteca UNAL")
    while True:
        print("\nSistema de Biblioteca Universitaria\n")
        print("1. Registrar nuevo libro")
        print("2. Registrar nuevo usuario")
        print("3. Salir del Programa")
        opcion_elegida = int(input("Por favor ingrese la opcion que desee: "))
        
        if opcion_elegida == 1:
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            print(biblio.registrar_libro(libro))

        elif opcion_elegida == 2:
            nombre = input("Nombre completo: ")
            numerodocumento = input("Numero Documento: ")
            programa = input("Programa: ")
            usuario = Usuario(nombre, numerodocumento, programa)
            print(biblio.registrar_usuario(usuario))

        elif opcion_elegida == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
