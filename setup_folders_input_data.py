
# Run this file while in the main folder

# %%
import os
import yaml
import shutil

with open(r"config.yml") as file:
    parsed_yaml_file = yaml.load(file, Loader=yaml.FullLoader)

    study_area = parsed_yaml_file["study_area"]

# %%
main_folders = [
    "data2/",
    "results2/",
    "data2/municipalities/",
    "data2/population/",
    "results2/compare_analysis/",
    "results2/osm_analysis/",
    "results2/ref_analysis/",
]
for p in main_folders:
    if not os.path.exists(p):
        os.mkdir(p)
        print("Successfully created folder " + p)


# %%
new_data_folders = main_folders[2:4]

for n in new_data_folders:
    sa_folder = n + f"{study_area}/"
    if not os.path.exists(sa_folder):
        os.mkdir(sa_folder)
        print("Successfully created folder " + sa_folder)
    for i in ["processed", "raw"]:
        sa_subfolder = n + f"{study_area}/{i}/"
        if not os.path.exists(sa_subfolder):
            os.mkdir(sa_subfolder)
            print("Successfully created folder " + sa_subfolder)

# %%
new_results_folders = main_folders[4:]

for n in new_results_folders:
    sa_folder = n + f"{study_area}/"
    if not os.path.exists(sa_folder):
        os.mkdir(sa_folder)
        print("Successfully created folder " + sa_folder)

    for i in ["data", "plots"]:
        sa_subfolder = n + f"{study_area}/{i}/"
        if not os.path.exists(sa_subfolder):
            os.mkdir(sa_subfolder)
            print("Successfully created folder " + sa_subfolder)

# %%

# TODO: copy results folder over - make folder names lower case

source_data = "/Users/anev/Dropbox/ITU/repositories/bikedna_denmark/data/"
source_results = "/Users/anev/Dropbox/ITU/repositories/bikedna_denmark/results/"

sources = [source_data, source_results]

destination_data = "data2/"
destination_results = "results2/"

destinations = [destination_data, destination_results]

for s, d in zip(sources, destinations):
    files = os.listdir(s)

    for f in files:
        shutil.copyfile(s + f, d)
# %%
