import os
import registro_ciudad as rc
menu = "1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar sismo por ciudad\n4. Informe de riesgo\n5. Salir\n:)"
isActive = True
opMenu = 0
cont = 0
arreglo_global = []
sumatoria = 0
numero_subarreglos = 1
ya_ingresados = []
subarreglos = [""]
bandera = False
cont_duplicado = 0
valor_encontrado = False
elemento = ""


print("Bienvenidos al sistema de monitoreo sismico")
print("A continuacion aparecera un menu para que haga el registro de la actividad sismica de algunas ciudades")
n = int(input("Ingrese el numero de sismos que va a agregar en las ciudades:  "))
#registro =[]*n

while (isActive) :
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            registro = rc.ingresoCiudad()
            
            print(registro)
        elif(opMenu==2):
            
            ciudades_enum = list(enumerate(registro))
            
            try:
                print("Elija el numero de la ciudad a la que va a agregar los sismos:  ")
                for i in range(len(registro)):
                    print(ciudades_enum[i])
                    
                num_ciudad = int(input(""))
                
        
            except ValueError:
                print("Lo escrito no es valido, digite de nuevo por favor")
            
            
            if(num_ciudad in ya_ingresados):
                print("Ya registro los simos de esa ciudad")
            else:
                           #_________________________________________________
                arreglo_grande = rc.ingresoSismo(n)
                union_arreglos = [registro[num_ciudad], arreglo_grande]
                arreglo_global.append(union_arreglos)
                #______________________________________________________
            ya_ingresados.append(num_ciudad) 
                
            #-------------------------------------------------------                
            print(f"Ciudades y sus respectivos sismos:  {arreglo_global}")
            
        elif(opMenu==3):
            
            ciudad_buscar = str(input("Ingrese la ciudad a la que va a buscarle los sismos: "))
            for subarreglo in arreglo_global:
                if ciudad_buscar in subarreglo[0]:
                    print(f"Los sismos de la ciudad {subarreglo[0]} son: {subarreglo[1]}")
                    
        elif(opMenu==4):
            print(f"INFORME DE RIESGO: la clasificacion por el promedio de sismos de cada ciudad: ")
            for subarreglo in arreglo_global:
                for elemento in subarreglo:
                    sumatoria = sum(subarreglo[1])
                    longitud = len(subarreglo[1])
                    
                    numero_subarreglos = numero_subarreglos + 1
                    promedio = sumatoria/n
                    if (promedio < 2.5):
                        print(f"{subarreglo[0]} --> {promedio}. Nivel de riesgo AMARILLO: sin riesgo.")
                    if (promedio >=2.6  and promedio < 4.5):
                        print(f"{subarreglo[0]} --> {promedio}. Nivel de riesgo NARANJA: riesgo medio.")
                    if (promedio >= 4.5):
                        print(f"{subarreglo[0]} --> {promedio}. Nivel de riesgo ROJO: riesgo alto.")
                    break

        elif(opMenu==5):
            isActive = False
