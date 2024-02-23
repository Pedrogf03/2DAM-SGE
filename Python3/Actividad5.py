cadena = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"

print(len(cadena)) # Longitud de la cadena

print(cadena[:5]) # Primeros 5 caracteres

print(cadena[-10:]) # Ultimos 10 caracteres

print(cadena[1:10:2]) # De los primeros 10 caracteres, los que estan en posicion par

print(cadena[-13::3]) # De los primeros 15 caracteres, los que estan en posicion múltiplo de 3

ue_exists = "ue" in cadena # Comprobacion de que la cadena existe
if(ue_exists): # Si existe se imprime su posicion, si no se indica que no se encuentra
  print(cadena.find('ue'))
else:
  print("La subcadena 'ue' no se encuentra")
  
M_exists = "M" in cadena # Comprobacion de que la cadena existe
if(M_exists): # Si existe se indica, si no se indica que no se encuentra
  print("El caracter 'M' está en la cadena")
else:
  print("El caracter 'M' no se encuentra")
  
h_exists = "h" in cadena # Comprobacion de que la cadena existe
if(h_exists): # Si existe se indica, si no se indica que no se encuentra
  print("El caracter 'h' está en la cadena")
else:
  print("El caracter 'h' no se encuentra")

print(cadena[4:10].upper()) # Caracteres del 4 al 10, en mayuscula