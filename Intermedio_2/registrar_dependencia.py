arreglo_dependencia = []
#arreglo_depen = []

def ingresoDependencia():
    rta = "S"
    
    while (rta in ["S","s"]):
        arreglo = input("Escriba el nombre de la dependencia:  ")
        if(arreglo in arreglo_dependencia):
            print("Ya habia ingresado esa dependencia antes: ")
        else:
            arreglo_dependencia.append(arreglo)
        rta = input("Desea registrar otra dependencia? S(si) o N(no u otra letra):  ").upper()
        if ((rta == "S")):
            rta = "S"        
        else:
            rta = "N"

    return arreglo_dependencia

def ingresoElectro(n):
    
    arreglo_gen_co2 = []
       
    for m in range(n):
        
        print(f"Ingrese el consumo del dispositivo {m+1} en Watts: ")
        consumo = int(input("Consumo: "))
        arreglo_gen_co2.append(consumo)
        
    return arreglo_gen_co2

def ingresoKm(h):
    arreglo_km_co2 = []
    for f in range(h):
        
        print(f"Ingrese los kilometros recorridos durante el mes por persona {f+1}: ")
        kilometros = int(input("km: "))
        arreglo_km_co2.append(kilometros)
        
    return arreglo_km_co2

    
    