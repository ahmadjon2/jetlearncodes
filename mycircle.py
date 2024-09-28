import pygame
pygame.init()

screen = pygame.display.set_mode([500,500])
red=(255,0,0)
blue=(0,0,255,)
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)
yellow=(255,255,0)
screen.fill(white)

class MyCircle():

    def __init__(self,color,pos,rad,wid=0) :
        self.color=color
        self.pos=pos
        self.rad=rad
        self.wid=wid
        self.screen=screen

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.rad,self.wid)
        
    def grow(self,x):
        self.rad += x
        pygame.draw.circle(self.screen,self.color,self.pos,self.rad,self.wid)
        
pos=(300,300)
rad=50
wid=2
pygame.draw.circle(screen,red,pos,rad,wid)

pygame.display.update()
bluecircle=MyCircle(blue,pos,rad+20)
redcircle=MyCircle(red,pos,rad+40)
greencircle=MyCircle(green,pos,20)
yellowcircle=MyCircle(yellow,pos,rad,5)

while(True):
    for event in pygame.event.get():
        if (event.type==pygame.MOUSEBUTTONDOWN):
            bluecircle.draw()
            redcircle.draw()
            yellowcircle.draw()
            greencircle.draw()
            pygame.display.update()
        elif(event.type==pygame.MOUSEBUTTONUP):
            bluecircle.grow(2)
            redcircle.grow(2)
            yellowcircle.grow(2)
            greencircle.grow(2)
            pygame.display.update()  
        elif(event.type==pygame.MOUSEMOTION):
            pos=pygame.mouse.get_pos()
            blackcircle=MyCircle(black,pos,5)
            blackcircle.draw()
            pygame.display.update()  

