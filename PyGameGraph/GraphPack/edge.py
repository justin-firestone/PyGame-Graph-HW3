import pygame
import numpy
from config import edge_set


class Edge:
    def __init__(self, eID, length, line_color):
        self.eID = eID
        self.length = length
        self.line_color = line_color

def buildEdges(graph_data, screen):
    for node1, (_, neighbors) in enumerate(graph_data):
        for node2 in neighbors:
            eID = edge_id(node1, node2)
            leftCoord = numpy.array(graph_data[node1][0])
            rightCoord = numpy.array(graph_data[node2][0])
            if eID not in edge_set:
                edge_set[eID] = Edge((node1, node2), get_distance(leftCoord, rightCoord), pygame.Color("Gray"))
        for node1, node2 in edge_set:
            pygame.draw.line(screen, pygame.Color("White"), graph_data[node1][0], graph_data[node2][0], 2)
    return
  
def edge_id(node1, node2):
    return tuple(sorted((node1, node2)))

def get_distance(coord1, coord2):
    sum_squares = numpy.sum(numpy.square(coord1 - coord2))
    return numpy.sqrt(sum_squares)

def drawEdges(graph_data, screen):
    for node1, node2 in edge_set:
        pygame.draw.line(screen, pygame.Color("White"), graph_data[node1][0], graph_data[node2][0], 2)
    return
