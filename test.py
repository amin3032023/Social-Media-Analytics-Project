import numpy as np
from d3graph import d3graph

# Define an adjacency matrix as a NumPy array
# This matrix represents a simple graph with four nodes
# Nodes are connected based on the value being 1 or greater
adj_matrix = np.array([
    [0, 1, 0, 0],  # Connections from Node 1 to Node 2
    [1, 0, 1, 1],  # Connections from Node 2 to Nodes 1, 3, and 4
    [0, 1, 0, 1],  # Connections from Node 3 to Nodes 2 and 4
    [0, 1, 1, 0]   # Connections from Node 4 to Nodes 2 and 3
])

# Initialize the D3Graph object
d3 = d3graph()

# Generate the interactive graph
# The method uses the adjacency matrix to create a graph
# and automatically saves it to an HTML file in the current directory
d3.graph(adj_matrix)

# Inform the user that the graph has been generated
print("Graph has been generated. Check the current directory for the 'd3graph.html' file.")
