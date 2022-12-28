# Importa la librería de Pygame
import pygame

# Inicializa Pygame
pygame.init()

# Obtiene medidas de la pantalla
screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

# Crea la ventana con el tamaño de pantalla obtenido
screen = pygame.display.set_mode(screen_size)

# Crea una fuente para escribir texto en la pantalla
font = pygame.font.Font(None, 70)

# Crea el mensaje que quieras dibujar por pantalla
message_font = "Menú principal"
text_font = font.render(message_font, 1, (255, 175, 230))
screen.blit(text_font, (200, 300))

# Crea un botón que servirá para comenzar el juego
button_font = pygame.font.Font(None, 50)
button_text = button_font.render("Comenzar a jugar ", 1, (80, 100, 255))
button_rect = button_text.get_rect()
button_rect.center = (700, 650)

# Dibuja el botón por pantalla
screen.blit(button_text, button_rect)

# Actualiza la pantalla para mostrar los cambios
pygame.display.flip()

# Crea un bucle para controlar los eventos del menú principal
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                text_font = font.render("¡Ha empezado el juego!", 1, (100, 255, 70))
                screen.blit(text_font, (450, 400))
                pygame.display.flip()

# Cierra Pygame al finalizar el juego
pygame.quit()
