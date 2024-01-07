import os
import modulo as ml
menu = "1. Registro de productos\n2. Visualizacion de productos\n3. Actualizacion de Stock\n4. Informe de productos críticos\n5. Calculo de ganancia potencial\n:)"
isActive = True
opMenu = 0
agregados = []
combinacion = []

print("Bienvenido al sistema de gestion de inventarios")
print("A continuacion aparecera un menu de opciones con la puede realizar las operaciones que necesite")

while (isActive) :
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            registro = ml.registroProd()
            print(type(registro))
            agregados.append(registro)
            print(agregados)
            print("")
        elif(opMenu==2):
            visualizar = [["código", "nombre", "valor de compra", "valor de venta", "stock mínimo", "stock máximo", "nombre del proveedor","Stock actual"]]
            
            ml.imprimir(visualizar,agregados)
                        
            print("")
        elif(opMenu==3):
            agregados = ml.actualizarStock(agregados)
            print(agregados)
                    
        elif(opMenu==4):
            ml.productosCri(agregados)
            print("")
        elif(opMenu==5):
            arreglo_poten = ml.gananciaPoten(agregados)
            print("")
        