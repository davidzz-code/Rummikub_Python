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
                screen.fill((0, 0, 255))

                # Set the number of rows and columns in the grid
                rows = 10
                cols = 10

                # Set the size of each cell in the grid
                cell_size = 50

                # Calculate the total width and height of the grid
                grid_width = cols * cell_size
                grid_height = rows * cell_size

                # Calculate the center position of the screen
                screen_center_x = screen_size[0] // 2
                screen_center_y = screen_size[1] // 2

                # Calculate the top left corner position of the grid
                grid_x = screen_center_x - grid_width // 2
                grid_y = screen_center_y - grid_height // 2

                for row in range(rows):
                    for col in range(cols):
                        x = col * cell_size + grid_x
                        y = row * cell_size + grid_y
                        rect = pygame.Rect(x, y, cell_size, cell_size)
                        pygame.draw.rect(screen, (255, 255, 255), rect, 1)
                pygame.display.flip()

# Cierra Pygame al finalizar el juego
pygame.quit()
