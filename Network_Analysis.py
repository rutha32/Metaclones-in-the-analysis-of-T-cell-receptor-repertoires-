# This code can you used for the network analysis code. It shows the 10 largest clusters and the number of nodes they have. It also computes the total number of all clusters and the Mean cluster size.



import pandas as pd
from tcrdist.repertoire import TCRrep

file_path = "YOUR_FILE_PATH_HERE"
df = pd.read_csv(file_path)

tr = TCRrep(
    cell_df=df,
    organism='human',
    chains=['alpha'],
    deduplicate = False,
    db_file='alphabeta_gammadelta_db.tsv'
)

x = tr.pw_alpha
x


#beta sample 1
import numpy as np
#call your distance matrix distance_matrix
#replace diagonals with 200 

distance_matrix = x
cm_i=np.diag_indices_from(distance_matrix)
distance_matrix [cm_i]=200



th = 25

# Iterate through thresholds

adj_m_comb=( distance_matrix < th).astype(int)
    # flattened_list = [item for sublist in adj_m_comb for item in sublist]
    # array_sum = sum(flattened_list)
    # print(f" {th}, Sum of adj_m_comb: {array_sum} ")



adj_m_comb


import pandas as pd
from igraph import Graph
import numpy as np

# Read CSV file into a DataFrame

df = pd.read_csv(file_path)

# Assuming 'counts' is a column in your DataFrame, replace it with the actual column name if different
counts = df['count']

# Create the adjacency matrix 'adj_m_comb' using your logic (not provided in the question)
# ...

# Create the graph
g = Graph.Adjacency(adj_m_comb, mode='lower', loops=False)

# Assign 'counts' values to the graph vertices
g.vs['count'] = counts.values

# Identify subclusters or subgraphs within a graph
cl = g.connected_components()

cl

import pandas as pd
import igraph as ig
import matplotlib.pyplot as plt

# Read CSV file into a DataFrame

df = pd.read_csv(file_path)

# Assuming 'counts' is a column in your DataFrame, replace it with the actual column name if different
counts = df['count']

# Create the adjacency matrix 'adj_m_comb' using your logic (not provided in the question)
# ...

# Create the graph
g = ig.Graph.Adjacency(adj_m_comb, mode='lower', loops=False)

# Assign 'counts' values to the graph vertices
g.vs['count'] = counts.values

# Identify subclusters or subgraphs within a graph
cl = g.connected_components()

# Sort subgraphs based on the number of nodes in descending order
sorted_subgraphs = sorted(enumerate(cl.subgraphs()), key=lambda x: -x[1].vcount())

# Store the first 10 subgraphs in a list
first_10_subgraphs = sorted_subgraphs[:10]

# Iterate through the first 10 subgraphs
for i, (original_index, subgraph) in enumerate(first_10_subgraphs):
    # Count the number of vertices in a subgraph
    n = subgraph.vcount()

    # Print the original subgraph index and the number of nodes
    print(f"Original Subgraph {original_index} - Number of Nodes: {n}")

    # Plotting a subgraph
    plt.close()
    fig, ax = plt.subplots(figsize=(5, 5))
    ig.plot(subgraph, vertex_size=2, target=ax, method='kk', vertex_color='red')
    plt.title(f'Original Subgraph {original_index} - Vertices: {n}')
    plt.tight_layout()


# Show the plots
plt.show()

# Store the remaining subgraphs in a list
remaining_subgraphs = sorted_subgraphs[10:]

# You can now use the 'remaining_subgraphs' list as needed.



#take an adjacency matrix (adj-m) and convert it into a graph  g
import igraph as ig
import matplotlib.pyplot as plt

#part i added 
default_color = 'red'

# Define vertex colors (all vertices will have the same color in this example)
vc = [default_color] * g.vcount()
##

g=ig.Graph.Adjacency(adj_m_comb, mode='lower',  loops=False)

#assign a value to a graph node; in this example we create a new attribute ‘counts’ which can hold the duplicate_counts value from the original TCR matrix.

g.vs['count']=counts.values

#identify subclusters or subgraphs (g_cl below)  within a graph – i.e. identify a set of connected vertices.

cl=g.connected_components()

#iterate this part of the code and work out n. 
g_cl=cl.subgraphs()

#count the number of vertices in a graph g

n=g.vcount()



# Read CSV file into a DataFrame

df = pd.read_csv(file_path)

# Assuming 'counts' is a column in your DataFrame, replace it with the actual column name if different
counts = df['count']

# Create the adjacency matrix 'adj_m_comb' using your logic (not provided in the question)
# ...

# Create the graph
g = ig.Graph.Adjacency(adj_m_comb, mode='lower', loops=False)

# Assign 'counts' values to the graph vertices
g.vs['count'] = counts.values

# Identify subclusters or subgraphs within a graph
cl = g.connected_components()

# Store the number of nodes in each subgraph
nodes_in_subgraphs = []

# Sort subgraphs based on the number of nodes in descending order
sorted_subgraphs = sorted(enumerate(cl.subgraphs()), key=lambda x: -x[1].vcount())

# Iterate through sorted subgraphs
for i, (original_index, subgraph) in enumerate(sorted_subgraphs):
    # Count the number of vertices in a subgraph
    n = subgraph.vcount()

    # Append the number of nodes to the list
    nodes_in_subgraphs.append(n)

#prints the number of all clusters
print("Number of Clusters", len(g_cl))


# Calculate the mean number of nodes in subgraphs
mean_nodes = sum(nodes_in_subgraphs) / len(nodes_in_subgraphs)
print(f"Mean Number of Nodes in Subgraphs: {mean_nodes}")





# Assuming you have a graph 'g' and its connected components 'cl'
cl = g.connected_components()

# Find subgraphs with a specific number of nodes (e.g., 1)
desired_node_count = 1
subgraphs_with_desired_node_count = [subgraph for subgraph in cl.subgraphs() if subgraph.vcount() == desired_node_count]

# Calculate the sum of node counts in subgraphs with the desired number of nodes
total_node_count = sum(subgraph.vcount() for subgraph in subgraphs_with_desired_node_count)

print(f"Total number of nodes in subgraphs with {desired_node_count} nodes: {total_node_count}")


