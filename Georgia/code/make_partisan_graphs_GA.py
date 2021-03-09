import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

sen = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_Senate_Map_estimates.csv')
sen12 = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_Senate12_Map_estimates.csv')
house = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_State_House_Map_estimates.csv')
cong = pd.read_csv('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Data/GA_Congressional_Map_estimates.csv')

measure = 'G20PREDBID'
add = 'G20PRERTRU'

# senate figure-------------------------------------------------------------------
sen['prop'] = (sen[measure]/((sen[measure].astype(int) + sen[add].astype(int)))*100)

sen['rank'] = sen['prop'].rank(ascending=True)

x = sen['rank']
y = sen['prop']
n = sen['DISTRICT']


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
ax.axhspan(40, 60, alpha=0.25, color='yellow')
ax.set_ylabel('Proportion Democratic Votes (President 2020)')
ax.set_ylim(-2,max(y)+2)
ax.set_xlabel('Rank (least to most Democratic)')
ax.set_xlim(0,max(x)+2)
#ax.axhline(50, color ='black')
ax.set_title('Georgia State Senate, Enacted Map')
#ax.set_title('Wisconsin Senate Map 2011-2020')
#plt.xticks(np.arange(1, 34, step=4))
#plt.yticks(np.arange(0, 105, step=10))

fig.savefig('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Figures/GA_Senate_Enacted_Pres20.pdf')

# senate12 figure--------------------------------------------------------------------------------------------------------
sen12['prop'] = (sen12[measure]/((sen12[measure].astype(int) + sen12[add].astype(int)))*100)

sen12['rank'] = sen12['prop'].rank(ascending=True)

x = sen12['rank']
y = sen12['prop']
n = sen12['DISTRICT']

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
ax.axhspan(40, 60, alpha=0.25, color='yellow')
ax.set_ylabel('Proportion Democratic Votes (President 2020)')
ax.set_ylim(-2,max(y)+2)
ax.set_xlabel('Rank (least to most Democratic)')
ax.set_xlim(0,max(x)+2)
#ax.axhline(50, color ='black')
ax.set_title('Georgia State Senate, 2012 Map')
#ax.set_title('Wisconsin Senate Map 2011-2020')
#plt.xticks(np.arange(1, 34, step=4))
#plt.yticks(np.arange(0, 105, step=10))

fig.savefig('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Figures/GA_Senate_2012_Pres20.pdf')

# house figure--------------------------------------------------------------------------------------------------------
house['prop'] = (house[measure]/((house[measure].astype(int) + house[add].astype(int)))*100)

house['rank'] = house['prop'].rank(ascending=True)

x = house['rank']
y = house['prop']
n = house['DISTRICT']

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
ax.axhspan(40, 60, alpha=0.25, color='yellow')
ax.set_ylabel('Proportion Democratic Votes (President 2020)')
ax.set_ylim(-2,max(y)+2)
ax.set_xlabel('Rank (least to most Democratic)')
ax.set_xlim(0,max(x)+2)
#ax.axhline(50, color ='black')
ax.set_title('Georgia State House, Enacted Map')
#ax.set_title('Wisconsin Senate Map 2011-2020')
#plt.xticks(np.arange(1, 34, step=4))
#plt.yticks(np.arange(0, 105, step=10))

fig.savefig('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Figures/GA_House_Enacted_Pres20.pdf')

#congressional figure--------------------------------------------------------------------------------------------------------
cong['prop'] = (cong[measure]/((cong[measure].astype(int) + cong[add].astype(int)))*100)

cong['rank'] = cong['prop'].rank(ascending=True)

x = cong['rank']
y = cong['prop']
n = cong['DISTRICT']

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
ax.axhspan(40, 60, alpha=0.25, color='yellow')
ax.set_ylabel('Proportion Democratic Votes (President 2020)')
ax.set_ylim(-2,max(y)+2)
ax.set_xlabel('Rank (least to most Democratic)')
ax.set_xlim(0,max(x)+2)
#ax.axhline(50, color ='black')
ax.set_title('US Congress, Enacted Map')
#ax.set_title('Wisconsin Senate Map 2011-2020')
#plt.xticks(np.arange(1, 34, step=4))
#plt.yticks(np.arange(0, 105, step=10))

fig.savefig('/Users/hwheelen/Documents/GitHub/PGP_RapidResponse/Georgia/Figures/GA_Congressional_Enacted_Pres20.pdf')
