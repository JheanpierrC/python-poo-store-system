class Carrito:
  def __init__(self):
    self.productos = [] 

  def agregar_producto(self, producto: Producto, cantidad: int) -> None:
    if not isinstance(producto, Producto):
      raise TypeError("El artículo debe ser un objeto de la clase Producto.")
    if cantidad <= 0:
      raise ValueError("La cantidad a agregar debe ser mayor que cero.")
    
    found = False
    for i, (prod_in_cart, qty_in_cart) in enumerate(self.productos):
        if prod_in_cart.nombre == producto.nombre:
            self.productos[i] = (prod_in_cart, qty_in_cart + cantidad)
            found = True
            break
    if not found:
        self.productos.append((producto, cantidad))

  def calcular_total(self) -> float:
    total = 0.0
    for producto, cantidad in self.productos:
      total += producto.precio * cantidad
    return total

  def mostrar_resumen(self) -> None:
    if not self.productos:
      print("El carrito está vacío.")
      return
    
    print("\n--- Resumen del Carrito ---")
    for producto, cantidad in self.productos:
      print(f"  - {producto.nombre}: {cantidad} unidades @ ${producto.precio:.2f} cada uno")
    print(f"---------------------------")
    print(f"Total: ${self.calcular_total():.2f}")
    print(f"---------------------------")
