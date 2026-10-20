# Introducir un número positivo (obligando a repetir la introducción del 
# número si fuese negativo) y realizar su Raíz Cuadrada. Realizarlo con while.
import math
num=int(input("Introduce un número positivo: "))
while num<0:
    print("El número introducido es negativo. Por favor, introduce un número positivo.")
    num=int(input("Introduce un número positivo: "))
raiz_cuadrada = math.sqrt(num)
print(f"La raíz cuadrada de {num} es: {raiz_cuadrada:.2f}")