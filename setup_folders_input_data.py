# Run this file while in the main folder

import os
import yaml
import shutil

with open(r"config.yml") as file:
    parsed_yaml_file = yaml.load(file, Loader=yaml.FullLoader)

    study_area = parsed_yaml_file["study_area"]
    source_data = parsed_yaml_file["bikedna_data_filepath"]
    source_results = parsed_yaml_file["results_data_filepath"]


main_folders = [
    "data/",
    "results/",
    "data/municipalities/",
    "data/population/",
    "results/compare_analysis/",
    "results/osm_analysis/",
    "results/ref_analysis/",
]
for p in main_folders:
    if not os.path.exists(p):
        os.mkdir(p)
        print("Successfully created folder " + p)


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

sources = [source_data, source_results]

destination_data = "data/"
destination_results = "results/"

destinations = [destination_data, destination_results]

for src, dst in zip(sources, destinations):
    shutil.copytree(src, dst, dirs_exist_ok=True)
    print(f"Successfully copied data from {src} to {dst}")

folder_names = os.listdir("data/")
folder_names = ["data/" + f for f in folder_names]

for f in folder_names:
    os.rename(f, f.lower())

folder_names = os.listdir("results/")
folder_names = ["results/" + f for f in folder_names]

for f in folder_names:
    os.rename(f, f.lower())
