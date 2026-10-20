# Introducir un número entero positivo (N) y realizar la SUMA N-ESIMA. 
# S = 1 + 2 + 3 + 4 +..........+ N    Visualizar por pantalla el resultado (S). 
num = int(input("Introduce un número entero positivo: "))
while num <= 0:
    print("El número introducido no es positivo. Por favor, introduce un número entero positivo.")
    num = int(input("Introduce un número entero positivo: "))
suma = sum(range(1, num + 1))
print(f"La suma de los números del 1 al {num} es: {suma}")
