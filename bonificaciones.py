import json
with open("usuarios.json","r") as i:
    usuarios=json.load(i)
def bonificacion():
    
    print(" Bonificacines ")
    print("")
    print("1. Comprobar clientes fieles")
    
    decision=str(input("--> "))
    users=usuarios["movistar"]["usuarios"]
    if decision=="1":
        año_actual=int(input("Ingrese año actual: "))
        print()
        for i in users:
            if i["Año"]<=año_actual:
                i["Categoria"]="Cliente fiel"
    with open("usuarios.json","w") as i:
            json.dump(usuarios,i,indent=4)