from all_colors import *
import random
import pygame
import pygame.mixer

# Инициализация Pygame
pygame.init()
pygame.mixer.init()

# Загрузка и воспроизведение музыки
pygame.mixer.music.load('La La Land.mp3')
pygame.mixer.music.play(-1)

# Настройка окна
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Список цветов
COLORS = [RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY, ORANGE, PINK, BROWN, PURPLE, LIME, NAVY, OLIVE, MAROON, TEAL, SILVER, GOLD]
BACKGROUND = (255, 255, 255)  # Белый фон
screen.fill(BACKGROUND)

# Список для хранения кругов
circles = []
circle_timer = 0  # Таймер для обновления кругов

# Настройка FPS
FPS = 60
clock = pygame.time.Clock()

# Основной игровой цикл
running = True
while running:
    # Обработка событий игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Основная логика игры
    circle_timer += clock.get_time()
    if circle_timer >= 1000:  # 1000 миллисекунд = 1 секунда
        circle_timer = 0  # Сброс таймера
        circles.clear()  # Очистка старых кругов

        # Генерация нового фона
        BACKGROUND = random.choice(COLORS)

        # Генерация случайного количества кругов
        num_circles = random.randint(10, 100)  # Рандомное количество кругов от 1 до 10
        for _ in range(num_circles):
            x = random.randint(0, 1280)  # Случайная позиция по X
            y = random.randint(0, 720)   # Случайная позиция по Y
            COLOR = random.choice(COLORS)  # Случайный цвет
            radius = random.randint(10, 100)  # Случайный радиус
            circles.append((x, y, COLOR, radius))  # Добавление круга в список

    # Очистка экрана
    screen.fill(BACKGROUND)

    # Отрисовка кругов
    for circle in circles:
        x, y, COLOR, radius = circle
        pygame.draw.circle(screen, COLOR, (x, y), radius)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(FPS)

# Завершение программы
pygame.quit()