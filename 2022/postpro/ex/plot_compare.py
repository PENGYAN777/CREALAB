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

n001 = pd.read_csv("nMM16_uJET_N2_001_mean_data_time_probes.csv", ",", skiprows=0)
n002 = pd.read_csv("nMM16_uJET_N2_002_mean_data_time_probes.csv", "\t", skiprows=0)
m001 = pd.read_csv("uJET_nMM16_MM_001_mean_data_time_probes.csv", "\t", skiprows=0)
m002 = pd.read_csv("uJET_nMM16_MM_002_mean_data_time_probes.csv", "\t", skiprows=0)


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
n = 0
# fig 1
fig1 = plt.figure( dpi=300)
lw = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(n001.iloc[:,0] ,n001.iloc[:,7+n], 'k', lw=lw, label="N001 PA40")
axes.plot(n002.iloc[:,0] ,n002.iloc[:,9+n], 'b', lw=lw, label="N002 PA40")

ax2 = axes.twinx()
ax2.plot(n001.iloc[:,0] ,n001.iloc[:,23+n], 'k--', lw=lw, label="N001 UPA40")
ax2.plot(n002.iloc[:,0] ,n002.iloc[:,25+n], 'b--', lw=lw, label="N002 UPA40")

axes.set_xlim([0, 38])
# ax2.set_ylim([0,1])
axes.set_xlabel('Time(s)',fontsize=12)
axes.set_ylabel('P(bar)',fontsize=12) 
ax2.set_ylabel('UP(bar)',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 
ax2.legend(loc=5) # 

fig1.savefig("ex_n001_PA40.pdf")

fig2 = plt.figure( dpi=300)
lw = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(m001.iloc[:,0] ,m001.iloc[:,9+n], 'k', lw=lw, label="M001 PA40")
axes.plot(m002.iloc[:,0] ,m002.iloc[:,9+n], 'b', lw=lw, label="M002 PA40")

ax2 = axes.twinx()
ax2.plot(m001.iloc[:,0] ,m001.iloc[:,25+n], 'k--', lw=lw, label="M001 UPA40")
ax2.plot(m002.iloc[:,0], m002.iloc[:,25+n], 'b--', lw=lw, label="M002 UPA40")

axes.set_xlim([0, 140])
# ax2.set_ylim([0,1])
axes.set_xlabel('Time(s)',fontsize=12)
axes.set_ylabel('P(bar)',fontsize=12) 
ax2.set_ylabel('UP(bar)',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 
ax2.legend(loc=5) # 

fig2.savefig("ex_m001_PA40.pdf")
