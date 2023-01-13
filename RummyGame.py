
def conjuntoFichas():
    fichas = []

    colores = ["Naranja", "Azul", "Negro", "Rojo"]
    valores = [1,2,3,4,5,6,7,8,9,10,11,12,13]

    for color in colores:
        for valor in valores:
            fichaVal = "{} {}".format(color, valor)
            fichas.append(fichaVal)
    print(fichas)
    return fichas

conjuntoFichas()