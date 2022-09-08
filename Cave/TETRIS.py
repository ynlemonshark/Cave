import sys
from math import floor

import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_DOWN, Rect



WIDTH = 10
HEIGHT = 15
SIZE = 30

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()
class Block:
    def __init__(self, rect):
        self.rect = rect
    def leftmove(self):
        self.rect.centerx += SIZE
    def righttmove(self):
        self.rect.centerx -= SIZE
    def down(self):
        self.rect.centery += SIZE
    def draw(self):
        pygame.draw.rect(SURFACE,(255,255,0), self.rect)
class Blocks:
    def __init__(self,posx,posy,type,color):
        self.posx = posx
        self.posy = posy
        self.type = type
        self.color = color
        #super.__init__()
        self.rect = Rect(self.posx, self.posy, SIZE, SIZE)
    def down(self):
        self.rect.centery += SIZE
    def draw(self):
        pygame.draw.rect(SURFACE, self.color, self.rect)
        # pygame.draw.lines(SURFACE, (255, 255, 0), 1, [[0, 0], [0+SIZE*3, 0], [SIZE*3, SIZE],[0,SIZE],[0,0]], 5)
        # pygame.draw.rect(SURFACE, self.color, [self.posx, self.posy, SIZE, SIZE])
        # pygame.draw.rect(SURFACE, self.color, [self.posx+SIZE, self.posy, SIZE, SIZE])
        # pygame.draw.rect(SURFACE, self.color, [self.posx+SIZE, self.posy+SIZE, SIZE, SIZE])
        # pygame.draw.rect(SURFACE, self.color, [self.posx+SIZE, self.posy+SIZE*2, SIZE, SIZE])


def tick():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print("LEFt")
            elif event.key == K_RIGHT:
                print("right")
            elif event.key == K_DOWN:
                print("down")

def main():
    cnt = 0
    fps = 30

    tmp = Blocks(0,0,1,(255,255,0))


    while True:
        cnt += 1
        if cnt == fps:
            tmp.down()
            cnt = 0


        tick()

        SURFACE.fill((0, 0, 0))

        #pygame.draw.lines(SURFACE, (255, 255, 0), 1, [[0, 0], [0, 100], [100, 150]], 100)

        tmp.draw()

        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == '__main__':
    main()

