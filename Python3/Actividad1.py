import datetime # Importar las librerias de fechas

anyo = int(input("Introduzca su año de nacimiento: ")) # Pregunta al usuario por su año de nacimiento y en la variable anyo se guarda el valor que introduce el usuario, convirtiendolo en un número
edad = datetime.datetime.now().year - anyo # En la variable edad de guarda el resultado de restar el año actual - anyo
print("Tu edad es", edad) # Imprime por pantalla el contenido de la variable edad
