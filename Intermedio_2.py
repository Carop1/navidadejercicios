import os
import registrar_dependencia as dp
menu = "1. Registrar Dependencia\n2. Registrar consumo por dependencia\n3. Ver CO2 producido\n4. Dependecia que produce mayor CO2\n5. Salir\n:)"
isActive = True
opMenu = 0
cont = 0
arreglo_global = []
arreglo_grande = []
valor_encontrado = False
cont_duplicado = 0
ya_ingresados = []
arreglo_global2 = []
ya_ingresados2 = []
arreglo_consumo = []
arreglo_consumo2 = []
arreglo_consumo = []
max_emision = 0

print("Bienvenidos a la calculadora de CO2")
print("A continuacion aparecera un menu de opciones con la puede hacer los calculos")

while (isActive) :
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            registro = dp.ingresoDependencia()
            print(registro)
            
        elif(opMenu==2):
            dependencia_enum = list(enumerate(registro))
            
            try:
                print("Elija el numero de la dependencia a la que va a agregar los dispositivos y el transporte:  ")
                for i in range(len(registro)):
                    print(dependencia_enum[i])
                num_depen = int(input(""))

            except ValueError:
                print("Lo escrito no es valido, digite de nuevo por favor")       
            
            if(num_depen in ya_ingresados):
                print("Ya registró los consumos de esa dependencia")
            else:
                numero_electro = int(input("Escriba el numero de dispositivos que tiene la dependencia: "))
                arreglo_grande = dp.ingresoElectro(numero_electro)
                union_arreglos = [registro[num_depen], arreglo_grande]
                arreglo_global.append(union_arreglos)
                ya_ingresados.append(num_depen) 
                print(f"Dependecias con su respectivos consumos de dispositivos:  {arreglo_global}")
            
                num_personas = int(input("Ingrese el numero de personas de la depencia: "))
                arreglo_grande2 = dp.ingresoKm(num_personas)
                union_arreglos2 = [registro[num_depen], arreglo_grande2]
                arreglo_global2.append(union_arreglos2)
                ya_ingresados2.append(num_depen) 
                print(f"Dependecias con su respectivos kilometros:  {arreglo_global2}")
        elif(opMenu==3):
            
                   
            for subarreglo, subarreglo2 in zip(arreglo_global, arreglo_global2):
                sumatoria = sum(subarreglo[1])
                consumo = sumatoria * 8 * 24
                emision_co2_dispo = round(consumo * 0.112378, 2)
                print(f"Emision de CO2 debido al consumo eléctrico de dependencia {subarreglo[0]} = {emision_co2_dispo} gramos/mensual")

                sumatoria2 = sum(subarreglo2[1])
                emision_co2_trans = round(sumatoria2 * 571.4, 2)
                print(f"Emisión de CO2 debido al transporte de las personas de la dependencia {subarreglo2[0]} = {emision_co2_trans} gramos/mensual")

                total_emision = emision_co2_dispo + emision_co2_trans
                arreglo_consumo.append(total_emision)
                print(f"Total emision dependencia {subarreglo[0]}: ", total_emision)
                if total_emision > max_emision:
                    max_emision = total_emision
                    max_dependencia = (f"{subarreglo[0]}")
                                            
        elif(opMenu==4):
             
            print(f"La dependencia con mayor produccion de CO2 es: {max_dependencia} con valor de {max_emision}")
           
        
        elif (opMenu==5):
            isActive = False