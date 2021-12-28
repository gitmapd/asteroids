from Vector2 import Vector
import pygame,sys
import random
pygame.init()
clock=pygame.time.Clock()
size=width,height=800,800
#location=Vector(100,100)
velocity=Vector(2.5,5)
screen=pygame.display.set_mode(size)
moving_rect=pygame.Rect(350,350,100,100)
xspeed,yspeed=5,4
#tree=pygame.image.load("tree.png")
#treerect=tree.get_rect()
#player=Vector(300,300)
class Asteroid:
    def __init__(self,pos,color,vel):
        self.pos=pos
        self.color=color
        self.vel=vel
    def __repr__(self): 
        return f"XY: {self.pos.x,self.pos.y}"
    def createrect(self,img,rect):
        self.img=img
        self.img=pygame.image.load(f"{self.rect}+'png'")        
    def move(self):
        self.pos+=self.vel
white=[255,255,255,255]
#a.createrect("tree.png")
asteroids = [ Asteroid( Vector(random.random()*width,random.random()*height), (255,0,0),Vector(random.random(),random.random())) for x in range(0,10)]
print(asteroids)
#def bouncing_rect():
#    global xspeed
#    global yspeed
#    moving_rect.x+=xspeed
#    moving_rect.y+=yspeed
#    if moving_rect.right >= width or moving_rect.left <=0:
#        xspeed *=-1
#    if moving_rect.bottom >= height or moving_rect.top <=0:
#        yspeed *=-1
#    pygame.draw.rect(screen,(255,0,0),moving_rect)
#def move():
#        keys=pygame.key.get_pressed()
#        if keys[pygame.K_a] and player.x>0:
#            print(f"left {player.x}")
#        if keys[pygame.K_d] and player.x <width:
#            print(f"right {player.x}")
#        if keys[pygame.K_w] and player.y>0 :
#            print("up {player.y}")
#        if keys[pygame.K_s] and player.y<height:
#            print("down {player.y}")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: sys.exit()
    #move()
    #for i in range(10):
    #    location.__add__(velocity)
    #    location.x=location.x+velocity.x+i
    #    location.y=location.y+velocity.y+i
    #pygame.draw.ellipse(screen,white , [location.x, location.y, 300, 300], 5) 
    #screen.blit(tree,treerect)
    screen.fill((30,30,30))
#    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)