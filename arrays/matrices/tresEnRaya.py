from random import randrange;

global posicionesOcupadas
posicionesOcupadas = [0]
global tablero
tablero = []

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

    if posicionesOcupadas[0] == 9: 
        return False
    elif xPlayer > 0 and xPlayer <= 3 and yPlayer > 0 and yPlayer <= 3:
        if tablero[xPlayer - 1][yPlayer - 1] == "-":
            tablero[xPlayer - 1][yPlayer - 1] = "O"
            posicionesOcupadas[0] += 1
        else:
            print("Esa casilla ya está ocupada")
            introducirMovimiento()
    else:
        print("Has introducido unas coordenadas fuera de los límites")
        introducirMovimiento()

def jugadaOponente():
    xOponent = randrange(3)
    #print(xOponent)
    yOponent = randrange(3)
    #print(yOponent)

    if posicionesOcupadas[0] == 9: 
        return False
    elif tablero[xOponent][yOponent] == "-":
        tablero[xOponent][yOponent] = "X"
        posicionesOcupadas[0] += 1
    else:
        jugadaOponente()

def comprobarGanador(jugador):
    for i in range(3):
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True

        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True

    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True

    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True


def tresEnRaya():
    while posicionesOcupadas[0] != 9:
        mostrarTablero()
        introducirMovimiento()
        jugadaOponente()

        if comprobarGanador("O"):
            print("Has ganado")
            mostrarTablero()
            break
        elif comprobarGanador("Y"):
            print("Has perdido")
            mostrarTablero()
            break
        elif posicionesOcupadas[0] == 9:
            print("Todas las casillas ocupadas")

tresEnRaya()