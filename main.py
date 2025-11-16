import time
from bases import instrucciones, menuJuego, juego, mostrarIngredientes, receta, tienda

def tuNombre():
    nombre = input("¿Cuál es tu nombre? ")
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
        opcion = input("Selecciona una opción del menú: ")
        if opcion not in ["0", "1", "2", "3", "4", "5"]:
            continue
        
        if opcion == "1":
            juego()
        elif opcion == "2":
            instrucciones()
        elif opcion == "3":
            mostrarIngredientes()
        elif opcion == "4":
            receta()
        elif opcion == "5":
            tienda()
        elif opcion == "0":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    iniciar_juego()