import time
from bases import instrucciones, menuJuego, juego, mostrarIngredientes, receta, tienda

def tuNombre():
    nombre = input("\n¿Cuál es tu nombre? ")
    print(f"¡Hola, {nombre}! Bienvenido al juego de la pastelería.")
    return nombre

def bienvenida(nombre):
    print(f"\n{nombre}, estás a punto de iniciar una aventura como dueño de una pastelería.")
    time.sleep(2)
    print("Tu objetivo es satisfacer las órdenes de tus clientes mientras manejas tus ingredientes y finanzas.")
    time.sleep(2)
    instrucciones()
    time.sleep(2)
    print("\n¡Buena suerte en tu aventura pastelera!")
    

def iniciar_juego():
    nombre = tuNombre()
    bienvenida(nombre)
    while True:
        menuJuego()
        opcion = input("\nSelecciona una opción del menú: ")
        if opcion not in ["0", "1", "2", "3"]:
            continue
        
        if opcion == "1":
            receta()
        elif opcion == "2":
            juego()
        elif opcion == "3":
            tienda()
        elif opcion == "0":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    iniciar_juego()