arreglo_ciudades = []*5
rta = ""
ya_ingresados = []

def ingresoCiudad():
    rta = "S"
    i = 0
    while (rta in ["S","s"]):
        arreglo = input("Escriba el nombre de la ciudad:  ")
        if(arreglo in arreglo_ciudades):
            print("Ya habia ingresado esa ciudad antes: ")
        else:    
            arreglo_ciudades.append(arreglo)
        rta = input("Desea registrar otra ciudad? S(si) o N(no u otra letra):  ").upper()
        if ((rta == "S") and (i<4)):
            i = i+1            
        elif i>=4:
            print("Solo puede ingresar maximo 5 ciudades")
            rta = "N"

    return arreglo_ciudades  
    
def ingresoSismo(n):
    
    arreglo_gen_sismos = []
          
    for m in range(n):
        
        k = float(input("Ingrese la magnitud del sismo "))
        arreglo_gen_sismos.append(k)
        
    return arreglo_gen_sismos
         
            
        
    
    
    