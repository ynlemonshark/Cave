import sys
import pygame
import numpy as np
from pygame.locals import QUIT, Rect

yellow = (255,255,0)
golden_color = (255, 191, 0)

FPSCLOCK = pygame.time.Clock()

pygame.init()
SURFACE = pygame.display.set_mode((1200, 900))

accuracy = 100


def main():
    theta = 0
    while True:
        x = 10
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((yellow))
        for i in range(accuracy):
            y = round(np.sin(theta), -1)
            xpos = i * 10
            ypos = 630 - y
            print(x,y,xpos,ypos)
            pygame.draw.rect(SURFACE, (golden_color), (xpos,ypos,x,y))
            i1 = i + 1
            theta = round(i1 , -1)
            pygame.display.update()
        FPSCLOCK.tick(1)


if __name__ == '__main__':
    main()