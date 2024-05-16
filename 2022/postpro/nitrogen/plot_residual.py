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

h = pd.read_csv("history_2nd.csv", ",", skiprows=0)


# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# fig 1
fig1 = plt.figure( dpi=300)
lw = 2
axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(h.iloc[:,2] ,h.iloc[:,3] , 'k', lw=lw, label="$\\rho$")

# axes.set_xlim([40, 160])
# axes.set_ylim([0,1])
axes.set_xlabel('Number of iteraion',fontsize=12)
axes.set_ylabel('Residual',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=0) # 


# fig1.savefig("jet_nn_t5.pdf")



