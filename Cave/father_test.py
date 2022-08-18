import sys
import pygame
from random import randint
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_SPACE

WIDTH = 100
HEIGHT = 80
SIZE = 10
TICK = 2
EAT_TICK = 2
ADDTAIL = 5


RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
STOP = 4

STARTED = False

tick_count = 0

window_size = [WIDTH*SIZE, HEIGHT*SIZE]

pygame.init()
SURFACE = pygame.display.set_mode(window_size)
FPSCLOCK = pygame.time.Clock()

def main():
    global STARTED
    tick_count = 0
    cue = 1
    dir = RIGHT
    tgt_xpos = WIDTH * SIZE / 2
    tgt_ypos = HEIGHT * SIZE / 2
    background_color = (255, 0, 0)
    object_color = (0, 0, 0)
    eat_color = (255,255,0)
    cue_list = []
    cur_dir = STOP
    eat_list = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                STARTED = True
#                pygame.quit()
#                sys.exit()
            if event.type == KEYDOWN:
                if (event.key == K_LEFT) and (cur_dir != RIGHT):
                    dir = LEFT
                elif event.key == K_RIGHT and (cur_dir != LEFT):
                    dir = RIGHT
                elif event.key == K_UP and (cur_dir != DOWN):
                    dir = UP
                elif event.key == K_DOWN and (cur_dir != UP):
                    dir = DOWN
                elif event.key == K_SPACE:
                    cue = cue + ADDTAIL


        object_possize = (tgt_xpos, tgt_ypos, SIZE, SIZE)  # x,y, x size, y size
        cue_list.append(object_possize)
        SURFACE.fill(background_color) # 바탕색갈
        cue_play = cue_list[-1*cue:]
        for body in cue_play:
            #pygame.draw.rect(SURFACE, object_color , object_possize)
            pygame.draw.rect(SURFACE, object_color, body)

        tick_count = tick_count + 1
        #if STARTED and (divmod(tick_count, TICK)[1] == 0):
        if STARTED and divmod(tick_count, TICK)[1]:
        #if STARTED:
            print("ti",tick_count)
            if dir == LEFT:
                tgt_xpos = tgt_xpos - SIZE
                cur_dir = dir
            elif dir == RIGHT:
                tgt_xpos = tgt_xpos + SIZE
                cur_dir = dir
            elif dir == UP:
                tgt_ypos = tgt_ypos - SIZE
                cur_dir = dir
            elif dir == DOWN:
                tgt_ypos = tgt_ypos + SIZE
                cur_dir = dir

        # if STARTED and (divmod(tick_count, EAT_TICK)[1] == 0):
        #     xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        #     eat_possize = (xpos*SIZE, ypos*SIZE, SIZE, SIZE)  # x,y, x size, y size
        #     eat_list.append(eat_possize)
        # for eat in eat_list:
        #     pygame.draw.rect(SURFACE, eat_color, eat)




        pygame.display.update()
        FPSCLOCK.tick(TICK)


if __name__ == '__main__':
    main()
