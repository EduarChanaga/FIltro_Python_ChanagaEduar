import json
with open("servicios.json","r") as i:
    servicioss=json.load(i)
def servicios():
    print("-------")
    print("Servicios")
    print("-------")
    print("")
    print("1. Crear nuevo servicio")
    print("2. Registro de servicios")
    decision=str(input("-->"))
    
    if decision == "1":
        nuevo_servicio={
            "Nombre_servicio" :str(input("Nombre servicio: ")),
            "Precio":str(input("Precio del servicio: ")),
            "caracteristicas":str(input("Caracteristicas: "))
        }
        servicioss["movistar"]["servicios"].append(nuevo_servicio)
        with open("servicios.json","w") as i:
            json.dump(servicioss,i,indent=4)
    if decision=="2":
        print("")