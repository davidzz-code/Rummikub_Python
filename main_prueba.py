import pygame, sys, os

pygame.init()

# Tamaño de pantalla
screen_size = (1000, 665)
screen = pygame.display.set_mode(screen_size)

# Paleta de colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
soft_blue = (133, 193, 233)

# Variables
FPS = 25
clock = (
    pygame.time.Clock()
)  # Creación de una variable "clock" para ajustar la velocidad de las imágenes
bg = pygame.image.load(
    os.path.join("Python", "Rummikub_Python", "resources", "bg.jpg")
)  # fondo del juego

# Crea una fuente para escribir texto en la pantalla
font = pygame.font.SysFont("Helvetica", 70)
run = True


def main_menu():  # Menu principal
    pygame.display.set_caption("Rummikub")  # Título de la ventana

    while run:
        # Crea el mensaje que quieras dibujar por pantalla
        message_font = "Menú principal"
        text_font = font.render(message_font, 1, (255, 175, 230))
        screen.blit(text_font, (100, 100))

        # Crea un botón que servirá para comenzar el juego
        button_font = pygame.font.SysFont("arial", 50)
        button_text = button_font.render("Comenzar a jugar ", 1, (80, 100, 255))
        button_rect = button_text.get_rect()
        button_rect.center = (600, 300)

        # Dibuja el botón por pantalla
        screen.blit(button_text, button_rect)

        # Actualiza la pantalla para mostrar los cambios
        pygame.display.flip()

        # bucle principal para salir de la pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Acceder al juego tras pulsar el botón
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    play()


def play():  # Pantalla de juego
    # Creación de un rectángulo
    rectangle = pygame.rect.Rect(200, 134, 65, 80)
    rectangle_draging = False

    # Bucle principal
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ####### Inicio condiciones Dragging #######
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rectangle.collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.x - mouse_x
                        offset_y = rectangle.y - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_draging = False

            elif event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle.x = mouse_x + offset_x
                    rectangle.y = mouse_y + offset_y
            ####### Final condiciones Dragging #######

            screen.blit(bg, (0, 0))
            pygame.draw.rect(screen, white, rectangle)
            pygame.display.flip()
            clock.tick(FPS)


main_menu()
