# Sistema de Gestión de Compras
class GestorCompras:
    def __init__(self):
        self.lista_compras = []
    
    def añadir_articulo(self):
        """Añade un nuevo artículo a la lista de compras"""
        articulo = input("Ingrese el nombre del artículo: ").strip()
        if articulo:
            self.lista_compras.append(articulo)
            print(f"✓ '{articulo}' se ha añadido correctamente")
        else:
            print("❌ El nombre del artículo no puede estar vacío")
    
    def mostrar_contenido(self):
        """Muestra todos los artículos en la lista"""
        if not self.lista_compras:
            print("\n📦 La lista de compras está vacía")
        else:
            print("\n📦 Contenido de tu lista:")
            for i, articulo in enumerate(self.lista_compras, 1):
                print(f"   {i}. {articulo}")
    
    def ejecutar(self):
        """Ejecuta el menú principal del sistema"""
        while True:
            print("\n" + "="*40)
            print("       SISTEMA DE GESTIÓN DE COMPRAS")
            print("="*40)
            print("1. Añadir artículo a la lista")
            print("2. Ver artículos en la lista")
            print("3. Finalizar programa")
            print("-"*40)
            
            seleccion = input("Seleccione una opción (1-3): ").strip()
            
            if seleccion == "1":
                self.añadir_articulo()
            elif seleccion == "2":
                self.mostrar_contenido()
            elif seleccion == "3":
                print("👋 ¡Hasta pronto!")
                break
            else:
                print("❌ Opción no válida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    sistema = GestorCompras()
    sistema.ejecutar()