# Analysis of BikeDNA Denmark

This repository contains the code for analyzing the results from running [BikeDNA](https://github.com/anerv/BikeDNA) on nationwide data for Denmark, comparing data from [OpenStreetMap](https://www.openstreetmap.org/) (OSM) and [GeoDenmark](https://www.geodanmark.dk/).

WHAT IT FOCUSES ON - spatial patterns

3. run data folder script
4. Add input data
    - muni
    - pop data

5. Run notebooks

## 0. Run BikeDNA

The first step is to successfuly run BikeDNA doing both intrinsic and extrinsic analysis of OSM and GeoDanmark data.

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
python setup_folders.py
```

This should return:

```python
Successfully created folder data/
Successfully created folder results/
Successfully created folder data/municipalities/
Successfully created folder data/population/
Successfully created folder results/compare_analysis/
Successfully created folder results/osm_analysis/
Successfully created folder results/ref_analysis/
...
```

To validate that the results and data were successfully copied to this directory, check that the `results` folder now contains a subfolder `reference` and `osm` with content matching the output of BikeDNA.

### Provide/Prepare data sets

# UPDATE - provide population rasters and municipality data

Once the folders have been created, provide:  

- a polygon defining the study area  
- for the extrinsic analysis (optional): a reference data set

## III. Analysis

### Notebooks

All analysis notebooks are in the [`scripts`](scripts) folder.

# TODO

### Population

### OSM

- osm_muni
- osm_tags

### GeoDanmark

- geodanmark muni

### Compare

- analysis-compare
- analysis-muni

# TODO UPDATE WARNING
>
> **Warning**
> Most notebooks can be run independently, but both they must both be run before the notebooks under 'Compare'.

## Get in touch

Do you have any questions or feedback?
Reach us at <anev@itu.dk> (Ane Rahbek Vierø) or <anvy@itu.dk> (Anastassia Vybornova).

## Data & Licenses

**Our code is free to use and repurpose under the [AGPL 3.0 license](https://www.gnu.org/licenses/agpl-3.0.html).**

The repository includes test data from the following sources:

### OpenStreetMap

© OpenStreetMap contributors  
License: [Open Data Commons Open Database License](https://opendatacommons.org/licenses/odbl/)

### GeoDanmark

Contains data from GeoDanmark (retrieved spring 2022)
© SDFE (Styrelsen for Dataforsyning og Effektivisering og Danske kommuner)  
License: [GeoDanmark](https://www.geodanmark.dk/wp-content/uploads/2022/08/Vilkaar-for-brug-af-frie-geografiske-data_GeoDanmark-grunddata-august-2022.pdf)

## Credits

Supported by the Danish Road Directorate.
