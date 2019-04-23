import pygame
import math
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
done = False
screen.fill((255, 255, 255))
width = 1
previous_mouse_pos = [0, 0]
current_mouse_pos = [0, 0]
color_wheel = pygame.image.load("color_wheel.png").convert_alpha()
color = (0, 0, 0)
print(color_wheel.get_rect())

while not done:
    screen.blit(color_wheel, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
            # print(event)
            if event.buttons[0]:
                previous_mouse_pos = current_mouse_pos
                current_mouse_pos = event.pos
                pygame.draw.line(screen, color, previous_mouse_pos, current_mouse_pos, width)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            previous_mouse_pos = current_mouse_pos = event.pos
            if math.sqrt((current_mouse_pos[0] - 110) ** 2 + (current_mouse_pos[1] - 110) ** 2) < 110:
                color = screen.get_at(current_mouse_pos)
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_UP:
                width += 1
            elif event.key == pygame.K_DOWN:
                if width > 1:
                    width -= 1
            elif event.key == pygame.K_SPACE:
                screen.fill((255, 255, 255))


    pygame.display.flip()
