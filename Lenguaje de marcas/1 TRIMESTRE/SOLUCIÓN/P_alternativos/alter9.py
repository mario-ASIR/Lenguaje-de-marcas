#Introducir dos números enteros y visualizar si el primer número es divisible 
#o no por el segundo número.
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
if n2==0:
    print("No se puede dividir por cero")
elif n1 % n2 == 0:
    print(f"{n1} es divisible por {n2}")
else:
    print(f"{n1} no es divisible por {n2}")