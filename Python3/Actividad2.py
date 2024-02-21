import datetime

dia = int(input("Introduce tu dia de nacimiento: ")) # Pregunta por el dia de nacimiento, se convierte en numero y se guarda en la variable dia
mes = int(input("Introduce tu mes de nacimiento: "))  # Pregunta por el mes de nacimiento, se convierte en numero y se guarda en la variable mes
anyo = int(input("Introduce tu año de nacimiento: ")) # Pregunta por el año de nacimiento, se convierte en numero y se guarda en la variable anyo

fecha_nacimiento = datetime.date(anyo, mes, dia) # Se crea una fecha con los datos dados por el usuario
fecha_actual = datetime.date.today() # Se coge la fecha actual

edad = fecha_actual.year - fecha_nacimiento.year # Se restan los años
tiene_que_cumplir = (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day) # Devuelve true si el mes y dia actual son menores que el mes y dia de nacimiento, por lo que guardaria si el usuario tiene que cumplir años o no
edad = edad - tiene_que_cumplir # La variable booleana actua como 1 si es es true y como 0 si es false, por lo que si aún tiene que cumplir, se le resta 1 a la edad

print("Tu edad es", edad) # Se imprime por pantalla el resultado
