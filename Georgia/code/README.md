# Data Preperation for Historical Analysis of Gerrymandering in GA

This folder contains everything you need to take GA district shapefiles 
(like the ones found [here](https://data-hub.gio.georgia.gov/datasets/GARC::georgia-senate-districts)) 
and [census blocks](https://catalog.data.gov/dataset/tiger-line-shapefile-2017-2010-state-georgia-2010-census-block-state-based)
plus demographic data and [precinct level election results](https://openprecincts.org/ga/)
to assess how granular data about people has been used during line drawing. 

## Code
The following is a list of the scripts in the folder /code, by order of use
- [cenpy_script_GA.py](https://github.com/hwheelen/PGP_RapidResponse/blob/master/Georgia/code/cenpy_script_GA.py)
    Uses python package [cenpy](https://pypi.org/project/cenpy/) to download census data for GA.
- [aggregate_pop_GA.py](https://github.com/hwheelen/PGP_RapidResponse/blob/master/Georgia/code/aggregate_pop_GA.py)
    Adds census data into district maps, once it has manually been merged into census geographies
- [aggregate_precincts_GA.py](https://github.com/hwheelen/PGP_RapidResponse/blob/master/Georgia/code/aggregate_precincts_GA.py)
    Adds precinct data into district maps
- [extract_data_GA.py](https://github.com/hwheelen/PGP_RapidResponse/blob/master/Georgia/code/extract_data_GA.py)
    Pulls census and election data from aggregated district maps to prepare for generating figures
- [make_partisan_graphs_GA.py](https://github.com/hwheelen/PGP_RapidResponse/blob/master/Georgia/code/make_partisan_graphs_GA.py)
    Uses partisanship to generate figures showing packing and cracking
- [make_demograpghic_graphs_GA.py](https://github.com/hwheelen/PGP_RapidResponse/blob/master/Georgia/code/make_demographic_graphs_GA.py)
    Uses demographic information to generate figures showing packing and cracking


## Data
The /data folder contains outputs from the /extract_data.py script for all maps from 2011-2020
These are ready to be used to generate the figures in both generate_figures scripts
or other analysis or figure generation
