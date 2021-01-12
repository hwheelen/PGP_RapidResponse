import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

#set paths for different shapefiles
prec_16 = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Georgia/2016/VEST/ga_2016/ga_2016.shp')
prec_18 = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Georgia/2018 Precincts/GA2018PrecElecs.shp')
blocks = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/census blocks with data/GABlocksDemographicBreakdown.geojson')

cols = ['G16PREDCli', 'G16PRELJoh', 'G16PRERTru', 'G16USSDBar', 'G16USSLBuc', 'G16USSRIsa', 'G16PSCLHos', 'G16PSCREch']
cols_blocks = ['tot', 'NHwhite',
       'NHblack', 'NHnat', 'NHasi', 'hispanic', 'totVAP', 'HVAP', 'WVAP',
       'BVAP', 'NatVAP', 'AVAP']
blocks[cols_blocks] = blocks[cols_blocks].astype(int)

prec_18.to_crs(blocks.crs)
prec_16.to_crs(blocks.crs)

aggregated = ai.aggregate(prec_16,blocks, source_columns=cols)[1] 

aggregated.to_file('/Users/hwheelen/Documents/GitHub/PGPRapidResponse/Georgia/shapefiles/blocks/GA_blocks_demog_18elecs.shp')

agg = ai.aggregate(aggregated,prec_18,source_columns=cols)[1]

agg = agg[['loc_prec', 'locality', 'prec_shp', 'prec_elec', 'G16PREDCli', 'G16PRELJoh', 'G16PRERTru', 'G16USSDBar',
       'G16USSLBuc', 'G16USSRIsa', 'G16PSCLHos', 'G16PSCREch', 'G18DATG', 'G18DCmAg',
       'G18DCmIns', 'G18DCmLab', 'G18DGOV', 'G18DLTG', 'G18DPbSrv', 'G18DSOS',
       'G18DSchSpr', 'G18DStSen', 'G18LCmIns', 'G18LGOV', 'G18LPbSrv',
       'G18LSOS', 'G18RATG', 'G18RCmAg', 'G18RCmIns', 'G18RCmLab', 'G18RGOV',
       'G18RLTG', 'G18RPbSrv', 'G18RSOS', 'G18RSchSpr', 'G18RStSen',
       'geometry']]

agg.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/precincts with census data/GA_precincts_16_18.shp')

agg_final = ai.aggregate(blocks, agg, source_columns = cols_blocks )[1]

agg_final.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/precincts with census data/final/GA_gerrychain_input.shp')
