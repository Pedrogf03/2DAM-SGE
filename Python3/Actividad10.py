N = 10 # Números que se le van a preguntar al usuario

positivos = [] # Lista de positivos
negativos = [] # Lista de negativos
nulos = [] # Lista de nulos

print("Introduce", N, "números")
for i in range(0, N):
  num = int(input())
  if num > 0: # Si el número es mayor que 0, es positivo
    positivos.append(num)
  elif num < 0: # Si el número es menor que 0, es negativo
    negativos.append(num)
  else: # Si no es mayor ni menor que 0, es nulo
    nulos.append(num)
    
# Se muestra cuntos números de cada tipo se han introducido
print("Has introducido", len(nulos), "valores nulos,", len(positivos), "números positivos y", len(negativos), "números negativos")