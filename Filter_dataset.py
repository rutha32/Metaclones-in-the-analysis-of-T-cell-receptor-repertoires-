
# The code below can be used to filter the original dataset for Day 2 and Day 7, recent and remote infections, MAIT/GEM/iNKT cell types

########################################################################################################################################################################################################################################
#code to remove MAIT, GEM and iNKT cells. 

import pandas as pd

# File path
file_path = "YOUR_FILE_PATH_HERE"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Define conditions to identify MAIT, GEM and iNKT cells
mait_conditions = (df['v_a_gene'].str.startswith('TRAV1-2')) & (df['j_a_gene'].str.startswith(('TRAJ33', 'TRAJ12', 'TRAJ20')))
inkt_conditions = (df['v_a_gene'].str.startswith('TRAV10')) & (df['j_a_gene'].str.startswith('TRAJ18'))
gem_conditions = (df['v_a_gene'].str.startswith('TRAV1-2')) & (df['j_a_gene'].str.startswith('TRAJ9'))

# Store the removed rows for each cell type
removed_mait = df[mait_conditions]
removed_inkt = df[inkt_conditions]
removed_gem = df[gem_conditions]

# Concatenate removed rows into a single DataFrame
removed_all = pd.concat([removed_mait, removed_inkt, removed_gem])

# Remove rows corresponding to MAIT cells, iNKT cells, and GEM cells
filtered_df = df[~(mait_conditions | inkt_conditions | gem_conditions)]

# Save the filtered DataFrame to a CSV file
filtered_df.to_csv("YOUR_FILE_PATH_HERE", index=False)

# Save all the removed rows to a single CSV file
removed_all.to_csv("YOUR_FILE_PATH_HERE", index=False)

# Get counts of each cell type
mait_count = len(removed_mait)
inkt_count = len(removed_inkt)
gem_count = len(removed_gem)

print("Number of MAIT cells:", mait_count)
print("Number of iNKT cells:", inkt_count)
print("Number of GEM cells:", gem_count)


################################################################################################################################################################################################################################################


#day 2 and day 7 filtering 

import pandas as pd

# Assuming df is your original DataFrame
file_path = "YOUR_FILE_PATH_HERE"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Filter rows with 'time' column equal to 'D7'
df_d7 = df[df['time'] == 'D7']

# Filter rows with 'time' column equal to 'D2'
df_d2 = df[df['time'] == 'D2']

# Create new filtered DataFrames to separate files
df_d7.to_csv("YOUR_FILE_PATH_HERE", index=False)  # Change the file name as needed
df_d2.to_csv("YOUR_FILE_PATH_HERE", index=False)  # Change the file name as needed


###################################################################################################################################################################################################################################################
#code to filer recent and remote infections

# Remote Infection Filtering

import pandas as pd


alpha_tcr_df = pd.read_csv("YOUR_FILE_PATH_HERE")

# Read the 'id_of_recently_exposed.csv' file into a DataFrame 
id_df = pd.read_csv("YOUR_FILE_PATH_HERE"\id_of_remote_exposed.csv')

# Filter rows in alpha_tcr_df based on 'clone_id' column
filtered_alpha_tcr_df = alpha_tcr_df[alpha_tcr_df['clone_id'].isin(id_df['TCR_ID'])]


# Save the filtered DataFrame to a new CSV file 'alpha_tcrdist_recent.csv'
filtered_alpha_tcr_df.to_csv("YOUR_FILE_PATH_HERE", index=False)

#Recent infection Filtering

import pandas as pd

# Read the 'Alpha_Day_7_TST.csv' file into a DataFrame
alpha_tcr_df = pd.read_csv("YOUR_FILE_PATH_HERE"')

# Read the 'id_of_recently_exposed.csv' file into a DataFrame
id_df = pd.read_csv("YOUR_FILE_PATH_HERE"\id_of_recently_exposed.csv')

# Filter rows in alpha_tcr_df based on 'clone_id' column
filtered_alpha_tcr_df = alpha_tcr_df[alpha_tcr_df['clone_id'].isin(id_df['TCR_ID'])]


# Save the filtered DataFrame to a new CSV file 'alpha_tcrdist_recent.csv'
filtered_alpha_tcr_df.to_csv("YOUR_FILE_PATH_HERE", index=False)


