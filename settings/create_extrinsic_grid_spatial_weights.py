from pysal.lib import weights
import pandas as pd
import geopandas as gpd
import pickle
import os.path

exec(open("../settings/yaml_variables.py").read())
exec(open("../settings/paths.py").read())


if os.path.isfile(extrinsic_grid_spatial_weights_fp): 
    pass

else:
    # Read extrinsic grid results
    with open(compare_results_data_fp + f"grid_results_extrinsic.pickle", "rb") as fp:
        ex_grid = pickle.load(fp)

    ex_grid.dropna(subset="edge_density_diff", inplace=True)

    # convert to centroids
    cents = ex_grid.centroid

    # Extract coordinates into an array
    pts = pd.DataFrame({"X": cents.x, "Y": cents.y}).values

    # w = weights.distance.DistanceBand.from_array(
    #     pts, 1000, binary=False
    # )

    w = weights.distance.KNN.from_array(pts, k=6)

    # row standardize
    w.transform = "R"

    # sns.histplot(w.cardinalities, bins=10, kde=True);

    adj_list = w.to_adjlist()

    adj_list.to_csv(extrinsic_grid_spatial_weights_fp, index=False)
