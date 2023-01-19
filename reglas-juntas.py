# Regla - Tríos mismo número
tablero = [['Rojo 4', 'Rojo 5', 'Rojo 6'], ['Azul 7', 'Negro 7', 'Naranja 7'], ['Negro 4', 'Negro 5', 'Negro 6', 'Negro 7', 'Negro 8', 'Negro 9']]

# Imprime la lista deseada en formato "num) ficha"
def tableroFunction(listaTablero):
    for i, ficha in enumerate(listaTablero, 1):
        print(f"{i}) {ficha}")

tableroFunction(tablero)
ficha = input("¿Qué ficha quieres usar?: ")
conjunto = int(input("¿En qué conjunto la quieres colocar?: "))

# Este bucle crea una lista con el color y el número separados.
colorFichaUsuario = ficha.split(" ")

# Hace un cambio de tipo "string" a tipo "int" para los números y así poder usarlos como integers más alante
numeroFichaUsuario = int(colorFichaUsuario.pop(1))

listaColoresTablero = []
listaNumerosTablero = []

for i in tablero[conjunto - 1]:
    colorConjunto = i.split(" ")
    numeroConjunto = int(colorConjunto.pop(1))
    listaColoresTablero.append(colorConjunto[0])
    listaNumerosTablero.append(numeroConjunto)


# Valora si es posible colocar la ficha en un trío

##### Arreglar que se queda pillado en "movimiento incorrecto"
correcto = False


if listaNumerosTablero[0] == listaNumerosTablero[1]:
    # Tríos
    while correcto == False:
        if colorFichaUsuario[0] in listaColoresTablero:
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


        elif numeroFichaUsuario != numeroConjunto:
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


        else:
            correcto = True
            tablero[conjunto - 1].append(ficha)
            tableroFunction(tablero)
            print("Ficha añadida con éxito!")
else:
    # Escalera
    correcto = False
    while correcto == False:
        if colorFichaUsuario != colorConjunto or numeroFichaUsuario != (numeroConjunto + 1):
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
        else:
            correcto = True
            tablero[conjunto - 1].append(ficha)
            tableroFunction(tablero)

