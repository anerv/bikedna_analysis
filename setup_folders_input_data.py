# Run this file while in the main folder

import os
import yaml
import shutil

with open(r"config.yml") as file:
    parsed_yaml_file = yaml.load(file, Loader=yaml.FullLoader)

    study_area = parsed_yaml_file["study_area"]


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


new_data_folders = main_folders[2:4]

for n in new_data_folders:
    for i in ["processed", "raw"]:
        folder = n + f"{study_area}/{i}/"
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Successfully created folder " + folder)

new_results_folders = main_folders[4:]

for n in new_results_folders:
    for i in ["data", "plots"]:
        folder = n + f"{study_area}/{i}/"
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Successfully created folder " + folder)


# TODO: muni and pop are filled manually

# TODO: copy data from bikedna folder - is there already a data folder? yes

# TODO: copy results folder over - make folder names lower case
# TODO: copy study area to data


source = f"{study_area}/processed/"
destination = f"../data/COMPARE/{study_area}/processed/"

files = os.listdir(source)

for f in files:
    shutil.move(source + f, destination)

source = f"{study_area}/results/"
destination = f"../results/COMPARE/{study_area}/data/"

files = os.listdir(source)

for f in files:
    shutil.move(source + f, destination)
