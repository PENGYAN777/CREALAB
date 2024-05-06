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

xp = pd.read_csv("../../taps_position.csv", " ", skiprows=0)
xp = xp.squeeze() # from dataframe to array
ex = pd.read_csv("pressure.csv", ",",skiprows=0, usecols=range(2,13))
# t703 = pd.read_csv("t703.csv", ",", skiprows=0)
# t704 = pd.read_csv("t704.csv", ",", skiprows=0)
# t705 = pd.read_csv("t705.csv", ",", skiprows=0)

t2603 = pd.read_csv("t2603.csv", ",", skiprows=0)
t2604 = pd.read_csv("t2604.csv", ",", skiprows=0)
t2605 = pd.read_csv("t2605.csv", ",", skiprows=0)

# t49 = pd.read_csv("t49.csv", ",", skiprows=0)
# t82 = pd.read_csv("t82.csv", ",", skiprows=0)


pt = [1.46e6,1.17e6,8.23e5, 4.26e5]

# axes.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

# # # fig 1
# fig1 = plt.figure( dpi=300)
# lw = 2
# axes = fig1.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
# axes.plot(t703.iloc[:,-3] ,t703.iloc[:,6]/pt[0] , 'k', lw=lw, label="n=17k")
# axes.plot(t704.iloc[:,-3] ,t704.iloc[:,6]/pt[0] , 'k--', lw=lw, label="n=36k")
# axes.plot(t705.iloc[:,-3] ,t705.iloc[:,6]/pt[0] , 'k-.', lw=lw, label="n=65k")
# axes.errorbar(xp ,ex.iloc[0,:]  , yerr = ex.iloc[1,:] , fmt = 'o',color = 'k', 
#             ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")
# # # compute diff
# # ax2 = axes.twinx()
# # idx = np.zeros(xp.size) # 
# # diff = np.zeros(xp.size) # diff between cfd and ex
# # for i in xp.index:
# #     idx[i] = np.argmin(abs(xp[i]-t5.iloc[:,-3])) # t5
# #     #pt[0] for t5, shitf of 1,  ex.iloc[0] for t5,shitf of 2 for next case
# #     diff[i] = (t5.iloc[int(idx[i]),6]/pt[0]-ex.iloc[0,i])/ex.iloc[0,i]*100 
    

# # ax2.plot(xp, abs(diff) , 'b*', lw=lw)    
# # ax2.set_ylabel('$\Delta_{P/P_t}$(%)',fontsize=12) 

# axes.set_xlim([40, 160])
# axes.set_ylim([0,1])
# axes.set_xlabel('$X[mm]$',fontsize=12)
# axes.set_ylabel('$P/P_t$',fontsize=12) 
# axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
# axes.legend(loc=1) # 


# fig1.savefig("jet_mm_t7.pdf")

# # fig 2
fig2 = plt.figure( dpi=300)
lw = 2
axes = fig2.add_axes([0.15, 0.15, 0.7, 0.7]) #size of figure
axes.plot(t2603.iloc[:,-3] ,t2603.iloc[:,6]/pt[1] , 'k', lw=lw, label="n=15k")
axes.plot(t2604.iloc[:,-3] ,t2604.iloc[:,6]/pt[1] , 'k--', lw=lw, label="n=29k")
axes.plot(t2605.iloc[:,-3] ,t2605.iloc[:,6]/pt[1] , 'k-.', lw=lw, label="n=45k")
axes.errorbar(xp ,ex.iloc[2,:]  , yerr = ex.iloc[3,:] , fmt = 'o',color = 'k', 
            ecolor = 'k', elinewidth = 1, capsize=5, label="Ex")

axes.set_xlim([40, 160])
axes.set_ylim([0,1])
axes.set_xlabel('$X[mm]$',fontsize=12)
axes.set_ylabel('$P/P_t$',fontsize=12) 
axes.set_title('$P/P_t$ along nozzle centerline',fontsize=14)
axes.legend(loc=1) # 


fig2.savefig("jet_mm_t26.pdf")


