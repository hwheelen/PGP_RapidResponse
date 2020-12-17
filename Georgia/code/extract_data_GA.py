import pandas as pd
import geopandas as gpd
import numpy as np

#set filepath to district files with aggregated population and election data
#sen_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Current Senate Districts/With Elections and Demographics/WI_Senate_Map_with_data.shp')
pgp_df = gpd.read_file('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/Shapefiles/Jonathan Senate Map/With Elections and Demographics/PGP_WI_Senate_Demo_Map_with_data.shp')

#extract demographic info and election data
cols = ['District','tot', 'NHwhite', 'NHblack', 'hispanic', 'totVAP', 'WVAP', 'BVAP',
            'HVAP', 'PRETOT16', 'PREDEM16', 'PREREP16', 'PREGRN16', 'PRELIB16',
            'PRECON16', 'PREIND16', 'USHTOT16', 'USHDEM16', 'USHREP16', 'USHGRN16',
            'USHLIB16', 'USHIND16', 'USSTOT16', 'USSDEM16', 'USSREP16', 'USSLIB16',
            'WSATOT16', 'WSADEM16', 'WSAREP16', 'WSALIB16', 'WSAIND16', 'WSSTOT16',
            'WSSDEM16', 'WSSREP16', 'WSSIND16', 'GOVTOT14', 'GOVDEM14', 'GOVREP14',
            'GOVCON14', 'GOVIND14', 'SOSTOT14', 'SOSDEM14', 'SOSREP14', 'SOSCON14',
            'SOSIND14', 'TRSTOT14', 'TRSDEM14', 'TRSREP14', 'TRSCON14', 'TRSIND14',
            'USHTOT14', 'USHDEM14', 'USHREP14', 'USHIND14', 'USSTOT14', 'USSDEM14',
            'USSREP14', 'USSIND14', 'WAGTOT14', 'WAGDEM14', 'WAGREP14', 'WAGIND14',
            'WSATOT14', 'WSADEM14', 'WSAREP14', 'WSAIND14', 'GOVTOT12', 'GOVDEM12',
            'GOVREP12', 'GOVIND12', 'PRETOT12', 'PREDEM12', 'PREREP12', 'PRECON12',
            'PREIND12', 'USHTOT12', 'USHDEM12', 'USHREP12', 'USHIND12', 'USSTOT12',
            'USSDEM12', 'USSREP12', 'USSCON12', 'USSIND12', 'WAGTOT12', 'WAGDEM12',
            'WAGREP12', 'WAGIND12', 'WSATOT12', 'WSADEM12', 'WSAREP12', 'WSAIND12',
            'WSSTOT12', 'WSSDEM12', 'WSSREP12', 'WSSCON12', 'WSSIND12','WSSAME12']

sen_csv = sen_df[[cols]]
pgp_csv = pgp_df[[cols]]

sen_csv.to_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/data/WI_State_Senate_Map_estimates.csv')
pgp_csv.to_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/data/PGP_WI_Senate_Demo_Map_estimates.csv')


