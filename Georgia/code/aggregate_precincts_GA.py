import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

#set paths for different shapefiles
prec_16 = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Georgia/2016/VEST/ga_2016/ga_2016.shp')
prec_18 = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/OpenPrecincts/States for site/Georgia/2018 Precincts/GA2018PrecElecs.shp')

sen = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE14/with census data/GA_Senate_Map_demo_breakdown.shp')
sen12 = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE12/with census data/GA_Senate12_Map_demo_breakdown.shp')
house = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/HOUSE15/with census data/GA_House_Map_demo_breakdown.shp')
cong = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/CONGRESS12/with census data/GA_Congressional_Map_demo_breakdown.shp')


#make list of maps to work on
maps = [sen, sen12, house, cong, prec_18]

#set district maps to same crs as blocks
for map in maps:
    map = map.to_crs(prec_16.crs)

#make list of election columns we want to aggregate from the precincts to the districts
cols16 = ['G16PREDCli', 'G16PRELJoh', 'G16PRERTru', 'G16USSDBar', 'G16USSLBuc','G16USSRIsa', 'G16PSCLHos', 'G16PSCREch']
cols18  =['G18DATG', 'G18DCmAg','G18DCmIns', 'G18DCmLab', 'G18DGOV', 'G18DLTG', 'G18DPbSrv', 'G18DSOS','G18DSchSpr', 'G18DStSen', 
          'G18LCmIns', 'G18LGOV', 'G18LPbSrv','G18LSOS', 'G18RATG', 'G18RCmAg', 'G18RCmIns', 'G18RCmLab', 'G18RGOV','G18RLTG', 'G18RPbSrv', 'G18RSOS', 'G18RSchSpr', 'G18RStSen']

prec_16[cols16] = prec_16[cols16].astype(float)
prec_18[cols18] = prec_18[cols18].astype(float)

#run aggregate function that does spatial aggregation
aggregated_sen = ai.aggregate(prec_16,sen, source_columns=cols16)[1]
aggregated_sen = ai.aggregate(prec_18,aggregated_sen, source_columns=cols18)[1] 

aggregated_sen12 = ai.aggregate(prec_16,sen12, source_columns=cols16)[1]
aggregated_sen12 = ai.aggregate(prec_18,aggregated_sen12, source_columns=cols18)[1]

aggregated_house = ai.aggregate(prec_16,house, source_columns=cols16)[1]
aggregated_house = ai.aggregate(prec_18,aggregated_house, source_columns=cols18)[1]

aggregated_cong = ai.aggregate(prec_16,cong, source_columns=cols16)[1]
aggregated_cong = ai.aggregate(prec_18,aggregated_cong, source_columns=cols18)[1]


#check that totals match
prec_total = prec_16['G16PREDCli'].sum()
print('prectot',prec_total)
sen_total = aggregated_sen['G16PREDCli'].sum()
print('sen tot',sen_total)
house_total = aggregated_house['G16PREDCli'].sum()
print('house tot',house_total)
cong_total = aggregated_cong['G16PREDCli'].sum()
print('cong tot',cong_total)

aggregated_sen.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE14/with election data/GA_Senate_Map.shp')
aggregated_sen12.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE12/with election data/GA_Senate12_Map.shp')
aggregated_house.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/HOUSE15/with election data/GA_House_Map.shp')
aggregated_cong.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/CONGRESS12/with election data/GA_Congressional_Map.shp')
