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

#Uses the thresholds 0, 2, 5, 10, 15, 20, 25, 30, 35 to work out the sum of the adjacency matrix/ Number of Edges


thresholds = [0, 2, 5, 10, 15, 20, 25, 30, 35]

# Iterate through thresholds
for th in thresholds:
    adj_m_comb=( distance_matrix < th).astype(int)
    flattened_list = [item for sublist in adj_m_comb for item in sublist]
    array_sum = sum(flattened_list)
    print(f" {th}, Sum of adj_m_comb: {array_sum} ")
