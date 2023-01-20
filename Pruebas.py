
tablero = [["Rojo 2", "Rojo 3", "Azul 2"], ["Negro 12", "Naranja 13"], ["Negro 2", "Verde 2"]]

def mostrarTablero(tablero):
    numero = 0
    for i in tablero:
        numero += 1
        print(numero,")",", ".join(i))

mostrarTablero(tablero)