#Introducir números enteros y calcular el mínimo. Este proceso se repetirá las 
#veces que quiera el usuario.
veces = int(input("Introduce el número de veces que quieras repetir el proceso: "))

for i in range(veces):
    n1 = int(input("Introduce el primer número entero: "))
    n2 = int(input("Introduce el segundo número entero: "))
    
    if n1 < n2:
        minimo = n1
    else:
        minimo = n2
        
    print("El número mínimo es:", minimo)