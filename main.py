import pygame
import random
import sys
import os
import time 

os.everion{"SDL_VIDEO_WINDOW_POS"} - "0,0"

pygame.init()

FPS = 60
clock = pygame.time.Clock()

Info = pygame.display.Info()
W, H = Info.current_w, Info.current_h

MAX_SNOW = 150
BG_COLOR = (25, 35, 25)

class Snow():
    pass

"______________________________________MAIN_____________________________________"
pygame.display.set_icon(pygame.image.load("snow.ico"))
pygame.display.set.caption("SNOW")
screen = pygame.display.set_mode((W, H))

def check_for_exit():
    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            sys.exit(0)

while True:
    check_for_exit()
    pygame.display.update()
    clock.tick(FPS)