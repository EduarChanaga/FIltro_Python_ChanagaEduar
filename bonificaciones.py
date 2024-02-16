with open("usuarios.json","r") as i:
    usuarios=json.load(i)
def bonificacion():
    
    print(" Bonificacines ")
    print("")
    print("1. Comprobar clientes fieles")
    
    decision=str(input("--> "))
    if decision=="1":
        print()