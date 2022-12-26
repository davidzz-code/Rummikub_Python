# Rummikub_Python

# Documento IDC

## Reglamento de Rummikub

### Especificaciones:
```
Número de jugadores: Mínimo 2, máximo 4.
Duración aproximada: 45 minutos.
Edad mínima recomendada: 8 años.
```

### Componentes:
```
- 106 fichas (8 conjuntos de fichas numeradas del 1-13 en 4 colores y 2 comodines).
- 4 soportes.
- Patas de soporte.
- Reglas del juego.
```

### Preparación:
```
1.1 Adquirimos el juego de mesa "Rummikub".
1.2 Extraemos los componentes pertenecientes al juego.
1.3 Volteamos y mezclamos las fichas.
1.4 Reagrupamos y amontonamos las fichas.
1.5 Proveemos a cada jugador 14 fichas.
1.6 Cada jugador extrae una ficha de las amontonadas para determinar el primer turno.
```

### Reglas del juego:

##### **Conjuntos**: Los conjuntos son aquellas fichas que se pueden juntar y jugar en el tablero. Hay dos tipos de conjuntos:

- **Mismo número, diferentes colores**: Este conjunto se basa en juntar fichas las cuales coincidan en su número, pero no en su color. Ejemplo: 12 azul, 12 naranja, 12 negro, 12 rojo.
- **Números consecutivos, mismo color**: Este conjunto se basa en juntar fichas consecutivas respecto a su número e iguales en su color. Ejemplo: 1 azul, 2 azul, 3 azul, 4 azul.

##### **Movimiento inicial**: El movimiento inicial lo hace el primer jugador (si no puede hacerlo, se le encarga al siguiente jugador), a partir de el movimiento inicial, los jugadores jugarán su turno en sentido horario. Además, el movimiento inicial debe estar compuesto por un total de 30 puntos, en un conjunto o en varios.

##### **Turno**: El turno de cada jugador tiene un tiempo límite de 2 minutos. Se tiene que jugar uno o varios conjuntos y, en caso de no poder jugar ningún conjunto, se deberá coger una ficha de las amontonadas. Se pueden dividir fichas individuales del tablero para realizar tu propio conjunto.
##### **Final**: El juego lo gana el jugador que se quede sin fichas en su soporte.

### Juego
```
2.1 El primer jugador hace el movimiento inicial.
2.2 El siguiente jugador intenta realizar un conjunto, con sus piezas o dividiendo las que hay en el tablero.
2.3 Se sigue consecutivamente hasta que se finalice el juego.
```

# Documento TEP:
```
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
```
