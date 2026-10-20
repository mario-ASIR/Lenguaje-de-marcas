#Introducir la medida en números enteros de un triángulo y visualizar si es  equilátero o no. 
lado1 = int(input("Introduce la medida del primer lado: "))
lado2 = int(input("Introduce la medida del segundo lado: "))
lado3 = int(input("Introduce la medida del tercer lado: "))
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
else:
    print("El triángulo no es equilátero")