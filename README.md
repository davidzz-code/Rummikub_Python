- [Documento IDC](#documento-idc)
  - [Reglamento de Rummikub](#reglamento-de-rummikub)
    - [Especificaciones](#especificaciones)
    - [Componentes](#componentes)
    - [Preparación](#preparación)
    - [Reglas del juego](#reglas-del-juego)
    - [Juego](#juego)
- [Documento TEP](#documento-tep)
  - [Menú principal](#menú-principal)
  - [Menú de pausa](#menú-de-pausa)

# Documento IDC

## Reglamento de Rummikub

### Especificaciones

- Número de jugadores: Mínimo 2, máximo 4.
- Duración aproximada: 45 minutos.
- Edad mínima recomendada: 8 años.

### Componentes

- 106 fichas (8 conjuntos de fichas numeradas del 1-13 en 4 colores y 2 comodines).
- 4 soportes.
- Patas de soporte.
- Reglas del juego.

### Preparación

1. Adquirimos el juego de mesa "Rummikub".
2. Extraemos los componentes pertenecientes al juego.
3. Volteamos y mezclamos las fichas.
4. Reagrupamos y amontonamos las fichas.
5. Proveemos a cada jugador 14 fichas.
6. Cada jugador extrae una ficha de las amontonadas para determinar el primer turno.

### Reglas del juego

#### **Conjuntos**: Los conjuntos son aquellas fichas que se pueden juntar y jugar en el tablero. Hay dos tipos de conjuntos

- **Mismo número, diferentes colores**: Este conjunto se basa en juntar fichas las cuales coincidan en su número, pero no en su color. Ejemplo: 12 azul, 12 naranja, 12 negro, 12 rojo.
- **Números consecutivos, mismo color**: Este conjunto se basa en juntar fichas consecutivas respecto a su número e iguales en su color. Ejemplo: 1 azul, 2 azul, 3 azul, 4 azul.

##### **Movimiento inicial**: El movimiento inicial lo hace el primer jugador (si no puede hacerlo, se le encarga al siguiente jugador), a partir de el movimiento inicial, los jugadores jugarán su turno en sentido horario. Además, el movimiento inicial debe estar compuesto por un total de 30 puntos, en un conjunto o en varios

##### **Turno**: El turno de cada jugador tiene un tiempo límite de 2 minutos. Se tiene que jugar uno o varios conjuntos y, en caso de no poder jugar ningún conjunto, se deberá coger una ficha de las amontonadas. Se pueden dividir fichas individuales del tablero para realizar tu propio conjunto

##### **Final**: El juego lo gana el jugador que se quede sin fichas en su soporte

### Juego

1. El primer jugador hace el movimiento inicial.
2. El siguiente jugador intenta realizar un conjunto, con sus piezas o dividiendo las que hay en el tablero.
3. Se sigue consecutivamente hasta que se finalice el juego.

# Documento TEP

## Menú principal

``` python
# Importa la librería de Pygame
import pygame

# Inicializa Pygame
pygame.init()

# Crea la paleta de colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
soft_blue = (133, 193, 233)

# Obtiene medidas de la pantalla
screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

# Crea la ventana con el tamaño de pantalla obtenido
screen = pygame.display.set_mode(screen_size)

# Crea el fondo
screen.fill(soft_blue)

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

# Crea un botón que servirá para abrir el menu de pausa
button_font_1 = pygame.font.Font(None, 50)
button_text_1 = button_font.render("Menú de pausa ", 1, (0, 0, 0))
button_rect_1 = button_text.get_rect()
button_rect_1.center = (1800, 50)

#Crea un botón que servirá para cerrar el menu de pausa
button_font_2 = pygame.font.Font(None, 50)
button_text_2 = button_font.render("Cerrar ", 1, (0, 0, 0))
button_rect_2 = button_text.get_rect()
button_rect_2.center = (1800, 50)

# Dibuja el botón por pantalla
screen.blit(button_text, button_rect)
screen.blit(button_text_1, button_rect_1)

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

## Menú de pausa

1. Dentro del bucle principal, añadir una condición para la creación del menú de pausa.
2. **Crear el menú**:

- Definir una variable para cargar las imágenes que queramos para el menú.
- Definir variables para ubicar las imágenes en el menú de pausa.
- Añadir las condiciones al bucle después del menú de pausa con los botones y sus funciones.

3. **Crear menú de opciones en el bucle**

- Ubicar mediante condiciones las diferentes opciones
Crear un botón para volver al menú principal.
