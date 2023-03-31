'''
TODO: Summary of REFERENCE intrinsic analysis
- everything in intrinsic summary? - read results, redo tables

TODO: Analysis of spatial autocorrelation of:
- over/undershoots
- potential missing edges/component connections

Always - make plots
Export results to txt/csv/json


'''

# TODO: Script for reading intrinsic results
# TODO: Code for redoing table

# TODO: Aggregate km of bicycle infra + nodes + dangling nodes PER MUNI
# TODO: Count number of over/under and potential missing edge/comp connc. per muni

# TODO: Look into correlation between number of errors and km of bicycle infra

# TODO: Spatial autocorrelation in over/under - use distance band, non-binary, K-nearest with max band?


#%%
import geopandas as gpd
import matplotlib.pyplot as plt
import pickle

#%%
%run ../settings/yaml_variables.py
#%%
# READ INTRINSIC GRID
with open(
    f"../results/REFERENCE/{study_area}/data/grid_results_intrinsic.pickle", "rb"
) as fp:
    ref_intrinsic_grid = pickle.load(fp)

# TODO: READ INTRINSIC RESULTS

# TODO: REDO TABLE
#%%