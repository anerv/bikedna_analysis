import folium
import geopandas as gpd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm, colors
import contextily as cx
from collections import Counter
from mpl_toolkits.axes_grid1 import make_axes_locatable
from IPython.display import Image, HTML, display


exec(open("../settings/yaml_variables.py").read())
exec(open("../settings/plotting.py").read())
# exec(open("../settings/tiledict.py").read())


def plot_scatter(
    df,
    metric_col,
    x="lng",
    y="lat",
    marker=".",
    alpha=1,
    figsize=(12, 8),
    colormap="viridis",
):
    """
    Helper function for plotting vectorized raster data from H3 tutorials: https://github.com/uber/h3-py-notebooks

    ...

    Arguments:
        df (dataframe): data to plot
        metric_col (str): name of column with variable to base colormap on
        x (str): name of column with x-coordinates
        y (str): name of column with y-coordinates
        marker (str): markertype for points
        alpha (numeric): value between 0 and 1 for transparency
        figsige (tuple): size of the figure
        colormap (str): colormap to use for plotting the metric_col

    Returns:
        None
    """
    df.plot.scatter(
        x=x,
        y=y,
        c=metric_col,
        title=metric_col,
        edgecolors="none",
        colormap=colormap,
        marker=marker,
        alpha=alpha,
        figsize=figsize,
    )
    plt.xticks([], [])
    plt.yticks([], [])


def plot_saved_maps(filepaths, figsize=pdict["fsmap"], alpha=None, plot_res=plot_res):
    """
    Helper function for printing saved plots/maps/images (up to two maps plotted side by side)

    Arguments:
        filepaths(list): list of filepaths of images to be plotted
        figsize(tuple): figsize
        alpha(list): list of len(filepaths) with values between 0-1 for setting the image transparency

    Returns:
        None
    """

    assert len(filepaths) <= 2, print(
        "This function cam plot max two images at a time!"
    )

    if plot_res == "low":
        filepaths = [f + ".png" for f in filepaths]

        fig = plt.figure(figsize=figsize)

        for i, f in enumerate(filepaths):
            img = plt.imread(f)
            ax = fig.add_subplot(1, 2, i + 1)

            if alpha is not None:
                plt.imshow(img, alpha=alpha[i])

            else:
                plt.imshow(img)

            ax.set_axis_off()

        fig.subplots_adjust(wspace=0)

    elif plot_res == "high":
        filepaths = [f + ".svg" for f in filepaths]

        filepaths.reverse()

        html_string = "<div class='row'></div>"

        for i, f in enumerate(filepaths):
            if alpha is None:
                img_html = "<img src='" + f + "'style='width:49%'> </img>"
                html_string = html_string[:17] + img_html + html_string[17:]

            else:
                if alpha[i] != 0:
                    img_html = "<img src='" + f + "'style='width:49%'> </img>"
                    html_string = html_string[:17] + img_html + html_string[17:]

        display(HTML(html_string))
