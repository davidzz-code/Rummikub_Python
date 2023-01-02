import pygame, sys

pygame.init()

#################### PANTALLA ####################
screen_size = (1000, 665)
screen = pygame.display.set_mode(screen_size)

# Crea una fuente para escribir texto en la pantalla
font = pygame.font.Font(None, 70)

run = True

def main_menu(): # Menu principal
    pygame.display.set_caption('Menu')

    while run:
        # Crea el mensaje que quieras dibujar por pantalla
        message_font = "Menú principal"
        text_font = font.render(message_font, 1, (255, 175, 230))
        screen.blit(text_font, (100, 100))

        # Crea un botón que servirá para comenzar el juego
        button_font = pygame.font.Font(None, 50)
        button_text = button_font.render("Comenzar a jugar ", 1, (80, 100, 255))
        button_rect = button_text.get_rect()
        button_rect.center = (600, 300)

        # Dibuja el botón por pantalla
        screen.blit(button_text, button_rect)

        # Actualiza la pantalla para mostrar los cambios
        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        play()

def play(): # Pantalla de juego

    rectangle = pygame.rect.Rect(200, 134, 65, 80)
    rectangle_draging = False
    WHITE   = (255,255,255)
    FPS = 144
    clock = pygame.time.Clock()
    bg = pygame.image.load("bg.jpg")


    while run:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
    
            screen.blit(bg, (0, 0))
            pygame.draw.rect(screen, WHITE, rectangle)
            pygame.display.flip()
            clock.tick(FPS)


main_menu()

