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


m9 = pd.read_csv("m9.csv", ",", skiprows=0)
m10 = pd.read_csv("m10.csv", ",", skiprows=0)
q1d= pd.read_csv("../adapt//Q1D/z6.csv", ",", skiprows=0)


# fig 2
fig2 = plt.figure( dpi=300)
lw = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(m9.iloc[:,-3]*1e3 ,m9.iloc[:,5] , 'k', lw=lw, label="level 9")
axes.plot(m10.iloc[:,-3]*1e3 ,m10.iloc[:,5] , 'k--', lw=lw, label="level 10")
axes.plot(q1d.iloc[:,-2]*1e3 ,q1d.iloc[:,6] , 'b', lw=lw, label="Q1D")


# axes.set_xlim([0, 43.9])
# axes.set_ylim([0,1])
axes.set_xlabel('X[mm]',fontsize=12)
axes.set_ylabel('Mach',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 

fig2.savefig("jet_mm_rans_u5_gv_m.pdf")

# fig 3
fig3 = plt.figure( dpi=300)
lw = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(m9.iloc[:,-3]*1e3 ,m9.iloc[:,10] , 'k', lw=lw, label="level 9")
axes.plot(m10.iloc[:,-3]*1e3 ,m10.iloc[:,10] , 'k--', lw=lw, label="level 10")
axes.plot(q1d.iloc[:,-2]*1e3 ,q1d.iloc[:,2] , 'b', lw=lw, label="Q1D")


# axes.set_xlim([0, 43.9])
# axes.set_ylim([0,1])
axes.set_xlabel('X[mm]',fontsize=12)
axes.set_ylabel('Pressure',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 

fig3.savefig("jet_mm_rans_u5_gv_p.pdf")









