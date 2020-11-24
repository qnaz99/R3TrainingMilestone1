import pygame
import random
import time

WIDTH = 800
HEIGHT = 800
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0,0,0]
screen.fill(white)
pygame.display.update()

running = True

def makemaze(size):
    pygame.draw.line(screen,black,[0, 0],[0,WIDTH],2)
    pygame.draw.line(screen,black,[0, 0],[HEIGHT,0],2)
    pygame.draw.line(screen,black,[HEIGHT-2, 0],[HEIGHT-2,WIDTH-2],2)
    pygame.draw.line(screen,black,[0, WIDTH-2],[HEIGHT-2,WIDTH-2],2)
    for y in range(int(HEIGHT/size),HEIGHT-1, int(HEIGHT/size)):
        for x in range(0,WIDTH-1, int(WIDTH/size)):
            if (x > ((WIDTH-1) - int(WIDTH/size))):
                pygame.draw.line(screen,black,[x+int(WIDTH/size), y],[x+int(WIDTH/size),y-int(HEIGHT/size)],2)
                pygame.display.update()
            elif (random.randrange(1,11)>5):
                pygame.draw.line(screen,black,[x, y],[x+int(WIDTH/size),y],2)
                pygame.display.update()
            else:
                pygame.draw.line(screen,black,[x+int(WIDTH/size), y],[x+int(WIDTH/size),y-int(HEIGHT/size)],2)
                pygame.display.update()
tmp = True
while running:
    clock.tick(FPS)
    if (tmp== True):
        tmp = False
        print("Enter dimensions for maze (?x?): ")
        size = input()
        size = int(size)
        makemaze(size)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

