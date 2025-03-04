from d3graph import d3graph
import os
size = [10, 20, 10, 10, 15, 10, 5]

# Initialize
d3 = d3graph()
# Load example
adjmat = d3.import_example('bigbang')
# Process adjmat
d3.graph(adjmat)
# Get script directory and save the file in the same folder
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "bigbang_graph.html")

# Show and save
d3.show(filepath=output_path)

print(f"Graph saved at: {output_path}")