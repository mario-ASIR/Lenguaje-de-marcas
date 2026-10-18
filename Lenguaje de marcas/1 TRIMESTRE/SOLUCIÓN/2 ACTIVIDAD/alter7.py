#Programa que a partir de la medida de los lados de un triángulo, es  capaz de decir si es equilátero, isósceles o escaleno. 
lado1 = int(input("Introduce la medida del primer lado: "))
lado2 = int(input("Introduce la medida del segundo lado: "))
lado3 = int(input("Introduce la medida del tercer lado: "))
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")