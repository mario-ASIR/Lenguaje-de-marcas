#Introducir dos números enteros y visualizar primero el menor y después el  
#mayor
n1= int(input("Introduce un número: "))
n2= int(input("Introduce otro número: "))
if n1<n2:
    print(f"El menor es {n1} y el mayor es {n2}")
else:
    print(f"El menor es {n2} y el mayor es {n1}")