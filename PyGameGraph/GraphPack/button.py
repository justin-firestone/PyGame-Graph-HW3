import pygame
import config

class Button:
    def __init__(self, text, position, size, background_color, text_color):
        self.x, self.y = position
        self.text = text
        self.font = pygame.font.SysFont("Arial", size)
        self.background_color = pygame.Color(background_color)
        self.text_color = pygame.Color(text_color)
        self.change_text(text)
 
    def change_text(self, text):
        self.text_surface = self.font.render(text, 1, self.text_color)
        self.size = self.text_surface.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.background_color)
        self.surface.blit(self.text_surface, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        
    def quit_game(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    pygame.quit()
                    exit()

    def reset(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    config.default_graph = False
                    config.reset = True
