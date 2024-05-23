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

t10 = pd.read_csv("history_rans_t10.csv", ",", skiprows=0)



# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# fig 1
fig1 = plt.figure( dpi=300)
lw = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(t10.iloc[:,2] ,t10.iloc[:,3] , 'k', lw=lw, label="$\\rho$")

# axes.set_xlim([0, 2000])
# axes.set_ylim([0,1])
axes.set_xlabel('Number of iteraion',fontsize=12)
axes.set_ylabel('Residual',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 


fig1.savefig("jet_mm_rans_t10_residual.pdf")






