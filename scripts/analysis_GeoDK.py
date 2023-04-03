'''
TODO: Summary of REFERENCE intrinsic analysis
- everything in intrinsic summary? - read results, redo tables

TODO: Analysis of spatial autocorrelation of:
- over/undershoots
- potential missing edges/component connections

Always - make plots
Export results to txt/csv/json

'''

# TODO: Look into correlation between number of errors and km of bicycle infra

# TODO: Spatial autocorrelation in over/under - use distance band, non-binary, K-nearest with max band?

#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import pickle
import json
import pandas as pd

%run ../settings/yaml_variables.py
%run ../settings/df_styler.py
%run ../settings/plotting.py
%run ../settings/load_refdata.py

#%%
# Read intrinsic grid results
with open(
    f"../results/REFERENCE/{study_area}/data/grid_results_intrinsic.pickle", "rb"
) as fp:
    ref_intrinsic_grid = pickle.load(fp)

# Import intrinsic results
ref_intrinsic_file = open(
    f"../results/REFERENCE/{study_area}/data/intrinsic_analysis.json"
)

ref_intrinsic_results = json.load(ref_intrinsic_file)

# Import summary dataframe
summarize_results_df = pd.read_csv(f"../results/REFERENCE/{study_area}/data/intrinsic_summary_results.csv",index_col=0)

summarize_results_df.style.pipe(format_ref_style)

#%%
# Assign municipal name and id to each hex cell based on centroid overlap
muni = gpd.read_file("../data/municipalities.gpkg")
muni = muni[['navn','kommunekode','geometry']]
assert muni.crs == study_crs
#%%
ref_intrinsic_grid.dropna(subset='count_ref_edges',inplace=True)

grid_centroids = ref_intrinsic_grid[['geometry','grid_id','count_ref_edges']].copy()
grid_centroids['geometry'] = grid_centroids.geometry.centroid

centroid_join = grid_centroids.sjoin(muni, predicate="intersects", how="inner")
centroid_join.drop('index_right',axis=1,inplace=True)

non_joined_centroid = grid_centroids[grid_centroids.count_ref_edges.notna() & ~grid_centroids.grid_id.isin(centroid_join.grid_id)] #drop(['navn','kommunekode'],axis=1)

centroid_join_2 = non_joined_centroid.sjoin_nearest(muni, how="left",distance_col='dist')

assert len(centroid_join_2) + len(centroid_join) == len(ref_intrinsic_grid)

joined_int_grid = pd.concat([centroid_join_2,centroid_join])

assert len(joined_int_grid) == len(ref_intrinsic_grid)

int_grid = ref_intrinsic_grid.merge(joined_int_grid[['grid_id','navn','kommunekode']],left_on='grid_id',right_on='grid_id')
assert len(int_grid) == len(ref_intrinsic_grid)

#%%
# Index nodes and edges by municipality
muni_edges = ref_edges_simplified.sjoin(muni,how="left",predicate="intersects")
muni_edges.drop('index_right',axis=1,inplace=True)

nodes_joined = gpd.sjoin(muni, ref_nodes_simplified, how="right",predicate="contains")
nodes_joined.drop('index_left',axis=1,inplace=True)

nodes_joined_2 = gpd.sjoin_nearest(muni, nodes_joined[nodes_joined.navn.isna()][['nodeID','x','y','geometry']], how='right', distance_col="dist")
nodes_joined_2.drop('index_left',axis=1,inplace=True)
nodes_joined_2 = nodes_joined_2.drop_duplicates(subset='nodeID', keep="first")

nodes_joined.dropna(subset='navn',inplace=True)

muni_nodes = pd.concat([nodes_joined,nodes_joined_2])

assert len(muni_nodes) == len(muni_nodes.nodeID.unique())
assert len(muni_nodes[muni_nodes.navn.isna()]) == 0
assert len(muni_edges[muni_edges.navn.isna()]) == 0
#%%
# Group by muni
grouped_edges = muni_edges.groupby('navn') 
grouped_nodes = muni_nodes.groupby("navn")

#%%
muni_infra = grouped_edges['infrastructure_length'].sum()
muni_infra.sort_values()
#%%
muni_node_count = grouped_nodes.size()
muni_node_count.sort_values()
#%%
# TODO: Aggregate dangling nodes PER MUNI

# TODO: PLOT with seaborn

#%%

# TODO: Read in node ids of under/overshoots
# TODO: read nodes
# TODO: assign under/over to grid cells

# TODO: Same for missing edge comp

# TODO: Count number of over/under and potential missing edge/comp connc. per muni

# %%
