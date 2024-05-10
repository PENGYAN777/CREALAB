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

# t703e = pd.read_csv("euler/t703.csv", ",", skiprows=0)
# t704e = pd.read_csv("euler/t704.csv", ",", skiprows=0)
# t705e = pd.read_csv("euler/t705.csv", ",", skiprows=0)
# t703r = pd.read_csv("rans/t703.csv", ",", skiprows=0)
# t704r = pd.read_csv("rans/t704.csv", ",", skiprows=0)
# t705r = pd.read_csv("rans/t705.csv", ",", skiprows=0)

# t2603e = pd.read_csv("euler/t2603.csv", ",", skiprows=0)
# t2604e = pd.read_csv("euler/t2604.csv", ",", skiprows=0)
# t2605e = pd.read_csv("euler/t2605.csv", ",", skiprows=0)
# t2603r = pd.read_csv("rans/t2603.csv", ",", skiprows=0)
# t2604r = pd.read_csv("rans/t2604.csv", ",", skiprows=0)
# t2605r = pd.read_csv("rans/t2605.csv", ",", skiprows=0)

# t4903e = pd.read_csv("euler/t4903.csv", ",", skiprows=0)
# t4904e = pd.read_csv("euler/t4904.csv", ",", skiprows=0)
# t4905e = pd.read_csv("euler/t4905.csv", ",", skiprows=0)
# t4903r = pd.read_csv("rans/t4903.csv", ",", skiprows=0)
# t4904r = pd.read_csv("rans/t4904.csv", ",", skiprows=0)
# t4905r = pd.read_csv("rans/t4905.csv", ",", skiprows=0)

t8203e = pd.read_csv("euler/t8203.csv", ",", skiprows=0)
t8204e = pd.read_csv("euler/t8204.csv", ",", skiprows=0)
t8205e = pd.read_csv("euler/t8205.csv", ",", skiprows=0)
t8203r = pd.read_csv("rans/t8203.csv", ",", skiprows=0)
t8204r = pd.read_csv("rans/t8204.csv", ",", skiprows=0)
t8205r = pd.read_csv("rans/t8205.csv", ",", skiprows=0)





pt = [1.46e6,1.17e6,8.23e5, 4.26e5]

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))


# # fig 1
# fig1 = plt.figure( dpi=300)
# lw = 2
# axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(t703e.iloc[:,-3] ,t703e.iloc[:,6]/pt[0] , 'k', lw=lw, label="Euler n=17k")
# axes.plot(t704e.iloc[:,-3] ,t704e.iloc[:,6]/pt[0] , 'k--', lw=lw, label="Euler n=36k")
# axes.plot(t705e.iloc[:,-3] ,t705e.iloc[:,6]/pt[0] , 'k-.', lw=lw, label="Euler n=65k")
# axes.plot(t703r.iloc[:,-3] ,t703r.iloc[:,10]/pt[0] , 'b', lw=lw, label="RANS n=15k")
# axes.plot(t704r.iloc[:,-3] ,t704r.iloc[:,10]/pt[0] , 'b--', lw=lw, label="RANS n=29k")
# axes.plot(t705r.iloc[:,-3] ,t705r.iloc[:,10]/pt[0] , 'b-.', lw=lw, label="RANS n=46k")
# axes.errorbar(xp ,ex.iloc[0,:]  , yerr = ex.iloc[1,:] , fmt = 'o',color = 'k', 
#             ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


# axes.set_xlim([40, 160])
# axes.set_ylim([0,1])
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
# axes.legend(loc=1) # 

# fig1.savefig("jet_mm_eulerrans_t7.pdf")

# # fig 2 
# fig2 = plt.figure( dpi=300)
# lw = 2
# axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(t2603e.iloc[:,-3] ,t2603e.iloc[:,6]/pt[1] , 'k', lw=lw, label="Euler n=15k")
# axes.plot(t2604e.iloc[:,-3] ,t2604e.iloc[:,6]/pt[1] , 'k--', lw=lw, label="Euler n=29k")
# axes.plot(t2605e.iloc[:,-3] ,t2605e.iloc[:,6]/pt[1] , 'k-.', lw=lw, label="Euler n=45k")
# axes.plot(t2603r.iloc[:,-3] ,t2603r.iloc[:,10]/pt[1] , 'b', lw=lw, label="RANS n=15k")
# axes.plot(t2604r.iloc[:,-3] ,t2604r.iloc[:,10]/pt[1] , 'b--', lw=lw, label="RANS n=30k")
# axes.plot(t2605r.iloc[:,-3] ,t2605r.iloc[:,10]/pt[1] , 'b-.', lw=lw, label="RANS n=47k")
# axes.errorbar(xp ,ex.iloc[2,:]  , yerr = ex.iloc[3,:] , fmt = 'o',color = 'k', 
#             ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


# axes.set_xlim([40, 160])
# axes.set_ylim([0,1])
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
# axes.legend(loc=1) # 

# fig2.savefig("jet_mm_eulerrans_t26.pdf")

# fig 4
fig4 = plt.figure( dpi=300)
lw = 2
axes = fig4.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(t8203e.iloc[:,-3] ,t8203e.iloc[:,6]/pt[3] , 'k', lw=lw, label="Euler n=13k")
axes.plot(t8204e.iloc[:,-3] ,t8204e.iloc[:,6]/pt[3] , 'k--', lw=lw, label="Euler n=28k")
axes.plot(t8205e.iloc[:,-3] ,t8205e.iloc[:,6]/pt[3] , 'k-.', lw=lw, label="Euler n=48k")
axes.plot(t8203r.iloc[:,-3] ,t8203r.iloc[:,10]/pt[3] , 'b', lw=lw, label="RANS n=k")
axes.plot(t8204r.iloc[:,-3] ,t8204r.iloc[:,10]/pt[3] , 'b--', lw=lw, label="RANS n=k")
axes.plot(t8205r.iloc[:,-3] ,t8205r.iloc[:,10]/pt[3] , 'b-.', lw=lw, label="RANS n=k")
axes.errorbar(xp ,ex.iloc[6,:]  , yerr = ex.iloc[7,:] , fmt = 'o',color = 'k', 
            ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")


axes.set_xlim([40, 160])
axes.set_ylim([0,1])
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=1) # 

fig4.savefig("jet_mm_eulerrans_t82.pdf")





