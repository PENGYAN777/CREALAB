#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:40:12 2024

@author: yan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import os
import CoolProp as CP
from IPython import get_ipython;   
get_ipython().magic('reset -sf')
os.system('clear')

xp = pd.read_csv("../taps_position.csv", " ", skiprows=0)
xp = xp.squeeze() # from dataframe to array

# t154 = pd.read_csv("../nitrogen/euler/t154.csv", ",", skiprows=0)

n001 = pd.read_csv("nMM16_uJET_N2_001_mean_data_time_probes.csv", ",", skiprows=0)

n = 105
p001 = [ n001.iloc[n,7], n001.iloc[n,11], n001.iloc[n,12], n001.iloc[n,13], n001.iloc[n,14], 
        n001.iloc[n,15], n001.iloc[n,16], n001.iloc[n,17], n001.iloc[n,18], n001.iloc[n,19], n001.iloc[n,20]]
up001 = [ n001.iloc[n,23], n001.iloc[n,27], n001.iloc[n,28], n001.iloc[n,29], n001.iloc[n,30], 
        n001.iloc[n,31], n001.iloc[n,32], n001.iloc[n,33], n001.iloc[n,34], n001.iloc[n,35], n001.iloc[n,36]]

p001 = np.array(p001)/n001.iloc[n,1]

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# fig 1
fig1 = plt.figure( dpi=300)
lw = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(xp ,p001, 'ko', lw=lw, label="N001")
# axes.plot(t154.iloc[:,-3] ,t154.iloc[:,6]/3.14e5 , 'k--', lw=lw, label="n=k")




# axes.set_xlim([0, 38])
# ax2.set_ylim([0,1])
axes.set_xlabel('Time(s)',fontsize=12)
axes.set_ylabel('P(bar)',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 

fig1.savefig("ex_t20_p.pdf")

