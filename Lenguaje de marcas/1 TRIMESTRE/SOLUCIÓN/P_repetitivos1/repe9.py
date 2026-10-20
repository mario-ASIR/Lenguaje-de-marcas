#Introducir todas las notas de tu primera evaluación y realizar la MEDIA.
total_notas = int(input("Introduce el número de notas que quieres introducir: "))
suma_notas = 0  # 1. Creamos un acumulador

for i in range(total_notas):
    nota = float(input(f"Introduce la nota {i+1}: "))
    suma_notas += nota  # 2. Vamos sumando cada nota


media = suma_notas / total_notas
print(f"La media de las notas es: {media:.2f}")
