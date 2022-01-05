bloques = int(input("Ingrese el número de bloques:"))
altura = 0
bloquesContados = 0;

while bloques > 0:
    bloques -= 1
    bloquesContados += 1
    
    if altura + 1 == bloquesContados:
        print(bloquesContados)
        altura+= 1
        bloquesContados = 0
        
    
print("La altura de la pirámide:", altura)


'''
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa 
superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de 
la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de 
bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
'''