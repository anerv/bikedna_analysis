import yaml

with open(r"../config.yml") as file:
    parsed_yaml_file = yaml.load(file, Loader=yaml.FullLoader)

    # Settings for plot resolution
    plot_res = parsed_yaml_file["plot_resolution"]

    # Settings for study area
    study_area = parsed_yaml_file["study_area"]
    area_name = parsed_yaml_file["area_name"]
    study_crs = parsed_yaml_file["study_crs"]

    # Settings for reference data
    reference_name = parsed_yaml_file["reference_name"]
