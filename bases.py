from random import choice
import random
import time

def instrucciones():
    print("\nPara este juego tenemos que seguir varias instrucciones: ⚠️")
    print("1. NO permitas que se te acaben los ingredientes. ❌")
    time.sleep(2)
    print("2. NO te endeudes más de lo que puedes pagar. ⚖️")
    time.sleep(2)
    print("3. De ti depende el éxito de tu negocio. 💼")
    time.sleep(2)
    print("¡Que inicie el juego!\n 🎮")


global ingredientes
ingredientes = {"harina": 5, "azucar": 4, "huevos": 3, "leche": 2, "mantequilla": 6}

def mostrarIngredientes():
    print("\nIngredientes disponibles: 🧾")
    for ingrediente, cantidad in ingredientes.items():
        print(f"{ingrediente}: {cantidad} unidades 📦")
    
def receta():
    print("\nReceta para hacer un pastel (un piso): 📜")
    print("1. Mezcla 2 unidades de harina, 1 unidad de azucar, 1 huevo, 1 unidad de leche y 1 unidad de mantequilla. 🥣")
    print("2. Hornea la mezcla a 180 grados Celsius durante 30 minutos. 🔥")
    print("3. Deja enfriar y decora al gusto. 🎨")
    

global ordenes
ordenes = {"Claudia": 1, "Luis": 2, "Ana": 4, "Pedro": 3, "Sofía": 2, "Marta": 1, "Jorge": 3, "Lucía": 1, "Carlos": 3, "Elena": 2, "Diego": 1, "Valeria": 2, "Andrés": 1, "Camila": 3, "Fernando": 2, "Isabela": 1, "Ricardo": 2, "Natalia": 1, "Santiago": 3, "Gabriela": 2, "Alejandro": 1, "Daniela": 2, "Sebastián": 5, "Mariana": 3, "Javier": 2, "Paula": 1, "Miguel": 3, "Laura": 1, "Antonio": 3, "Sara": 2, "Rafael": 1, "Andrea": 2, "Jorge": 1, "Carmen": 3, "Diego": 2, "Elena": 1, "Luis": 2, "Marta": 1, "Pedro": 3, "Sofía": 2, "Claudia": 1, "Ana": 2, "Carlos": 4, "Valeria": 3, "Andrés": 2, "Camila": 1, "Fernando": 2, "Isabela": 4, "Ricardo": 3, "Natalia": 2, "Santiago": 1, "Gabriela": 4, "Alejandro": 1, "Daniela": 3, "Sebastián": 2, "Mariana": 4, "Javier": 2, "Paula": 1, "Miguel": 3, "Laura": 2, "Antonio": 1, "Sara": 2, "Rafael": 5, "Andrea": 3}

global dineroA
dineroA = [20]
def dinero():
    return sum(dineroA)

def tienda():
    mostrarIngredientes()
    mone = str(dinero())
    print("\nTu dinero                          $"  +mone + " 💰")
    print("\nBienvenido a la tienda de ingredientes. 🏬")
    print("\nPrecios por unidad: 🧾")
    print("Harina: $2 🌾")
    print("Azucar: $1.5 🍚")
    print("Huevos: $0.5 🥚")
    print("Leche: $1 🥛")
    print("Mantequilla: $3 🧈")
    print("\nPuedes comprar ingredientes para reponer tu inventario. 🛒")
    
    while True:
        print("1. Comprar ingredientes 🛒")
        print("0. Salir de la tienda ⛔")
        opcion = input("\nSelecciona una opción: ")
        if opcion not in ["0", "1"]:
            continue
        if opcion == "1":
            comprar()
        elif opcion == "0":
            print("Saliendo de la tienda. 👋")
            return


def juego():
    aleatorio = choice(list(ordenes.keys()))
    print(f"\nNuestr@ cliente: {aleatorio}, necesita: {ordenes[aleatorio]} pisos en su pastel. 🎂")
    print("¡Manos a la obra!\n 🛠️")
    
    while True:
        print("1. Hacer pastel 🍰")
        print("0. Rendirse y salir del juego 🏳️")
        opcion = input("Selecciona una opción del menú: ")
        if opcion not in ["0", "1"]:
            continue
        if opcion == "1":
            hacerPastel(aleatorio)
            return
        elif opcion == "0":
            print("Gracias por jugar. ¡Hasta la próxima! 👋")
            break


def comprar():
    while True:
        ingrediente = input("\nDeme el ingrediente a comprar: ").strip().lower()
        if ingrediente in ingredientes:
            break
        else:
            print("Ingrediente no disponible. Por favor, elige otro. ❌")
    while True:
        cantidad = int(input("Deme la cantidad a adicionar: "))
        if cantidad > 0:
            break
        else:
            print("Cantidad inválida. Por favor, ingresa una cantidad positiva. ⚠️")
    cantidadNueva = ingredientes[ingrediente] + cantidad
    ingredienteNuevo = {ingrediente: cantidadNueva}
    ingredientes.update(ingredienteNuevo)
    if ingrediente == "harina":
        costo = 2 * cantidad
    elif ingrediente == "azucar":
        costo = 1.5 * cantidad  
    elif ingrediente == "huevos":
        costo = 0.5 * cantidad
    elif ingrediente == "leche":
        costo = 1 * cantidad
    elif ingrediente == "mantequilla":
        costo = 3 * cantidad
    dineroA.append(-costo)
    print(f"\nHas comprado {cantidad} unidades de {ingrediente} por ${costo}. 🧾")
    print(f"Dinero restante: ${dinero()} 💰\n")


def hacerPastel(aleatorio):
    if (ingredientes["harina"] >= 2 * ordenes[aleatorio] and
        ingredientes["azucar"] >= 1 * ordenes[aleatorio] and
        ingredientes["huevos"] >= 1 * ordenes[aleatorio] and
        ingredientes["leche"] >= 1 * ordenes[aleatorio] and
        ingredientes["mantequilla"] >= 1 * ordenes[aleatorio]):
        
        ingredientes["harina"] -= 2 * ordenes[aleatorio]
        ingredientes["azucar"] -= 1 * ordenes[aleatorio]
        ingredientes["huevos"] -= 1 * ordenes[aleatorio]
        ingredientes["leche"] -= 1 * ordenes[aleatorio]
        ingredientes["mantequilla"] -= 1 * ordenes[aleatorio]
        
        print()
        time.sleep(2)
        print("   i i i i i i 🍰")
        time.sleep(2)
        print("  |~~~~~~~~~~~| 🍰")
        time.sleep(2)
        print("__|___________|__ 🍰")
        time.sleep(2)
        print("|^^^^^^^^^^^^^^^^^| 🎉")
        print("|                 |")
        time.sleep(2)
        print("|     PASTEL      | 🎂")      
        time.sleep(2)   
        print("|_________________|")
        time.sleep(2)

        print("\n¡Pastel preparado con éxito! ✅")
        print(f"Has preparado un pastel de {ordenes[aleatorio]} pisos para {aleatorio}. 🎉")
        print("Has ganado dinero: +$20 💵")
        
        dineroC = 20
        dineroA.append(dineroC)
    else:
        print()
        time.sleep(2)
        print("   i i i i i i ❌")
        time.sleep(2)
        print("|^^^^^^^^^^^^^^^^^|")
        print("|                 |")
        time.sleep(2)
        print("|    NO PASTEL    | 😢")      
        time.sleep(2)   
        print("No hubo pastel :c")
        print("Perdiste dinero :c -$10 💸")
        dineroC = -10
        dineroA.append(dineroC)

def menuJuego():
    print("\nMenú del Juego: 📋")
    print("1. Ver receta 📖")
    print("2. Elegir una orden de pastel 🧾")
    print("3. Ir a la tienda de ingredientes 🏬")
    print("0. Rendirse y salir del juego 🏁")
