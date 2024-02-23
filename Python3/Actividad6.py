entrada = input("Introduce un numero mayor que 0: ") # Pregunta por un numero

if not entrada.isdigit() or int(entrada) < 1:
  print("Error: El numero debe ser mayor que 0") # Si no es un número o es menor que 1 o es una cadena, imprime un error
else:
  n = int(entrada)
  for i in range(1, 11): # Si no, lo multiplica por todos los numeros de 1 a 10, mostrando el resultado
    print(str(n) + " x " + str(i) + " = " + str(n * i))
