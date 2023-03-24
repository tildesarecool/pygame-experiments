# https://www.youtube.com/watch?v=QFvqStqPCRU&list=PLKTpDLYL46hUVylborWHaHdRwVpRAWKO0&index=17
import pygame 

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close upon clicking x in window
            pygame.quit()
            sys.exit()

                
    # draw all the elements
    pygame.display.update()
    clock.tick(60) # the while true will run at most 60 times per second == 60fps



"""
import pygame as pg
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    pg.display.flip()
    clock.tick(60)
"""