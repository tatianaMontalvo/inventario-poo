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
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def actualizar_precio(self, nuevo_precio):
        """
        funcion que sirve para modificar el precio validando que sea mayor o igual que cero
        """
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser mayor o igual que cero.")
        if nuevo_precio >= 0:
            self.precio = nuevo_precio

    def actualizar_cantidad(self,nueva_cantidad): 
        """
        funcion que sirve para modificar la cantidad validando que sea mayor o igual a cero
        """
        if nueva_cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que cero.")
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad

    def calcular_valor_total(self):
        """
        funcion que sirve para devolver el valor total (precio × cantidad)
        """
        return self.precio * self.cantidad
        
    def __str__(self):
        """
        funcion que sirve para mostrar la información del producto de forma legible
        """
        return ( f"📦 [{self.nombre.upper()}]\n"
            f" ├─ Precio: ${self.precio:,.2f}\n"
            f" └─ Cantidad:  {self.cantidad} unidades")
