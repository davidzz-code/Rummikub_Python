import pygame

# Inicializa Pygame
pygame.init()

# Obtiene el tamaño de la pantalla
screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

# Crea la ventana con el tamaño de pantalla obtenido
screen = pygame.display.set_mode(screen_size)

# Establece el fondo de la ventana en negro
screen.fill((0, 0, 0))

# Actualiza la ventana para que se muestre en pantalla
pygame.display.flip()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Cierra Pygame al finalizar el juego
pygame.quit()
