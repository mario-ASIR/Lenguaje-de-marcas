#Introducir una letra, tal que si es A, realizaremos el área de una  circunferencia y si es L, realizaremos la longitud de la circunferencia. Sea  cualquiera de las opciones elegidas, visualizar el resultado indicando si  se trata del área o de la longitud. 
import math
letra= input("Introduce una letra: ")
if letra.lower() == 'a':
    radio = float(input("Introduce el radio de la circunferencia: "))
    area = math.pi * radio ** 2
    print(f"El área de la circunferencia es: {area:.2f}")
elif letra.lower() == 'l':
    radio = float(input("Introduce el radio de la circunferencia: "))
    longitud = 2 * math.pi * radio
    print(f"La longitud de la circunferencia es: {longitud:.2f}")
else:
    print("Opción incorrecta")