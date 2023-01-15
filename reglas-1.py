# Regla  - Escalera mismo color
tablero = []

sublista1 = ['Rojo 4', 'Rojo 5', 'Rojo 6']
tablero.append(sublista1)

sublista2 = ['Azul 7', 'Negro 7', 'Naranja 7']
tablero.append(sublista2)

sublista3 = ['Rojo 4', 'Rojo 5', 'Rojo 6', 'Rojo 7', 'Rojo 8', 'Rojo 9']
tablero.append(sublista3)


# Imprime la lista deseada en formato "num) ficha"
def tableroFunction(listaTablero):
    for i, ficha in enumerate(listaTablero, 1):
        print(f"{i}) {ficha}")

tableroFunction(tablero)
ficha = input("¿Qué ficha quieres usar?: ")
posicion = int(input("¿En qué posición la quieres colocar?: "))

while " " in ficha:
    fichasSeparadas = ficha.split(" ")
    tableroSeparado = sublista1[-1].split(" ")
    numeroEscalera = int(tableroSeparado.pop(1))
    numeroFicha = int(fichasSeparadas.pop(1))

# Valora si es posible colocar la ficha en una escalera
# Se puede quitar los dos elif que están comentados pero ahora mismo te dice en qué está el fallo, si el NUMERO o el COLOR
    if posicion == 1:
        if fichasSeparadas[0] != tableroSeparado[0] or numeroFicha != (numeroEscalera + 1):
            print("Incorrecto, ni el NÚMERO y ni el COLOR coinciden. Vuelve a probar.")
            posicion = int(input("¿En qué posición la quieres colocar?: "))
        # elif fichasSeparadas[0] == tableroSeparado[0] and numeroFicha != (numeroEscalera + 1):
        #     print("Incorrecto, tienes un fallo en el NÚMERO. Vuelve a probar.")
        #     posicion = int(input("¿En qué posición la quieres colocar?: "))
        # elif fichasSeparadas[0] != tableroSeparado[0] and numeroFicha == (numeroEscalera + 1):
        #     print("Incorrecto, tienes un fallo en el COLOR. Vuelve a probar.")
        #     posicion = int(input("¿En qué posición la quieres colocar?: "))
        else:
            sublista1.append(ficha)
            tableroFunction(tablero)
    elif posicion == 2:
        print("hola")
    elif posicion == 3:
        print("hola")
    break










# Regla - Tríos mismo número