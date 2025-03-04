import networkx as nx
import numpy as np
from d3graph import d3graph
import webbrowser
import random
import os

# Load the edge list from the SNAP Facebook dataset.
# Make sure to download "facebook_combined.txt" from SNAP and place it in the same directory.
G = nx.read_edgelist("facebook_combined.txt", nodetype=int)

# For demonstration purposes, randomly sample 100 nodes from the network.
sample_size = 300
nodes_sample = random.sample(list(G.nodes()), sample_size)

# Create a subgraph using the sampled nodes.
subG = G.subgraph(nodes_sample).copy()

# Sort the nodes to maintain a consistent order.
nodes_list = sorted(subG.nodes())

# Generate an adjacency matrix for the subgraph.
# Each entry with a value >= 1 represents an edge.
adj_matrix = nx.to_numpy_array(subG, nodelist=nodes_list)

# Initialize d3graph with interactive features:
d3 = d3graph()
# - slider: to filter edges based on weight,
# - double_click_highlight: to highlight a node and its edges on double-click.
graph = d3.graph(adj_matrix)

# Get script directory and save the file in the same folder
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "facebook_graph.html")

# Show and save
d3.show(filepath=output_path)

print(f"Graph saved at: {output_path}")
webbrowser.open(output_path)