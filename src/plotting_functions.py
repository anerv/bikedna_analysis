import matplotlib.pyplot as plt


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
    Helper function from H3 tutorials: https://github.com/uber/h3-py-notebooks
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
