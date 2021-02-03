import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

#set paths for different shapefiles
prec_16 = gpd.read_file('/Users/hwheelen/Desktop/GA Precincts/ga_2016/ga_2016.shp')
prec_18 = gpd.read_file('/Users/hwheelen/Desktop/GA Precincts/ga_2018/ga_2018.shp')
prec_20 = gpd.read_file('/Users/hwheelen/Desktop/GA Precincts/ga_2020/ga_2020.shp')
blocks = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/census blocks with data/GABlocksDemographicBreakdown.geojson')

#specify columns you want to work with and set to int
cols_16 = ['G16PRERTRU', 'G16PREDCLI','G16PRELJOH', 'G16USSRISA', 'G16USSDBAR', 'G16USSLBUC']
cols_18 = ['G18GOVRKEM', 'G18GOVDABR','G18GOVLMET', 'G18LTGRDUN', 'G18LTGDAMI', 'G18SOSRRAF', 'G18SOSDBAR','G18SOSLDUV', 'G18ATGRCAR', 'G18ATGDBAI']
cols_blocks = ['tot', 'NHwhite','NHblack', 'NHnat', 'NHasi', 'hispanic', 'totVAP', 'HVAP', 'WVAP','BVAP', 'NatVAP', 'AVAP']
blocks[cols_blocks] = blocks[cols_blocks].astype(int)

#make sure files are in the same CRS
prec_20 = prec_20.to_crs(blocks.crs)
prec_18 = prec_18.to_crs(blocks.crs)
prec_16 = prec_16.to_crs(blocks.crs)

#bring 2016 and 2018 elections down to block level so we can bring them back to the precinct level in 2020 precincts
aggregated = ai.aggregate(prec_16,blocks, source_columns=cols_16)[1] 
aggregated = ai.aggregate(prec_18, aggregated, source_columns = cols_18)[1]

#save file for use later
aggregated.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/blocks/GA_blocks_demog_16_18elecs.shp')


aggregated = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/blocks/GA_blocks_demog_16_18elecs.shp')
prec_20['geometry'] = prec_20.geometry.buffer(0)

#specify all columns to bring to 2020 precincts
total_cols = ['G18GOVRKEM', 'G18GOVDABR','G18GOVLMET', 'G18LTGRDUN', 'G18LTGDAMI', 'G18SOSRRAF', 'G18SOSDBAR','G18SOSLDUV', 'G18ATGRCAR', 'G18ATGDBAI',
              'G16PRERTRU', 'G16PREDCLI','G16PRELJOH', 'G16USSRISA', 'G16USSDBAR', 'G16USSLBUC',
              'tot', 'NHwhite','NHblack', 'NHnat', 'NHasi', 'hispanic', 'totVAP', 'HVAP', 'WVAP','BVAP', 'NatVAP', 'AVAP']

#aggregate block level data into 2020 precincts
agg = ai.aggregate(aggregated,prec_20,source_columns=total_cols)[1]

#remove any unwanted columns and rearrange order
agg = agg[['DISTRICT', 'CTYSOSID', 'PRECINCT_I', 'PRECINCT_N', 'CTYNAME',
       'CTYNUMBER', 'CTYNUMBER2', 'FIPS2', 'G20PRERTRU', 'G20PREDBID',
       'G20PRELJOR', 'C20PRERTRU', 'C20PREDBID', 'C20PRELJOR', 'G20USSRPER',
       'G20USSDOSS', 'G20USSLHAZ', 'S20USSRLOE', 'S20USSRCOL', 'S20USSRGRA',
       'S20USSRJAC', 'S20USSRTAY', 'S20USSRJOH', 'S20USSDWAR', 'S20USSDJAC',
       'S20USSDLIE', 'S20USSDJOH', 'S20USSDJAM', 'S20USSDSLA', 'S20USSDWIN',
       'S20USSDTAR', 'S20USSLSLO', 'S20USSGFOR', 'S20USSIBUC', 'S20USSIBAR',
       'S20USSISTO', 'S20USSIGRE', 'G20PSCRSHA', 'G20PSCDBRY', 'G20PSCLMEL',
       'G20PSCRMCD', 'G20PSCDBLA', 'G20PSCLWIL', 'G18GOVRKEM',
       'G18GOVDABR', 'G18GOVLMET', 'G18LTGRDUN', 'G18LTGDAMI', 'G18SOSRRAF',
       'G18SOSDBAR', 'G18SOSLDUV', 'G18ATGRCAR', 'G18ATGDBAI', 'G16PRERTRU',
       'G16PREDCLI', 'G16PRELJOH', 'G16USSRISA', 'G16USSDBAR', 'G16USSLBUC',
       'tot', 'NHwhite', 'NHblack', 'NHnat', 'NHasi', 'hispanic', 'totVAP',
       'HVAP', 'WVAP', 'BVAP', 'NatVAP', 'AVAP', 'geometry']]

#save for use later since this was all the stuff that takes a long time
agg.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/precincts with census data/GA_20precincts_16_18_pop.shp')


#load here so you don't have to start over
agg_final = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/precincts with census data/GA_20precincts_16_18_pop.shp')



#interpolate district labels from different district maps and counties
sen_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE14/with election data/GA_Senate_Map.shp')
sen12_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/SENATE12/with election data/GA_Senate12_Map.shp')
house_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/HOUSE15/with election data/GA_House_Map.shp')
cong_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/CONGRESS12/with election data/GA_Congressional_Map.shp')
county_df = gpd.read_file('/Volumes/GoogleDrive/Shared drives/princeton_gerrymandering_project/mapping/GA/GA_Counties/GA_Counties.shp')

agg1 = ai.aggregate(agg_final, sen_df, target_columns=['DISTRICT'])[0]
agg1.rename(columns = {"DISTRICT": "SenDist"}, inplace = True)
agg2 = ai.aggregate(agg1, sen12_df, target_columns=['DISTRICT'])[0]
agg2.rename(columns = {"DISTRICT": "Sen12Dist"}, inplace = True)
agg3 = ai.aggregate(agg2, house_df, target_columns=['DISTRICT'])[0]
agg3.rename(columns = {"DISTRICT": "HouseDist"}, inplace = True)
agg4 = ai.aggregate(agg3, cong_df, target_columns=['DISTRICT'])[0]
agg4.rename(columns = {"DISTRICT": "CongDist"}, inplace = True)
agg4 = ai.aggregate(agg4, county_df, target_columns=['FIPSCODE','CON'])[0]


agg4.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/precincts with census data/final/GA_gerrychain_input.shp')