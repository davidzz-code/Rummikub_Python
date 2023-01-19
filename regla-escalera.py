# Regla  - Escalera mismo color
tablero = [['Rojo 4', 'Rojo 5', 'Rojo 6'], ['Azul 7', 'Negro 7', 'Naranja 7'], ['Negro 4', 'Negro 5', 'Negro 6', 'Negro 7', 'Negro 8', 'Negro 9']]

# Imprime la lista deseada en formato "num) ficha"
def tableroFunction(listaTablero):
    for i, ficha in enumerate(listaTablero, 1):
        print(f"{i}) {ficha}")


# Imprime tablero y preguntas para el usuario
tableroFunction(tablero)
ficha = input("¿Qué ficha quieres usar?: ")
conjunto = int(input("¿En qué conjunto la quieres colocar?: "))

# Crea una lista con el color y el número separados.
colorFichaUsuario = ficha.split(" ")

# Hace un cambio de tipo "string" a tipo "int" para los números y así poder usarlos como integers más adelante
numeroFichaUsuario = int(colorFichaUsuario.pop(1))


listaColoresTablero = []
listaNumerosTablero = []

for i in tablero[conjunto - 1]:
    colorConjunto = i.split(" ")
    numeroConjunto = int(colorConjunto.pop(1))
    listaColoresTablero.append(colorConjunto[0])
    listaNumerosTablero.append(numeroConjunto)


# Valora si es posible colocar la ficha en una escalera
correcto = False
while correcto == False:
    if colorFichaUsuario != colorConjunto or numeroFichaUsuario != (listaNumerosTablero[-1] + 1) and  numeroFichaUsuario != (listaNumerosTablero[0] - 1):
        print("Movimiento incorrecto, vuelve a probar.")
        ficha = input("¿Qué ficha quieres usar?: ")
        conjunto = int(input("¿En qué conjunto la quieres colocar?: "))

        colorFichaUsuario = ficha.split(" ")
        numeroFichaUsuario = int(colorFichaUsuario.pop(1))

        for i in tablero[conjunto - 1]:
            colorConjunto = i.split(" ")
            numeroConjunto = int(colorConjunto.pop(1))
            listaColoresTablero.append(colorConjunto[0])
            listaNumerosTablero.append(numeroConjunto)

    elif numeroFichaUsuario == (listaNumerosTablero[0] - 1):
        correcto = True
        listaNumerosTablero.append(numeroFichaUsuario)
        listaNumerosTablero.sort()
        tablero[conjunto - 1].insert(0, ficha)
        tableroFunction(tablero)
        
    else:
        correcto = True
        tablero[conjunto - 1].append(ficha)
        tableroFunction(tablero)
