# -*- coding: utf-8 -*-

graph = {'A': ['B', 'C'], 'B': ['A'] ['D'], 'C': ['A'], 'D': ['B'] }
graph = {'A': ['B', 'C'], 'B': ['D'] ['E'], 'C': ['F'] ['G'], 'D': ['H'], 'E': [''],  'F': [''],  'G': [''],  'H': [''], }
graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'] ['G'], 'D': ['B', 'H', 'I'], 'E': ['B', 'J', 'K'],  'F': ['C', 'H', 'L', 'M'],  'G': ['C', 'N', 'O'],  'H': ['D'], 'I': ['D'], 'J': ['E'], 'K': ['E'], 'L': ['F'], 'M': ['F'], 'N': ['G'], 'O': ['G'] }


def create_adjacency_matrix(adj_list):
    vertices = sorted(adj_list.keys())
    matrix = [[0] * len(vertices) for _ in range(len(vertices))]

    for i, vertex in enumerate(vertices):
        for neighbor in adj_list[vertex]:
            j = vertices.index(neighbor)
            matrix[i][j] = 1

    return vertices, matrix

def display_adjacency_matrix(vertices, matrix):
    print("  " + " ".join(vertices))
    for i, row in enumerate(matrix):
        print(vertices[i] + " " + " ".join(map(str, row)))

vertices, adj_matrix = create_adjacency_matrix(graph)
display_adjacency_matrix(vertices, adj_matrix)
