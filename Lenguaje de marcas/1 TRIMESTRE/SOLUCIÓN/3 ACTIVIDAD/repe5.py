# Introducir una nota y visualizar por pantalla cuántos aprobados y cuántos 
#suspensos hay. Este proceso se repetirá las veces que quiera el usuario.
veces=int(input("Introduce el número de veces que quieras repetir el proceso:")) 
aprobados=0
suspensos=0
for i in range(veces):
    nota=int(input("Introducir una nota:"))
    if nota < 5 :
        print ("suspenso")
        suspensos += 1
    else:
        print("aprobado")
        aprobados += 1

print(f"Número de estudiantes aprobados: {aprobados}")
print(f"Número de estudiantes suspensos: {suspensos}")
