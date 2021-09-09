import pygame

class StaticSprite(pygame.sprite.Sprite):

    def __init__(self, image, position, color_key):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        if color_key:
            self.image.set_colorkey(pygame.Color(color_key))
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]
