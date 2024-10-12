import pygame
from pygame.locals import *
import os
pygame.font.init()
pygame.mixer.init()

play_x=300
play_y=200

play_x1=600
play_y1=200

keys=[False,False,False,False]

screen=pygame.display.set_mode((900,500))

player=pygame.image.load("D:/Foldergamedevelopment/assets/red.png")
player1=pygame.image.load("D:/Foldergamedevelopment/assets/yellow.png")
background=pygame.image.load("D:/Foldergamedevelopment/assets/background.png")

def red():
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
                    keys[2]=True
                if event.key == K_RIGHT:
                    keys[3]=True
                if event.key == K_LEFT:
                    keys[1]=True
            if  event.type == pygame.KEYUP:
                if event.key == K_UP:
                    keys[0]=False
                if event.key == K_DOWN:
                    keys[2]=False
                if event.key == K_RIGHT:
                    keys[3]=False
                if event.key == K_LEFT:
                    keys[1]=False

        if keys[0]:
            if play_y > 0:
                play_y -=7
        elif keys[1]:
            if play_x > 0:
                play_x -=2
        if keys[3]:
            if play_x < 900:
                play_x +=2
        elif keys[2]:
            if play_y < 900:
                play_y +=7


def yellow():
    while play_y1 < 600:
        screen.blit(background,(0,0))
        screen.blit(player1,(play_x1,play_y1))   
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    keys[1]=True
                if event.key == K_s:
                    keys[2]=True
                if event.key == K_d:
                    keys[3]=True
                if event.key == K_a:
                    keys[1]=True
            if  event.type == pygame.KEYUP:
                if event.key == K_w:
                    keys[0]=False
                if event.key == K_s:
                    keys[2]=False
                if event.key == K_d:
                    keys[3]=False
                if event.key == K_a:
                    keys[1]=False

        if keys[0]:
            if play_y1 > 0:
                play_y1 -=7
        elif keys[1]:
            if play_x1 > 0:
                play_x1 -=2
        if keys[3]:
            if play_x1 < 900:
                play_x1 +=2
        elif keys[2]:
            if play_y1 < 900:
                play_y1 +=7       

    