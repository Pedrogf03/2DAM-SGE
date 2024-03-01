# Asignaturas del alumno
asignaturas = ["Aplicaciones Ofimáticas", "Montaje y Mantenimiento", "Sistemas Operativos Monopuestos", "Formacion y Orientacion Laboral", "Redes Locales"]
# Lista de asignaturas a recuperar
recuperar = []

# Se recorren las asignaturas preguntando por la nota de cada una
for asignatura in asignaturas:
  nota = int(input("Nota de " + asignatura + ": "))
  # Si la nota es menor que 5, se guarda en la lista de recuperar
  if nota < 5:
    recuperar.append(asignatura)
    
print()
    
if len(recuperar) > 0:
  # Si hay algun valor en la lista de recuperar, se muestra
  print("Asignaturas que tienes que recuperar:")
  for asignatura in recuperar:
    print(asignatura)
else:
  # Si no se muestra un mensaje
  print("No tienes nada que recuperar")