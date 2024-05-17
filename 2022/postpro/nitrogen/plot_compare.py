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

t102e = pd.read_csv("euler/t102.csv", ",", skiprows=0)
t103e = pd.read_csv("euler/t103.csv", ",", skiprows=0)
t104e = pd.read_csv("euler/t104.csv", ",", skiprows=0)
t102r = pd.read_csv("rans/t102.csv", ",", skiprows=0)
t103r = pd.read_csv("rans/t103.csv", ",", skiprows=0)
t104r = pd.read_csv("rans/t104.csv", ",", skiprows=0)

# t153e = pd.read_csv("euler/t152.csv", ",", skiprows=0)
# t154e = pd.read_csv("euler/t153.csv", ",", skiprows=0)
# t155e = pd.read_csv("euler/t154.csv", ",", skiprows=0)
# t153r = pd.read_csv("rans/t153.csv", ",", skiprows=0)
# t154r = pd.read_csv("rans/t154.csv", ",", skiprows=0)
# t155r = pd.read_csv("rans/t155.csv", ",", skiprows=0)


pt = [4.36e5,3.14e5]

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))


# fig 2
fig2 = plt.figure( dpi=300)
lw = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(t102e.iloc[:,-3] ,t102e.iloc[:,6]/pt[0] , 'k', lw=lw, label="Euler n=17k")
axes.plot(t103e.iloc[:,-3] ,t103e.iloc[:,6]/pt[0] , 'k--', lw=lw, label="Euler n=28k")
axes.plot(t104e.iloc[:,-3] ,t104e.iloc[:,6]/pt[0] , 'k-.', lw=lw, label="Euler n=44k")
axes.plot(t102r.iloc[:,-3] ,t102r.iloc[:,10]/pt[0] , 'b', lw=lw, label="RANS n=15k")
axes.plot(t103r.iloc[:,-3] ,t103r.iloc[:,10]/pt[0] , 'b--', lw=lw, label="RANS n=25k")
axes.plot(t104r.iloc[:,-3] ,t104r.iloc[:,10]/pt[0] , 'b-.', lw=lw, label="RANS n=40k")
axes.errorbar(xp ,ex.iloc[2,:]  , yerr = ex.iloc[3,:] , fmt = 'o',color = 'k', 
            ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


axes.set_xlim([40, 160])
axes.set_ylim([0,1])
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=1) # 

fig2.savefig("jet_nn_eulerrans_t10.pdf")

# # fig 3
# fig3 = plt.figure( dpi=300)
# lw = 2
# axes = fig3.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(t153e.iloc[:,-3] ,t153e.iloc[:,6]/pt[1] , 'k', lw=lw, label="Euler n=6k")
# axes.plot(t154e.iloc[:,-3] ,t154e.iloc[:,6]/pt[1] , 'k--', lw=lw, label="Euler n=12k")
# axes.plot(t155e.iloc[:,-3] ,t155e.iloc[:,6]/pt[1] , 'k-.', lw=lw, label="Euler n=18k")
# axes.plot(t153r.iloc[:,-3] ,t153r.iloc[:,8]/pt[1] , 'b', lw=lw, label="RANS n=8k")
# axes.plot(t154r.iloc[:,-3] ,t154r.iloc[:,8]/pt[1] , 'b--', lw=lw, label="RANS n=15k")
# axes.plot(t155r.iloc[:,-3] ,t155r.iloc[:,8]/pt[1] , 'b-.', lw=lw, label="RANS n=25k")
# axes.errorbar(xp ,ex.iloc[4,:]  , yerr = ex.iloc[5,:] , fmt = 'o',color = 'k', 
#             ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


# axes.set_xlim([40, 160])
# axes.set_ylim([0,1])
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
# axes.legend(loc=1) # 

# fig3.savefig("jet_nn_eulerrans_t15.pdf")


