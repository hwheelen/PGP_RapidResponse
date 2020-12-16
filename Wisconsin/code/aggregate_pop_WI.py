import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

#set paths for different shapefiles
blocks = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Census Blocks with pop/WIBlocksDemBreakdown.shp')
sen_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Current Senate Districts/Shapefile/Wisconsin_Senate_Districts.shp')
pgp_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Jonathan Senate Map/WI Senate Demo.json')

#set district maps to same crs as blocks
sen_map = sen_map.to_crs(blocks.crs)
pgp_map = pgp_map.to_crs(blocks.crs)

#make list of columns we want to aggregate from the blocks to the districts
cols = ['tot', 'NHwhite', 'NHblack', 'hispanic', 'totVAP','WVAP', 'BVAP', 'HVAP']
blocks[cols] = blocks[cols].astype(float)

#run aggregate function that does spatial aggregation
aggregated_sen = ai.aggregate(blocks,sen_map, source_columns=cols)[1] 
aggregated_pgp = ai.aggregate(blocks,pgp_map, source_columns=cols)[1] 

#check that totals match
block_total = blocks['tot'].sum()
print('block tot',block_total)
sen_total = aggregated_sen['tot'].sum()
print('sen tot',sen_total)
pgp_total = aggregated_pgp['tot'].sum()
print('pgp tot',pgp_total)

aggregated_sen.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Current Senate Districts/With Demographics/WI_Senate_Map_demographic_breakdown.shp')
aggregated_pgp.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Jonathan Senate Map/With Demographics/PGP_WI_Senate_Demo_Map_demo_breakdown.shp')
