"""
Sistema de inventario con POO
Autor: Tatiana Montalvo
Fecha: 18 de julio 2026
"""

class Producto:
    """
    Clase que contiene los atributos y metodos disponibles del producto
    """
    nombre =""
    precio = 0.0
    cantidad = 0

    def __init__(self, nombre,precio,cantidad):
        """
        Metodo constructor que inicializa los atributos
        """
        if precio < 0:
            raise ValueError("El precio debe ser mayor o igual que cero.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío ni contener solo espacios.")
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que cero.")
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio):
        """
        funcion que sirve para modificar el precio validando que sea mayor o igual que cero
        """
        if nuevo_precio >= 0:
            precio = nuevo_precio

    def actualizar_cantidad(self,nueva_cantidad): 
        """
        funcion que sirve para modificar la cantidad validando que sea mayor o igual a cero
        """
        if nueva_cantidad >= 0:
            cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """
        funcion que sirve para devolver el valor total (precio × cantidad)
        """
        valor_total = precio * cantidad
        
    def __str__(self):
        """
        funcion que sirve para mostrar la información del producto de forma legible
        """
        return ( f"📦 [{self.nombre.upper()}]\n"
            f" ├─ Precio: ${self.precio:,.2f}\n"
            f" └─ Cantidad:  {self.cantidad} unidades")

  class Inventario:
    """
     Clase que contiene los atributos y metodos disponibles del Inventario
    """
    def __init__(self):
        
        """
        Metodo constructor que inicializa una lista vacia
        """
        self.productos = []


    def agregar_producto(self,nuevo_producto):
        """
        funcion que sirve para añadir un objeto de tipo Producto a la lista
        """
        self.productos.append(nuevo_producto)

    def buscar_producto(self,nombre):
        """
        funcion que sirve para encontrar un producto por su nombre (búsqueda exacta, insensible a mayúsculas/minúsculas)
        """
        for prod in self.productos:
            if prod.nombre.casefold() == nombre.casefold():
                return prod  
        return None

    def calcular_valor_inventario(self):
        """
        funcion que sirve para sumar el valor total de todos los productos
        """
        total = 0.0
        for producto in self.productos:
            total += producto.precio  * producto.cantidad
        return total

    def listar_productos(self):
        """
        funcion que sirve para mostrar todos los productos del inventario
        """
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("***** Todos los productos del inventario:*****")
        for producto in self.productos:
            print(str(producto))


def menu_principal(inventario):
    """
    funcion que muestra opciones al usuario y procesa la entrada del usuario en un bucle hasta que elija salir
    """
    while True:
        opcion = input("Seleccione una opción : \n 1. Agregar producto \n 2. Buscar producto \n 3. Listar productos \n 4. Calcular valor total del inventario \n 5. Salir \n ").strip()
        if opcion == "5":
            break
        elif opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = input("Precio del producto: ")
            cantidad = input("Cantidad del producto: ")
            try:
                if not nombre or not nombre.strip():
                    raise ValueError("El nombre no puede estar vacío ni contener solo espacios.")
                if precio.strip() == "":
                    raise ValueError("El campo precio no puede estar vacío.")
                precio = float(precio) 
                if precio < 0:
                    raise ValueError("El precio no puede ser negativo.")
                if cantidad.strip() == "":
                    raise ValueError("El campo cantidad no puede estar vacío.")
                cantidad = int(cantidad) 
                if cantidad < 0:
                    raise ValueError("La cantidad debe ser mayor o igual que cero.") 
                nuevo = Producto(nombre, precio,cantidad)
                inventario.agregar_producto(nuevo)
            except ValueError as error:
                print(f"Error: {error}")
        elif opcion == "2":
            nombre = input("Nombre del producto a buscar: ")
            try:
                if not nombre or not nombre.strip():
                    raise ValueError("El nombre no puede estar vacío ni contener solo espacios.")
                resultado = inventario.buscar_producto(nombre)
                if resultado is not None:
                    print(str(resultado))
                else:
                    print(resultado)
            except ValueError as error:
                print(f"Error: {error}")    
            
        elif opcion == "3":
            inventario.listar_productos()
        
        elif opcion == "4":
            total = inventario.calcular_valor_inventario()
            print("Valor total del inventario:",total)
        else:
            print("Opción inválida. Por favor, intenta de nuevo.")
        
def main():
    mi_inventario = Inventario()
    menu_principal(mi_inventario)
    input("\nPresiona Enter para salir...")


if __name__ == '__main__':
    main() 
