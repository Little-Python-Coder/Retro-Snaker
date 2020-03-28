import pygame,sys,os,time,random
from pygame.locals import *
pygame.init()
pygame.mixer.init()

screen=pygame.display.set_mode((660,480))
screen.fill((0,0,0))

pygame.display.set_caption('Retro Snaker Alpha Vision 0.9.9')

food=[160,200]
shenti=[[200,200],[220,200],[240,200]]
head=[200,200]
fangxiang='a'
qingqiu=fangxiang
eatfood=0
score=0
sleep=0.1

def draw():
    pygame.draw.rect(screen,(255,255,0),(food[0],food[1],20,20),2)
    for a in shenti:
        pygame.draw.rect(screen,(0,0,255),(a[0],a[1],20,20),2)
def GameOver():
    d=pygame.font.SysFont('微软雅黑',70)
    e=d.render('GameOver',True,(220,20,60))
    screen.blit(e,(200,220))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit()
def Score():
    f=pygame.font.SysFont('微软雅黑',50)
    g=f.render('SCORE:'+str(score),True,(255,255,255))
    screen.blit(g,(0,0))
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                qingqiu='w'
            elif event.key==K_DOWN:
                qingqiu='s'
            elif event.key==K_LEFT:
                qingqiu='a'
            elif event.key==K_RIGHT:
                qingqiu='d'
    if qingqiu=='w' and not fangxiang=='s':
        fangxiang=qingqiu
    elif qingqiu=='s' and not fangxiang=='w':
        fangxiang=qingqiu
    elif qingqiu=='a'and not fangxiang=='d':
        fangxiang=qingqiu
    elif qingqiu=='d' and not fangxiang=='a':
        fangxiang=qingqiu
    if fangxiang=='w':
        head[1]=head[1]-20
    elif fangxiang=='a':
        head[0]=head[0]-20
    elif fangxiang=='s':
        head[1]=head[1]+20
    elif fangxiang=='d':
        head[0]=head[0]+20
    shenti.insert(0,list(head))
    if head[0]==food[0] and head[1]==food[1]:
        eatfood=1
    else:
        shenti.pop()
    if eatfood==1:
        b=random.randint(0,33)
        c=random.randint(0,24)
        x=b*20
        y=c*20
        food[0]=x
        food[1]=y
        eatfood=0
        score=score+1
    if head[0]>652 or head[0]<0 or head[1]>482 or head[1]<0:
        GameOver()
    draw()
    Score()
    time.sleep(0.1)
    pygame.display.update()
