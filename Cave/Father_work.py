# 이거는 연우가 작업중인 겁니다.

import pygame
import sys
from pygame.locals import QUIT

SIZE_X = 300
SIZE_Y = 300

pygame.init()
SURFACE = pygame.display.set_mode((SIZE_X,SIZE_Y))
FPSCLOCK = pygame.time.Clock()

gold = (255, 191, 0)


def main():
    s_x = 50
    s_y = 50
    wid_b = 20
    ORG_hei = 20
    hei_b = ORG_hei
    FALL = True
    MOVE = True
    vel = 10
    acc = 1
    max_vel = 20
    bounce_rate = 0.8
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            SURFACE.fill((255, 255, 0))

            pygame.draw.ellipse(SURFACE, gold, (s_x, s_y, wid_b,hei_b))
            if FALL and MOVE:

                if (s_y + hei_b) >= SIZE_Y:
                    FALL = False
                    vel = (int) (vel * bounce_rate)
                    if vel <= 0:
                        MOVE = False
                else:
                    vel += acc
                    if vel >= max_vel:
                        vel = max_vel
                s_y += vel
            elif MOVE:

                if s_y <= 0:
                    FALL = True
                else:
                    vel -= acc
                    if vel < 0: FALL = True
                s_y -= vel

            # if falling:
            #     acceleration += acceleration * gravity + gravity
            #     height -= acceleration
            #     if height <= 0:
            #         height = 0
            #         rebound = round(acceleration / mitigation, -1)
            #         falling = False
            #     ypos = 1000 - height
            #
            # else:
            #     acceleration -= rebound * gravity + gravity * 10
            #     rebound -= round(rebound / 2, -1)
            #     height += round(acceleration / 10, -1)
            #     if rebound <= 1:
            #         height = 0
            #         falling = True
            #     ypos = 1000 - height
            #
            # print(height)

            pygame.display.update()
            FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()