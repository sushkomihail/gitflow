import time

import pygame

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Желтый круг')
    size = width, height = 800, 400
    screen = pygame.display.set_mode(size)

    running = True
    v = 10  # пикселей в секунду
    fps = 60
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('blue'))
    do_draw = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(pygame.Color('blue'))
                pos = event.pos
                r = 1
                do_draw = True
        if do_draw:
            pygame.draw.circle(screen, pygame.Color('yellow'), pos, r)
            r += v / fps 
            clock.tick(fps)
            pygame.display.flip()
    pygame.quit()