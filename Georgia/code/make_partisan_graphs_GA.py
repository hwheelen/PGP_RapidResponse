import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

#load in datasets
sen_df= pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/data/WI_State_Senate_Map_estimates.csv')
pgp_df = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Wisconsin/data/PGP_WI_Senate_Demo_Map_estimates.csv')


#calculate y proportion and set, sometimes this might require calculating an average of ma
x = df['rank']
y = df['propD']
n = df['District']

x = [4,7,9,10,6,11,3]
seq = sorted(x)
index = [seq.index(v) for v in x]


fig, ax = plt.subplots()

col =[] 
  
for i in range(0, len(x)): 
    if y[i]<50: 
        col.append('red')   
    else: 
        col.append('blue')  
  
for i in range(len(x)): 
      
    # plotting the corresponding x with y  
    # and respective color 
    ax.scatter(x[i], y[i], c = col[i], s = 30 )
ax.axhspan(45, 55, alpha=0.25, color='grey')
ax.set_ylabel('Democratic vote share (%)')
ax.set_ylim(0,max(y)+2)
ax.set_xlabel('Rank (least to most Democratic)')
ax.set_xlim(0,max(x)+2)
ax.axhline(50, color ='black')
ax.set_title('Wisconsin Senate, Princeton demonstration map')
#ax.set_title('Wisconsin Senate Map 2011-2020')
plt.xticks(np.arange(1, 34, step=4))
plt.yticks(np.arange(0, 105, step=10))

fig.savefig('/Users/hwheelen/Desktop/Wisconsin/Images/PGPWIDemoMap.pdf')
#fig.savefig('/Users/hwheelen/Desktop/Wisconsin/Images/WIStSenateMap.pdf')
