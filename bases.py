def instrucciones():
    print("Para este juego tenemos que seguir varias instrucciones: ")
    print("1. NO permitas que se te acaben los ingredientes.")
    print("2. Son 5 rondas, depende de ti si ganas o pierdes.")
    print("3. NO te endeudes más de lo que puedes pagar.")
    print("4. De ti depende el éxito de tu negocio.")
    print("¡Que inicie el juego!")

def ingredientes():
    global ingredientes
    ingredientes = {"harina": 5, "azúcar": 4, "huevos": 3, "leche": 2, "mantequilla": 6}
    return ingredientes

def mostrar_ingredientes():
    print("Ingredientes disponibles:")
    for ingrediente, cantidad in ingredientes.items():
        print(f"{ingrediente}: {cantidad} unidades")
    
def receta():
    print("\nReceta para hacer un pastel (un piso):")
    print("1. Mezcla 2 unidades de harina, 1 unidad de azúcar, 1 huevo, 1 unidad de leche y 1 unidad de mantequilla.")
    print("2. Hornea la mezcla a 180 grados Celsius durante 30 minutos.")
    print("3. Deja enfriar y decora al gusto.")
    
def ordenes():
    ordenes = {"Claudia": 1, "Luis": 2, "Ana": 4, "Pedro": 3, "Sofía": 2, "Marta": 1, "Jorge": 3, "Lucía": 1, "Carlos": 3, "Elena": 2, "Diego": 1, "Valeria": 2, "Andrés": 1, "Camila": 3, "Fernando": 2, "Isabela": 1, "Ricardo": 2, "Natalia": 1, "Santiago": 3, "Gabriela": 2, "Alejandro": 1, "Daniela": 2, "Sebastián": 5, "Mariana": 3, "Javier": 2, "Paula": 1, "Miguel": 3, "Laura": 1, "Antonio": 3, "Sara": 2, "Rafael": 1, "Andrea": 2, "Jorge": 1, "Carmen": 3, "Diego": 2, "Elena": 1, "Luis": 2, "Marta": 1, "Pedro": 3, "Sofía": 2, "Claudia": 1, "Ana": 2, "Carlos": 4, "Valeria": 3, "Andrés": 2, "Camila": 1, "Fernando": 2, "Isabela": 4, "Ricardo": 3, "Natalia": 2, "Santiago": 1, "Gabriela": 4, "Alejandro": 1, "Daniela": 3, "Sebastián": 2, "Mariana": 4, "Javier": 2, "Paula": 1, "Miguel": 3, "Laura": 2, "Antonio": 1, "Sara": 2, "Rafael": 5, "Andrea": 3}
    return ordenes

def diner():
    global dinero
    dinero = 20
    return dinero

def tienda():
    print("Bienvenido a la tienda de ingredientes.")
    print("\nPrecios por unidad:")
    print("Harina: $2")
    print("Azúcar: $1.5")
    print("Huevos: $0.5")
    print("Leche: $1")
    print("Mantequilla: $3")
    print("\nPuedes comprar ingredientes para reponer tu inventario.")

def menuJuego():
    print("\nMenú del Juego:")
    print("1. Ver instrucciones")
    print("2. Ver ingredientes disponibles")
    print("3. Ver receta del pastel")
    print("4. Ir a la tienda de ingredientes")
    print("0. Salir del juego")
