import random
from colorama import Back, Fore, Style, init
from rich.console import Console

init(autoreset = True)
console = Console()


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
    print("Jugador {}".format(jugador + 1))
    print("Tu mano")
    print("|-----------------|")
    y = 1
    for ficha in manoJugador:
        if "Naranja" in ficha:
            print(Style.BRIGHT + Fore.YELLOW + f"{y}) {ficha}")
        if "Azul" in ficha:
            print(Style.BRIGHT + Fore.BLUE + f"{y}) {ficha}")
        if "Negro" in ficha:
            print(Style.BRIGHT + Fore.BLACK + f"{y}) {ficha}")
        if "Rojo" in ficha:
            print(Style.BRIGHT + Fore.RED + f"{y}) {ficha}")
        y += 1
    print("")


# Funcion para mostrar las opciones que tiene el jugador en su turno
def mostrarTurno(puedePasar, puedeCogerFicha):
    if puedeCogerFicha:
        print("Opcion 1: Coger ficha")

    if partidaTurno > 1:
        print("Opcion 2: Añadir ficha a una posición existente.")

    print("Opcion 3: Añadir ficha a una posición nueva")

    if puedePasar:
        print("Opcion 4: Pasar turno")


# Funcion para mostrar el tablero
def mostrarTablero(tablero):
    numero = 0
    for i in tablero:
        numero += 1
        print("El tablero actual es: ")
        print(str(numero) + ". " + ", ".join(i) + ",")
        print("")


# Primera opcion del turno: Anadir una ficha a la mano del jugador
def opcion1(manoJugador):
    manoJugador.extend(cogerFichas(1))

    print("Tu ficha se ha añadido con éxito.")
    print("")
    print("Tu mano actual es:")
    print("|-----------------|")
    y = 1
    for ficha in manoJugador:
        print(f"{y}) {ficha}")
        y += 1
    print("")
    print("Elige una nueva opcion: ")


# Segunda opcion del turno: Anadir una ficha a una posicion existente
def opcion2():
    fichaUsuario = int(input("Elige la ficha que quieres añadir: "))

    if fichaUsuario > len(jugadores[jugadorTurno]):
        print("No tienes esta ficha en la mano.")
        return

    conjunto = int(input("Elige el conjunto del tablero en la que la quieres anadir: "))
    if conjunto > len(tablero):
        print("Este conjunto no se encuentra en el tablero.")
        return

    prinFin = int(input("Al principio (1) o al final (2)? "))
    if prinFin == 1:
        tablero[conjunto - 1] = [jugadores[jugadorTurno].pop(fichaUsuario - 1)] + tablero[
            conjunto - 1
        ]

    elif prinFin == 2:
        tablero[conjunto - 1].append(jugadores[jugadorTurno].pop(fichaUsuario - 1))
    
    else: 
        print("Esa posición no existe.")

    mostrarTablero(tablero)


# Tercera opcion del turno: Anadir fichas a una nueva posicion
def opcion3(manoJugador):
    nuevoConjunto = []
    valorConjunto = 0
    listaSoporte = []

    fichaUsuario = int(
        input(
            "Elige la ficha que quieres añadir. Si no quieres anadir mas, inserta 0: "
        )
    )

    while fichaUsuario != 0:
        # Si el número indicado supera el índice de la mnao, indica que no tiene la ficha y cierra el bucle
        if fichaUsuario > len(jugadores[jugadorTurno]):
            print("No tienes esta ficha en la mano.")

            return

        # Divide la ficha y suma el valor numérico
        splitFicha = jugadores[jugadorTurno][fichaUsuario - 1].split(" ")
        valorConjunto += int(splitFicha[1])

        # Añade la ficha a la lista de soporte
        listaSoporte.append(jugadores[jugadorTurno][fichaUsuario - 1])

        # Añade la ficha al conjunto y la elimina de la mano
        nuevoConjunto.append(jugadores[jugadorTurno].pop(fichaUsuario - 1))

        print("Tu nueva mano es:")
        print("-----------------")
        y = 1
        for ficha in manoJugador:
            print(f"{y}) {ficha}")
            y += 1
        print("")

        print(f"El conjunto que quieres anadir, por ahora, es: {nuevoConjunto}")

        fichaUsuario = int(input("Elige otra ficha que quieres añadir: "))

        if fichaUsuario == 0:
            if len(nuevoConjunto) <= 2:
                print("El conjunto minimo debe ser de 3 fichas. Añade mas fichas.")

            elif len(nuevoConjunto) < 1:
                print("Debes insertar, como mínimo, una ficha.")
                nuevoConjunto.clear()

            else:
                break

    # El conjunto del primer turno debe tener un valor superior a 30 puntos.
    if primerTurno and valorConjunto < 30:
        print(
            "El valor de este conjunto debe ser mayor o igual a 30. Vuelve a elegir las fichas:"
        )
        nuevoConjunto.clear()
        manoJugador.extend(listaSoporte)
        mostrarMano(jugadorTurno, jugadores[jugadorTurno])
    else:
        tablero.append(nuevoConjunto)

    mostrarTablero(tablero)

def finalPartida(jugador):
    print('¡ENHORABUENA!')
    print('El juego ha acabado porque te has quedado sin fichas.')
    print(f'El jugador {jugador + 1} es el ganador de esta partida.')


# Crear el conjunto de fichas ordenadas aleatoriamente
fichasRummy = conjuntoFichas()
fichasRummy = shuffleFichas(fichasRummy)
fichasRummy = shuffleFichas(fichasRummy)

# Crear lista de tablero.
tablero = []

# Definir el número de jugadores
jugadores = []
numJugadores = int(input("¿Cuántos jugadores? "))
while numJugadores < 2 or numJugadores > 4:
    numJugadores = int(input("Inválido. Por favor, inserta un número entre 2 y 4. "))

# Se reparten 14 fichas por cada jugador en juego
for jugador in range(numJugadores):
    jugadores.append(cogerFichas(14))

# Definimos el turno del jugador,
# el turno de la partida y
# la condición para que el bucle del juego principal se cumpla mediante un booleano
# Añadimos una primera ficha al tablero --> TO DO: quitar la ficha, porque es parte del UNO
jugadorTurno = 0
partidaTurno = 1
jugando = True

# Definir si es el primer turno
primerTurno = False
if numJugadores == 2 and partidaTurno <= 2:
    primerTurno = True
if numJugadores == 3 and partidaTurno <= 3:
    primerTurno = True
if numJugadores == 4 and partidaTurno <= 4:
    primerTurno = True

# Dividimos el valor y el color de la ficha para hacer las comparaciones
splitFicha = fichasRummy[0].split(" ", 1)
color = splitFicha[0]
valorFicha = int(splitFicha[1])

# Booleano para detectar si puede pasar y si puede coger ficha, de esta manera en el
# menu se le mostrara o no la opcion
puedePasar = False
puedeCogerFicha = True

if not primerTurno:
    # Bucle princial:
    while jugando:
        # Muestra la mano y el tablero.
        mostrarMano(jugadorTurno, jugadores[jugadorTurno])
        mostrarTablero(tablero)

        # Mostrar las opciones que se pueden realizar
        mostrarTurno(puedePasar, puedeCogerFicha)
        accion = int(input(f"Elige una accion a realizar: "))

        while accion != 4:
            if accion == 1 and puedeCogerFicha:
                opcion1(
                    jugadores[jugadorTurno]
                )  # Añade una ficha a la mano del jugador

            elif accion == 2:
                opcion2()
                puedeCogerFicha = False
                puedePasar = True

            elif accion == 3:
                opcion3(jugadores[jugadorTurno])
                puedeCogerFicha = False
                puedePasar = True

            elif accion == 4 and puedePasar:
                # Pasar al siguiente turno
                if len(jugadores[jugadorTurno]) == 0: #Si la mano del jugador está vacía, gana el juego
                    jugando = False
                    finalPartida(jugadorTurno)

            else:
                print("Opcion no valida")

            # Mostrar las opciones que se pueden realizar
            mostrarTurno(puedePasar, puedeCogerFicha)
            accion = int(input(f"Elige una accion a realizar: "))

        # Si el turno del ultimo jugador acaba, volver a empezar los turnos
        if jugadorTurno == numJugadores:
            jugadorTurno = 0
        
        # Suma 1 al turno de la partida
        partidaTurno += partidaTurno

else:
        # Bucle princial:
    while jugando:
        # Muestra la mano y el tablero.
        mostrarMano(jugadorTurno, jugadores[jugadorTurno])
        mostrarTablero(tablero)

        # Mostrar las opciones que se pueden realizar
        mostrarTurno(puedePasar, puedeCogerFicha)
        accion = int(input(f"Elige una accion a realizar: "))

        while accion != 4:
            if accion == 1 and puedeCogerFicha:
                opcion1(
                    jugadores[jugadorTurno]
                )  # Añade una ficha a la mano del jugador

            elif accion == 2:
                opcion2()
                puedeCogerFicha = False
                puedePasar = True

            elif accion == 3:
                opcion3(jugadores[jugadorTurno])
                puedeCogerFicha = False
                puedePasar = True

            else:
                print("Opción no válida")
                print("")

            # Mostrar las opciones que se pueden realizar
            mostrarTurno(puedePasar, puedeCogerFicha)
            accion = int(input(f"Elige una accion a realizar: "))

        if len(jugadores[jugadorTurno]) == 0: #Si la mano del jugador está vacía, gana el juego
            jugando = False
            finalPartida(jugadorTurno)
        else: 
            # Sumar 1 al turno de la partida
            partidaTurno += partidaTurno
            # Si el turno del ultimo jugador acaba, volver a empezar los turnos
            if jugadorTurno == numJugadores:
                jugadorTurno = 0
