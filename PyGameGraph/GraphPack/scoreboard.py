import pygame
from numpy.lib import math

import config
from object_data import player_data

player_text = []


def build_scoreboard(screen, distance, title_font, player_font):
    pygame.draw.rect(screen, pygame.Color("Green"), [config.scoreboard_x-config.border_width, config.scoreboard_y-config.border_width, config.scoreboard_width+config.border_width, config.scoreboard_height+config.border_width])
    pygame.draw.rect(screen, pygame.Color("Black"), [config.scoreboard_x, config.scoreboard_y, config.scoreboard_width-config.border_width, config.scoreboard_height-config.border_width])

    for i in range(1, 16):
        spot_x = config.scoreboard_x
        spot_y = config.scoreboard_y + (i * 30)
        pygame.draw.line(screen, pygame.Color("White"), (spot_x, spot_y), (spot_x + config.scoreboard_width - config.border_width, spot_y), 2)

    title_text = title_font.render("Direct distance to exit: " + str(distance), 1, pygame.Color("White"))
    screen.blit(title_text, (config.scoreboard_x + 4, config.scoreboard_y + 1))

    for i in range(len(player_data)):
        spot_x = config.scoreboard_x + 4
        spot_y = config.scoreboard_y + 34 + (90 * i)
        player_text.append(player_font.render(f"{i+1}: {player_data[i][0]} Player", 1, pygame.Color(player_data[i][2])))
        screen.blit(player_text[i], (spot_x, spot_y))


class Stat(pygame.sprite.DirtySprite):
    def __init__(self, player, font, position, text_color, description1, description2):
        pygame.sprite.DirtySprite.__init__(self)
        self.player = player
        self.font = font
        self.position = position
        self.text_color = text_color
        self.description1 = description1
        self.description2 = description2
        self.text = self.description1 + self.description2  # need to add some code here!
        self.dirty = False

        self.update()

    def update(self):
        self.text = self.description1 + self.description2  # need to add some code here!
        self.image = self.font.render(self.text, 1, self.text_color)
        self.rect = self.image.get_rect(topleft=self.position)
        self.dirty = True
