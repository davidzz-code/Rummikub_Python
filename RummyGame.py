import random


def conjuntoFichas():
    fichas = []

    colores = ["Naranja", "Azul", "Negro", "Rojo"]
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    for z in range(2):
        for color in colores:
            for valor in valores:
                fichaVal = "{} {}".format(color, valor)
                fichas.append(fichaVal)
    return fichas

def shuffleFichas(fichas):
    for fichasPos in range(len(fichas)):
        randPos = random.randint(0, 51)
        fichas[fichasPos], fichas[randPos] = fichas[randPos], fichas[fichasPos]
    return fichas

def manoFichasJugador(numFichas):
    fichasJugador = []
    for x in range(numFichas):
        fichasJugador.append(fichasRummy.pop(0))
    return fichasJugador

def mostrarMano(jugador, manoFichasJugador):
    print(f"Player {jugador+1}")
    print("Tu mano")
    print("|-----------------|")
    for ficha in manoFichasJugador:
        print(ficha)
    print("")

# Crear el conjunto de fichas ordenadas aleatoriamente
fichasRummy = conjuntoFichas()
fichasRummy = shuffleFichas(fichasRummy)
fichasRummy = shuffleFichas(fichasRummy)

# Crear listas de descartes y de jugadores.
descartes = []
jugadores = []

# Definir el número de jugadores
numJugadores = int(input("¿Cuántos jugadores? "))
while numJugadores < 2 or numJugadores > 4:
    numJugadores = int(input('Inválido. Por favor, inserta un número entre 2 y 4. '))

for jugador in range(numJugadores):
    jugadores.append(manoFichasJugador(14))

jugadorTurno = 0
jugando = True
descartes.append(fichasRummy.pop(0))

while jugando:
    mostrarMano(jugadorTurno, jugadores[jugadorTurno])
    print(f"Pieza en el top de la pila de descartes: {descartes[-1]}")
    jugando = False
