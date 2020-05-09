import pygame
import math
import random
from time import sleep
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Zombie Killer")

background=pygame.image.load('background.png')

mixer.music.load("background.mp3")
mixer.music.play(-1)

playerImg=pygame.image.load('killer.png')
p_x=536
p_y=536
p_x_c=0
p_y_c=0

zombieImg=[]
z_x=[]
z_y=[]
z_x_c=[]
z_y_c=[]
n=5
for i in range(n):
    zombieImg.append(pygame.image.load("zombie.png"))
    z_x.append(random.randint(1,535))
    z_y.append(random.randint(0,300))
    z_x_c.append(2)
    z_y_c.append(40)

weaponImg = pygame.image.load('weapon.png')
w_x=0
w_y=0
w_x_c =0
w_y_c=-2
w_state=0
gameover = pygame.image.load('gameover.png')

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
                
def zombie(x,y,i):
    screen.blit(zombieImg[i],(x,y))
def player(x,y):
    screen.blit(playerImg,(x,y))
def weapon(x,y):
    screen.blit(weaponImg,(x+32,y+32))
def shoot():
    global w_x,w_y,p_x,p_y,w_state
    w_y = p_y
    w_x = p_x
    weapon(w_x,w_y)
    w_state=1
def isCollision(x1,y1,x2,y2):
    d = math.sqrt(math.pow(x1 - x2 ,2) + math.pow(y1 - y2 , 2))
    if d < 30:
        return True
    else:
        return False
    
    

running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p_x_c=-2
            if event.key == pygame.K_RIGHT:
                p_x_c=2
            if event.key == pygame.K_UP:
                p_y_c=-2
            if event.key == pygame.K_DOWN:
                p_y_c=2
            if event.key == pygame.K_SPACE and w_state==0:
                shoot()
        if event.type == pygame.KEYUP:
            p_x_c=0;p_y_c=0
    p_x += p_x_c
    p_y += p_y_c
    if p_x<0:
        p_x=0
    if p_x>536:
        p_x=536
    if p_y<0:
        p_y=0
    if p_y>536:
        p_y=536
    for i in range(n):
        z_x[i]+=z_x_c[i]
        if z_x[i]<=0:
            z_x[i]=0
            z_x_c[i]=2
            z_y[i]+=z_y_c[i]
        if z_x[i]>=536:
            z_x[i]=536
            z_x_c[i]=-2
            z_y[i]+=z_y_c[i]
            
        coll1 =isCollision(z_x[i],z_y[i],w_x,w_y)
        if coll1:
            killing=mixer.Sound('killing.wav')
            killing.play()
            score_value +=1
            z_x[i]=random.randint(1,535)
            z_y[i]=random.randint(0,300)
            w_state=0  
        zombie(z_x[i],z_y[i],i)
        coll2 = isCollision(z_x[i],z_y[i],p_x,p_y)
        if coll2:
            running = False        
        
    if w_state==1:
        w_y += w_y_c;w_x +=w_x_c
        weapon(w_x,w_y)
        if w_y <=0:
            w_state =0

    

    player(p_x,p_y)
    show_score(textX, testY)
    pygame.display.update()
    
#gameover    
screen.fill((0,0,0))
screen.blit(gameover,(32,32))
show_score(textX, testY)
pygame.display.update()
sleep(2)

pygame.quit()
