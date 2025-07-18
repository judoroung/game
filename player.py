import pygame
from load import test
vec = pygame.math.Vector2


GRAVITY = 1
WIDTH = 800
HEIGHT = 600
detach = True

class player(pygame.sprite.Sprite):
    def __init__(self, block):
        pygame.sprite.Sprite.__init__(self)
        self.block = block
        self.image = test
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.collide = lambda: pygame.sprite.spritecollide(self, self.block, False)
        self.detach = True

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vel.x -= 4
        if keys[pygame.K_RIGHT]:
            self.vel.x += 4
        
        self.vel.x *= 0.6
        self.pos.x += self.vel.x
        self.rect.midbottom = self.pos

        if self.collide():
            self.pos.x -= self.vel.x
            self.vel.x = 0

        self.vel.y += GRAVITY
        self.pos.y += self.vel.y
        self.rect.midbottom = self.pos

        if self.collide():
            self.pos.y -= self.vel.y
            self.vel.y = 0
            if keys[pygame.K_UP]:
                if self.detach:
                    self.vel.y = -15
                    self.detach = False
            else :
                self.detach = True
        self.rect.midbottom = self.pos