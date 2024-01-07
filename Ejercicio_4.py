i = 0
nuevo_arreglo = []
total_numeros = 0
cont_pares = 0
arreglo_pares = []
cont_impares = 0
arreglo_impares = []
cont_e = 0
cont_f = 0
cont_g = 0

print("Bienvenido, por favor escriba numeros enteros positivos,")
print("para totalizar escriba un numero entero negativo")
n = int(input("Escriba la cantidad de numeros que desea ingresar:  "))
arreglo = [1]*n

for i in range(len(arreglo)):
  while True:
    try:
      arreglo[i] = int(input("Ingrese un numero entero positivo o negativo:  "))
      break
    except ValueError:
      print("No es un numero entero. Intente de nuevo.")
   
  auxiliar = int(arreglo[i])
  if (auxiliar>0):
    total_numeros = total_numeros + 1
    if auxiliar % 2 == 0: 
      cont_pares = cont_pares + 1
      arreglo_pares.append(auxiliar)
    else:
      cont_impares = cont_impares + 1
      arreglo_impares.append(auxiliar)
    if (auxiliar<20):
      cont_e = cont_e + 1
    elif (auxiliar>= 20 and auxiliar<=50):
      cont_f = cont_f + 1
    elif (auxiliar>100):
      cont_g = cont_g + 1
  elif (auxiliar < 0):
    break
    
  nuevo_arreglo.append(auxiliar)

suma_prom_pares = sum(arreglo_pares)
prom_pares = (suma_prom_pares/cont_pares)
suma_prom_impares = sum(arreglo_impares)
prom_impares = (suma_prom_impares/cont_impares)
print(f"Total numeros ingresados: {total_numeros}")
print(f"Total numeros pares ingresados: {cont_pares}")
print(f"Promedio numeros pares ingresados: {prom_pares}")
print(f"Promedio numeros impares ingresados: {prom_impares}")
print(f"Total numeros menores a 20: {cont_e}")
print(f"Total numeros en 20 y 50: {cont_f}")
print(f"Total numeros mayores a 100: {cont_g}")