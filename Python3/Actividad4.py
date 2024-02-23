n = int(input("Introduce un número: "))  # Preguntar por un número
factorial = 1

# Bucle que va desde 1 hasta el numero introducido
for i in range(n, 0, -1):
  factorial = factorial * i # Se multiplica regresivamente desde el numero introducido hasta 1
  
print(factorial) # Se imprime el factorial
