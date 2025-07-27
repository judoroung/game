import pygame
import pytmx


map_sprites = pygame.sprite.Group()

def mapload(map: pytmx.pytmx.TiledMap, all_block: pygame.sprite.Group):
    layer = map.get_layer_by_name("Tile Layer 1")

    for x, y, gid in layer:
        tile = map.get_tile_image_by_gid(gid)
        if tile:
            all_block.add(mapblock(tile, x, y))
    
class mapblock(pygame.sprite.Sprite):
    def __init__(self, img: pygame.surface.Surface, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x*32, y*32)
        

