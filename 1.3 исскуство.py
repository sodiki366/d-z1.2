#
from all_colors import *
import random
import pygame
import pygame.mixer
pygame.init()
pygame.mixer.init()
# pygame.mixer.music.load('resurs/La La Land.mp3')
# pygame.mixer.music.play(-1)

size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
COLORS = [RED,GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN , PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
BACKGROUND = (255, 255, 255)
screen.fill(BACKGROUND)


FPS = 60
clock = pygame.time.Clock()


running = True

while running:
    #Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Основная логика игры
    BACKGROUND = random.choice(COLORS)

    # Отрисовка объектов
    x = random.randint(0,1280)
    y = random.randint(0,720)
    COLOR = random.choice(COLORS)
    radius = random.randint(0,100)

    pygame.draw.ellipse(screen, COLOR, (x,y,radius))

    screen.fill(BACKGROUND)#очистка экрана







    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()