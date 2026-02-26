class Producto:
  def __init__(self, nombre:str, precio:float, stock:int):
    self.nombre = nombre
    if precio < 0:
      raise ValueError("El precio no puede ser negativo")
    self.precio = precio
    if stock < 0:
      raise ValueError("El stock no puede ser negativo")
    self.stock = stock

  def reducir_stock(self, cantidad:int) -> None:
    if cantidad > self.stock:
      raise ValueError("No hay suficiente stock para reducir esta cantidad.")
    self.stock -= cantidad
  
  def __str__(self) -> str:
    return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"