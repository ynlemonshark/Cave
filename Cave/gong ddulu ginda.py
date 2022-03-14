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
    bounce = 5
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
                height -= gravity * acceleration
                if height <= 0:
                    height = 0
                    falling = False
                    rebound = acceleration * gravity
                ypos = 1000 - height

            else:
                rebound -= gravity * bounce
                acceleration = rebound
                height += acceleration
                if rebound <= 0:
                    rebound = 0
                    acceleration = 0
                    falling = True
                ypos = 1000 - height



            pygame.display.update()
            FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()