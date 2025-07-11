import pygame
from load import test
vec = pygame.math.Vector2


GRAVITY = 0.8
ACC = 1.5
FRICTION = -0.2
WIDTH = 800
HEIGHT = 600

class player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = test
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)

        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        

    def jump(self):
        self.rect.y += 0.1
        hits = pygame.sprite.spritecollide(self)
        self.rect.y -= 0.1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = ACC
        self.acc.x += self.vel.x*FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        self.rect.midbottom = self.pos
        if self.vel.y > 0:
            hits = pygame.sprite.spritecollide(self)
            self.player.pos.y = hits[0].rect.top + 0.1
            self.vel.y = 0


