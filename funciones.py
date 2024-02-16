import json

def reporte_servicios():
    with open("servicios.json","r") as i:
        servicios=json.load(i)
        servicioss=servicios["movistar"]["servicios"]
    for i in servicioss:
        print("-----> ",i["Nombre_servicio"]  ," <-----")
        print("Precio: ",i["Precio"])
        print("Caracteristicas: ",i["caracteristicas"])
        print("")
        print("")
        
def personas_servicios():
    with open("usuarios.json","r") as i:
        usuarios=json.load(i)
    with open("servicios.json","r") as i:
        servicios=json.load(i)
    servicioss=servicios["movistar"]["servicios"]
    users=usuarios["movistar"]["usuarios"]
    for j in servicioss:
        print("")
        print("------------------------------")
        print("Nombre: ", j["Nombre_servicio"]) 
        print("")
    name_servicio=str(input("Ingrese el nombre del servicio:"))
    contador=0
    for i in users:
        if i["servicios"]=name_servicio:
            contar=contador+1
    print("la cantidad de usuarios que tienen ",name_servicio)
          
     