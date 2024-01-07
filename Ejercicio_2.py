#Calculadora de IMC
nombre = input("ingrese su nombre: ")
edad = input("ingrese su edad:  ")
estatura = float(input("ingrese su estatura (m):  "))
peso = float(input("ingrese su peso (kg): "))

imc = peso/(estatura)**2

if imc > 18.5 and imc < 24.9:
  categoria = "normal"
elif imc > 25 and imc < 29.9:
  categoria = "sobrepeso"
elif imc > 30 and imc < 34.9:
  categoria = "obesidad I"
elif imc > 35 and imc < 39.9:
  categoria = "obesidad II"
elif imc > 40:
  categoria = "obesidad III"
  
print(f"{nombre} tiene {edad} años, su indice de masa corporal es {imc} y pertenece a la categoria {categoria}")