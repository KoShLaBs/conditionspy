#Llamar variables globales
from inventario import productos, carrito

def verProductos():
    print("\n___________________")
    for clave, valor in productos.items():
        print(f"|{clave} - ${valor}|")
    print("___________________")

def agregarCarrito():
    verProductos()
    while True:
        nombreProducto = input("\nIngrese el nombre del producto que desea agregar al carrito: ")

        try:
            precio = productos[nombreProducto]   # Si la clave no existe → KeyError
        except KeyError:
            print("Ese nombre no está en nuestros productos, intente de nuevo.\n")
            continue  # ← vuelve a pedir el producto

        # Si no hubo excepción, significa que el producto existe
        producto = {"nombre": nombreProducto, "precio": precio}
        carrito.append(producto)
        print(f"{nombreProducto} ha sido agregado al carrito.\n")
        break  # ← salimos del while porque ya fue válido
        
def verCarrito():
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
    else:
        print("\nProductos en el carrito:")
        print("___________________")
        for item in carrito:
            print(f"|{item['nombre']} - ${item['precio']}|")
        print("___________________")
        total = sum(item["precio"] for item in carrito)
        print(f"Total a pagar: ${total}")

def eliminarCarrito():
    if len(carrito) == 0:
        print("\nEl carrito está vacío. No hay productos para eliminar.")
        return
    else:
        print("\nProductos en el carrito:")
        for index, item in enumerate(carrito):
            print(f"{index + 1}. {item['nombre']} - ${item['precio']}")
    
    while True:
        try:
            opcion = int(input("\nSeleccione el número del producto que desea eliminar del carrito: ")) - 1
            if 0 <= opcion < len(carrito):
                eliminado = carrito.pop(opcion)
                print(f"Producto eliminado del carrito.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
    

def menuCliente():
    while True:
        print("\n--- Bienvenido to Katstore Tec Online ---")
        print("1. Ver productos")
        print("2. Agregar al carrito")
        print("3. Eliminar del carrito")
        print("4. Ver carrito")
        print("0. Salir")
        
        while True:
            opcion = input("Seleccione una opción: ")
            try:
                if opcion in ['0', '1', '2', '3', '4']:
                    break   
            except Exception as e:
                print("Opción no válida. Por favor, intente de nuevo.")
                raise e
        
        if opcion == '1':
            verProductos()
        elif opcion == '2':
            agregarCarrito()
        elif opcion == '3':
            eliminarCarrito()
        elif opcion == '4':
            verCarrito()
        elif opcion == '0':
            return
        
