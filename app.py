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
drops = [0] * columns

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    for i in range(len(drops)):
        if random.random() > 0.13:
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            text = font.render(char, True, green)
            screen.blit(text, (i * font_size, drops[i] * font_size))

        if drops[i] * font_size > height and random.random() > 0.975:
            drops[i] = 0

        drops[i] += 1

    pygame.display.flip()
    pygame.time.delay(50)
