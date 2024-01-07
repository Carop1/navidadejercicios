def registroProd():
    
    cod_prod = int(input("Ingrese el código del producto: "))
    nom_prod = input("Ingrese el nombre del producto: ")
    valor_com_pro = float(input("Escriba el valor de compra del producto: "))
    valor_vent_pro = float(input("Escriba el valor de venta del producto: "))
    stock_min = int(input("Ingrese el stock minimo permitido: "))
    stock_max = int(input("Ingrese el stock maximo permitido: "))
    nom_prov_prod = input("Ingrese el nombre del proveedor del producto: ")
    stock_actual = int(input("Ingrese el stock actual del producto: "))
    
    producto = [cod_prod,nom_prod,valor_com_pro,valor_vent_pro,stock_min,stock_max,nom_prov_prod,stock_actual]
    
    return producto

def imprimir(visualizar,agregados):
    
    nuevo_arreglo = []
    visu = []
    subor = []
    agregado = [""]
    subarreglo = []
    for subarreglo in agregados:
        union_subarreglos = subarreglo + [""]
        nuevo_arreglo.extend(union_subarreglos)
    visual = visualizar*(len(agregados))
    for sub in visual:
        subor=(sub + agregado)
        visu.extend(subor)

    juntar = zip(visu,nuevo_arreglo)
    for key, value in juntar:
        print(f"{key}: {value}") 
        
    #return nuevo_arreglo
    
def actualizarStock(agregados):
   
    subarreglo = []
    arreglo_actu = []
    codigo_a_actualizar = int(input("Ingrese el código del producto a actualizar: "))
    cantidad_a_actualizar = int(input("Ingrese la cantidad a agregar(numero positivo) o restar(numero negativo) al stock : "))
    for subarreglo in agregados:
        if subarreglo[0] == codigo_a_actualizar:
            subarreglo[7] += cantidad_a_actualizar  # Actualizar el stock
        arreglo_actu.append(subarreglo)
            
        #else: 
             #arreglo_actu = agregados
                
    return arreglo_actu   

def productosCri(agregados):
    print("INFORME DE PRODUCTOS CRITICOS")
    for subarreglo in agregados:
        
        if subarreglo[7] <= subarreglo[4]:
            print(f"Producto: {subarreglo[1]}, Cantidad: {subarreglo[7]} unidades, Stock Mínimo: {subarreglo[4]}")
        else:
            print("")
        
                
    #print("INFORME DE PRODUCTOS CRITICOS")  
    #for i in range(len(productos)-1):
        
        
def gananciaPoten(agregados):
    arreglo_potencial = []
   
    for subarreglo in agregados:
        diferencia = subarreglo[3]-subarreglo[2]
        ganan_potencial = diferencia*subarreglo[7]
        arreglo_potencial.append(ganan_potencial)
        print(f"El producto {subarreglo[1]} tiene una ganancia potencial de {ganan_potencial} ")
       
          
    #return arreglo_potencial