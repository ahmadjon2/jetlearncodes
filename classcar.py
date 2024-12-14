import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 800
screen_height = 930
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Car Game")
font = pygame.font.SysFont("arial", 70)
white = (255, 255, 255)
score = 0
groundscroll = 0
scrollspeed = 2
driving = False
gameover = False

road = pygame.image.load("D:/Foldergamedevelopment/images/carbackround.png")
button_img = pygame.image.load("D:/Foldergamedevelopment/assets/restart.png")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    car.rect.x = 100
    car.rect.y = int(screen_height / 2)
    score = 0
    return score

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("D:/Foldergamedevelopment/images/car.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        global driving, gameover
        if not gameover:
            self.rect.y += 2            
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                self.rect.x -= 5
            if keys[K_RIGHT]:
                self.rect.x += 5
            if keys[K_UP]:
                self.rect.y -= 4     
            if keys[K_DOWN]:
                self.rect.y += 2
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

cargroup = pygame.sprite.Group()
car = Car(100, int(screen_height / 2))
cargroup.add(car)
button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_img)

run = True
while run:
    clock.tick(fps)
    screen.blit(road, (0, 0))
    cargroup.draw(screen)
    cargroup.update()
    screen.blit(road, (0, groundscroll))
    screen.blit(road, (0, groundscroll - screen_height))

    groundscroll += scrollspeed
    if groundscroll >= screen_height:
        groundscroll = 0

    if gameover:
        if button.draw():
            gameover = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not driving and not gameover:
            driving = True

    pygame.display.update()

pygame.quit()
