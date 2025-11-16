calendario = {}

def menu():
    print("Calendario de Actividades")
    print("1. Agregar actividad")
    print("2. Ver actividades de una fecha")
    print("3. Ver todas las actividades")
    print("4. Eliminar una actividad")
    print("5. Salir")
    

def pedirFecha():
    fecha = input("Ingrese la fecha (DD/MM/AAAA): ").strip()
    
    if fecha == "":
        print("La fecha no puede estar vacía.")
        return None
    return fecha

def agregarActividad():
    fecha = pedirFecha()
    if fecha is None:
        return
    
    hora = input("Ingrese la hora (HH:MM): ").strip()
    if hora == "":
        print("La hora no puede estar vacía.")
        return
    
    titulo = input("Ingrese el título de la actividad: ").strip()
    if titulo == "":
        print("El título no puede estar vacío.")
        return
    
    if fecha not in calendario:
        calendario[fecha] = []
    
    actividad = {"hora": hora, "titulo": titulo}
    calendario[fecha].append(actividad)
    print("Actividad agregada exitosamente.")
    
def verActividadesFecha():
    fecha = pedirFecha()
    if fecha is None:
        return
    
    if fecha not in calendario or len(calendario[fecha]) == 0:
        print("No hay actividades para esta fecha.")
        return
    
    print(f"Actividades para {fecha}:") 
    for idx, actividad in enumerate(calendario[fecha], start=1):
        print(f"{idx}. {actividad['hora']} - {actividad['titulo']}")
        

def verTodasActividades():
    if not calendario:
        print("No hay actividades en el calendario.")
        return
    
    print("Todas las actividades en el calendario:")
    for fecha in sorted(calendario.keys()):
        print(f"\n{fecha}:")
        if len(calendario[fecha]) == 0:
            print("  No hay actividades.")
        else:
            for idx, actividad in enumerate(calendario[fecha], start=1):
                print(f"  {idx}. {actividad['hora']} - {actividad['titulo']}")

def eliminarActividad():
    fecha = pedirFecha()
    if fecha is None:
        return
    
    if fecha not in calendario or len(calendario[fecha]) == 0:
        print("No hay actividades para esta fecha.")
        return
    
    print(f"Actividades para {fecha}:")
    for idx, actividad in enumerate(calendario[fecha], start=1):
        print(f"{idx}. {actividad['hora']} - {actividad['titulo']}")
    try:
        numero = int(input("Ingrese el número de la actividad a eliminar: "))
    except ValueError:
        print("Digite un número válido.")
        return
    
    if numero >= 0 and numero <= len(calendario[fecha]):
        actividad_eliminada = calendario[fecha].pop(numero - 1)
        print(f"Actividad '{actividad_eliminada['titulo']}' eliminada exitosamente.")
        
    if len(calendario[fecha]) == 0:
        del calendario[fecha]
    else:
        print("Número inválido.")

def ejecutarCalendario():
    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            agregarActividad()
        elif opcion == "2":
            verActividadesFecha()
        elif opcion == "3":
            verTodasActividades()
        elif opcion == "4":
            eliminarActividad()
        elif opcion == "5":
            print("Saliendo del calendario. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            
if __name__ == "__main__":
    ejecutarCalendario()