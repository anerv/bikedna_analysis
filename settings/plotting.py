import matplotlib as mpl
from matplotlib import cm, colors

import matplotlib_inline.backend_inline


def set_renderer(f="svg"):
    matplotlib_inline.backend_inline.set_matplotlib_formats(f)


# Plot and map renderers
# Change renderer_map to svg to get crisp maps with the full vector data.
# Do this only for small areas (sub-city) due to html/pdf size explosion!
renderer_map = "png"
renderer_plot = "svg"

# Plot parameters
mpl.rcParams["savefig.bbox"] = "tight"
mpl.rcParams["xtick.minor.visible"] = False
mpl.rcParams["xtick.major.size"] = 0
mpl.rcParams["xtick.labelbottom"] = True
mpl.rcParams["ytick.major.size"] = 3
mpl.rcParams["font.size"] = 10
mpl.rcParams["figure.titlesize"] = 10
mpl.rcParams["legend.title_fontsize"] = 10
mpl.rcParams["legend.fontsize"] = 9
# mpl.rcParams["figure.labelsize"] = 10 # use if figure.titlesize does not work?
mpl.rcParams["axes.labelsize"] = 10
mpl.rcParams["xtick.labelsize"] = 9
mpl.rcParams["ytick.labelsize"] = 9
mpl.rcParams["hatch.linewidth"] = 0.5


pink = "#c82582"
green = "#539725"
orange = "#f87d2a"
light_orange = "#fd9c51"
dark_orange = "#a23403"
purple = "#796eb2"
light_purple = "#abaad1"
dark_purple = "#52238d"

blue = "#3787c0"
light_blue = "#82badb"
dark_blue = "#084d97"

red = "#e32f27"
light_red = "#f6553d"
dark_red = "#9e0d14"


# pdict for plotting styles
pdict = {
    "compare_base": "black",  # "dimgray",
    "osm_base": purple,  # base: for nodes and edges
    "ref_base": orange,  # base: for nodes and edges
    "fsmap": (13, 7.3125),
    "fsbar_small": (4, 3.5),
}
