import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((1200,300))
FPSCLOCK = pygame.time.Clock()

def main():
    sysfont = pygame.font.SysFont(None, 150)
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        counter += 1
        SURFACE.fill((255, 255, 0))
        count_image = sysfont.render("count is {} ".format(counter), True, (255, 191, 0))
        SURFACE.blit(count_image, (50, 150))
        pygame.display.update()

        count_image = sysfont.render("lemonshark's CLOCK", True, (255, 191, 0))
        SURFACE.m
        SURFACE.blit(count_image, (50, 50))
        pygame.display.update()
        FPSCLOCK.tick(1)

if __name__=='__main__':
    main()