import pygame
import random
from constants import ASTEROID_MIN_RADIUS 
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)

    def update(self, dt):
        self.position.x += self.velocity.x * dt  # use velocity's x component
        self.position.y += self.velocity.y * dt  # use velocity's y component
    # Keep x,y in sync with position
        self.x = self.position.x
        self.y = self.position.y

    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            
            return
        
        print("new")
        rd_angle = random.uniform(20, 50) # get random angle between 20 and 50
        a1_angle = self.velocity.rotate(rd_angle)
        a2_angle = self.velocity.rotate(rd_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = a1_angle * 1.2
        a2.velocity = a2_angle * 1.2
       # self.kill()

        
