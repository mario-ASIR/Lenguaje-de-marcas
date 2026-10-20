#2. Introducir una edad (número entero) y visualizar por pantalla si es MAYOR ó 
#MENOR de edad. Este proceso se repetirá 5 veces. 
veces=int(input("Introduce el número de veces que quieres repetir el proceso: "))
for i in range(veces):
    edad=int(input("Introduce una edad: "))
    if edad>=18:
       print("Es mayor de edad")
    else:
       print("Es menor de edad")
