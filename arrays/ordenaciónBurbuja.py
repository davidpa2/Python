miLista = []
hayIntercambios = True
num = int (input("¿Cuántos elementos deseas ordenar?:"))

for i in range(num):
    val = float(input("Introduce un elemento de la lista:"))
    miLista.append(val)

while hayIntercambios:
    hayIntercambios = False
    for i in range(len(miLista) - 1):
        if miLista[i] > miLista[i + 1]:
            hayIntercambios = True
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print("\nOrdenado:")
print(miLista)

#MANERA SENCILLAMENTE FÁCIL
miLista2 = [8, 10, 6, 2, 4]
miLista2.sort() 
print(miLista2)