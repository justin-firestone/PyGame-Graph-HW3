import pygame
import config

class Toggle_Button(pygame.sprite.DirtySprite):

    def __init__(self, position, image_path_a, image_path_b):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image_path_b).convert()
        self.image_a = image_path_a
        self.image_b = image_path_b
        self.position = position
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]
        self.dirty = False

    def update(self):
        if config.sound_on:
            self.image = pygame.image.load(self.image_a).convert()
        else:
            self.image = pygame.image.load(self.image_b).convert()
        self.rect = self.image.get_rect(topleft=self.position)
        self.dirty = True

    def toggle_sound(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if config.sound_on:
                        config.sound_on = False
                    else:
                        config.sound_on = True


