# -*- coding: utf-8 -*-"

import networkx as nx
import matplotlib.pyplot as plt

graph = {'A': ['B', 'C'], 'B': ['A'] ['D'], 'C': ['A'], 'D': ['B'] }
graph = {'A': ['B', 'C'], 'B': ['D'] ['E'], 'C': ['F'] ['G'], 'D': ['H'], 'E': [''],  'F': [''],  'G': [''],  'H': [''], }
graph = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F', 'G'] ['G'], 'D': ['B', 'H', 'I'], 'E': ['B', 'J', 'K'],  'F': ['C', 'H', 'L', 'M'],  'G': ['C', 'N', 'O'],  'H': ['D'], 'I': ['D'], 'J': ['E'], 'K': ['E'], 'L': ['F'], 'M': ['F'], 'N': ['G'], 'O': ['G'] }

G = nx.DiGraph(graph)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()
