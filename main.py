import time
from bases import instrucciones, menuJuego, juego, mostrarIngredientes, receta, tienda, dinero

def tuNombre():
    nombre = input("\n¿Cuál es tu nombre? 🧑‍🍳 ")
    print(f"\n¡Hola, {nombre}! Bienvenido al juego de la pastelería. 🎂")
    return nombre

def bienvenida(nombre):
    print(f"\n🍰 {nombre}, estás a punto de iniciar una aventura como dueño de una pastelería.")
    time.sleep(2)
    print("📋 Tu objetivo es satisfacer las órdenes de tus clientes mientras manejas tus ingredientes y finanzas.")
    time.sleep(2)
    print("\n📜 Instrucciones:")
    instrucciones()
    time.sleep(2)
    print("\n🎉 ¡Buena suerte en tu aventura pastelera!")

def iniciar_juego():
    nombre = tuNombre()
    bienvenida(nombre)
    try:
        while True:
            menuJuego()
            opcion = input("\nSelecciona una opción del menú (0-3) ➤ ")
            if opcion not in ["0", "1", "2", "3"]:
                print("⚠️ Opción inválida. Intenta de nuevo.")
                continue
            if dinero() <= 0:
                print("\n⚠️ No tienes suficiente dinero para continuar. El juego ha terminado. ⚠️")
                break
            if opcion == "1":
                print("📝 Abriendo recetas...")
                receta()
            elif opcion == "2":
                print("🎯 Iniciando juego...")
                juego()
            elif opcion == "3":
                print("🏬 Abriendo tienda...")
                tienda()
            elif opcion == "0":
                print("👋 Gracias por jugar. ¡Hasta la próxima!")
                break
    except KeyboardInterrupt:
        print("\n🛑 Juego interrumpido. ¡Hasta luego!")

if __name__ == "__main__":
    iniciar_juego()