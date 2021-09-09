import pygame
import config

def build_border(screen):
        pygame.draw.rect(screen, config.scoreboard_border_color, [0, 0, config.display_width, config.border_width])
        pygame.draw.rect(screen, config.scoreboard_border_color, [0, config.display_height, config.display_width, config.border_width])
        pygame.draw.rect(screen, config.scoreboard_border_color, [0, 0, config.border_width, config.display_height])
        pygame.draw.rect(screen, config.scoreboard_border_color, [config.display_width, 0, config.border_width, config.display_height+config.border_width])
