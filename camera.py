import pygame
from player import player

class object(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 100)
    
    def target_camera(self, target):
        self.offset.x = target.rect.centerx - self.surface.get_size()[0]//2
        self.offset.y = target.rect.centery - self.surface.get_size()[1]//2

    def camera_draw(self, player):
        self.target_camera(player)

        self.sprites().reverse()

        #sprite는 pygame.sprite.Sprite
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.surface.blit(sprite.image, offset_pos)
    

