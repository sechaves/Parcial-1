# Autor: Sergio Gabriel Chaves Mosquera
# Asignación: Parcial 1
# Objetivo del programa: simulador de operaciones básicas de una biblioteca universitaria.

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        #atributos principales para cada libro
        self.titulo = titulo
        self.autor = autor
        self._categoria = categoria #categoria se maneja como privada
        self._isbn = int(isbn) #ISBN se recibe en formato entero para evitar confusiones 
    #Metodo para devolver el ISBN
    def obtener_isbn(self):
        return self._isbn
    #Metodo para consultar info del libro en una sola linea
    def obtener_info_libro(self):
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Categoria: {self._categoria} | ISBN: {self._isbn}"

class Usuario:
    def __init__(self, nombre, documento, programa):
        self._nombre = nombre
        self._documento = int(documento) #Documento se guardda como entero para evitar confusiones
        self._programa = programa

    def obtener_documento(self):
        return self._documento
    #Metodo para consultar info del usuario en una sola linea
    def obtener_info(self):
        return f"Usuario: {self._nombre} | Documento: {self._documento} | Programa: {self._programa}"

class Biblioteca:
    #Clase principal del sistema "Fachada"
    def __init__(self, nombrebiblio):
        self.nombrebiblio = nombrebiblio
        self._catalogo = {}
        self._usuarios = {}
        # Categorías predefinidas, se elijen de manera numerica en consola
        self._categorias = ["Novela", "Ciencia", "Historia", "Desarrollo Personal", "Cuentos", "Guias", "Otro"]

    def registrar_libro(self, libronuevo):
        isbn = libronuevo.obtener_isbn()
        #Comprobar si el libro esta regsitrado
        if isbn in self._catalogo:
            return f"ERROR: El libro con ISBN {isbn} ya existe."
        self._catalogo[isbn] = libronuevo 
        return f"Libro registrado con exito: {libronuevo.obtener_info_libro()}"

    def registrar_usuario(self, usuarioNuevo):
        doc = usuarioNuevo.obtener_documento()
        #Comprobar si el usuario esta registrado
        if doc in self._usuarios:
            return f"ERROR: Usuario con documento {doc} ya existe."
        self._usuarios[doc] = usuarioNuevo
        return f"Usuario registrado con exito: {usuarioNuevo.obtener_info()}"

    def listar_libros(self):
        #Muestra todos los libros registrados o un aviso si no hay
        if not self._catalogo:
            return "No hay libros registrados."
        return "\n".join([libro.obtener_info_libro() for libro in self._catalogo.values()])

    def listar_usuarios(self):
        #Muestra todos los usuarios registrados o un aviso si no hay
        if not self._usuarios:
            return "No hay usuarios registrados."
        return "\n".join([usuario.obtener_info() for usuario in self._usuarios.values()])

def menu_principal():
    #Menu principal del programa (frontend)
    biblio = Biblioteca("Biblioteca UNAL")
    while True:
        print("\nSistema de Biblioteca Universitaria\n")
        print("1. Registrar nuevo libro")
        print("2. Registrar nuevo usuario")
        print("3. Salir del Programa")
        print("4. Listar libros")
        print("5. Listar usuarios")
        
        try:
            opcion_elegida = int(input("Por favor ingrese la opcion que desee: "))
        except ValueError:
            print("Entrada inválida, ingrese un número.")
            continue

        if opcion_elegida == 1:
            #Registro nuevo libro
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            print("\nCategorías disponibles:")
            for i, cat in enumerate(biblio._categorias, start=1):
                print(f"{i}. {cat}")
            op_cat = int(input("Seleccione la categoría (número): "))
            while op_cat < 1 or op_cat > len(biblio._categorias):
                op_cat = int(input("Opción inválida. Seleccione de nuevo: "))
            categoria = biblio._categorias[op_cat - 1]
            isbn = input("ISBN (solo números): ")
            libro = Libro(titulo, autor, categoria, isbn)
            print(biblio.registrar_libro(libro))

        elif opcion_elegida == 2:
            #Registro nuevo usuario
            nombre = input("Nombre completo: ")
            documento = input("Documento: ")
            programa = input("Programa: ")
            usuario = Usuario(nombre, documento, programa)
            print(biblio.registrar_usuario(usuario))

        elif opcion_elegida == 3:
            print("Saliendo del programa...")
            break

        elif opcion_elegida == 4:
            #Muestra los libros registrados
            print("\nLista de Libros Registrados:")
            print(biblio.listar_libros())

        elif opcion_elegida == 5:
            #Muestra los usuarios registrados
            print("\nLista de Usuarios Registrados:")
            print(biblio.listar_usuarios())

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()

