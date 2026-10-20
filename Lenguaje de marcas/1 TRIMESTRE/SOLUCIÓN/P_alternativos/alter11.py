# Crea un programa-calculadora con un menú de opciones que dé a 
#elegir entre suma, resta, multiplicación, división o resto entre dos 
#números enteros.

print("Calculadora")
print("Elige una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Resto")
opcion = int(input("Introduce el número de la operación: "))
n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
if opcion == 1:
    resultado = n1 + n2
    print(f"El resultado de la suma es: {resultado}")
elif opcion == 2:
    resultado = n1 - n2
    print(f"El resultado de la resta es: {resultado}")
elif opcion == 3:
    resultado = n1 * n2
    print(f"El resultado de la multiplicación es: {resultado}")
elif opcion == 4:
    if n2 == 0:
        print("No se puede dividir por cero")
    else:
        resultado = n1 / n2
        print(f"El resultado de la división es: {resultado}")
else:
    if n2 == 0:
        print("No se puede dividir por cero")
    else:
        resultado = n1 % n2
        print(f"El resultado del resto es: {resultado}")