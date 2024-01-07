arreglo = ["","",""]
i = 0
nuevo_arreglo = []

print("Bienvenido, por favor escriba 3 numeros enteros positivos")

for i in range(len(arreglo)):
  arreglo[i] = input("Ingrese un numero entero positivo:  ")
  while not arreglo[i].isdigit():
    arreglo[i] = input("Ingrese un numero entero positivo:  ")
  auxiliar = int(arreglo[i])
  if (arreglo[i].isdigit()) and (auxiliar>0):
    print("El numero es correcto")

  else:
    print("El caracter digitado es incorrecto, por favor digite un numero entero positivo")
  nuevo_arreglo.append(auxiliar)
print(nuevo_arreglo)
suma_arreglo = sum(nuevo_arreglo)
print("La suma de los numeros es: ", suma_arreglo)