import pygame, os, random

pygame.init()

width = 600
height = 800
screen = pygame.display.set_mode((height, width))


def fichas():
    # Guarda la ruta de las imagenes en variables
    carpetaFichas = "resources/Fichas"
    archivosFichas = os.listdir(carpetaFichas)

    # Crea un diccionario que asocia las imagenes con su valor
    fichas = {}
    for archivo in archivosFichas:
        if archivo.endswith(".png"):
            imagen = pygame.image.load(os.path.join(carpetaFichas, archivo))
            color = archivo.split("-")[0]
            numero = archivo.split("-")[1].split(".")[0]
            fichas[(int(numero), color)] = imagen

    fichas_keys = random.sample(list(fichas.keys()), 14) # Select 14 random keys

    x, y = 0, 0 # initialize x and y coordinates for the tile's position

    for key in fichas_keys:
        screen.blit(fichas[key], (x,y))
        x += 70
        if x > width-70:  # if x exceeds the width of the screen, move to the next row
            x = 0
            y += 110

fichas()

pygame.display.flip()

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.sys.exit()

