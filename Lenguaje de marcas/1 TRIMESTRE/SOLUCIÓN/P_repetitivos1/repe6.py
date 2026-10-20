# Introducir números enteros y calcular el máximo. Este proceso se repetirá las 
#veces que quiera el usuario
# Pedir los dos números enteros al usuario
veces = int(input("Introduce el número de veces que quieras repetir el proceso: "))

for i in range(veces):
    n1 = int(input("Introduce el primer número entero: "))
    n2 = int(input("Introduce el segundo número entero: "))
    
    if n1 > n2:
        maximo = n1
    else:
        maximo = n2
        
    print("El número máximo es:", maximo)

    
    
    