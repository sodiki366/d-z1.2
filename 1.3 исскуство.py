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
circles = []
circle_timer = 0

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
    circle_timer += clock.get_time()
    if circle_timer >= 1000:  # 1000 миллисекунд = 1 секунда
        circle_timer = 0
        num_circles = random.randint(1, 10)  # Рандомное количество кругов от 1 до 10
        for _ in range(num_circles):
            x = random.randint(0, 1280)
            y = random.randint(0, 720)
            COLOR = random.choice(COLORS)
            radius = random.randint(10, 100)  # Минимальный радиус 10, чтобы круги были видимыми
            circles.append((x, y, COLOR, radius))

    # Отрисовка объектов
    x = random.randint(0,1280)
    y = random.randint(0,720)
    COLOR = random.choice(COLORS)
    radius = random.randint(0,100)
    num_circles = random.randint(10, 100)

    pygame.draw.ellipse(screen, COLOR, (x,y,radius),num_circles)

    screen.fill(BACKGROUND)#очистка экрана







    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()