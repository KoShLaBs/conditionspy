#File para correr el archivo
from inventario import menuInventario
from cliente import menuCliente

def main():
    while True:
        print("\n--- Bienvenido a Katstore Tec Online ---")
        print("1. Modo Inventario")
        print("2. Modo Cliente")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        try:
            if opcion in ['0', '1', '2']:   
                opcion = opcion
                pass
        except Exception as e:
            print("Opción no válida. Por favor, intente de nuevo.")
            raise e
        
        if opcion == '1':
            menuInventario()
        elif opcion == '2':
            menuCliente()
        elif opcion == '0':
            print("\nGracias por visitar Katstore Tec Online. ¡Hasta luego!")
            break
            

main()