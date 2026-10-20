#Introducir los tres valores para una ecuación de segundo grado (a, b, c). Visualizar el resultado solo si sus raíces son reales (cuando al realizar el cálculo de dentro de la raíz nos da ≥ 0).
import math
a = float(input("Introduce a: "))
b = float(input("Introduce b: "))
c = float(input("Introduce c: "))

d = b**2 - 4*a*c

if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(x1, x2)
else:
    print("No tiene raices reales")


