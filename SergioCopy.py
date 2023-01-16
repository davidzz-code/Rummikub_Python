import random

# Función para crear las fichas con las que se va a jugar.
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

# Función para randomizar fichas.
def shuffleFichas(fichas):
    for fichasPos in range(len(fichas)):
        randPos = random.randint(0, 51)
        fichas[fichasPos], fichas[randPos] = fichas[randPos], fichas[fichasPos]
    return fichas

# Función para coger fichas.
def cogerFichas(numFichas):
    fichasJugador = []
    for x in range(numFichas):
        fichasJugador.append(fichasRummy.pop(0))
    return fichasJugador

# Función para mostrar la mano del jugador actual.
def mostrarMano(jugador, manoJugador):
    print("Player {}".format(jugador + 1))
    print("Tu mano")
    print("|-----------------|")
    y = 1
    for ficha in manoJugador:
        print(f"{y}) {ficha}")
        y += 1
    print("")

# Función para comprobar si se puede jugar una ficha en la mano o no.
def puedeJugar(color, valorFicha, manoJugador):
    for ficha in manoJugador:
        if color in ficha or valorFicha in ficha:
            return True
    return False


# Crear el conjunto de fichas ordenadas aleatoriamente
fichasRummy = conjuntoFichas()
fichasRummy = shuffleFichas(fichasRummy)
fichasRummy = shuffleFichas(fichasRummy)

# Crear listas de tablero y de posicion.
tablero = []
posicion = []

# Definir el número de jugadores
jugadores = []
numJugadores = int(input("¿Cuántos jugadores? "))
while numJugadores < 2 or numJugadores > 4:
    numJugadores = int(input("Inválido. Por favor, inserta un número entre 2 y 4. "))

# Se reparten 14 fichas por cada jugador en juego
for jugador in range(numJugadores):
    jugadores.append(cogerFichas(14))

#Definimos el turno del jugador, 
# la condición para que el bucle se cumpla mediante un booleano
# Añadimos una primera ficha al tablero --> TO DO: quitar la ficha, porque es parte del UNO 
jugadorTurno = 0
jugando = True
tablero.append(fichasRummy.pop(0))

# Definir si es el primer turno
primerTurno = False
if numJugadores == 2 and jugadorTurno <= 1:
    primerTurno = True
if numJugadores == 3 and jugadorTurno <= 2:
    primerTurno = True
if numJugadores == 4 and jugadorTurno <= 3:
    primerTurno = True


# Dividimos el valor y el color de la ficha para hacer las comparaciones
splitFicha = fichasRummy[0].split(" ", 1)
color = splitFicha[0]
valorFicha = splitFicha[1]

# Bucle princial:
while jugando:
    mostrarMano(jugadorTurno, jugadores[jugadorTurno])
    print(f"La/s ficha/s en el tablero es: {tablero}")

    # Si la mano del jugador es jugable, elige un ficha para jugarla.
    if puedeJugar(color, valorFicha, jugadores[jugadorTurno]):
        fichaEscogida = int(input("¿Qué ficha quieres escoger? "))

        # Si la ficha escogida no es valida segun las normas, debe escoger otra ficha.
        while not puedeJugar(
            color, valorFicha, [jugadores[jugadorTurno][fichaEscogida - 1]]
        ):
            fichaEscogida = int(
                input("No es una ficha valida. ¿Qué ficha quieres escoger? ")
            )
        tablero.append(jugadores[jugadorTurno].pop(fichaEscogida - 1))

    # Si no tiene fichas para jugar, el programa añade una ficha a la mano del jugador.
    else:
        print("No puedes jugar. Debes coger otra ficha.")
        jugadores[jugadorTurno].extend(cogerFichas(1))

    # Pasar al siguiente turno
    jugadorTurno += jugadorTurno

    # Si el turno del ultimo jugador acaba, volver a empezar los turnos
    if jugadorTurno == numJugadores:
        jugadorTurno = 0
