import pygame
import numpy

# global variables

display_width = 1350  # 1366 by 768 is average laptop screen
display_height = 750
border_width = 5
clock_speed = 30  # frames per second
player_speed_fast = 15
player_speed_slow = 1
scoreboard_x = 950
scoreboard_y = 20
scoreboard_width = 390
scoreboard_height = 480 + border_width
euclidean_distance = 0
sound_on = False

node_set = {}
edge_set = {}
player_set = pygame.sprite.LayeredDirty()
static_set = pygame.sprite.Group()
stat_set = pygame.sprite.LayeredDirty()
toggle_set = pygame.sprite.LayeredDirty()
button_set = {}
midi_tracks = []

screen = None
clock = None
background = None
graph_choice = 0
start_node = None
target_node = None
exit_node = None

outer_node_radius = 35
inner_node_radius = 32
outer_node_color = pygame.Color("White")
inner_node_color = pygame.Color("Red")
node_text_color = pygame.Color("White")
scoreboard_border_color = pygame.Color("Yellow")

spawn_player = True
player_counter = 0
reset = False
default_graph = True

scream_sound = None
bell_sound = None


def get_linear_distance(node1, node2):
    return numpy.linalg.norm(numpy.array(node1) - numpy.array(node2))


def play_midi_sound(midi_sound):
    pygame.mixer.music.load(midi_sound)
    pygame.mixer.music.play()

