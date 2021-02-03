import pandas as pd
import geopandas as gpd
import numpy as np

#set filepath to district files with aggregated population and election data
sen_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE14/with election data/GA_Senate_Map.shp')
sen12_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE12/with election data/GA_Senate12_Map.shp')
house_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/HOUSE15/with election data/GA_House_Map.shp')
cong_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/CONGRESS12/with election data/GA_Congressional_Map.shp')


#extract demographic info and election data
cols = ['DISTRICT','tot', 'NHwhite',
       'NHblack', 'hispanic', 'totVAP', 'WVAP', 'BVAP', 'HVAP', 'G16PREDCli',
       'G16PRELJoh', 'G16PRERTru', 'G16USSDBar', 'G16USSLBuc', 'G16USSRIsa',
       'G16PSCLHos', 'G16PSCREch', 'G18DATG', 'G18DCmAg', 'G18DCmIns',
       'G18DCmLab', 'G18DGOV', 'G18DLTG', 'G18DPbSrv', 'G18DSOS', 'G18DSchSpr',
       'G18DStSen', 'G18LCmIns', 'G18LGOV', 'G18LPbSrv', 'G18LSOS', 'G18RATG',
       'G18RCmAg', 'G18RCmIns', 'G18RCmLab', 'G18RGOV', 'G18RLTG', 'G18RPbSrv',
       'G18RSOS', 'G18RSchSpr', 'G18RStSen', 'G20PRERTRU', 'G20PREDBID','G20PRELJOR', 
       'C20PRERTRU', 'C20PREDBID', 'C20PRELJOR', 'G20USSRPER','G20USSDOSS', 'G20USSLHAZ', 
       'S20USSRLOE', 'S20USSRCOL', 'S20USSRGRA','S20USSRJAC', 'S20USSRTAY', 'S20USSRJOH', 
       'S20USSDWAR', 'S20USSDJAC','S20USSDLIE', 'S20USSDJOH', 'S20USSDJAM', 'S20USSDSLA', 
       'S20USSDWIN','S20USSDTAR', 'S20USSLSLO', 'S20USSGFOR', 'S20USSIBUC', 'S20USSIBAR',
       'S20USSISTO', 'S20USSIGRE', 'G20PSCRSHA', 'G20PSCDBRY', 'G20PSCLMEL','G20PSCRMCD', 
       'G20PSCDBLA', 'G20PSCLWIL']

sen_csv = sen_df[cols]
sen12_csv = sen12_df[cols]
house_csv = house_df[cols]
cong_csv = cong_df[cols]


sen_csv.to_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_Senate_Map_estimates.csv')
sen12_csv.to_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_Senate12_Map_estimates.csv')
house_csv.to_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_House_Map_estimates.csv')
cong_csv.to_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_Congressional_Map_estimates.csv')


