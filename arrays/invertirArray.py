#Para una cantidad pequeña:
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista) 

#Con un bucle for
miLista2 = [10, 1, 8, 3, 5]
longitud = len(miLista2)

for i in range (longitud // 2):
    miLista2[i], miLista2[longitud-i-1] = miLista2[longitud-i-1], miLista2[i]

print(miLista2) 