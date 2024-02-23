while(True): # Bucle while para pedir al usuario numeros
  n = input("Introduce un numero: ")
  if n == " ": # Si es un espacio, sale del bucle
    break
  elif not n.isdigit(): # Si no es un numero, se le indica al usuario
    print("Eso no es un numero")
  else: # Si es un numero
    n = int(n)
    divisores = [] # Se crea la lista
    for i in range(1, n+1): # Se recorren sus divisores y se guarda en la lista
      if n % i == 0:
        divisores.append(i)
        
    print("Los divisores de", n, "son:", divisores) # Se muestra la lista
    print("La longitud de la lista es", len(divisores)) # Se muestra la longitud de la lista
    print("La lista en orden inverso es:", divisores[::-1]) # Se muestra la lista a la inversa