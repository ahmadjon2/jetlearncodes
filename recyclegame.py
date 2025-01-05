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
    bg = background 
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
clock = pygame.time.Clock()
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
        screen.blit(text,(250,40))
    else:
        changebackground("bee_backround.png")
        countDown = timingfont.render("time left:"+str(60-int(timelapsed)),True,white)
        screen.blit(countDown,(20,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y > 0 :
                bin.rect.y -= 30
        if keys[pygame.K_DOWN]:
            if bin.rect.y < 630:
                bin.rect.y += 30       
        if keys[pygame.K_LEFT]:
            if bin.rect.x > 0 :
                bin.rect.x -= 30
        if keys[pygame.K_RIGHT]:
            if bin.rect.x < 950:
                bin.rect.x += 30
        item_hit_list = pygame.sprite.spritecollide(bin,items_list,True)     
        plastic_hit_list = pygame.sprite.spritecollide(bin,plastic_list,True) 
        for item in item_hit_list:
            score += 1
            text = myFont.render("score = "+str(score),True,white)
        for plastic in plastic_hit_list:
            score -= 5
            text = myFont.render("score ="+str(score),True,white)
        screen.blit(text,(200,10))
        all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()