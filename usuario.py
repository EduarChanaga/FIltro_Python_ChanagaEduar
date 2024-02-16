import json 
with open("usuarios.json","r") as i:
    usuarios=json.load(i)
with open("servicios.json","r") as i:
    servicios=json.load(i)
with open("consultas.json","r") as i:
    consultas=json.load(i)
def usuario():
    print("-------")
    print("Usuario")
    print("-------")
    print("")
    print("1. Registrar usuario")
    print("2. Registro de servicios")
    print("3. consultas de servicios")
    decision=str(input("-->"))
    
    if decision == "1":
        nuevo_usuario={
            "N_identidad" :str(input("documento: ")),
            "nombre":str(input("Nombre completo: ")),
            "email":str(input("Email: ")),
            "Dirrecion":str(input("Dirrecion: ")),
            "Categoria":"Nuevo cliente",
            "servicios":""
        }
        usuarios["movistar"]["usuarios"].append(nuevo_usuario)
        with open("usuarios.json","w") as i:
            json.dump(usuarios,i,indent=4)
    if decision=="2":
        datos=usuarios["movistar"]["usuarios"]
        servicioss=servicios["movistar"]["servicios"]
        
        print("----> Registrar un servicio <---")
        for i in datos:
            print(i["nombre"], " iD: ", i["N_identidad"]) 
        print("")  
        id_usuario=str(input("Ingrese el id del usuario a agregar un servicio: "))
        for i in datos:
            if id_usuario==i["N_identidad"]:
                for j in servicioss:
                    print("")
                    print("------------------------------")
                    print("Nombre: ", j["Nombre_servicio"]) 
                    print("Precio: ", j["Precio"])
                    print("Caracteristicas: ", j["caracteristicas"])
                    print("")
                    print("")
                name_servicio=str(input("Ingrese el nombre del servicio:"))
                for j in servicioss:
                    print("hola")
                    for p in servicioss:
                        if name_servicio==p["Nombre_servicio"]:
                            for x in datos:
                                if id_usuario==x["N_identidad"]:
                                    print("perro")
                                    x["servicios"]= name_servicio
                                    print("¡Ingreso de servicio exitoso!")
                                    
        with open("usuarios.json","w") as i:
            json.dump(usuarios,i,indent=4)
        input("enter para continuar")
        print("")
    if decision=="3":
        print("")
        print("")
        print("Que desea realizar?")
        print("1. consultas")
        print("2. reclamaciones")
        print("3. sugerencias")
        decision2=str(input("--> "))
        if decision2=="1":
            nueva_consulta={
                "Nombre_cliente":str(input("ingrese su nombre: ")),
                "Numero_contacto":str(input("Ingrese un numero de contacto: " )),
                "consulta":str(input("Ingrese su consulta: "))
            }
            consultas["movistar"]["consultas"].append(nueva_consulta)
            with open("consultas.json","w") as i:
                json.dump(consultas,i,indent=4)