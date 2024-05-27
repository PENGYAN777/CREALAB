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



t103e = pd.read_csv("euler/t103.csv", ",", skiprows=0)
t104e = pd.read_csv("euler/t104.csv", ",", skiprows=0)
t103r = pd.read_csv("rans/t103.csv", ",", skiprows=0)
t104r = pd.read_csv("rans/t104.csv", ",", skiprows=0)

t703e = pd.read_csv("euler/t703.csv", ",", skiprows=0)
t704e = pd.read_csv("euler/t704.csv", ",", skiprows=0)
t703r = pd.read_csv("rans/t703.csv", ",", skiprows=0)
t704r = pd.read_csv("rans/t704.csv", ",", skiprows=0)

pt = [1.415e6, 5.3420e5]

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))



# # fig 2
# fig2 = plt.figure( dpi=300)
# lw = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(t103e.iloc[:,-3] ,t103e.iloc[:,6]/pt[0] , 'k', lw=lw, label="Euler n=k")
# axes.plot(t104e.iloc[:,-3] ,t104e.iloc[:,6]/pt[0] , 'k--', lw=lw, label="Euler n=k")
# axes.plot(t103r.iloc[:,-3] ,t103r.iloc[:,10]/pt[0] , 'b', lw=lw, label="RANS n=k")
# axes.plot(t104r.iloc[:,-3] ,t104r.iloc[:,10]/pt[0] , 'b--', lw=lw, label="RANS n=k")
# axes.errorbar(xp ,ex.iloc[0,:]  , yerr = ex.iloc[1,:] , fmt = 'o',color = 'k', 
#             ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


# axes.set_xlim([40, 155])
# axes.set_ylim([0,1])
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
# axes.legend(loc=1) # 

# fig2.savefig("jet_mm_eulerrans_t10.pdf")

# fig 2
fig3 = plt.figure( dpi=300)
lw = 3
axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(t703e.iloc[:,-3] ,t703e.iloc[:,6]/pt[1] , 'k', lw=lw, label="Euler n=k")
axes.plot(t704e.iloc[:,-3] ,t704e.iloc[:,6]/pt[1] , 'k--', lw=lw, label="Euler n=k")
axes.plot(t703r.iloc[:,-3] ,t703r.iloc[:,10]/pt[1] , 'b', lw=lw, label="RANS n=k")
axes.plot(t704r.iloc[:,-3] ,t704r.iloc[:,10]/pt[1] , 'b--', lw=lw, label="RANS n=k")
axes.errorbar(xp ,ex.iloc[2,:]  , yerr = ex.iloc[3,:] , fmt = 'o',color = 'k', 
            ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


axes.set_xlim([40, 155])
axes.set_ylim([0,1])
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=1) # 

fig3.savefig("jet_mm_eulerrans_t70.pdf")


