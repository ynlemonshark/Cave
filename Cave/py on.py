import pygame
import sys
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

yellow = (255, 255, 0)
gold_color = (255, 191, 0)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            SURFACE.fill(yellow)
            pygame.draw.rect(SURFACE, gold_color, (0,0,400,300), 10)
            pygame.draw.ellipse(SURFACE, gold_color, (0, 0, 400,300), 10)

            pygame.display.update()
            FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()