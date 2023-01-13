import random

def conjuntoFichas():
    fichas = []

    colores = ["Naranja", "Azul", "Negro", "Rojo"]
    valores = [1,2,3,4,5,6,7,8,9,10,11,12,13]

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
    print(fichas)
    return fichas

fichasRummy = conjuntoFichas()
fichasRummy = shuffleFichas(fichasRummy)

