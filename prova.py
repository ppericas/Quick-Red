import pygame
from random import randint
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
PLAYER_WIDTH = 32
PLAYER_HEIGHT = 46 * 4
FPS = 60

BACKGROUND_IMAGE = pygame.image.load(
    os.path.join('assets', 'background.png'))
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

PLAYER_IMAGE = pygame.image.load(
    os.path.join('assets', 'player.png'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))

PLAYER_FACING_NORTH = (0, 0, PLAYER_WIDTH , PLAYER_HEIGHT/4 ) 

def draw_window():
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(PLAYER, (100, 100), PLAYER_FACING_NORTH)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()