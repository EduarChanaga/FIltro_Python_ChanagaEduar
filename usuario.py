import json
with open("usuarios.json","r") as i:
    usuarios=json.load(i)
def usuario():
    print("-------")
    print("Usuario")
    print("-------")
    print("")
    print("1. Registrar usuario")
    print("2. Asignar categorias")
    decision=str(input("-->"))
    
    if decision == "1":
        nuevo_usuario={
            "N° identidad" :str(input("documento: ")),
            "nombres":str(input("Nombres: ")),
            "apellidos":str(input("Apellidos: ")),
            "email":str(input("Email: ")),
            "Dirre":str(input("Dirre: ")),
        }
        