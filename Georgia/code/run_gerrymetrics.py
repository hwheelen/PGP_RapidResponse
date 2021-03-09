import pandas as pd
import geopandas as gpd
import numpy as np
import gerrymetrics as g
from collections import defaultdict

sen_csv = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_Senate_Map_estimates.csv')
sen12_csv = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_Senate12_Map_estimates.csv')
house_csv = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_House_Map_estimates.csv')
cong_csv = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_Congressional_Map_estimates.csv')

# impute uncontested races at a voteshare of 0 or 1; in other words, don't impute them
impute_val = 1

# only consider races after 1972
min_year = 1972

# when identifying the worst gerrymanders:
# only examine races where D voteshare is between .45 and .55
competitiveness_threshold = .6 

# only examine races in states with at least 7 districts
min_districts = 7

n = cong_csv

metric_dict = {'t_test_diff':            g.t_test_diff,
            #    't_test_p':            g.t_test_p,
               'mean_median_diff':       g.mean_median,
               'declination':            g.declination,
            #    'declination_buffered':   g.bdec,
               'efficiency_gap':         g.EG,
            #    'loss_gap':               g.EG_loss_only,
            #    'difference_gap':         g.EG_difference,
            #    'surplus_gap':            g.EG_surplus_only,
            #    'vote_centric_gap':       g.EG_vote_centric,
            #    'vote_centric_gap_two':   g.EG_vote_centric_two,
               'partisan_bias':          g.partisan_bias,
            #    'equal_vote_weight_bias': g.equal_vote_weight
               }

dat = cong_csv[['DISTRICT','G20PREDBID','G20PRERTRU']]
dat
# dat = g.parse_results(dat_path)

# dat.index = dat.index.set_levels(['STATE'], level=1)
# merged = pd.concat([elect_df, dat]).sort_index() #!! merge congressional data 

#test_df = g.tests_df(g.run_all_tests(merged, impute_val=1, metrics=metric_dict))

test_df_1 = g.tests_df(g.run_all_tests(dat, impute_val=1, metrics=metric_dict))

perc_df = g.generate_percentiles(test_df, metric_dict.keys(), competitiveness_threshold=competitiveness_threshold, min_districts=min_districts)
perc_df.loc[2009, 'STATE']

test_df.loc(axis=0)[:, 'STATE']