from smtplib import SMTPServerDisconnected
from turtle import speed
import pygame
import random

pygame.init()
W,H = 500,500
win = pygame.display.set_mode((W,H))

class Stars():
    def __init__(self):
         self.x = random.randint(0,W)
         self.y = random.randint(0,H)
         self.speed = random.randint(1,3)        
         self.rad = 1
         self.color = (255,255,255)

    def draw(self):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.rad)

    def move(self):
        self.y += self.speed
        if self.y >= H:
            self.y = 0
            self.x = random.randint(0,W)


stones_img = pygame.image.load("stone.png")

stones_img = pygame.transform.scale(stones_img,(50,50))

class Rocks():
    def __init__(self):
        self.x = random.randint(0,W)
        self.y = random.randint(-H//3,0)
        self.speed = random.randint(2,4)
        self.image = stones_img

    def move(self):
            self.y += self.speed
            if self.y >= H:
                self.y = -50
                self.x = random.randint(0,W)

    def draw(self):
            win.blit(self.image,(self.x,self.y)), 

rocks = []
for i in range(20):
        rocks.append(Rocks())

stars = []
for i in range(20):
        stars.append(Stars())



while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    win.fill((0,0,0))

    for i in stars:
        i.draw()
        i.move()

    for i in rocks:
        i.draw()
        i.move()

    pygame.display.update()
    pygame.time.delay(10)
    
        


