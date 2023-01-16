# Regla  - Escalera mismo color
tablero = []
correcto = "no"

################ DUDA: He pensado que el tablero será una lista de listas. Así podemos imprimir cada conjunto en cada fila.
# La duda es si esa sublista será una variable siempre con el mismo nombre o serán distinta sublistas?
# Básicamente los problemas son: 
#       En caso de tener una variable sola. Se vacía para poner la nueva lista de conjuntos, 
#       pero no podremos accder a la primera lista de conjuntos ya que esa lista se va sobreescribiendo

#       Por lo que he pensado que lo ideal sería que cada sublista tenga un nombre distinto para 
#       poder acceder siempre que queramos a cualquier conjunto de fichas
#           Problema de varios nombres es que hay que programar que se cree una nueva lista con un nombre que vaya cambiando 
#           (igual basta con una palabra que se quede fija y un número al final que se itere siempre que se añada un conjunto 
#           nuevo a una fila nueva)
# 
# Todo esto sería para la parte de tablero 
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

# Este bucle crea una lista con el color y el número separados.

fichasSeparadas = ficha.split(" ")
tableroSeparado1 = sublista1[-1].split(" ")
tableroSeparado2 = sublista2[-1].split(" ")
tableroSeparado3 = sublista3[-1].split(" ")

    # Hace un cambio de tipo "string" a tipo "int" para los números y así poder usarlos como integers más alante
numeroEscalera1 = int(tableroSeparado1.pop(1))
numeroEscalera2 = int(tableroSeparado2.pop(1))
numeroEscalera3 = int(tableroSeparado3.pop(1))
numeroFicha = int(fichasSeparadas.pop(1))


# Valora si es posible colocar la ficha en una escalera

##### Arreglar que se queda pillado en "movimiento incorrecto"
while correcto == "no":
    if posicion == 1:
        if fichasSeparadas[0] != tableroSeparado1[0] or numeroFicha != (numeroEscalera1 + 1):
            correcto = "no"
            print("Movimiento incorrecto, vuelve a probar.")
            ficha = input("¿Qué ficha quieres usar?: ")
            posicion = int(input("¿En qué posición la quieres colocar?: "))
        else:
            correcto = "si"
            sublista1.append(ficha)
            tableroFunction(tablero)

    elif posicion == 2:
        if fichasSeparadas[0] != tableroSeparado2[0] or numeroFicha != (numeroEscalera2 + 1):
            correcto = "no"
            print("Movimiento incorrecto, vuelve a probar.")
            ficha = input("¿Qué ficha quieres usar?: ")
            posicion = int(input("¿En qué posición la quieres colocar?: "))
        else:
            correcto = "si"
            sublista2.append(ficha)
            tableroFunction(tablero)

    elif posicion == 3:
        if fichasSeparadas[0] != tableroSeparado3[0] or numeroFicha != (numeroEscalera3 + 1):
            correcto = "no"
            print("Movimiento incorrecto, vuelve a probar.")
            ficha = input("¿Qué ficha quieres usar?: ")
            posicion = int(input("¿En qué posición la quieres colocar?: "))
        else:
            correcto = "si"
            sublista3.append(ficha)
            tableroFunction(tablero)

# Regla - Tríos mismo número