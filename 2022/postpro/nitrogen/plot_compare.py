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
ex = pd.read_csv("pressure.csv", ",",skiprows=0, usecols=range(2,13))

t603e = pd.read_csv("euler/t603.csv", ",", skiprows=0)
t604e = pd.read_csv("euler/t604.csv", ",", skiprows=0)
t603r = pd.read_csv("rans/t603.csv", ",", skiprows=0)
t604r = pd.read_csv("rans/t604.csv", ",", skiprows=0)

t103e = pd.read_csv("euler/t103.csv", ",", skiprows=0)
t104e = pd.read_csv("euler/t104.csv", ",", skiprows=0)
t103r = pd.read_csv("rans/t103.csv", ",", skiprows=0)
t104r = pd.read_csv("rans/t104.csv", ",", skiprows=0)

pt = [5.8685e5,4.2114e5]

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))


# # fig 2
# fig2 = plt.figure( dpi=300)
# lw = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(t603e.iloc[:,-3] ,t603e.iloc[:,6]/pt[0] , 'k', lw=lw, label="Euler n=28k")
# axes.plot(t604e.iloc[:,-3] ,t604e.iloc[:,6]/pt[0] , 'k--', lw=lw, label="Euler n=44k")
# axes.plot(t603r.iloc[:,-3] ,t603r.iloc[:,10]/pt[0] , 'b', lw=lw, label="RANS n=48k")
# axes.plot(t604r.iloc[:,-3] ,t604r.iloc[:,10]/pt[0] , 'b--', lw=lw, label="RANS n=109k")
# axes.errorbar(xp ,ex.iloc[0,:]  , yerr = ex.iloc[1,:] , fmt = 'o',color = 'k', 
#             ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


# axes.set_xlim([40, 155])
# axes.set_ylim([0,1])
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
# axes.legend(loc=1) # 

# fig2.savefig("jet_nn_eulerrans_t6.pdf")

# fig 3
fig3 = plt.figure( dpi=300)
lw = 2
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(t103e.iloc[:,-3] ,t103e.iloc[:,6]/pt[1] , 'k', lw=lw, label="Euler n=44k")
axes.plot(t104e.iloc[:,-3] ,t104e.iloc[:,6]/pt[1] , 'k--', lw=lw, label="Euler n=83k")
axes.plot(t103r.iloc[:,-3] ,t103r.iloc[:,10]/pt[1] , 'b', lw=lw, label="RANS n=48k")
axes.plot(t104r.iloc[:,-3] ,t104r.iloc[:,10]/pt[1] , 'b--', lw=lw, label="RANS n=118k")
axes.errorbar(xp ,ex.iloc[2,:]  , yerr = ex.iloc[3,:] , fmt = 'o',color = 'k', 
            ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


axes.set_xlim([40, 155])
axes.set_ylim([0,1])
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=1) # 

fig3.savefig("jet_nn_eulerrans_t105.pdf")


