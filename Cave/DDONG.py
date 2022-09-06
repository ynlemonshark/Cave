import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_SPACE, Rect

class Flag:
    def __init__(self):
        print("Init flag")
        self.standby = 1
        self.score = 0
        self.collide = 0
        self.ddongCnt = 5
        self.point = 10
        self.stage = 1
        self.sec = 0

class Ddong:
    def __init__(self,rect,speed = 0):
        #print("Init Class")
        self.speed = speed
        self.rect = rect
        self.ship_image = pygame.image.load("dd.png")

    def move(self):
        self.rect.centery += self.speed

    def draw(self):
        pygame.draw.rect(SURFACE, (255, 255, 0), self.rect)
        SURFACE.blit(self.ship_image,self.rect[:2])

class Human:
    def __init__(self, rect):
        print("Init Human")
        self.rect = rect
        self.man_image = pygame.image.load("man2.png")

    def move(self):
        #self.rect.centerx
        print("move_co")

    def draw(self):
        pygame.draw.rect(SURFACE, (0, 0, 0), self.rect)
        SURFACE.blit(self.man_image,self.rect[:2])

def tick():
    global DDONGS

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                if HUMAN.rect[0] > 0:
                    HUMAN.rect.centerx -= 2
            elif event.key == K_RIGHT:
                if HUMAN.rect[0] < (600-30):
                    HUMAN.rect.centerx += 2
            elif event.key == K_SPACE:
                FLAG.standby = 0
                FLAG.__init__()
                print("start game")
    for idx, dd in enumerate(DDONGS):
        dd.move()
        if dd.rect.centery > 800:
            del DDONGS[idx]
            if FLAG.collide == 0:
                FLAG.score += FLAG.point

    if len(DDONGS) < FLAG.ddongCnt:
        DDONGS.append(Ddong(Rect(random.randint(0, 600), 100, 3, 3), random.randint(3,10)))


    #dCnt = len(DDONGS)
    #tmp = [x for x in DDONGS if not x.rect.colliderrect]
    for x in DDONGS:
        if x.rect.colliderect(HUMAN.rect):
            #print("wag~~")
            FLAG.collide = 1
            break



# Flag Class를 만들어서 전역 변수처럼 사용
FLAG = Flag()
print("flag->",FLAG.standby)
pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600, 800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
DDONGS = []
#for i in range(0,5):
DDONGS.append(Ddong(Rect(random.randint(0,600),100,20,10),5))
#DD = Ddong(Rect(100,100,100,30),5)
HUMAN = Human(Rect(300,750,25,25))
def main():

    cnt = 0


    sysfont = pygame.font.SysFont(None, 36)
    myfont = pygame.font.SysFont(None, 80)
    mess_standby = myfont.render("Press to Start", True, (255, 0, 0))
    mess_clear = myfont.render("Cleared", True, (255, 255, 0))
    mess_over = myfont.render("Game Over", True, (255, 255, 0))

    fps = 30

    while True:
        cnt += 1
        if cnt == fps:
#            if len(DDONGS) < FLAG.ddongCnt:
                #DDONGS.append(Ddong(Rect(random.randint(0, 600), 100, 20, 10), 5))
#                DDONGS.append(Ddong(Rect(random.randint(0, 600), 100, 3, 3), random.randint(3,10)))
            cnt = 0
            FLAG.sec += 1
        if (FLAG.sec == 10) and (FLAG.collide == 0):

            FLAG.ddongCnt += 20
            FLAG.point += 2
            FLAG.stage += 1
            FLAG.sec = 0



        tick()



        SURFACE.fill((0, 0, 0))
        #SURFACE.blit(ship_image, (100, 200))

        score_image = sysfont.render("score is {} ".format(FLAG.score), True, (255, 255, 255))
        SURFACE.blit(score_image, (30, 20))
        stage_image = sysfont.render("stage {} ".format(FLAG.stage), True, (255, 255, 0))
        SURFACE.blit(stage_image, (480, 20))


        HUMAN.draw()
#        DD.move()
#        DD.draw()
        for dd in DDONGS:

            dd.draw()

        if FLAG.collide == 1:
            SURFACE.blit(mess_over,(120,300))

#        if FLAG.standby:
#            SURFACE.blit(mess_standby, (130, 400))
#        else:
#            mess_standby = myfont.render("aaa", True, (255, 0, 0))
            #SURFACE.blit(mess_clear, (130, 400))

        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == '__main__':
    main()