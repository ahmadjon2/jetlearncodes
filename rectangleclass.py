import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
screen.fill(white)
pygame.display.update()


class Rect: 

    def __init__(self,color,dimension):
        self.rect_surf = screen
        self.rect_color = color
        self.rect_dimension = dimension

        
    #def move(self):


    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surf,self.rect_color,self.rect_dimension)
greenRect = Rect(green,(50,20,100,100))
redRect = Rect(red,(150,200,150,150))
blueRect = Rect(blue,(300,400,200,200))
greenRect.draw()
blueRect.draw()
redRect.draw()
pygame.display.update()

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
pygame.quit()
