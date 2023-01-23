import random, os, time, math
from rich.console import Console
from rich.progress import track

console = Console()

#################################### FUNCIONES ESTETICAS ####################################
# Funciones para escribir en color
def prRed(ficha, end="\n"):
    print("\033[31m {}\033[00m".format(ficha), end=end)


def prOrange(ficha, end="\n"):
    print("\033[33m {}\033[00m".format(ficha), end=end)


def prBlue(ficha, end="\n"):
    print("\033[34m {}\033[00m".format(ficha), end=end)


def prPurple(ficha, end="\n"):
    print("\033[35m {}\033[00m".format(ficha), end=end)


def prGreen(ficha, end="\n"):
    print("\033[32m {}\033[00m".format(ficha), end=end)


# Función para borrar la terminal
def borrarTerminal():
    os.system("clear")


# Función para pintar una ficha de un color. Sin salto de linea
def pintarFichaColor(text, color):
    if color == "Rojo":
        prRed(text, end="")
        return
    if color == "Negro":
        prPurple(text, end="")
        return
    if color == "Azul":
        prBlue(text, end="")
        return
    if color == "Naranja":
        prOrange(text, end="")
        return
    print(text, end="")


# Bienvendia al juego
def darBienvenida():
    borrarTerminal()
    console.print(
        "____                                    _   _  __          _      \n"
        + "  |  _ \   _   _   _ __ ___    _ __ ___   (_) | |/ /  _   _  | |__  \n"
        + "  | |_) | | | | | | '_ ` _ \  | '_ ` _ \  | | | ' /  | | | | | '_ \ \n"
        + "   |  _ <  | |_| | | | | | | | | | | | | | | | | . \  | |_| | | |_) |\n"
        + "  |_| \_\  \__,_| |_| |_| |_| |_| |_| |_| |_| |_|\_\  \__,_| |_.__/ \n",
        justify="center",
        style="bold",
    )
    print("\n\n")
    console.print(
        ":fire:",
        "¡Bienvenido a Rummikub!",
        ":fire:",
        justify="center",
        style="bold cyan",
    )
    console.print(
        "Estamos preparándolo todo para poder iniciar el juego cuanto antes.\n"
        + "Antes de nada, necesitamos saber algunas cosas para ajustar la partida.\n",
        justify="center",
    )
    print("\n\n")
    console.print(
        "Este es un producto creado por: \n "
        + "Sergi Darder, David Ramírez y Sergio Majada",
        justify="center",
    )
    print("\n\n")


# Cargar el juego
def progressBar():
    for i in track(range(100), description="Cargando..."):
        time.sleep(0.05)


# Función para dar inicio al juego
def startGameTxt():
    borrarTerminal()
    console.print("\n\n¡TODO LISTO¡\n¡A JUGAR!", justify="center")
    console.print("Mucha suerte y que gane el mejor", justify="center")
    time.sleep(1.5)


# Función para acabar la partida
def finalPartida(jugador):
    borrarTerminal()

    console.print("El juego ha acabado ¡Te has quedado sin fichas!", justify="center")
    console.print("EL GANADOR ES:\n", justify="center")
    console.print(f"\tEl jugador {jugador + 1}\n", justify="center")

    console.print(
        " _ ______ _   _ _    _  ____  _____            ____  _    _ ______ _   _          _  \n"
        + "(_)  ____| \ | | |  | |/ __ \|  __ \     /\   |  _ \| |  | |  ____| \ | |   /\   | | \n"
        + "| | |__  |  \| | |__| | |  | | |__) |   /  \  | |_) | |  | | |__  |  \| |  /  \  | | \n"
        + "| |  __| | . ` |  __  | |  | |  _  /   / /\ \ |  _ <| |  | |  __| | . ` | / /\ \ | | \n"
        + "| | |____| |\  | |  | | |__| | | \ \  / ____ \| |_) | |__| | |____| |\  |/ ____ \|_| \n"
        + "|_|______|_| \_|_|  |_|\____/|_|  \_\/_/    \_\____/ \____/|______|_| \_/_/    \_(_) ", justify="center"
    )


#################################### FUNCIONES DEL JUEGO ####################################

# Función para imprimir el estado de todo el juego por pantalla
def mostrarEstadoJuego(numJugador, manoJugador):
    console.print(f"JUGADOR {numJugador + 1}", style="bold")
    print("\n\t■ El tablero actual es: ")
    mostrarTablero(tablero)
    print("\n\t■ Tu mano")
    mostrarMano(manoJugador)

    # Mostrar las opciones que se pueden realizar
    print("\n\t■ Las acciones que puedes hacer son:")
    mostrarTurno(puedePasar, puedeCogerFicha)


# Función para crear las fichas con las que se va a jugar.
def conjuntoFichas():
    fichas = []

    colores = ["Naranja", "Azul", "Negro", "Rojo"]

    for z in range(2):
        for color in colores:
            for valor in range(1, 14):
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
def mostrarMano(manoJugador):
    print("|" + "-" * 120 + "|")
    porFila = 7
    y = 1
    for fila in range(math.ceil(len(manoJugador) / porFila)):
        for x in range(porFila):
            if y > len(manoJugador):
                break
            splitFicha = manoJugador[x + (fila * porFila)].split(" ", 1)
            color = splitFicha[0]
            print(f"({y})", end="")
            pintarFichaColor(f"{manoJugador[x+(fila*porFila)]}\t", color)
            y += 1
        print("")
    print("|" + "-" * 120 + "|")


# Funcion para mostrar las opciones que tiene el jugador en su turno
def mostrarTurno(puedePasar, puedeCogerFicha):
    if puedeCogerFicha:
        console.print(
            "[bold cyan]Opción 1:[/bold cyan] [underline]Coger ficha.[/underline]"
        )

    if partidaTurno > 1 or len(tablero) >= 1:
        console.print(
            "[bold cyan]Opcion 2:[/bold cyan] [underline]Añadir ficha a una posición existente.[/underline]"
        )

    console.print(
        "[bold cyan]Opción 3:[/bold cyan] [underline]Añadir ficha a una posición nueva.[/underline]"
    )

    if puedePasar:
        console.print(
            "[bold cyan]Opción 4:[/bold cyan] [underline]Pasar turno.[/underline]"
        )


# Función para pintar una monton del tablero
def mostrarMonton(monton):
    f = 1
    for ficha in monton:
        splitFicha = ficha.split(" ", 1)
        color = splitFicha[0]
        pintarFichaColor(f"{ficha}", color)
        f += 1
        if f <= len(monton):
            print(" -", end="")


# Funcion para mostrar el tablero
def mostrarTablero(tablero):
    print("|" + "-" * 120 + "|")
    porFila = 3
    numero = 1
    for fila in range(math.ceil(len(tablero) / porFila)):
        for x in range(porFila):
            if numero > len(tablero):
                break
            print("", end="")
            print(f"({numero})", end="")
            mostrarMonton(tablero[x + (fila * porFila)])
            print("\t\t", end="")
            numero += 1
        print("")
    print("|" + "-" * 120 + "|")


# Primera opcion del turno: Anadir una ficha a la mano del jugador
def opcion1(manoJugador):
    manoJugador.extend(cogerFichas(1))
    prGreen("\nTu ficha se ha añadido con éxito.")


# Segunda opcion del turno: Anadir una ficha a una posicion existente
def opcion2():
    global fichaUsuario
    global conjunto
    fichaUsuario = int(input("Elige la ficha que quieres añadir: "))

    if fichaUsuario > len(jugadores[jugadorTurno]):
        prRed("\tNo tienes esta ficha en la mano.")
        return False

    conjunto = int(input("Elige el conjunto del tablero en la que la quieres anadir: "))
    if conjunto > len(tablero):
        prRed("\tEste conjunto no se encuentra en el tablero.")
        return False
    elif conjunto <= len(tablero):
        return reglasOpcion2()


# Tercera opcion del turno: Anadir fichas a una nueva posicion
def opcion3(manoJugador):
    global nuevoConjunto
    global fichaUsuario

    nuevoConjunto = []
    acabarMonton = False

    while not acabarMonton:
        fichaUsuario = int(
            input(
                "\nElige la ficha que quieres añadir. Si no quieres anadir mas, inserta 0: "
            )
        )

        if fichaUsuario == 0:
            if len(nuevoConjunto) <= 2:
                prRed("\tEl conjunto mínimo debe ser de 3 fichas.")
                cancelOpcion = input("¿Quieres cancelar la operación? (s/n)")

                if str(cancelOpcion).lower() == "s":
                    acabarMonton = True
                    jugadores[jugadorTurno].extend(nuevoConjunto)
                    nuevoConjunto.clear()

                elif (
                    str(cancelOpcion).lower() != "n" or str(cancelOpcion).lower() != "s"
                ):
                    prRed("\tOpción no válida.")

            else:
                acabarMonton = True
                tablero.append(nuevoConjunto)

        # Si el número indicado supera el índice de la mano, indica que no tiene la ficha y cierra el bucle
        elif fichaUsuario > len(jugadores[jugadorTurno]):
            prRed("\tNo tienes esta ficha en la mano.")

        else:
            # Añade la ficha al conjunto y la elimina de la mano
            if len(nuevoConjunto) == 0:
                nuevoConjunto.append(jugadores[jugadorTurno][fichaUsuario - 1])
                jugadores[jugadorTurno].pop(fichaUsuario - 1)
                prGreen("\nTu ficha se ha añadido con éxito.")
            else:
                if reglasOpcion3():
                    jugadores[jugadorTurno].pop(fichaUsuario - 1)
                    prGreen("\nTu ficha se ha añadido con éxito.")
                else:
                    prRed("\tNo se puede añadir esta ficha al conjunto.")

            print("\n\n\t■ Tu nueva mano es: ")
            mostrarMano(manoJugador)

            print("\n\t■ El conjunto que quieres anadir, por ahora, es: ", end="")
            mostrarMonton(nuevoConjunto)

    return len(nuevoConjunto) != 0


# Reglas escalera y tíos para la opción 2
def reglasOpcion2():
    # Guarda el color y por otro lado el número de la ficha seleccionada
    colorFichaUsuario = jugadores[jugadorTurno][fichaUsuario - 1].split(" ")
    numeroFichaUsuario = int(colorFichaUsuario.pop(1))

    # Crea lista de colores y números de las fichas del tablero por separado
    listaColoresTablero = []
    listaNumerosTablero = []

    # Accede a las fichas del conjunto seleccionado en el tablero y las separa en color y número.
    # Luego los añade a las listas creadas anteriormente
    for i in tablero[conjunto - 1]:
        colorConjunto = i.split(" ")
        numeroConjunto = int(colorConjunto.pop(1))
        listaColoresTablero.append(colorConjunto[0])
        listaNumerosTablero.append(numeroConjunto)

    # Bucle principal de las reglas.
    # Valora si el conjunto está formado por tríos o escalera de números y así ejecuta una regla u otra
    if listaNumerosTablero[0] == listaNumerosTablero[1]:

        # REGLA - TRÍOS
        correcto = False
        while not correcto:
            if colorFichaUsuario[0] in listaColoresTablero:
                prRed("\tMovimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario != numeroConjunto:
                prRed("\tMovimiento incorrecto, vuelve a probar.")
                return False

            else:
                correcto = True
                tablero[conjunto - 1].append(jugadores[jugadorTurno][fichaUsuario - 1])
                prGreen("\nTu ficha se ha añadido con éxito.")
                return True
    else:
        # REGLA - ESCALERA
        correcto = False
        while correcto == False:
            if (
                colorFichaUsuario != colorConjunto
                or numeroFichaUsuario != (listaNumerosTablero[-1] + 1)
                and numeroFichaUsuario != (listaNumerosTablero[0] - 1)
            ):
                prRed("\tMovimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario == (listaNumerosTablero[0] - 1):
                correcto = True
                listaNumerosTablero.append(numeroFichaUsuario)
                listaNumerosTablero.sort()
                tablero[conjunto - 1].insert(0, jugadores[jugadorTurno][fichaUsuario - 1])

            else:
                correcto = True
                tablero[conjunto - 1].append(jugadores[jugadorTurno][fichaUsuario - 1])

        return correcto


# Reglas escalera y tíos para la opción 3
def reglasOpcion3():
    # Guarda el color y por otro lado el número de la ficha seleccionada
    colorFichaUsuario = jugadores[jugadorTurno][fichaUsuario - 1].split(" ")
    numeroFichaUsuario = int(colorFichaUsuario.pop(1))

    # Crea lista de colores y números de las fichas por separado del nuevo conjunto que se está creando
    listaColoresTablero = []
    listaNumerosTablero = []

    # Accede a las fichas del nuevo conjunto en el tablero y las separa en color y número.
    # Luego los añade a las listas creadas anteriormente
    for i in nuevoConjunto:
        colorConjunto = i.split(" ")
        numeroConjunto = int(colorConjunto.pop(1))
        listaColoresTablero.append(colorConjunto[0])
        listaNumerosTablero.append(numeroConjunto)

    # Bucle principal de las reglas.
    # Valora si el conjunto está formado por tríos o escalera de números y así ejecuta una regla u otra
    if listaNumerosTablero[0] == numeroFichaUsuario:
        # REGLA - TRÍOS
        correcto = False
        while not correcto:
            if colorFichaUsuario[0] in listaColoresTablero:
                prRed("\tMovimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario != numeroConjunto:
                prRed("\tMovimiento incorrecto, vuelve a probar.")
                return False

            else:
                correcto = True
                return True
    else:
        # REGLA - ESCALERA
        correcto = False
        while not correcto:
            if (colorFichaUsuario != colorConjunto or numeroFichaUsuario != (listaNumerosTablero[-1] + 1) and numeroFichaUsuario != (listaNumerosTablero[0] - 1)):
                prRed("\tMovimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario == (listaNumerosTablero[0] - 1):
                correcto = True
                listaNumerosTablero.append(numeroFichaUsuario)
                listaNumerosTablero.sort()
                nuevoConjunto.insert(0, jugadores[jugadorTurno][fichaUsuario - 1])
            else:
                correcto = True
                nuevoConjunto.append(jugadores[jugadorTurno][fichaUsuario - 1])
        return correcto


#################################### INICIO DEL JUEGO ####################################

# Crear el conjunto de fichas ordenadas aleatoriamente
fichasRummy = conjuntoFichas()
fichasRummy = shuffleFichas(fichasRummy)
fichasRummy = shuffleFichas(fichasRummy)

# Crear lista de tablero.
tablero = []

darBienvenida()

# Definir el número de jugadores
jugadores = []
numJugadores = int(console.input("[b]¿Cuántos jugadores?[/b] "))
while numJugadores < 2 or numJugadores > 4:
    prRed("\tInválido. Por favor, inserta un número entre 2 y 4.\n")
    numJugadores = int(input("¿Cuántos jugadores? "))

print("¡Perfecto! En unos segundos estará todo listo.\n")
progressBar()

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
primerTurno = True

# Dividimos el valor y el color de la ficha para hacer las comparaciones
splitFicha = fichasRummy[0].split(" ", 1)
color = splitFicha[0]
valorFicha = int(splitFicha[1])

# Booleano para detectar si puede pasar y si puede coger ficha, de esta manera en el
# menu se le mostrara o no la opcion
puedePasar = False
puedeCogerFicha = True

startGameTxt()

# Bucle princial:
while jugando:

    # Si no es el primer turno
    if not primerTurno:

        puedeCogerFicha = True
        puedePasar = False
        acabarAccion = False

        while not acabarAccion:
            time.sleep(1)
            borrarTerminal()
            # Muestra la mano y el tablero.
            mostrarEstadoJuego(jugadorTurno, jugadores[jugadorTurno])
            while True:
                try:
                    accion = int(input("\n¿Qué acción quieres hacer?: "))
                    break
                except ValueError:
                    prRed("\tPor favor, introduce un número válido.")

            if accion == 1 and puedeCogerFicha:
                # Añade una ficha a la mano del jugador
                opcion1(jugadores[jugadorTurno])

            elif accion == 2:
                correcto = opcion2()

                if correcto:
                    puedeCogerFicha = False
                    puedePasar = True

            elif accion == 3:
                correcto = opcion3(jugadores[jugadorTurno])

                if correcto:
                    puedeCogerFicha = False
                    puedePasar = True

            elif accion == 4:
                acabarAccion = True

            else:
                prRed("\tOpcion no valida")

    # Si es primer turno:
    else:
        puedeCogerFicha = True
        puedePasar = False
        acabarAccion = False

        while not acabarAccion:
            time.sleep(1)
            borrarTerminal()
            # Muestra la mano y el tablero.
            mostrarEstadoJuego(jugadorTurno, jugadores[jugadorTurno])
            while True:
                try:
                    accion = int(input("\n¿Qué acción quieres hacer?: "))
                    break
                except ValueError:
                    prRed("\tPor favor, introduce un número válido.")

            if accion == 1 and puedeCogerFicha:
                # Añade una ficha a la mano del jugador
                opcion1(jugadores[jugadorTurno])

            elif accion == 2:
                correcto = opcion2()

                if correcto:
                    puedePasar = True

            elif accion == 3:
                correcto = opcion3(jugadores[jugadorTurno])

                if correcto:
                    puedePasar = True

            elif accion == 4:
                # Divide la ficha y suma el valor numérico
                valorFichas = 0
                for conjunto in tablero:
                    for ficha in conjunto:
                        splitFicha = ficha.split(" ")
                        valorFichas += int(splitFicha[1])

                # Comprueba que tenga 30 puntos en el valor de sus fichas
                if valorFichas < 30:
                    prRed("\tEl valor de los conjuntos añadidos no es mayor de 30.")
                else:
                    acabarAccion = True
                    if partidaTurno == numJugadores:
                        primerTurno = False
            else:
                prRed("\tOpción no válida \n")

    if (
        len(jugadores[jugadorTurno]) == 0
    ):  # Si la mano del jugador está vacía, se acaba el juego
        jugando = False

    else:
        # Pasar al siguiente turno
        jugadorTurno = jugadorTurno + 1
        time.sleep(1.5)

        if jugadorTurno == numJugadores:
            jugadorTurno = 0

        # Sumar 1 al turno de la partida
        partidaTurno += 1

finalPartida(jugadorTurno)
