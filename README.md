<p align="center"><img src="images/BikeDNA_logo.svg" width="50%" alt="BikeDNA logo"/></p>

# Analysis of BikeDNA Denmark

This repository contains the code for analyzing the results from running [BikeDNA](https://github.com/anerv/BikeDNA), in a [version](https://github.com/anerv/BikeDNA_BIG) adapted for large data sets, on nationwide data for Denmark, comparing data from [OpenStreetMap](https://www.openstreetmap.org/) (OSM) and [GeoDanmark](https://www.geodanmark.dk/).

The analysis is an exploratory analysis focused on detecting spatial patterns in the data quality, looking at, for example, the correlations between administrative divisions and differences in data completeness, correlations between OSM tag quality and population density, and dentifying areas with large differences between the two data sources.

<!-- TODO: ADD FIGURE/ILLUSTRATION -->

## 0. Run BikeDNA

The first step is to successfuly run [BikeDNA BIG](https://github.com/anerv/BikeDNA_BIG) doing both intrinsic and extrinsic analysis of OSM and GeoDanmark data.

## I. Installation

First [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository (recommended) to your local machine or download it.

To avoid cloning the history and larger branches with example data and plots, use:

```python
git clone -b main --single-branch https://github.com/anerv/bikedna_dk_analysis --depth 1
```

### Create Python conda environment

To ensure that all packages needed for the analysis are installed, it is recommended to create and activate a new conda environment using the `environment.yml`:

```python
conda env create --file=environment.yml
conda activate bikedna_analysis
```

If this fails, the environment can be created by running:

```python
conda config --prepend channels conda-forge
conda create -n bikedna_analysis --strict-channel-priority geopandas pyarrow pandas folium pyyaml matplotlib contextily rasterio rioxarray jupyterlab ipykernel h3-py splot pysal plotly plotly_express
conda activate bikedna_analysis
```

*This method does not control the library versions and should be used as a last resort.*

The code for BikeDNA has been developed and tested using macOS 13.2.1.

### Install package

The repository has been set up using the structure described in the [Good Research Developer](https://goodresearch.dev/setup.html). Once the repository has been downloaded, navigate to the main folder in a terminal window and run the command

```python
pip install -e .
```

Lastly, add the environment kernel to Jupyter via:

```python
python -m ipykernel install --user --name=bikedna_analysis
```

Run Jupyter Lab or Notebook with kernel *bikedna* (Kernel > Change Kernel > bikedna_analysis).

## II. Setup

### Fill out the configuration file

In order to run the code, the configuration file [`config.yml`](config.yml) must be filled out. The config.yml on the main branch contains settings for, for example, CRS and the name of the study area used for folder structure setup, plot naming, and result labelling. The configuration file also specifies where to find the data and results from running BikeDNA (step 0).

Plot settings can be changed in [`scripts/settings/plotting.py`](scripts/settings/plotting.py).

### Set up the folder structure

Next, to create the required folder structure and to copy the results from running BikeDNA, navigate to the main folder in a terminal window and run the Python file `setup_folders_input_data.py`

```python
python setup_folders_input_data.py
```

This should return:

```python
...
Successfully created folder results/compare_analysis/
Successfully created folder results/osm_analysis/
Successfully created folder results/ref_analysis/
...
```

To validate that the results and data were successfully copied to this directory, check that the `results` folder now contains a subfolder `reference` and `osm` with content matching the output of BikeDNA.

### Provide/Prepare data sets

In addition to the input data from BikeDNA, the analysis makes use of:

* A dataset with muncipal boundaries: `municipalities.gpkg`
* A dataset with the total population in each municipality: `muni_pop.csv`
* Population rasters with the local population density

These data sets are already provided as part of this repository. If other datasets are to be used, once the folders have been created:

<!-- TODO: ADD THAT THEY ARE PROVIDED FOR THE STUDY AREA DK/DENMARK WITH CONFIG as is -->

* remove the existing data files
* place the files `municipalities.gpkg` and `muni_pop.csv` in the folder data > municipalities > 'study_area' > raw
* place the population rasters in the folder data > population > 'study_area' > raw
* specify the name of the population rasters in config.yml

>
> **Warning**
> The notebooks making use of the municipal and population input data are at the moment hardcoded to use the datasets provided on this reposity, with municipal boundaries for Denmark from Dataforsyningen, municipal population data from [Statistics Denmark](<https://www.dst.dk/da/>), and population rasters from the [Global Human Settlement Layer (GHSL)](<https://ghsl.jrc.ec.europa.eu/ghs_pop2023.php>).

## III. Analysis

### Notebooks

All analysis notebooks are in the [`scripts`](scripts) folder.

#### Population

* **`prepare_population_grid.ipynb`:** This notebook processes the population rasters and converts the data into H3 hexagons at the chosen resolutions.

#### OSM

* **`municipal_analysis_OSM.ipynb`:** The notebook indexes the results of the intrinsic analysis of OSM by municipality and examines correlations between municipality and high/low data quality.
* **`analyze_OSM_tags.ipynb`:** The notebook runs an analysis of spatial patterns in existing and missing tags in the OSM data.

#### GeoDanmark

* **`municipal_analysis_reference.ipynb`:** The notebook indexes the results of the intrinsic analysis of the GeoDanmark data by municipality and examines correlations between municipality and high/low data quality.

#### Compare

* **`extrinsic_analysis.ipynb`:** Looks at spatial patterns in differences between the two data sets, and contrats the findings with areas of high and low population density.
* **`municipal_comparison.ipynb`:** Compares the outcome of the notebooks looking at the quality and completeness at the municipal level.

Additionally, the scripts folder contain the notebook `explore_spatia_weights_sensitivity.ipynb` used to explore the sensitivity of the analysis of spatial patterns in infrastructure density differences to the definition of spatial weights.

<!-- TODO: ADD NOTE ABOUT DATA FOR QGIS PLOTS and QGIS PROJECT FILE -->

>
> **Warning**
> Most notebooks can be run independently, but both `municipal_analysis_OSM.ipynb` and `municipal_analysis_reference.ipynb` must be run before `municipal_comparison.ipynb`, and `pop_grid.ipynb` must be run before `extrinsic_analysis.ipynb`.

## Results

<!-- TODO: ADD GUIDE TO WHERE TO FIND RESULTS -->

## Get in touch

Do you have any questions or feedback?
Reach us at <anev@itu.dk> (Ane Rahbek Vierø) or <anvy@itu.dk> (Anastassia Vybornova).

## Data & Licenses

**Our code is free to use and repurpose under the [AGPL 3.0 license](https://www.gnu.org/licenses/agpl-3.0.html).**

The repository includes data from the following sources:

### OpenStreetMap

© OpenStreetMap contributors  
License: [Open Data Commons Open Database License](https://opendatacommons.org/licenses/odbl/)

Downloaded spring 2023.

### GeoDanmark

Contains data from GeoDanmark (retrieved spring 2022)
© SDFI (Styrelsen for Dataforsyning og Infrastruktur)  
License: [GeoDanmark](https://www.geodanmark.dk/wp-content/uploads/2022/08/Vilkaar-for-brug-af-frie-geografiske-data_GeoDanmark-grunddata-august-2022.pdf)

Downloaded spring 2023.

### Dataforsyningen

© SDFI (Styrelsen for Dataforsyning og Infrastruktur)
License: [Vilkår for brug af frie geografiske data](https://dataforsyningen.dk/asset/PDF/rettigheder_vilkaar/Vilk%C3%A5r%20for%20brug%20af%20frie%20geografiske%20data.pdf)

Downloaded spring 2023.

### Statistics Denmark

Contains data from Statistics Denmark - <https://statistikbanken.dk/folk1a>

Downloaded spring 2023.

### GHSL

Contains data from the European Commision's [GHSL (Global Human Settlement Layer)](https://ghsl.jrc.ec.europa.eu/download.php?ds=pop)

Schiavina M., Freire S., Carioli A., MacManus K. (2023):
GHS-POP R2023A - GHS population grid multitemporal (1975-2030).European Commission, Joint Research Centre (JRC).

Downloaded fall 2022.

## Credits

Supported by the Danish Road Directorate.
