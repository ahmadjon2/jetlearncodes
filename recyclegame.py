import pygame
from pygame.locals import *
pygame.init()
import random 
import time

screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode([screen_width,screen_height])
score = 0

def changebackground(img):
    background = pygame.image.load(img)
    bg = pygame.transform.scale(background,(screen_height,screen_width))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def  __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()
        
class Recyclable(pygame.sprite.Sprite):
    def  __init__(self,img):
        super().__init__()   
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

class Nonrecyclable(pygame.sprite.Sprite):
    def  __init__(self,):
        super().__init__()   
        self.image = pygame.image.load("bag.png")        
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

images = ["pencil.png","box.png","paper.png"]
items_list = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()

for i in range(50):
    items = Recyclable(random.choice(images))
    items.rect.x = random.randrange(screen_width)
    items.rect.y = random.randrange(screen_height)
    items_list.add(items)
    all_sprites.add(items)

for i in range(20):
    plastic = Nonrecyclable()
    plastic.rect.x = random.randrange(screen_width)
    plastic.rect.y = random.randrange(screen_height)
    plastic_list.add(plastic)
    all_sprites.add(plastic)

bin = Bin()
all_sprites.add(bin)
white = (255,255,255)
red = (255,0,0)
playing=True
scor = 0
clock = pygame.time.clock()
startime = time.time()
myFont = pygame.font.SysFont("arial",22)
timingfont = pygame.font.SysFont("arial",22)
text = myFont.render("score="+str(0),True,white)

while playing:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    timelapsed = time.time()-startime
    if timelapsed >=60:
        if score >50:
            text = myFont.render("binloot succesful",True,red)
            changebackground("winscreen.jpg")
        else:
            text = "BETTER LUCK NEXT TIME",True,red
            changebackground("tolosescreen.jpg")
            
            
    

