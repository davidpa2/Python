from random import randrange;

global tablero, posicionesOcupadas
tablero = []
posicionesOcupadas = 0

ganada = False



#Generar la matriz rellena de guiones
for i in range(3):
    fila = ["-" for i in range(3)]
    tablero.append (fila)
    
#print(tablero, sep="\n")

def mostrarTablero():
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end=" ")
        print()

def introducirMovimiento():
    xPlayer = int(input("Introduza la coordenada x: "))
    yPlayer = int(input("Introduza la coordenada y: "))

    if xPlayer > 0 and xPlayer <= 3 and yPlayer > 0 and yPlayer <= 3:
        if tablero[xPlayer - 1][yPlayer - 1] == "-" or tablero[xPlayer - 1][yPlayer - 1] == "X" or tablero[xPlayer - 1][yPlayer - 1] == "O":
            tablero[xPlayer - 1][yPlayer - 1] = "O"
            posicionesOcupadas += 1
        else:
            print("Esa casilla ya está ocupada")
            introducirMovimiento()
    else:
        print("Has introducido unas coordenadas fuera de los límites")
        introducirMovimiento()

def jugadaOponente():
    xOponent = randrange(3)
    print(xOponent)
    yOponent = randrange(3)
    print(yOponent)

    if tablero[xOponent][yOponent] == "-" or tablero[xOponent][yOponent] == "X" or tablero[xOponent][yOponent] == "O":
        tablero[xOponent][yOponent] = "X"
        posicionesOcupadas += 1
    else:
        jugadaOponente()


def tresEnRaya():
    while ganada == False:
        mostrarTablero()
        introducirMovimiento()
        jugadaOponente()

tresEnRaya()