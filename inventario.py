#Declarando variables globales
global productos
global carrito

productos = { 
            "laptop": 2500,
            "mouse": 50,
            "teclado": 120,
            "audifonos": 80,
            "monitor": 300}
carrito = []  

def verProductos():
    print("\n___________________")
    for clave, valor in productos.items():
        print(f"|{clave} - ${valor}|")
    print("___________________")

def agregarInventario():
    nombreProducto = input("\nIngrese el nombre del producto que desea agregar al inventario: ")
    while True:
        try:
            precioProducto = int(input("Ingrese el precio del producto: "))
            if precioProducto < 0:
                print("\nEl precio no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("\nEntrada no válida. Por favor, ingrese un número válido para el precio.")
    
    productos[nombreProducto] = precioProducto
    print(f"\n{nombreProducto} ha sido agregado al inventario con un precio de ${precioProducto}.\n")

def eliminarInventario():
    verProductos()
    while True:
        nombreProducto = input("\nIngrese el nombre del producto que desea eliminar del inventario: ")
        if nombreProducto in productos:
            del productos[nombreProducto]
            print(f"\n{nombreProducto} ha sido eliminado del inventario.\n")
            break
        else:
            print("Ese nombre no está en nuestros productos, intente de nuevo.\n")

def menuInventario():
    while True:
        print("\n--- Bienvenido to Katstore Tec Online ---")
        print("1. Ver productos")
        print("2. Agregar productos al inventario")
        print("3. Eliminar productos del inventario")
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
            agregarInventario()
        elif opcion == '3':
            eliminarInventario()
        elif opcion == '0':
            return
        
