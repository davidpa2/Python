print("holaaa world!!");

#Comentario de una línea
'''
Comentario multilinea
'''
print("Fundamentos","Programación","en",sep="***",end="...")
print("Python")

#Uso de input y casteo
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)

#Para el bucle for hay que usar range()
#range() puede aceptar tres argumentos , desde donde, hasta donde, y el incremento
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)