def main():
  productos_disponibles = []

  print("--- Creación de Productos ---")
  while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
      break

    try:
      precio = float(input(f"Ingrese el precio de {nombre}: "))
      stock = int(input(f"Ingrese el stock inicial de {nombre}: "))
      nuevo_producto = Producto(nombre, precio, stock)
      productos_disponibles.append(nuevo_producto)
      print(f"Producto '{nombre}' creado con éxito.\n")
    except ValueError as e:
      print(f"Error al crear producto: {e}. Intente de nuevo.\n")
    except Exception as e:
      print(f"Ocurrió un error inesperado: {e}. Intente de nuevo.\n")
  
  if not productos_disponibles:
    print("No se crearon productos. Saliendo del programa.")
    return

  print("\n--- Productos Disponibles ---")
  for p in productos_disponibles:
    print(p)
  print("-----------------------------")

  mi_carrito = Carrito()
  print("\n--- Agregar productos al carrito ---")
  while True:
    if not productos_disponibles:
        print("No hay productos disponibles para añadir al carrito.")
        break
    
    print("Productos disponibles:")
    for i, p in enumerate(productos_disponibles):
        print(f"  {i+1}. {p.nombre} (Stock: {p.stock})")

    opcion = input("Seleccione el número del producto a agregar (o 'fin' para terminar): ")
    if opcion.lower() == 'fin':
      break
    
    try:
      idx = int(opcion) - 1
      if 0 <= idx < len(productos_disponibles):
        producto_seleccionado = productos_disponibles[idx]
        cantidad = int(input(f"¿Cuántas unidades de '{producto_seleccionado.nombre}' desea agregar?: "))
        if cantidad > producto_seleccionado.stock:
            print(f"Error: No hay suficiente stock de {producto_seleccionado.nombre}. Stock disponible: {producto_seleccionado.stock}")
        else:
            mi_carrito.agregar_producto(producto_seleccionado, cantidad)
            print(f"{cantidad} unidades de '{producto_seleccionado.nombre}' añadidas al carrito.\n")
            producto_seleccionado.reducir_stock(cantidad)
      else:
        print("Opción inválida. Intente de nuevo.\n")
    except ValueError:
      print("Entrada inválida. Por favor, ingrese un número o 'fin'.\n")
    except Exception as e:
      print(f"Ocurrió un error inesperado: {e}. Intente de nuevo.\n")
  
  mi_carrito.mostrar_resumen()

  print("\n--- Reducción de Stock y Pruebas de Errores ---")
  if productos_disponibles:
      if productos_disponibles[0].stock > 0:
          print(f"\nIntentando reducir más stock del disponible para {productos_disponibles[0].nombre}...")
          try:
              productos_disponibles[0].reducir_stock(productos_disponibles[0].stock + 1)
          except ValueError as e:
              print(f"Error al reducir stock: {e}")
          print(f"Stock actual de {productos_disponibles[0].nombre}: {productos_disponibles[0].stock}")

if __name__ == "__main__":
    main()
        