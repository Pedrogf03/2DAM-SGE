import math # Importa las librerias

n = int(input("Introduce un número: ")) # Se le pide al usuario un numero y se guarda en la variable n
es_primo = True # Se define la variable es_primo como verdadera

if n <= 1:
    es_primo = False # Si el numero es menor o igual a uno, es_primo es false
else:
    # Si no, se hace un bucle que va desde 2 hasta su raiz cuadrada +1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: # Si 
            es_primo = False
            break

if es_primo:
    print("El número", n, "es primo.")
else:
    print("El número", n, "no es primo.")
