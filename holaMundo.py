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

#Intercambio inteligente de variables
variable1 = 1
variable2 = 2
variable1, variable2 = variable2, variable1

print(variable1)
print(variable2)

#Declarar un array
numeros = [10, 5, 7, 2, 3]
print("Contenido de la lista:", numeros) # imprimiendo contenido de la lista original.
print("\nLongitud de la lista:", len(numeros)) # imprimiendo la longitud de la lista
del numeros[1] # eliminando el segundo elemento de la lista
#Numeros negativos de un array
print(numeros[-1]) #Mostrará 3
print(numeros[-2]) #Mostrará 2
#Agregar un nuevo elemento a la lista:
numeros.append(6)
#Insertar un nuevo elemento a la lista en una posición específica
numeros.insert(4,8) #(ubicación,valor)
#Ordenar lista
miLista2 = [8, 10, 6, 2, 4]
miLista2.sort() 
print(miLista2)
miLista2.sort() 
print(miLista2)
# Comprobar si un elemento está en una lista o si no lo está:
miLista3 = [0, 3, 12, 8, 2]

print(5 in miLista3) # Devuelte False
print(5 not in miLista3) # Devuelte True
print(12 in miLista3) # Devuelte True

#Declaración de una matriz
tablero = [["3" for i in range(8)] for j in range(8)]

# None sirve para saber que una variable no tiene valor, está nula
valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor") 


#TUPLAS
miTupla = (1, 10, 100, 1000)

print(miTupla[0])
print(miTupla[-1])
print(miTupla[1:])
print(miTupla[:-2])

for elem in miTupla:
    print(elem)

miTupla2 = (1, 10, 100)

t1 = miTupla2 + (1000, 10000)
t2 = miTupla2 * 3

print(len(t2))
print(t1)
print(t2)
print(10 in miTupla2)
print(-10 not in miTupla2) #Devuelve False ya que la posición -10 no está en la tupla


#DICCIONARIOS (como los arrays asociativos en PHP)
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
#Trae como clave-valor todas los valores de la tupla
for spanish, french in dict.items():
    print(spanish, "->", french)

#Añadir un elemento
dict['gato'] = 'minou'
print(dict)
