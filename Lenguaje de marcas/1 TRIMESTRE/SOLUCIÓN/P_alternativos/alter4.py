#Introducir una letra y visualizar si es vocal o consonante. 
letra= input("Introduce una letra: ")
if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("vocal")
else:
    print("consonante")