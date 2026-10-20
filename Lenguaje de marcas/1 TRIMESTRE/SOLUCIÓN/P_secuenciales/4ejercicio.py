#Calcular la hipotenusa de un triángulo 
import math
CatetoA=float(input("Dame el cateto A: "))
CatetoB=float(input("Dame el cateto B: "))
#h=math.hypot(CatetoA,CatetoB)
Hipotenusa=math.sqrt(CatetoA**2+CatetoB**2)
print(f"La hipotenusa es: {Hipotenusa:.2f}")
