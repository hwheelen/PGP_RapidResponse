import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

#set paths for different shapefiles
blocks = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/census blocks with data/GABlocksDemographicBreakdown.geojson')
sen_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE14/SENATE14-Shape.shp')
sen12_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE12/SENPROP1-SHAPE.shp')
house_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/HOUSE15/HOUSE15.shp')
cong_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/CONGRESS12/CONGPROP2.shp')


#make list of maps to work on
maps = [sen_map, sen12_map, house_map, cong_map]

#set district maps to same crs as blocks
for map in maps:
    map = map.to_crs(blocks.crs)

#make list of columns we want to aggregate from the blocks to the districts
cols = ['tot', 'NHwhite', 'NHblack', 'hispanic', 'totVAP','WVAP', 'BVAP', 'HVAP']
blocks[cols] = blocks[cols].astype(float)

#run aggregate function that does spatial aggregation
aggregated_sen = ai.aggregate(blocks,sen_map, source_columns=cols)[1] 
aggregated_sen12 = ai.aggregate(blocks,sen12_map, source_columns=cols)[1] 
aggregated_house = ai.aggregate(blocks,house_map, source_columns=cols)[1] 
aggregated_cong = ai.aggregate(blocks,cong_map, source_columns=cols)[1] 

#check that totals match
block_total = blocks['tot'].sum()
print('block tot',block_total)
sen_total = aggregated_sen['tot'].sum()
print('sen tot',sen_total)
sen12_total = aggregated_sen12['tot'].sum()
print('sen12 tot',sen12_total)
house_total = aggregated_house['tot'].sum()
print('house tot',house_total)
cong_total = aggregated_cong['tot'].sum()
print('congressional tot',cong_total)

aggregated_sen.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE14/with census data/GA_Senate_Map_demo_breakdown.shp')
aggregated_sen12.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE12/with census data/GA_Senate12_Map_demo_breakdown.shp')
aggregated_house.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/HOUSE15/with census data/GA_House_Map_demo_breakdown.shp')
aggregated_cong.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/CONGRESS12/with census data/GA_Congressional_Map_demo_breakdown.shp')
