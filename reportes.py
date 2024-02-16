import funciones
def reportes():
    print("-------")
    print("Reportes")
    print("-------")
    print("")
    print("1. Reporte de servicios")
    print("2. Ver cantidad de personas con servicios")
    decision=str(input("-->"))
    
    if decision == "1":
        print(funciones.reporte_servicios())
    elif decision=="2":
        print()
    elif decision=="3":
        print(funciones.personas_servicios())