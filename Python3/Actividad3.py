import math

n = int(input("Introduce un número: "))  # Preguntar por un número
es_primo = True 

# Si el número es menor o igual a 1, no puede ser primo
if n <= 1:
    es_primo = False
else:
    # Comprobamos si el número es divisible por algún número hasta su raíz cuadrada
    for i in range(2, int(math.sqrt(n)) + 1):
        # Si el número es divisible por i, entonces no es primo
        if n % i == 0:
            es_primo = False
            break  # Salimos del bucle ya que hemos encontrado un divisor

# Imprimimos si el número es primo o no
if es_primo:
    print("El número", n, "es primo.")
else:
    print("El número", n, "no es primo.")
