# Se pide una palabra al usuario y se pasa a minúscula para evitar errores
palabra = input("Introduce una palabra: ")
palabra = palabra.lower()

# Si la palabra al revés es igual a la original, es un palíndromo
if palabra == palabra[::-1]:
  print(palabra, "es un palíndromo")
else:
  print(palabra, "no es un palíndromo")