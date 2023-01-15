print(".....:¡Bienvenido a Rummikub!:.....")
print("Para empezar el juego escribe 'jugar'")
print("Para salir del juego escribe 'salir' en cualquier momento")
print()

manoFichasJugador = ['Rojo 1', 'Rojo 4', 'Negro 10', 'Azul 1', 'Azul 2', 'Azul 3', 'Azul 4', 'Azul 5', 'Azul 8', 'Negro 13', 'Naranja 11', 'Rojo 2']
numeros = "1234567890"
menu = input("Escribe 'jugar' cuando estés listo/a: ")


# Menú principal del juego
while menu != "salir":
    print("Tablero:")
    # FUNCION TABLERO
    print("******************************+")
    print()

    print("Tus fichas son:")
    #FUNCION FICHAS USUARIO REPARTIRDAS
    for i, ficha in enumerate(manoFichasJugador, 1):
        print(f"{i}) {ficha}")
    print()
    
        ####### NO FUNCIONA #######
    # # PROBANDO IMPRIMIR LA FICHA SELECCIONADA POR EL JUGADOR
    # # Y DELIMITANDO OPCIONES SI EL USUARIO ESCRIBE LETRAS EN LUGAR DE NUMEROS

    # menu = int(input("¿Qué ficha quieres usar?: "))
    # while menu >= 1 and menu <= 50:
    #     for i in range(len(manoFichasJugador) + 1):
    #         if menu == i:
    #             # menu = int(menu)
    #             fichaJugador = manoFichasJugador[menu - 1]
    #             print(f"La ficha es: {fichaJugador}")
    #     if menu > i:
    #         menu = int(input("Incorrecto, vuelve a probar"))











    # fichaJugador = input("¿Que ficha quieres usar?: ")
    # while fichaJugador != "salir":
    #     if fichaJugador in numeros:
    #         fichaJugador = int(fichaJugador)
    #         print("El número es: ", fichaJugador)
    #     else:
    #         print("Incorrecto, vuelve a intentarlo.")
    #     print()

    # menu = int(input("¿En que posición del tablero quieres ponerla?: "))
    

print("¡Gracias por jugar! Vuelve pronto.")