# break - ejemplo

print("La instrucción de ruptura:")
for i in range(1,6):
    if i == 3:
        break
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1,6):
    if i == 3:
        continue
    print("Dentro del ciclo.", i)
print("Fuera del ciclo.")

#----------------------USO DE BREAK
numeroMayor = -99999999
contador = 0

while True:
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
    if numero == -1:
        break
    contador = 1
    if numero > numeroMayor:
        numeroMayor = numero

if contador != 0:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 


#-----------------------USO DE CONTINUE

numeroMayor = -99999999
contador = 0

numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

while numero != -1:
    if numero == -1:
        continue
    contador = 1

    if numero > numeroMayor:
        numeroMayor = numero
    numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

if contador:
    print("El número más grande es", numeroMayor)
else:
    print("No ha ingresado ningún número") 