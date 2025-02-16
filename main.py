# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from pygame.locals import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    loop(screen, updatable, drawable, asteroids, player, shots)
   
def loop(screen, updatable, drawable, asteroids, player, shots):
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for a in asteroids:
            if(a.collide(player)):
                sys.exit("Game over!")

        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            for s in shots:
                if(a.collide(s)):
                    a.split()
                    s.kill()

        pygame.display.flip()

        dt = (clock.tick(60) / 1000)
        

if __name__ == "__main__":
    main()