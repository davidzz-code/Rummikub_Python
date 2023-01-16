tablero = []
posicion = []

fichaEscogida = int(input("¿Qué primera ficha quieres escoger? "))
fichaEscogida2 = int(input("¿Qué segunda ficha quieres escoger? "))
fichaEscogida3 = int(input("¿Qué tercera ficha quieres escoger? "))

def mayorDe30(fichaEscogida, fichaEscogida2, fichaEscogida3):
    listaValorFicha = []

    listaValorFicha.append(fichaEscogida)
    listaValorFicha.append(fichaEscogida2)
    listaValorFicha.append(fichaEscogida3)

    sumValorFicha = sum(listaValorFicha)

    if sumValorFicha >= 30:
        posicion.append(fichaEscogida)
        posicion.append(fichaEscogida2)
        posicion.append(fichaEscogida3)

    else:
        while sumValorFicha < 30:
            print("La suma de esos valores no es mayor que 30. Debes escoger otras fichas.")
            fichaEscogida = int(input("Escoge otra primera ficha: "))
            fichaEscogida2 = int(input("Escoge otra segunda ficha: "))
            fichaEscogida3 = int(input("Escoge otra tercera ficha: "))

    tablero.append(posicion)
    print(tablero)

mayorDe30(fichaEscogida, fichaEscogida2, fichaEscogida3)

