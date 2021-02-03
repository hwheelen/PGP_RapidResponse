# -*- coding: utf-8 -*-
"""
running through gerrychain with pa data from tutorial
https://people.csail.mit.edu/ddeford/GerryChain_Guide.pdf
amanda kmetz 11-24-20

"""

from gerrychain import Graph, Partition, Election, metrics
from gerrychain.updaters import Tally, cut_edges
import geopandas as gpd

# -------- IMPORT DATA + BUILD GRAPH

# set file path
file_path = '/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/shapefiles/for gerrychain/precincts with census data/final/GA_gerrychain_input.shp'

# read df
df = gpd.read_file(file_path)

# make graph
dual_graph = Graph.from_file(file_path) # directly from shp

dual_graph.data.info()
dual_graph.data.dtypes

# -------- BUILD UPDATERS

# election udpaters - all 3 2016 races
elections = [
    Election("T16PRES", {"Democratic": "PRES16D", "Republican": "T16PRESR"}),
    Election("T16SEN", {"Democratic": "SEN16D", "Republican": "T16SENR"}),
    Election("T16ATG", {"Democratic": "T16ATGD", "Republican": "T16ATGR"})
    ]

# set initial updaters
my_updaters = {"population": Tally("TOTPOP", alias="population"),
               "cut_edges": cut_edges}

# dictionary of election updaters
election_updaters = {election.name: election for election in elections}

# add election updaters to updaters list
my_updaters.update(election_updaters)

# # measure county splits - more efficient way if you have access to gdf with same columns
def num_splits(partition, df=df):
    df["current"] = df.index.map(partition.assignment)
    return sum(df.groupby('COUNTYFP10')['current'].nunique() >1)

my_updaters.update({"County Splits": num_splits})

# --------- BUILD INITIAL PARTITION
initial_partition2 = Partition(
    dual_graph2,
    assignment='REMEDIAL',
    updaters=my_updaters
)

# checking out stats for initial partition - based on the updaters we set 
print(initial_partition["T16PRES"].wins("Republican"))  # num of rep wins in each district (pres-16)
print(initial_partition["T16PRES"].percents("Republican"))  # pct rep vote in each district (pres-16)
print(initial_partition["County Splits"]) # total county splits
print(initial_partition["population"])  # population in each district
print(initial_partition["cut_edges"])   # lists each cut edge


# mean-median score for initial partition
metrics.mean_median(initial_partition["T16PRES"])
metrics.partisan_bias(initial_partition["T16PRES"])
metrics.partisan_gini(initial_partition["T16PRES"])
metrics.efficiency_gap(initial_partition["T16PRES"])
metrics.polsby_popper(initial_partition)    # not working
metrics.wasted_votes(initial_partition["T16PRESD"], initial_partition["T16PRESR"])  # not working


# -------- CONFIGURE MARKOV CHAIN

from gerrychain import MarkovChain
from gerrychain import constraints
from gerrychain.constraints import single_flip_contiguous
from gerrychain.proposals import propose_random_flip
from gerrychain.accept import always_accept

# helper function to define constraint
population_constraint = constraints.within_percent_of_ideal_population(initial_partition, .05)


# configure the markov chain
chain = MarkovChain(
    proposal=propose_random_flip, # proposes a random node on boundary of one district be flipped into neighbor district
    constraints=[single_flip_contiguous, population_constraint], # 2 constraints - each district is contiguous and population is within .05 of ideal
    accept=always_accept, # always accepts valid proposed states (metropolis-hastings, or other > use custom function)
    initial_state=initial_partition, # set to our initial partition - the remedial map
    total_steps=1000
)


# empty lists to keep track of details
D_wins = []
EGs = []
boundary_length = []
pops = []
plan_assignments = []


# loop through chain and append relevant updaters to lists
# can evaluate any function that takes a partition object on the states of the chain
# we can interact with chain after it has finished

for current_partition in chain:
    D_wins.append(current_partition["T16PRES"].wins("Democratic"))  #track number of dem wins
    EGs.append(metrics.efficiency_gap(current_partition["T16PRES"]))    # track efficiency gaps according to pres election
    pops.append(sorted(current_partition["population"].values()))   # track lists of population values
    boundary_length.append(num_splits(current_partition))   # track number of splits total
    plan_assignments.append(current_partition.assignment.to_series())

# ------- ANALYSIS

# print mean EG, D_wins, number of county splits
print(sum(EGs) / len(EGs))
print(sum(D_wins) / len(D_wins))
print(sum(boundary_length) / len(boundary_length))

# test - appended the values (district nums) of a single assignment in a new column
df['plan_999'] = plan_assignments[999][df.index]

# for each assignment, (limit of 100 here)
# generate a plan name
# and add a new column in the df with that name
# which will contain to the value of the current assignment (district num)
for i in range(100):
    plan_name = "plan_" + str(i)
    df[plan_name] = plan_assignments[i][df.index]
   

#save splits to shapefile
df.to_file(driver = 'ESRI Shapefile', filename= "PA_MCMC.shp")








