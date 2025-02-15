# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame.locals import *
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    loop(screen, updatable, drawable)
   
def loop(screen, updatable, drawable):
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for d in drawable:
            d.draw(screen)
        #drawable.draw(screen)
        
        pygame.display.flip()
        dt = (clock.tick(60) / 1000)
        updatable.update(dt)

if __name__ == "__main__":
    main()