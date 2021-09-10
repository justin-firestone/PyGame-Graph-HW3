import unittest
import config
import math

test_graphs = [
    [
        [(450, 450), [1, 2]],
        [(45, 45), [0]],
        [(1100, 700), [0]]
    ]
]

test_paths = [
    [1, 0, 2]
]

def calculate_straight_line_distance(graph_index):
    test_graph = test_graphs[graph_index]
    distance = math.floor(config.get_linear_distance(test_graph[-2][0], test_graph[-1][0]))
    return distance


def calculate_path_distance(graph_index):
    test_graph = test_graphs[graph_index]
    test_path = test_paths[graph_index]
    total = 0
    for i in range(len(test_path) - 1):
        total += math.floor(config.get_linear_distance(test_graph[test_path[i]][0], test_graph[test_path[i + 1]][0]))
    return total


class TestDistanceMethods(unittest.TestCase):

    def test_first_graph_straight_line_distance(self):
        distance = calculate_straight_line_distance(0)
        self.assertAlmostEqual(distance, 1241, delta=1)

    def test_first_graph_path_distance(self):
        graph_index = 0
        distance = calculate_path_distance(graph_index)
        self.assertAlmostEqual(distance, 1267, msg=f"Path Distance for graph {graph_index} is wrong!", delta=1)
