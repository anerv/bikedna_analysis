from pysal.lib import weights
import pandas as pd
import geopandas as gpd
import pickle
import os.path

exec(open("../settings/yaml_variables.py").read())
exec(open("../settings/paths.py").read())


if os.path.isfile(osm_grid_spatial_weights_fp):

    pass

else:

    # Read intrinsic grid results
    with open(
        f"../results/OSM/{study_area}/data/grid_results_intrinsic.pickle", "rb"
    ) as fp:
        osm_int_grid = pickle.load(fp)

    osm_int_grid.dropna(subset="count_osm_edges", inplace=True)

    # convert to centroids
    cents = osm_int_grid.centroid

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

    adj_list.to_csv(osm_grid_spatial_weights_fp, index=False)
