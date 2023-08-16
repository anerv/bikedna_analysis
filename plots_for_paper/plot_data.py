# %%
"""
Export data sets for maps made in QGIS
"""

import geopandas as gpd
import pickle
import pandas as pd

exec(open("../settings/paths.py").read())
exec(open("../settings/yaml_variables.py").read())
# %%
# Table for paper

osm_muni = pd.read_csv(
    osm_analysis_data_fp + "muni_network_counts.csv", index_col=False
)
ref_muni = pd.read_csv(
    ref_analysis_data_fp + "muni_network_counts.csv", index_col=False
)

osm_muni.set_index("navn", inplace=True)
ref_muni.set_index("navn", inplace=True)

osm_muni.fillna(0, inplace=True)
ref_muni.fillna(0, inplace=True)

cols = ["infrastructure_length", "infra_dens", "component_count"]
merged = osm_muni[cols].merge(
    ref_muni[cols], left_index=True, right_index=True, suffixes=("_osm", "_geodk")
)

assert len(merged) == 98

merged["Difference in infrastructure length"] = round(
    merged.infrastructure_length_geodk - merged.infrastructure_length_osm, 0
)
merged["Difference in infrastructure length"] = merged[
    "Difference in infrastructure length"
].astype(int)
merged["Percent difference"] = round(
    100
    * (merged.infrastructure_length_geodk - merged.infrastructure_length_osm)
    / merged.infrastructure_length_osm,
    2,
)

merged["infrastructure_length_osm"] = round(merged.infrastructure_length_osm)
merged["infrastructure_length_geodk"] = round(merged.infrastructure_length_geodk)

merged["infrastructure_length_osm"] = merged.infrastructure_length_osm.astype(int)
merged["infrastructure_length_geodk"] = merged.infrastructure_length_geodk.astype(int)

rename_dict = {
    "infrastructure_length_osm": "Infrastructure length (OSM)",
    "infrastructure_length_geodk": "Infrastructure length (GeoDK)",
    "infra_dens_osm": "Infrastructure density (OSM)",
    "infra_dens_geodk": "Infrastructure density (GeoDK)",
    "component_count_osm": "Components (OSM)",
    "component_count_geodk": "Components (GeoDK)",
}
merged.rename(columns=rename_dict, inplace=True)

merged.index.rename("Municipality", inplace=True)

reorder_cols = [
    "Infrastructure length (OSM)",
    "Infrastructure length (GeoDK)",
    "Difference in infrastructure length",
    "Percent difference",
    # "Infrastructure density (OSM)",
    # "Infrastructure density (GeoDK)",
    # "Components (OSM)",
    # "Components (GeoDK)",
]

final_df = merged[reorder_cols]
final_df.to_csv("../data_for_maps/muni_overview.csv", index=True)


# %%

# Municipal infrastructure density with geometries

osm_muni = pd.read_csv(
    osm_analysis_data_fp + "muni_network_counts.csv", index_col=False
)
ref_muni = pd.read_csv(
    ref_analysis_data_fp + "muni_network_counts.csv", index_col=False
)

munis = osm_muni.merge(
    ref_muni, left_on="navn", right_on="navn", suffixes=("_osm", "_ref")
)

munis["edge_dens_diff"] = munis.infra_dens_ref - munis.infra_dens_osm

munis_geom = gpd.read_file(muni_polygons_fp)
munis_geom = munis_geom.merge(munis, left_on="navn", right_on="navn", how="inner")

assert len(munis_geom) == 98
assert len(munis_geom.navn.unique()) == 98

# %%
munis_geom["comp_per_km_diff"] = munis_geom.comp_per_km_ref - munis_geom.comp_per_km_osm
# %%
munis_geom.to_file("../data_for_maps/municipality_data.gpkg")
# %%
# OSM INTRINSIC GRID + TAG SPATIAL AUTO

# Read intrinsic grid results
with open(
    f"../results/OSM/{study_area}/data/grid_results_intrinsic.pickle", "rb"
) as fp:
    osm_intrinsic_grid = pickle.load(fp)

osm_intrinsic_grid.dropna(subset="count_osm_edges", inplace=True)

tags_sa = pd.read_csv(osm_analysis_fp + "tags_spatial_autocorrelation.csv")

intrinsic_grid_tags = osm_intrinsic_grid[["geometry", "hex_id"]].merge(
    tags_sa, left_on="hex_id", right_on="hex_id", how="left"
)

assert len(intrinsic_grid_tags) == len(osm_intrinsic_grid)

intrinsic_grid_tags.to_file("intrinsic_grid_tags.gpkg")

# %%
# GRID WITH EDGE DENSITY DIFF TO GEOPACKAGE

with open("../results/compare/dk/data/grid_results_extrinsic.pickle", "rb") as fp:
    extrinsic_grid = pickle.load(fp)


density_diff_sa = pd.read_csv(
    "../results/compare_analysis/dk/data/density_spatial_autocorrelation.csv"
)
density_diff_sa = density_diff_sa[["hex_id", "infrastructure_density_difference_q"]]

extrinsic_grid = extrinsic_grid.merge(
    density_diff_sa, left_on="hex_id_osm", right_on="hex_id", how="left"
)

extrinsic_grid["comp_count_diff"] = (
    extrinsic_grid.component_count_ref - extrinsic_grid.component_count_osm
)

extrinsic_grid.loc[
    (extrinsic_grid.component_count_ref == 0)
    | (extrinsic_grid.component_count_osm == 0),
    ["comp_count_diff"],
] = pd.NA

# %%
cols = [
    "grid_id",
    "geometry",
    "count_osm_edges",
    "count_ref_edges",
    "component_count_ref",
    "component_count_osm",
    "osm_edge_density",
    "ref_edge_density",
    "edge_density_diff",
    "infrastructure_density_difference_q",
    "comp_count_diff",
]

extrinsic_grid[cols].to_file("../data_for_maps/extrinsic_grid.gpkg")

# %%

with open("../results/compare/dk/data/grid_results_extrinsic.pickle", "rb") as fp:
    extrinsic_grid = pickle.load(fp)

osm_fm_sa = pd.read_csv(
    "../results/compare_analysis/dk/data/osm_fm_spatial_autocorrelation.csv"
)

osm_fm_sa = osm_fm_sa[
    [
        "hex_id",
        "osm_matched_q",
        "osm_unmatched_q",
        "osm_matched_pct_q",
        "osm_unmatched_pct_q",
    ]
]


fm_grid = extrinsic_grid.merge(
    osm_fm_sa, left_on="hex_id_osm", right_on="hex_id", how="left"
)

ref_fm_sa = pd.read_csv(
    "../results/compare_analysis/dk/data/ref_fm_spatial_autocorrelation.csv"
)
ref_fm_sa = ref_fm_sa[
    [
        "hex_id",
        "geodk_matched_q",
        "geodk_unmatched_q",
        "geodk_matched_pct_q",
        "geodk_unmatched_pct_q",
    ]
]

fm_grid = fm_grid.merge(ref_fm_sa, left_on="hex_id_osm", right_on="hex_id", how="left")

assert len(extrinsic_grid) == len(fm_grid)

cols = [
    "geometry",
    "grid_id",
    "geodk_matched_q",
    "geodk_unmatched_q",
    "geodk_matched_pct_q",
    "geodk_unmatched_pct_q",
    "osm_matched_q",
    "osm_unmatched_q",
    "osm_matched_pct_q",
    "osm_unmatched_pct_q",
    "count_osm_edges",
    "count_ref_edges",
]


fm_grid[cols].to_file("../data_for_maps/fm_grid.gpkg")
# %%
# GRID WITH OSM TAG RESULTS TO GEOPACKAGE
with open("../results/osm/dk/data/grid_results_intrinsic.pickle", "rb") as fp:
    osm_int_grid = pickle.load(fp)

cols = [
    "hex_id",
    "geometry",
    "count_osm_edges",
    "existing_tags_surface_count",
    "existing_tags_surface_length",
    "existing_tags_width_count",
    "existing_tags_width_length",
    "existing_tags_speedlimit_count",
    "existing_tags_speedlimit_length",
    "existing_tags_lit_count",
    "existing_tags_lit_length",
    "existing_tags_sum",
    "existing_tags_surface_count_pct",
    "existing_tags_surface_count_pct_missing",
    "existing_tags_surface_length_pct",
    "existing_tags_surface_length_pct_missing",
    "existing_tags_width_count_pct",
    "existing_tags_width_count_pct_missing",
    "existing_tags_width_length_pct",
    "existing_tags_width_length_pct_missing",
    "existing_tags_speedlimit_count_pct",
    "existing_tags_speedlimit_count_pct_missing",
    "existing_tags_speedlimit_length_pct",
    "existing_tags_speedlimit_length_pct_missing",
    "existing_tags_lit_count_pct",
    "existing_tags_lit_count_pct_missing",
    "existing_tags_lit_length_pct",
    "existing_tags_lit_length_pct_missing",
]

osm_int_grid[cols].to_file("../data_for_maps/osm_grid.gpkg")

# %%

# LARGEST CONNECTED COMPONENT EDGES
osm_com_edges = gpd.read_parquet(
    "../results/osm/dk/data/largest_connected_component.parquet"
)

osm_com_edges.to_file("../data_for_maps/osm_largest_cc.gpkg")


ref_com_edges = gpd.read_parquet(
    "../results/reference/dk/data/largest_connected_component.parquet"
)

ref_com_edges.to_file("../data_for_maps/ref_largest_cc.gpkg")


# ALL COMPONENT EDGES
osm_com_edges = gpd.read_parquet(
    "../results/osm/dk/data/osm_edges_component_id.parquet"
)

osm_com_edges.to_file("../data_for_maps/osm_comp_edges.gpkg")

ref_com_edges = gpd.read_parquet(
    "../results/reference/dk/data/ref_edges_component_id.parquet"
)

ref_com_edges.to_file("../data_for_maps/ref_comp_edges.gpkg")

# FEATURE MATCHING RESULTS
buffer_dist = 15
hausdorff_threshold = 17
angular_threshold = 30

compare_results_data_fp = "../results/compare/dk/data/"

osm_matched_segments = gpd.read_parquet(
    compare_results_data_fp
    + f"osm_matched_segments_{buffer_dist}_{hausdorff_threshold}_{angular_threshold}.parquet"
)
osm_unmatched_segments = gpd.read_parquet(
    compare_results_data_fp
    + f"osm_unmatched_segments_{buffer_dist}_{hausdorff_threshold}_{angular_threshold}.parquet"
)
ref_matched_segments = gpd.read_parquet(
    compare_results_data_fp
    + f"ref_matched_segments_{buffer_dist}_{hausdorff_threshold}_{angular_threshold}.parquet"
)
ref_unmatched_segments = gpd.read_parquet(
    compare_results_data_fp
    + f"ref_unmatched_segments_{buffer_dist}_{hausdorff_threshold}_{angular_threshold}.parquet"
)

osm_matched_segments.to_file("../data_for_maps/osm_matched.gpkg")
osm_unmatched_segments.to_file("../data_for_maps/osm_unmatched.gpkg")
ref_matched_segments.to_file("../data_for_maps/ref_matched.gpkg")
ref_unmatched_segments.to_file("../data_for_maps/ref_unmatched.gpkg")

# %%

"""
Recreate plots for paper
"""
# Network density grid plots

from src import plotting_functions as plot_func

exec(open("../settings/yaml_variables.py").read())
exec(open("../settings/plotting.py").read())
exec(open("../settings/paths.py").read())

# %%
set_renderer("svg")

grid = extrinsic_grid

plot_cols = ["edge_density_diff"]

plot_titles = [
    area_name + f": {reference_name} edge density differences to OSM (m/km2)",
]
filepaths = [
    compare_results_static_maps_fp + "edge_density_compare",
]

cmaps = [pdict["diff"]]

# Cols for no-data plots
no_data_cols = [
    ("osm_edge_density", "ref_edge_density"),
]

cblim_edge = max(
    abs(min(grid["edge_density_diff"].fillna(value=0))),
    max(grid["edge_density_diff"].fillna(value=0)),
)

norm_min = [-cblim_edge]
norm_max = [cblim_edge]

plot_func.plot_grid_results(
    grid=grid,
    plot_cols=plot_cols,
    plot_titles=plot_titles,
    filepaths=filepaths,
    cmaps=cmaps,
    alpha=pdict["alpha_grid"],
    cx_tile=cx_tile_2,
    no_data_cols=no_data_cols,
    use_norm=True,
    norm_min=norm_min,
    norm_max=norm_max,
)

# %%
# UNDERSHOOTS

osm_nodes_simplified = gpd.read_parquet(osm_nodes_simplified_fp)
ref_nodes_simplified = gpd.read_parquet(ref_nodes_simplified_fp)

osm_undershoots_ids = pd.read_csv(osm_results_data_fp + "undershoot_nodes_3.csv")
ref_undershoots_ids = pd.read_csv(ref_results_data_fp + "undershoot_nodes_3.csv")

osm_undershoots = osm_nodes_simplified.loc[
    osm_nodes_simplified.osmid.isin(osm_undershoots_ids.node_id.to_list())
]

ref_undershoots = ref_nodes_simplified.loc[
    ref_nodes_simplified.nodeID.isin(ref_undershoots_ids.node_id.to_list())
]

assert len(osm_undershoots) == len(osm_undershoots_ids)
assert len(ref_undershoots) == len(ref_undershoots_ids)
# %%
osm_undershoots[["geometry"]].to_file("osm_undershoots.gpkg")
ref_undershoots[["geometry"]].to_file("ref_undershoots.gpkg")

# %%
