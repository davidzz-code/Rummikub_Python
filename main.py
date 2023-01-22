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
    print("Jugador {}".format(jugador + 1))
    print("Tu mano")
    print("|-----------------|")
    y = 1
    for ficha in manoJugador:
        print(f"{y}) {ficha}")
        y += 1
    print("")


# Funcion para mostrar las opciones que tiene el jugador en su turno
def mostrarTurno(puedePasar, puedeCogerFicha):
    if puedeCogerFicha:
        print("Opcion 1: Coger ficha")

    if partidaTurno > 1 or len(tablero) > 1:
        print("Opcion 2: Añadir ficha a una posición existente.")

    print("Opcion 3: Añadir ficha a una posición nueva")

    if puedePasar:
        print("Opcion 4: Pasar turno")


# Funcion para mostrar el tablero
def mostrarTablero(tablero):
    numero = 0
    print("El tablero actual es: ")
    for i in tablero:
        numero += 1
        print(str(numero) + ". " + ", ".join(i) + ",")
        print("")


# Primera opcion del turno: Anadir una ficha a la mano del jugador
def opcion1(manoJugador):
    manoJugador.extend(cogerFichas(1))
    print("Tu ficha se ha añadido con éxito.")


# Segunda opcion del turno: Anadir una ficha a una posicion existente
def opcion2():
    global fichaUsuario
    global conjunto
    fichaUsuario = int(input("Elige la ficha que quieres añadir: "))

    if fichaUsuario > len(jugadores[jugadorTurno]):
        print("No tienes esta ficha en la mano.")
        return False

    conjunto = int(input("Elige el conjunto del tablero en la que la quieres anadir: "))
    if conjunto > len(tablero):
        print("Este conjunto no se encuentra en el tablero.")
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
        fichaUsuario = int(input("Elige la ficha que quieres añadir. Si no quieres anadir mas, inserta 0: "))
        
        if fichaUsuario == 0:
            if len(nuevoConjunto) <= 2:
                print("El conjunto mínimo debe ser de 3 fichas.")
                cancelOpcion = input("¿Quieres cancelar la operación? (s/n)")

                if str(cancelOpcion).lower() == "s":
                    acabarMonton = True
                    jugadores[jugadorTurno].extend(nuevoConjunto)
                    nuevoConjunto.clear()


                elif str(cancelOpcion).lower() != "n" or str(cancelOpcion).lower() != "s":
                    print("Opción no válida.")

            else:
                acabarMonton = True
                tablero.append(nuevoConjunto)

        # Si el número indicado supera el índice de la mano, indica que no tiene la ficha y cierra el bucle
        elif fichaUsuario > len(jugadores[jugadorTurno]):
            print("No tienes esta ficha en la mano.")

        else:
            # Añade la ficha al conjunto y la elimina de la mano
            if len(nuevoConjunto) == 0:
                nuevoConjunto.append(jugadores[jugadorTurno][fichaUsuario - 1])
                jugadores[jugadorTurno].pop(fichaUsuario - 1)
                print("Ficha añadida con éxito!")
            else:
                if reglasOpcion3():
                    nuevoConjunto.append(jugadores[jugadorTurno][fichaUsuario - 1])
                    jugadores[jugadorTurno].pop(fichaUsuario - 1)
                    print("Ficha añadida con éxito!")
                else:
                    print("No se puede añadir esta ficha al conjunto.")

            print("Tu mano actual es:")
            print("-----------------")
            y = 1
            for ficha in manoJugador:
                print(f"{y}) {ficha}")
                y += 1
            print("")

            print(f"El conjunto que quieres anadir, por ahora, es: {nuevoConjunto}")

    return len(nuevoConjunto) != 0

# Función para acabar la partida
def finalPartida(jugador):
    print('¡ENHORABUENA!')
    print('El juego ha acabado porque te has quedado sin fichas.')
    print(f'El jugador{jugador + 1} es el ganador de esta partida.')


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

        # REGLA - TRÍOS
        correcto = False
        while not correcto:
            if colorFichaUsuario[0] in listaColoresTablero:
                print("Movimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario != numeroConjunto:
                print("Movimiento incorrecto, vuelve a probar.")
                return False

            else:
                correcto = True
                tablero[conjunto - 1].append(jugadores[jugadorTurno][fichaUsuario - 1])
                print("Ficha añadida!")
                return True
    else:
        # REGLA - ESCALERA
        correcto = False
        while correcto == False:
            if colorFichaUsuario != colorConjunto or numeroFichaUsuario != (listaNumerosTablero[-1] + 1) and  numeroFichaUsuario != (listaNumerosTablero[0] - 1):
                print("Movimiento incorrecto, vuelve a probar.")
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
        # REGLA - TRÍOS
        correcto = False
        while not correcto:
            if colorFichaUsuario[0] in listaColoresTablero:
                print("Movimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario != numeroConjunto:
                print("Movimiento incorrecto, vuelve a probar.")
                return False

            else:
                correcto = True
                return True
    else:
        # REGLA - ESCALERA
        correcto = False
        while not correcto:
            if colorFichaUsuario != colorConjunto or numeroFichaUsuario != (listaNumerosTablero[-1] + 1) and  numeroFichaUsuario != (listaNumerosTablero[0] - 1):
                print("Movimiento incorrecto, vuelve a probar.")
                return False

            elif numeroFichaUsuario == (listaNumerosTablero[0] - 1):
                correcto = True
                listaNumerosTablero.append(numeroFichaUsuario)
                listaNumerosTablero.sort()
                nuevoConjunto.insert(jugadores[jugadorTurno].pop(fichaUsuario - 1))

            else:
                correcto = True
                nuevoConjunto.append(jugadores[jugadorTurno].pop(fichaUsuario - 1))
        return correcto


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
primerTurno = True

# Dividimos el valor y el color de la ficha para hacer las comparaciones
splitFicha = fichasRummy[0].split(" ", 1)
color = splitFicha[0]
valorFicha = int(splitFicha[1])

# Booleano para detectar si puede pasar y si puede coger ficha, de esta manera en el
# menu se le mostrara o no la opcion
puedePasar = False
puedeCogerFicha = True

# Bucle princial:
while jugando:

    # Si no es el primer turno
    if not primerTurno:

        puedeCogerFicha = True
        puedePasar = False
        acabarAccion = False

        while not acabarAccion:

            # Muestra la mano y el tablero.
            mostrarMano(jugadorTurno, jugadores[jugadorTurno])
            mostrarTablero(tablero)

            # Mostrar las opciones que se pueden realizar
            mostrarTurno(puedePasar, puedeCogerFicha)

            accion = int(input(f"Elige una accion a realizar: "))
        
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
                print("Opcion no valida")

#Si es primer turno:        
    else:
        puedeCogerFicha = True
        puedePasar = False
        acabarAccion = False

        while not acabarAccion:
            # Muestra la mano y dibuja el tablero.
            mostrarMano(jugadorTurno, jugadores[jugadorTurno])
            mostrarTablero(tablero)

            # Mostrar las opciones que se pueden realizar
            mostrarTurno(puedePasar, puedeCogerFicha)
            accion = int(input(f"Elige una accion a realizar: "))

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
                    print("El valor de los conjuntos añadidos no es mayor de 30.")
                else:
                    acabarAccion = True
                    if partidaTurno == numJugadores:
                        primerTurno = False
            else:
                print("Opción no válida \n")

    if len(jugadores[jugadorTurno]) == 0: #Si la mano del jugador está vacía, se acaba el juego
        jugando = False

    else:
        # Pasar al siguiente turno
        jugadorTurno = jugadorTurno + 1
        
        if jugadorTurno == numJugadores:
            jugadorTurno = 0

        # Sumar 1 al turno de la partida
        partidaTurno += 1

finalPartida(jugadorTurno)