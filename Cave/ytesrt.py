
import sys
import pygame
from pygame.locals import QUIT
pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.update()
                pygame.quit()
                sys.exit()
        SURFACE.fill((255,255,0))

if __name__ == '__main__':
    main()