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




ref= pd.read_csv("ref.csv", ",", skiprows=0)
t103= pd.read_csv("t103.csv", ",", skiprows=0)
t104= pd.read_csv("t104.csv", ",", skiprows=0)

nc = 10
colors = plt.cm.tab20(np.linspace(0, 1, nc))


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# fig 2
fig2 = plt.figure( dpi=300)
lw = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(ref.iloc[:,-3]*1e3 ,ref.iloc[:,10] , color=colors[0], lw=lw, label="Reference")
axes.plot(t103.iloc[:,-3]*1e3 ,t103.iloc[:,10] , color=colors[1], lw=lw, label="n = 93k")
axes.plot(t104.iloc[:,-3]*1e3 ,t104.iloc[:,10] , color=colors[2], lw=lw, label="n = 222k")






axes.set_xlim([0, 100])
# axes.set_ylim([0,1])
axes.set_xlabel('X[mm]',fontsize=12)
axes.set_ylabel('Pressure[Pa]',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 

fig2.savefig("jet_mm_rans_t10_pressure.pdf")




