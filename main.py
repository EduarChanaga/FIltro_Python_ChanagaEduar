import usuario
import servicios
import reportes
import bonificaciones
while True:
    print("Bienvenido")
    print("1. Usuario")
    print("2. Gestion de servicios")
    print("3. Reportes")
    print("4. Bonificacion clientes leales")
    decision=str(input("--> "))

    if decision=="1":
        print(usuario.usuario())
    elif decision=="2":
        print(servicios.servicios())
    elif decision=="3":
        print(reportes.reportes()) 
    elif decision=="4":
        print(bonificaciones.bonificacion())