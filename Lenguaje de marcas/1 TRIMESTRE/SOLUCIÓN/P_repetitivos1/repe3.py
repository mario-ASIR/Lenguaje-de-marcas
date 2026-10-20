#Introducir un número entero y visualizar por pantalla si es POSITIVO, 
#NEGATIVO o NULO. Este proceso se repetirá las veces que quiera el usuario
veces=int(input("Introduce el número de veces que quieras repetir el proceso:"))
for i in range(veces):
    num=int(input("Introducir un número entero:"))
    if num == 0:
       print("El número es nulo")
    elif num>0:
         print("El número es positivo")
    else:
        print("El número es negativo")