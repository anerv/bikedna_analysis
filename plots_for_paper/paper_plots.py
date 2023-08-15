# %%
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
import pandas as pd
import math
from matplotlib.patches import Patch

exec(open("../settings/paths.py").read())
exec(open("../settings/yaml_variables.py").read())
exec(open("../settings/plotting.py").read())
# %%
grid_subset = gpd.read_file("../data_for_maps/grid_matching_density_subset.gpkg")

col_names = [
    "length_osm_matched",
    "length_osm_unmatched",
    "length_ref_matched",
    "length_ref_unmatched",
]

title_input = [
    "length of matched OSM segments",
    "length of unmatched OSM segments",
    "length of matched GeoDK segments",
    "length of unmatched GeoDK segments",
]


labels = {
    "osm_edge_density": "OSM infrastructure density m/sqkm",
    "ref_edge_density": "GeoDK infrastructure density m/sqkm",
    "edge_density_diff": "Differences in infrastructure density (GeoDK - OSM) (m/sqkm)",
    "length_osm_matched": "Matched OSM segments (m)",
    "length_osm_unmatched": "Unmatched OSM segments (m)",
    "length_ref_matched": "Matched GeoDK segments (m)",
    "length_ref_unmatched": "Unmatched GeoDK segments (m)",
}

for i, c in enumerate(col_names):
    fig = px.scatter(
        grid_subset,
        x="edge_density_diff",
        y=c,
        color_discrete_sequence=["black"],
        title=f"Correlation between infrastructure density difference and {title_input[i]}",
        labels=labels,
    )

    fig.update_layout(
        font=dict(size=12, color="black"), autosize=False, width=1000, height=800
    )
    fig.write_image(f"paper_illustrations/fm_dens_diff_{c}.jpeg")
    fig.show()
# %%
# PLOT OF LOCAL COMPONENT COUNT

# Read extrinsic grid results
with open(compare_results_data_fp + f"grid_results_extrinsic.pickle", "rb") as fp:
    extrinsic_grid = pickle.load(fp)

osm_comp_count = extrinsic_grid[["grid_id", "component_count_osm"]].copy()
osm_comp_count = osm_comp_count[osm_comp_count.component_count_osm > 0]

osm_comp_count["source"] = "OSM"
osm_comp_count.rename({"component_count_osm": "component_count"}, inplace=True, axis=1)

geodk_comp_count = extrinsic_grid[["grid_id", "component_count_ref"]].copy()
geodk_comp_count = geodk_comp_count[geodk_comp_count.component_count_ref > 0]

geodk_comp_count["source"] = "GeoDK"
geodk_comp_count.rename(
    {"component_count_ref": "component_count"}, inplace=True, axis=1
)

comp_count = pd.concat([osm_comp_count, geodk_comp_count])

assert len(comp_count) == len(osm_comp_count) + len(geodk_comp_count)

# comp_count_subset = comp_count[comp_count.component_count > 0]

labels = {"source": "Source", "component_count": "Components"}

fig = px.histogram(
    comp_count,
    x="component_count",
    color="source",
    labels=labels,
    nbins=18,
    opacity=[0.8],
    # text_auto=True,
    marginal="rug",
    color_discrete_sequence=["#796eb2", "#f87d2a"],
    # title="Distribution of local component count in OSM and GeoDanmark data",
)
fig.update_layout(
    font=dict(size=12, color="black"),
    autosize=False,
    width=800,
    height=600,
    yaxis_title="Count",
)
fig.write_image(f"paper_illustrations/component_count_distribution.jpeg")
fig.show()

# %%
import plotly.graph_objects as go

x0 = osm_comp_count.component_count.to_list()
x1 = geodk_comp_count.component_count.to_list()

fig = go.Figure()
fig.add_trace(go.Histogram(x=x0, marker_color="#796eb2", name="OSM"))
fig.add_trace(go.Histogram(x=x1, marker_color="#f87d2a", name="GeoDanmark"))

# Overlay both histograms
fig.update_layout(
    barmode="overlay",
    font=dict(size=12, color="black"),
    autosize=False,
    width=800,
    height=400,
    yaxis_title="Count",
    xaxis_title="Components",
    title="Distribution of local component count in OSM and GeoDanmark data",
)
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.6)

fig.show()

# %%
# Zipf plot of component lengths

set_renderer(renderer_plot)

osm_component_edges = gpd.read_parquet(
    osm_results_data_fp + "osm_edges_component_id.parquet"
)

grouped_osm_edges = osm_component_edges.groupby("component")

osm_components_length = {}
for comp_nr, group in grouped_osm_edges:
    osm_components_length[comp_nr] = group.length.sum()


assert len(osm_components_length) == len(grouped_osm_edges) == 10686

osm_components_df = pd.DataFrame.from_dict(osm_components_length, orient="index")
osm_components_df.rename(columns={0: "component_length"}, inplace=True)

geodk_component_edges = gpd.read_parquet(
    ref_results_data_fp + "ref_edges_component_id.parquet"
)

grouped_geodk_edges = geodk_component_edges.groupby("component")

geodk_components_length = {}
for comp_nr, group in grouped_geodk_edges:
    geodk_components_length[comp_nr] = group.length.sum()


assert len(geodk_components_length) == len(grouped_geodk_edges) == 4408

geodk_components_df = pd.DataFrame.from_dict(geodk_components_length, orient="index")
geodk_components_df.rename(columns={0: "component_length"}, inplace=True)


# %%
fig = plt.figure(figsize=pdict["fsbar_small"])
axes = fig.add_axes([0, 0, 1, 1])

axes.set_axisbelow(True)
axes.grid(True, which="major", ls="dotted")

geodk_yvals = sorted(list(geodk_components_df["component_length"] / 1000), reverse=True)

osm_yvals = sorted(list(osm_components_df["component_length"] / 1000), reverse=True)

axes.scatter(
    x=[i + 1 for i in range(len(osm_components_df))],
    y=osm_yvals,
    s=18,
    color=pdict["osm_base"],
)

axes.scatter(
    x=[i + 1 for i in range(len(geodk_components_df))],
    y=geodk_yvals,
    s=18,
    color=pdict["ref_base"],
)

y_min = min(min(osm_yvals), min(geodk_yvals))
y_max = max(max(osm_yvals), max(geodk_yvals))
axes.set_ylim(
    ymin=10 ** math.floor(math.log10(y_min)),
    ymax=10 ** math.ceil(math.log10(y_max)),
)
axes.set_xscale("log")
axes.set_yscale("log")

axes.set_ylabel("Component length [km]")
axes.set_xlabel("Component rank (largest to smallest)")

legend_patches = [
    Patch(
        facecolor=pdict["osm_base"], edgecolor=pdict["osm_base"], label="Color Patch"
    ),
    Patch(
        facecolor=pdict["ref_base"], edgecolor=pdict["ref_base"], label="Color Patch"
    ),
]

axes.legend(legend_patches, ["OSM", "GeoDanmark"])
axes.set_title("Component length distribution")

fig.savefig("paper_illustrations/zipf.svg")
# %%
