import pygame
from time import *
from pygame.locals import *
pygame.init()

screen=pygame.display.set_mode((500,600))

play_x=200
play_y=200

keys=[False,False,False,False]

player=pygame.image.load("D:/Foldergamedevelopment/images/rocket.png")
background=pygame.image.load("D:/Foldergamedevelopment/images/bg satel.png")

while play_y < 600:
    screen.blit(background,(0,0))
    screen.blit(player,(play_x,play_y))   

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                keys[0]=True
            if event.key == K_DOWN:
                keys[1]=True
            if event.key == K_RIGHT:
                keys[2]=True
            if event.key == K_LEFT:
                keys[3]=True
        if  event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0]=False
            if event.key == K_DOWN:
                keys[1]=False
            if event.key == K_RIGHT:
                keys[2]=False
            if event.key == K_LEFT:
                keys[3]=False

    if keys[0]:
        if play_y > 0:
            play_y -= 7
    elif keys[2]:
        if play_y < 536:
            play_y +=7
    if keys[1]:
        if play_x > 0:
            play_x -=2
    elif keys[3]:
        if play_x < 536:
            play_x +=2
        
    play_y += 5
    sleep(0.05)
print("GAME OVER")