import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONUP

LEFT_CLICK = 1
RIGHT_CLICK = 3

WIDTH = 11
HEIGHT = 11
SIZE = 50

MAPPED = [[randint(0, 1) for _ in range(WIDTH-1)] for _ in range(HEIGHT-1)]
MASKING = [[0 for _ in range(WIDTH-1)] for _ in range(HEIGHT-1)]
pygame.init()
SURFACE = pygame.display.set_mode([WIDTH*SIZE, HEIGHT*SIZE])
FPSCLOCK = pygame.time.Clock()


def calcRow(all):

    ret = []
    for tmp in all[:]:
        dic = []
        num = 0
        # print(tmp)
        for cha in tmp:
            if cha == 1:
                num += 1
            else:
                if num != 0:
                    dic.append(num)
                num = 0
        if num != 0:
            dic.append(num)
        # print(dic)
        ret.append(dic)
    return ret

def calcCol(all):
    ret = []
    for col in range(WIDTH-1):
        dic = []
        num = 0
        for row in range(HEIGHT-1):
            cha = all[row][col]
            if cha == 1:
                num += 1
            else:
                if num != 0:
                    dic.append(num)
                num = 0
        if num != 0:
            dic.append(num)
        ret.append(dic)
        # print(dic)
    return ret


def main():
    game_over = False
    cleared = False
    q_image = pygame.image.load("question.png")
    bomb_image = pygame.image.load("bomb.png")
    x_image = pygame.image.load("x.png")

    smallfont = pygame.font.SysFont(None, 18)
    middlefont = pygame.font.SysFont(None, 64)
    largefont = pygame.font.SysFont(None, 64)
    mess_gameover = largefont.render("GAME OVER", True, (100, 0, 0))
    mess_cleared = largefont.render("!!CLEARED!!", True, (255, 255, 0))
    mess_rect = mess_cleared.get_rect()

    print(MAPPED)
    rowD = calcRow(MAPPED)
    print(rowD)
    colD = calcCol(MAPPED)
    print(colD)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONUP and event.button == LEFT_CLICK:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE),
                MASKING[xpos][ypos] = 1
                # print(xpos+1, ypos+1)
            if event.type == MOUSEBUTTONUP and event.button == RIGHT_CLICK:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE),
                MASKING[xpos][ypos] = 2
                # print("r",xpos+1, ypos+1)


        SURFACE.fill((0, 0, 0))

        # 지뢰 정보 표시
        for ypos in range(HEIGHT-1):
            num_image = smallfont.render("{}".format(' '.join(str(x) for x in rowD[ypos])), True, (255, 255, 0))
            SURFACE.blit(num_image, ((WIDTH-1)*SIZE, ypos*SIZE+SIZE/2))

        for xpos in range(WIDTH-1):
            num_image = smallfont.render("{}".format(' '.join(str(x) for x in colD[xpos])), True, (255, 255, 0))
            SURFACE.blit(num_image, (xpos*SIZE, ((HEIGHT-1)*SIZE+SIZE/2)))

        # 클릭표시
        qcnt = 0
        for xpos in range(WIDTH-1):
            for ypos in range(HEIGHT - 1):
                tile = MASKING[ypos][xpos]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == 1:
                    #num_image = middlefont.render("1", True, (0, 255, 200))
                    #bomb_image = pygame.image.load("bomb.png")

                    SURFACE.blit(bomb_image, (ypos*SIZE, xpos*SIZE))
                    #pygame.draw.rect(SURFACE())
                elif tile == 0:
                    qcnt += 1
                    SURFACE.blit(q_image, (ypos*SIZE, xpos*SIZE))
                elif tile == 2:
                    #num_image = middlefont.render("2", True, (0, 0, 200))
                    SURFACE.blit(x_image, (ypos*SIZE, xpos*SIZE))

                    if MAPPED[xpos][ypos]:
                        game_over = True

        if not game_over:
            if qcnt == 0:
                print(MASKING)
                rowD_m = calcRow(MASKING)
                print(rowD_m)
                colD_m = calcCol(MASKING)
                print(colD_m)
                game_over = True
                if rowD == colD_m:
                    if colD == rowD_m:
                        cleared = True
                        SURFACE.blit(mess_cleared, mess_rect.center)



        if game_over:
            if cleared:
                #SURFACE.blit(mess_gameover, (HEIGHT*SIZE/2,WIDTH*SIZE/2))
                SURFACE.blit(mess_cleared, mess_rect.center)
            else:
                SURFACE.blit(mess_gameover, mess_rect.center)
        # SURFACE.blit()

        # 선 그리기
        for index in range(0, WIDTH*SIZE, SIZE):
            pygame.draw.line(SURFACE, (100,100,100), (index, 0), (index, HEIGHT*SIZE))

        for index in range(0, HEIGHT*SIZE, SIZE):
            pygame.draw.line(SURFACE, (100,100,100), (0, index), (WIDTH*SIZE, index))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()
