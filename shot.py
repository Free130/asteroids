import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius
        #self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius)

    def update(self, dt):
        self.position.x += self.velocity.x * dt  # use velocity's x component
        self.position.y += self.velocity.y * dt  # use velocity's y component
    # Keep x,y in sync with position
        self.x = self.position.x
        self.y = self.position.y
