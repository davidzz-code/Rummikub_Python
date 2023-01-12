import pygame, random, os

pygame.init()

screen = pygame.display.set_mode((800, 600))

def fichas():
    # Guarda la ruta de las imagenes en variables
    carpetaFichas = "resources/Fichas"
    archivosFichas = os.listdir(carpetaFichas)

    # Coordenadas iniciales de las fichas
    x = 10
    y = 20

    # Crea un diccionario que asocia las imagenes con su valor
    fichas = {}
    for archivo in archivosFichas:
        if archivo.endswith(".png"):
            imagen = pygame.image.load(os.path.join(carpetaFichas, archivo))
            color = archivo.split("-")[0]
            numero = archivo.split("-")[1].split(".")[0]
            fichas[(int(numero), color)] = imagen

    # Variables para recorrer
    colores = ["Azul", "Rojo", "Negro", "Naranja"]
    numeros = list(range(1, 14))

    # Recorre las variables anteriores e imprime cada ficha
    for color in colores:
        color_select = color
        for numero in numeros:
            numero_select = numero
            screen.blit(fichas[(numero_select, color_select)], (x, y)) 
            x += 13
            y += 5

    # Actualiza la pantalla
    pygame.display.update()

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.sys.exit()
    fichas()
    pygame.display.flip()