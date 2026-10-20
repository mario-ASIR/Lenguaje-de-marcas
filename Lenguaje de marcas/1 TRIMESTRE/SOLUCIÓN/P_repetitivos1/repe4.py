# Introducir 5 edades y visualizar por pantalla cuántos son mayores de edad. 
veces=int(input("Introduce el número de veces que quieras repetir el proceso:"))
mayores_de_edad=0
menores_de_edad=0
for i in range(veces):
    num=int(input("Introducir un número entero:"))
    if num>=18:
       print("El número es mayor de edad")
       mayores_de_edad += 1
    else:
         print("El número es menor de edad")
         menores_de_edad += 1

print(f"Número de personas mayores de edad: {mayores_de_edad}")
print(f"Número de personas menores de edad: {menores_de_edad}")