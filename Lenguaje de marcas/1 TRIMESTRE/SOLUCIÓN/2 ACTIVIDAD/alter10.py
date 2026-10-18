#  A partir de la nota numérica con decimales de un alumno, construye el 
#programa que indique su calificación en texto: Suspenso, Suficiente, 
#Bien, etc. 
nota = float(input("Introduce la nota numérica del alumno: "))
if nota < 5:
    print("Suspenso")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")