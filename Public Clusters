# This code provides a template to identify the number of public clusters. Public Clusters are the number of clusters that meet the criteria of containing at least 3 TCRs from 3 individuals. 

import pandas as pd
from tcrdist.repertoire import TCRrep
from igraph import Graph, plot
import matplotlib.pyplot as plt
import numpy as np

# File path
file_path = "YOUR_FILE_PATH_HERE"
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Create TCRrep object
tr = TCRrep(
    cell_df=df,
    organism='human',
    chains=['alpha'],
    deduplicate=False,
    db_file='alphabeta_gammadelta_db.tsv'
)

# Get the pairwise distance matrix for alpha/beta chain
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

# Identify subclusters or subgraphs within a graph
cl = g.connected_components()
g_cl = cl.subgraphs()

# Count of subgraphs meeting the criteria of Public Clusters 
subgraphs_meeting_criteria_count = 0

# Iterate through subgraphs
for i, subgraph in enumerate(g_cl):
    # Get clone IDs from the subgraph
    clone_ids_subgraph = subgraph.vs['clone_id']
    
    # Select rows from DataFrame based on clone IDs in the subgraph
    subgraph_df = df[df['clone_id'].isin(clone_ids_subgraph)]
    
    # Count the number of TCRs from each unique clone_id within the subgraph
    clone_counts = subgraph_df['clone_id'].value_counts()

    # Check if there are at least 3 clone_ids with more than 3 TCRs
    if (clone_counts >= 3).sum() >= 3:
        subgraphs_meeting_criteria_count += 1

# Prints the number of Public Clusters
print("Number of subgraphs meeting the criteria:", subgraphs_meeting_criteria_count)
