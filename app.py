import pygame
import random
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aurebesh Matrix")

font_size = 20
font = pygame.font.Font("Aurebesh.otf", font_size)

black = (0, 0, 0)
green = (0, 255, 0)

columns = width // font_size
drops = [[] for _ in range(columns)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    for i in range(len(drops)):
        if random.random() > 0.9:  # Adjust this value for density
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            speed = random.randint(1, 5)
            drops[i].append((char, 0, speed))

        for j in range(len(drops[i])):
            char, y, speed = drops[i][j]
            text = font.render(char, True, green)
            screen.blit(text, (i * font_size, y * font_size))
            drops[i][j] = (char, y + speed, speed)

        drops[i] = [drop for drop in drops[i] if drop[1] * font_size < height]

    pygame.display.flip()
    pygame.time.delay(50)
