import pygame, random, os

pygame.init()

screen = pygame.display.set_mode((800, 600))

def fichas():
    # Guarda la ruta de las imagenes en variables
    carpetaFichas = "resources/Fichas"
    archivosFichas = os.listdir(carpetaFichas)

    # Coordenadas iniciales de las fichas
    x = 0
    y = 0

    # Crea un diccionario que asocia las imagenes con su valor
    fichas = {}
    for archivo in archivosFichas:
        if archivo.endswith(".png"):
            imagen = pygame.image.load(os.path.join(carpetaFichas, archivo))
            color = archivo.split("-")[0]
            numero = archivo.split("-")[1].split(".")[0]
            fichas[(int(numero), color)] = imagen

    # Dibujar 14 fichas random
    fichas_keys = list(fichas.keys())
    random.shuffle(fichas_keys)
    
    for key in fichas_keys:
        screen.blit(fichas[key], (x,y))
        x += 70

    pygame.display.update()

while True:
    screen.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.sys.exit()
    fichas()
    pygame.display.flip()