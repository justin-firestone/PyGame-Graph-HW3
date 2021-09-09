import sys
from collections import deque
import heapq as heap
from numpy import random
from edge import edge_id
import config
import node
import graph_data

def get_path(path_type):
    if path_type == "Test":
        return_path = graph_data.test_paths[config.graph_choice].copy()
        return return_path.copy()
    elif path_type == "Random":
        pass
    elif path_type == "DFS":
        pass
    elif path_type == "BFS":
        pass
    elif path_type == "Dijkstra":
        pass
    else:
        return -1


def get_random_path(start, end):
    pass

def get_dfs_path(start, end):
    pass

def get_bfs_path(start, end):
    pass

def get_dijkstra_path(start, end):
    pass
