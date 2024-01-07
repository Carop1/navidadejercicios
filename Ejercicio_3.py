#Calculadora de IMC
normal = 0
sobrepeso = 0
obesidadI = 0
obesidadII = 0
obesidadIII = 0

print("Bienvenido a la calculadora de IMC")
print("Por favor digite los datos de estatura y peso de los 20 estudiantes")
for i in range(20):
  #nombre = input("ingrese su nombre: ")
  #edad = input("ingrese su edad:  ")
  estatura = float(input("ingrese estatura (m):  "))
  peso = float(input("ingrese peso (kg): "))
  imc = peso/(estatura)**2

  if imc > 18.5 and imc < 24.9:
    categoria = "normal"
    normal = normal + 1
  elif imc > 25 and imc < 29.9:
    categoria = "sobrepeso"
    sobrepeso = sobrepeso + 1
  elif imc > 30 and imc < 34.9:
    categoria = "obesidad I"
    obesidadI = obesidadI + 1
  elif imc > 35 and imc < 39.9:
    categoria = "obesidad II"
    obesidadII = obesidadII + 1
  elif imc > 40:
    categoria = "obesidad III"
    obesidadIII = obesidadIII +1 

print("La comunidad estudiantil tiene el siguiente estado de salud: ")
print(f"Normal: {normal}")
print(f"Sobrepeso: {sobrepeso}")
print(f"Obesidad I: {obesidadI}")
print(f"Obesidad II: {obesidadII}")
print(f"Obesidad III: {obesidadIII}")
