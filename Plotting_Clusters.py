#code used to generate and plot clusters

import pandas as pd
from tcrdist.repertoire import TCRrep
from igraph import Graph
import igraph as ig
import matplotlib.pyplot as plt
import numpy as np

# File path
file_path = "YOUR_FILE_PATH_HERE"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Create a color dictionary for each unique clone_id
unique_clone_ids = df['clone_id'].unique()
color_dict = {clone_id: tuple(np.random.rand(3,)) for clone_id in unique_clone_ids} 

# Create TCRrep object from TCRdist3. This example uses the alpha chain, replace 'chains' to beta if you wish to analyse beta chain.

tr = TCRrep(
    cell_df=df,
    organism='human',
    chains=['alpha'],
    deduplicate=False,
    db_file='alphabeta_gammadelta_db.tsv'
)

# Get the pairwise distance matrix for alpha chain. replace this if you want to analysis the beta chain
x = tr.pw_alpha

# Replace diagonals with 200
np.fill_diagonal(x, 200)

# Set the threshold
th = 25

# Create adjacency matrix
adj_m_comb = (x < th).astype(int)

# Create the graph
g = Graph.Adjacency(adj_m_comb.tolist(), mode='lower', loops=False)

# Assign 'clone_id' values to the graph vertices
g.vs['clone_id'] = df['clone_id'].values

# Define vertex colors based on 'clone_id'
vc = [color_dict[clone_id] for clone_id in g.vs['clone_id']]

# Identify subclusters or subgraphs within a graph
cl = g.connected_components()
g_cl = cl.subgraphs()

# Plotting a specific subgraph (cluster)
subgraph_index_to_plot = 14  # Change this index as needed
subgraph_to_plot = g_cl[subgraph_index_to_plot]

# Plot the subgraph
plt.close()
fig, ax = plt.subplots(figsize=(5, 5))
ig.plot(subgraph_to_plot, vertex_size=12, target=ax, method='kk', vertex_color=vc)

# # Save the plot as a PNG file (specify your own path and file name)
# plt.savefig("YOUR_FILE_PATH_HERE")

# Show the plot
plt.show()
