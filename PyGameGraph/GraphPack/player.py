import pygame
import config
import pathing
import math
import numpy
from graph_data import graph_data
from object_data import midi_data

class Player(pygame.sprite.DirtySprite):

    def __init__(self, label, image_path, color):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = pygame.image.load(image_path).convert()
        self.image.set_colorkey(pygame.Color("White"))
        self.label = label
        self.color = pygame.Color(color)
        self.path = pathing.get_path(self.label)
        self.paint_path()
        self.start_node = self.path.pop(0)
        self.next_node = 0
        self.exit_flag = False
        self.speed = config.player_speed_fast
        self.rect = self.image.get_rect()
        self.position = config.node_set[self.start_node].position  # starting at the Start
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]
        self.travel_vector = pygame.math.Vector2(0, 0)
        self.velocity = self.travel_vector * self.speed
        self.waypoint = pygame.math.Vector2(0, 0)
        self.distance_traveled = 0
        self.travel_distance = 10000
        self.excess_distance = 0 - config.euclidean_distance
        self.dirty = False
        self.need_waypoint = True

    def update(self):
        if len(self.path) == 0 and math.floor(self.travel_distance) <= 2:
            self.position = self.waypoint
            self.exit_flag = True
            self.exit_game()
            return

        if len(self.path) > 0 and self.need_waypoint:
            self.next_node = self.path.pop(0)
            self.need_waypoint = False
            self.waypoint = pygame.math.Vector2(config.node_set[self.next_node].position)
            self.travel_vector = self.waypoint - pygame.math.Vector2(self.position)
            self.travel_distance = self.travel_vector.length()

        while math.floor(self.travel_distance) >= 2: # we are nearing our
            self.travel_vector.normalize_ip() # normalize in place with length 1
            if math.floor(self.travel_distance) <= 15:
                self.speed = config.player_speed_slow # animation clicks slow down to trigger next waypoint
            else:
                self.speed = config.player_speed_fast
            self.velocity = self.travel_vector * self.speed
            self.position += self.velocity
            self.distance_traveled += self.velocity.length()
            self.excess_distance += self.velocity.length()
            self.rect.centerx = self.position[0]
            self.rect.centery = self.position[1]
            self.travel_vector = self.waypoint - pygame.math.Vector2(self.position)
            self.travel_distance = self.travel_vector.length()

            if math.floor(self.travel_distance) < 2:
                if config.sound_on:
                    if self.next_node == config.target_node.nodeID:
                        config.bell_sound.play()
                self.need_waypoint = True
            self.dirty = True
            break

    def paint_path(self):
        if self.path:
            edges_to_paint = zip(self.path[:-1], self.path[1:])  # get a list of pair-wise nodes
            for edge in edges_to_paint:
                pygame.draw.line(config.screen, self.color, graph_data[config.graph_choice][edge[0]][0], graph_data[config.graph_choice][edge[1]][0], 5)
            pygame.display.update()

    def exit_game(self):
        self.dirty = True
        self.visible = False
        config.spawn_player = True
        if config.sound_on:
            config.scream_sound.play()
            #  config.play_midi_sound(midi_data[numpy.random.randint(len(midi_data))][1])
        pygame.time.wait(500)
        return
