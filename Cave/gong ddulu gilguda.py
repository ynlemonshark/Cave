import pygame
import sys
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((1000,1000))
FPSCLOCK = pygame.time.Clock()

gold = (255, 191, 0)


def main():
    xpos = 500
    ypos = 0
    gravity = 1
    acceleration = 1
    height = 800
    mitigation = 10
    rebound = 0
    falling = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            SURFACE.fill((255, 255, 0))

            pygame.draw.ellipse(SURFACE, gold, (xpos - 50,ypos - 50, 50, 50))

            if falling:
                acceleration += acceleration * gravity + gravity
                height -= acceleration
                if height <= 0:
                    height = 0
                    rebound = round(acceleration / mitigation, -1)
                    falling = False
                ypos = 1000 - height

            else:
                acceleration -= rebound * gravity + gravity * 10
                rebound -= round(rebound / 2, -1)
                height += round(acceleration / 10, -1)
                if rebound <= 1:
                    height = 0
                    falling = True
                ypos = 1000 - height

            print(height)

            pygame.display.update()
            FPSCLOCK.tick(50)

if __name__ == '__main__':
    main()