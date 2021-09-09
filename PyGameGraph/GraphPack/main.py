import os

import config
import screen_builder
import button
import node
import edge
import player
import static_sprite
import scoreboard
import toggle_button
from object_data import player_data
from object_data import toggle_button_data
from object_data import button_data
from object_data import sound_data
from graph_data import graph_data
import math
import pygame


def initialize(screen):
    # rotate through different graphs here
    if not config.default_graph:
        config.graph_choice += 1
        if config.graph_choice == len(graph_data):
            config.graph_choice = 0
        config.euclidean_distance = math.floor(config.get_linear_distance(graph_data[config.graph_choice][-2][0], graph_data[config.graph_choice][-1][0]))

    screen.fill(pygame.Color("Black"))
    config.node_set.clear()
    config.edge_set.clear()
    config.player_set.empty()
    config.player_set.draw(config.screen)
    config.static_set.empty()
    config.stat_set.empty()
    edge.buildEdges(graph_data[config.graph_choice], screen)
    edge.drawEdges(graph_data[config.graph_choice], screen)
    node.build_nodes(graph_data[config.graph_choice], screen)
    screen_builder.build_border(screen)
    build_static_elements()

    for element in toggle_button_data:
        new_button = toggle_button.Toggle_Button(element[0], element[1], element[2])
        config.toggle_set.add(new_button)

    config.spawn_player = True
    config.player_counter = 0
    scoreboard.build_scoreboard(screen, config.euclidean_distance, title_font, player_font)
    pygame.display.update()


def build_static_elements():
    # add buttons
    for i, element in enumerate(button_data):
        new_button = button.Button(element[0], element[1], element[2], element[3], element[4])
        new_button.show(config.screen)
        config.button_set[i] = new_button

    # build node text as static sprites
    for element in config.node_set:
        static_label = node.Static_Text(config.node_set[element].label, config.node_text_color, config.node_set[element].position)
        config.static_set.add(static_label)

    start_image = static_sprite.StaticSprite("../images/start.png", graph_data[config.graph_choice][-2][0], "White")
    exit_image = static_sprite.StaticSprite("../images/exit.png", graph_data[config.graph_choice][-1][0], "White")
    target_image = static_sprite.StaticSprite("../images/target.png", node.get_random_target(), "White")
    config.start_node = config.node_set[len(graph_data[config.graph_choice]) - 2]
    config.exit_node = config.node_set[len(graph_data[config.graph_choice]) - 1]
    config.static_set.add(start_image)
    config.static_set.add(exit_image)
    config.static_set.add(target_image)
    config.static_set.draw(config.screen)

    # for refreshing sprite locations
    config.background = config.screen.copy()


def build_sounds():
    config.scream_sound = pygame.mixer.Sound(sound_data[0][1])
    config.bell_sound = pygame.mixer.Sound(sound_data[1][1])


def mainloop():
    config.reset = False
    pygame.time.wait(100) # milliseconds
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            config.button_set[0].quit_game(event)  # first button_data is exit, second is reset, third is sound
            config.button_set[1].reset(event)
            for toggle in config.toggle_set:
                toggle.toggle_sound(event)

        if config.reset:
            config.sound_on = False
            running_player.exit_game()
            config.player_set.clear(config.screen, config.background)
            config.player_set.empty()
            config.stat_set.clear(config.screen, config.background)
            config.stat_set.empty()
            config.static_set.clear(config.screen, config.background)
            config.static_set.empty()
            config.toggle_set.clear(config.screen, config.background)
            config.toggle_set.empty()
            player_rects = config.player_set.draw(config.screen)
            static_rects = config.static_set.draw(config.screen)
            toggle_rects = config.toggle_set.draw(config.screen)
            pygame.display.update(player_rects)
            pygame.display.update(static_rects)
            pygame.display.update(toggle_rects)
            initialize(config.screen)
            mainloop()

        if config.spawn_player and config.player_counter < len(player_data):
            stat_x = config.scoreboard_x + 10
            stat_y = config.scoreboard_y + 66 + (90 * config.player_counter)
            running_player = player.Player(player_data[config.player_counter][0], player_data[config.player_counter][1], player_data[config.player_counter][2])
            travel_distance = scoreboard.Stat(running_player, stat_font, (stat_x, stat_y), pygame.Color(player_data[config.player_counter][2]), "Travel distance: ", " | Excess distance: ")
            path_stat = stat_font.render(str(running_player.path), 1, running_player.color)
            if path_stat.get_rect().width > config.scoreboard_width:
                print(f"{running_player.label} path too wide for scoreboard!")
                print(f"{running_player.label} path: {running_player.path}")
                path_stat = stat_font.render("Path too long for scoreboard! See console.", 1, running_player.color)
            config.screen.blit(path_stat, (stat_x, stat_y + 30))
            pygame.display.update()
            config.stat_set.add(travel_distance)
            config.player_counter += 1
            config.player_set.add(running_player)
            config.spawn_player = False

        for runner in config.player_set:
            if runner.exit_flag is False:
                runner.update()
                player_rects = config.player_set.draw(config.screen)

        for stat in config.stat_set:
            stat.update()
            stat_rects = config.stat_set.draw(config.screen)

        for toggle in config.toggle_set:
            toggle.update()
            toggle_rects = config.toggle_set.draw(config.screen)

        config.clock.tick(config.clock_speed)
        pygame.display.update(player_rects)
        pygame.display.update(stat_rects)
        pygame.display.update(toggle_rects)
        config.player_set.clear(config.screen, config.background)
        config.stat_set.clear(config.screen, config.background)
        config.toggle_set.clear(config.screen, config.background)


pygame.init()
running = True
config.reset = False
title_font = pygame.font.SysFont("Arial", 24, bold=True)
player_font = pygame.font.SysFont("Arial", 20, bold=True)
stat_font = pygame.font.SysFont("Arial", 16, bold=True)
config.screen = pygame.display.set_mode(size=(config.display_width + config.border_width, config.display_height + config.border_width))
config.clock = pygame.time.Clock()

build_sounds()

config.euclidean_distance = math.floor(config.get_linear_distance(graph_data[config.graph_choice][-2][0], graph_data[config.graph_choice][-1][0]))

initialize(config.screen)
mainloop()
