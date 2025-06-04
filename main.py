import pygame
import sys
import os

# Инициализация
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame: Движение вручную с изображением")

# Цвет фона
BACKGROUND_COLOR = (30, 30, 30)

# Загрузка изображения
# Предполагаем, что в папке рядом с файлом есть файл "character.png"
image_path = os.path.join(os.path.dirname(__file__), "character.png")
if not os.path.exists(image_path):
    print("❌ Файл character.png не найден рядом со скриптом!")
    pygame.quit()
    sys.exit()

character = pygame.image.load(image_path)
character = pygame.transform.scale(character, (64, 64))  # масштабирование

# Позиция и скорость
x, y = WIDTH // 2, HEIGHT // 2
speed = 5

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление с клавиатуры
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < WIDTH - 64:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < HEIGHT - 64:
        y += speed

    # Отображение изображения
    screen.blit(character, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
