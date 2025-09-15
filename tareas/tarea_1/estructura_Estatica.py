# Sistema de Gestión de Biblioteca
class SistemaBiblioteca:
    def __init__(self):
        self.inventario_libros = {
            'L001': {
                'autor': 'Mollo Alberto Mamani',
                'titulo': 'Programación Básica',
                'ejemplares': 4,
                'categoria': 'Informática'
            },
            'L002': {
                'autor': 'Juan Carlos Contreras',
                'titulo': 'Programación Avanzada',
                'ejemplares': 6,
                'categoria': 'Informática'
            },
            'L003': {
                'autor': 'Vallet Corrado',
                'titulo': 'Lenguaje Ensamblador',
                'ejemplares': 2,
                'categoria': 'Sistemas'
            }
        }
    
    def mostrar_catalogo(self):
        """Muestra el catálogo completo de libros disponibles"""
        print("\n📚 CATÁLOGO DE LIBROS DISPONIBLES")
        print("═" * 50)
        
        for codigo, datos in self.inventario_libros.items():
            print(f"🔖 Código: {codigo}")
            print(f"   📖 Título: {datos['titulo']}")
            print(f"   👤 Autor: {datos['autor']}")
            print(f"   📦 Ejemplares: {datos['ejemplares']}")
            print(f"   🏷️  Categoría: {datos['categoria']}")
            print("─" * 30)
    
    def prestar_ejemplar(self):
        """Realiza el préstamo de un ejemplar"""
        codigo = input("Ingrese el código del libro: ").strip().upper()
        
        if codigo in self.inventario_libros:
            libro = self.inventario_libros[codigo]
            
            if libro['ejemplares'] > 0:
                libro['ejemplares'] -= 1
                print(f"\n✅ Préstamo exitoso!")
                print(f"   Libro: {libro['titulo']}")
                print(f"   Ejemplares restantes: {libro['ejemplares']}")
            else:
                print(f"\n❌ No hay ejemplares disponibles de '{libro['titulo']}'")
        else:
            print("\n⚠️  Código de libro no encontrado")
    
    def menu_principal(self):
        """Interfaz principal del sistema"""
        while True:
            print("\n" + "✦" * 40)
            print("       SISTEMA DE GESTIÓN BIBLIOTECARIA")
            print("✦" * 40)
            print("1. Ver catálogo completo")
            print("2. Solicitar préstamo")
            print("3. Salir del sistema")
            print("─" * 40)
            
            opcion = input("Seleccione una opción (1-3): ")
            
            if opcion == "1":
                self.mostrar_catalogo()
            elif opcion == "2":
                self.prestar_ejemplar()
            elif opcion == "3":
                print("\n👋 ¡Gracias por usar el sistema!")
                break
            else:
                print("\n❌ Opción no válida. Intente nuevamente.")

# Ejecución del programa
if __name__ == "__main__":
    biblioteca = SistemaBiblioteca()
    biblioteca.menu_principal()