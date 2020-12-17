import sys
sys.path.append('/Users/hwheelen/Documents/GitHub/gerrymander-geoprocessing/areal_interpolation')
import areal_interpolation as ai
import geopandas as gpd
import matplotlib

#set paths for different shapefiles
precincts_mggg = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Precinct Data/WI_wards_12_16_mggg/WI_ltsb_corrected_final.shp')
sen_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Current Senate Districts/With Demographics/WI_Senate_Map_demographic_breakdown.shp')
pgp_map = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Jonathan Senate Map/With Demographics/PGP_WI_Senate_Demo_Map_demo_breakdown.shp')

#set all maps to same crs
sen_map = sen_map.to_crs(precincts_mggg.crs)
pgp_map = pgp_map.to_crs(precincts_mggg.crs)



#cleanup precincts 
precincts_mggg['PREIND16'] = precincts_mggg['PREIND16'] + precincts_mggg['PREIND216']+ precincts_mggg['PREIND316']+ precincts_mggg['PREIND416']+ precincts_mggg['PREIND516']+ precincts_mggg['PREIND616']+ precincts_mggg['PREIND716']+ precincts_mggg['PREIND816']+ precincts_mggg['PREIND916']+ precincts_mggg['PREIND1016']+ precincts_mggg['PREIND1116']
precincts_mggg['USHDEM16'] = precincts_mggg['USHDEM16'] + precincts_mggg['USHDEM216']
precincts_mggg['USSREP16'] = precincts_mggg['USSREP16'] + precincts_mggg['USSREP216']
precincts_mggg['GOVREP14'] = precincts_mggg['GOVREP14'] + precincts_mggg['GOVREP214']+ precincts_mggg['GOVREP314']
precincts_mggg['GOVIND14'] = precincts_mggg['GOVIND14'] + precincts_mggg['GOVIND214']+ precincts_mggg['GOVIND314']+ precincts_mggg['GOVIND414']+ precincts_mggg['GOVIND514']
precincts_mggg['TRSIND14'] = precincts_mggg['TRSIND14'] + precincts_mggg['TRSIND214']
precincts_mggg['USHIND14'] = precincts_mggg['USHIND14'] + precincts_mggg['USHIND214']
precincts_mggg['WSAREP14'] = precincts_mggg['WSAREP14'] + precincts_mggg['WSAREP214']
precincts_mggg['PREIND12'] = precincts_mggg['PREIND12'] + precincts_mggg['PREIND212']+ precincts_mggg['PREIND312']+ precincts_mggg['PREIND412']+ precincts_mggg['PREIND512']+ precincts_mggg['PREIND612']
precincts_mggg['USSIND12'] = precincts_mggg['USSIND12'] + precincts_mggg['USSIND212']+ precincts_mggg['USSIND312']
precincts_mggg['WAGDEM12'] = precincts_mggg['WAGDEM12'] + precincts_mggg['WAGDEM212']
precincts_mggg['WSADEM12'] = precincts_mggg['WSADEM12'] + precincts_mggg['WSADEM212']
precincts_mggg['WSAREP12'] = precincts_mggg['WSAREP12'] + precincts_mggg['WSAREP212']
precincts_mggg['WSAIND12'] = precincts_mggg['WSAIND12'] + precincts_mggg['WSAIND212']
precincts_mggg['WSSREP12'] = precincts_mggg['WSSREP12'] + precincts_mggg['WSSREP212']

precincts_mggg = precincts_mggg[['PRETOT16','PREDEM16','PREREP16','PREGRN16','PRELIB16','PRECON16','PREIND16',#President 2016
        'USHTOT16','USHDEM16','USHREP16','USHGRN16','USHLIB16','USHIND16', #US House of reps 2016
        'USSTOT16','USSDEM16','USSREP16','USSLIB16', #US senate 2016
        'WSATOT16','WSADEM16','WSAREP16','WSALIB16','WSAIND16', #Wisconsin State Assembly 2016
        'WSSTOT16','WSSDEM16','WSSREP16','WSSIND16', #Wisconsin State Senate 2016
        'GOVTOT14','GOVDEM14','GOVREP14','GOVCON14','GOVIND14', # WI Gov 2014
        'SOSTOT14','SOSDEM14','SOSREP14','SOSCON14','SOSIND14', #WI SOS 2014
        'TRSTOT14','TRSDEM14','TRSREP14','TRSCON14','TRSIND14', #WI Treasurer 2014
        'USHTOT14','USHDEM14','USHREP14','USHIND14', #US House of Rep 2014
        'USSTOT14','USSDEM14','USSREP14','USSIND14', #WI State Senate 2014
        'WAGTOT14','WAGDEM14','WAGREP14','WAGIND14', #WI Attorney general 2014
        'WSATOT14','WSADEM14','WSAREP14','WSAIND14',#WI state assembly 2014
        'GOVTOT12','GOVDEM12','GOVREP12','GOVIND12', #WI Gov 2012
        'PRETOT12','PREDEM12','PREREP12','PRECON12','PREIND12', #Presidential 2012
        'USHTOT12','USHDEM12','USHREP12','USHIND12', #US House 2012
        'USSTOT12','USSDEM12','USSREP12','USSCON12','USSIND12',#US Senate 2012
        'WAGTOT12','WAGDEM12','WAGREP12','WAGIND12', #WI Attorney General 2012
        'WSATOT12','WSADEM12','WSAREP12','WSAIND12',#WI State Assembly 2012
        'WSSTOT12','WSSDEM12','WSSREP12','WSSCON12','WSSIND12','WSSAME12', 'geometry']] #WI State Senate



#make list of election columns we want to aggregate from the precincts to the districts
cols = ['PRETOT16','PREDEM16','PREREP16','PREGRN16','PRELIB16','PRECON16','PREIND16',#President 2016
        'USHTOT16','USHDEM16','USHREP16','USHGRN16','USHLIB16','USHIND16', #US House of reps 2016
        'USSTOT16','USSDEM16','USSREP16','USSLIB16', #US senate 2016
        'WSATOT16','WSADEM16','WSAREP16','WSALIB16','WSAIND16', #Wisconsin State Assembly 2016
        'WSSTOT16','WSSDEM16','WSSREP16','WSSIND16', #Wisconsin State Senate 2016
        'GOVTOT14','GOVDEM14','GOVREP14','GOVCON14','GOVIND14', # WI Gov 2014
        'SOSTOT14','SOSDEM14','SOSREP14','SOSCON14','SOSIND14', #WI SOS 2014
        'TRSTOT14','TRSDEM14','TRSREP14','TRSCON14','TRSIND14', #WI Treasurer 2014
        'USHTOT14','USHDEM14','USHREP14','USHIND14', #US House of Rep 2014
        'USSTOT14','USSDEM14','USSREP14','USSIND14', #WI State Senate 2014
        'WAGTOT14','WAGDEM14','WAGREP14','WAGIND14', #WI Attorney general 2014
        'WSATOT14','WSADEM14','WSAREP14','WSAIND14',#WI state assembly 2014
        'GOVTOT12','GOVDEM12','GOVREP12','GOVIND12', #WI Gov 2012
        'PRETOT12','PREDEM12','PREREP12','PRECON12','PREIND12', #Presidential 2012
        'USHTOT12','USHDEM12','USHREP12','USHIND12', #US House 2012
        'USSTOT12','USSDEM12','USSREP12','USSCON12','USSIND12',#US Senate 2012
        'WAGTOT12','WAGDEM12','WAGREP12','WAGIND12', #WI Attorney General 2012
        'WSATOT12','WSADEM12','WSAREP12','WSAIND12',#WI State Assembly 2012
        'WSSTOT12','WSSDEM12','WSSREP12','WSSCON12','WSSIND12','WSSAME12'] #WI state senate

precincts_mggg[cols] = precincts_mggg[cols].astype(float)

#run aggregate function that does spatial aggregation
aggregated_sen = ai.aggregate(precincts_mggg,sen_map, source_columns=cols)[1] 
aggregated_pgp = ai.aggregate(precincts_mggg,pgp_map, source_columns=cols)[1] 

#check that totals match
prec_total = precincts_mggg['PRETOT16'].sum()
print('prectot',prec_total)
sen_total = aggregated_sen['PRETOT16'].sum()
print('sen tot',sen_total)
pgp_total = aggregated_pgp['PRETOT16'].sum()
print('pgp tot',pgp_total)

aggregated_sen.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Current Senate Districts/With Elections and Demographics/WI_Senate_Map_with_data.shp')
aggregated_pgp.to_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Jonathan Senate Map/With Elections and Demographics/PGP_WI_Senate_Demo_Map_with_data.shp')
