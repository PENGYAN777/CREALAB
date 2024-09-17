#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 16:05:08 2022

@author: yan

plot (P,T) diagram. show contour of compressibility factor Z and 
fundamental derivative of gasdynamics Gamma
"""

import matplotlib
import numpy as np
import CoolProp as CP
import matplotlib.pyplot as plt
import scipy.interpolate


# give fluid name
fluidname = "MM"

# update fluid
fluid = CP.AbstractState("HEOS", fluidname)

pc = fluid.keyed_output(CP.iP_critical)
Tc = fluid.keyed_output(CP.iT_critical)
Tmin =  CP.CoolProp.PropsSI("Ttriple",fluidname)
Tmax =  CP.CoolProp.PropsSI("Tmax",fluidname)
pmax = fluid.keyed_output(CP.iP_max)
pmin = fluid.keyed_output(CP.iP_min)
fillcolor = 'g'

# fig = plt.figure(figsize = (6,6))
# ax = fig.add_subplot(111)
fig = plt.figure(figsize=(6,5))
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax = fig.add_axes([left, bottom, width, height]) 
lw = 3


# ----------------
# Saturation curve
# ----------------
Ts = np.linspace(Tmin, Tc, 1000)
ps = CP.CoolProp.PropsSI('P','T',Ts,'Q',0,fluidname)

# ----------------
# Contour of Z and Gamma
# ----------------
n = 400 # number of points
x = np.linspace(Tmin, Tmax,n)
y = np.linspace(0.5e5, 1e7,n)
X,Y = np.meshgrid(x,y)
Z =  CP.CoolProp.PropsSI('Z','T',X,'P',Y,fluidname)
Gamma =  CP.CoolProp.PropsSI('fundamental_derivative_of_gas_dynamics','T',X,'P',Y,fluidname)
#print(Z.shape)
levels = [0.6, 0.7, 0.8, 0.9, 0.95, 0.98, ]
cp = ax.contour(X, Y, Z, levels, colors='black', linestyles='dashed')
plt.clabel(cp, inline=True,  fontsize=10)
plt.contourf(X, Y, Gamma, [0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4], cmap='rainbow')
plt.colorbar(location='right', orientation='vertical', label='$\Gamma$')
# ------
# Labels
# ------

plt.plot(Ts,ps,'k',lw = lw, solid_capstyle = 'round', label = "LVS")
plt.plot(0,0,'k--',lw = lw/2, solid_capstyle = 'round', label = "Z")
# Critical lines
plt.axvline(Tc, dashes = [2, 2])
plt.axhline(pc, dashes = [2, 2])

"""
test points
"""

nc = 10
colors = plt.cm.tab20(np.linspace(0, 1, nc))

zt_p = [1.4e6, ]
zt_t = [503.84, ]
plt.plot(zt_t,zt_p,'ro' , lw = lw, label = "$Z_t$=0.6")

za_p = [6.69e5, 2.23e5, 1.34e5, ]
za_t = [495, 485, 490, ]
plt.plot(za_t,za_p,'bo' , lw = lw, label = "$Z_a$")



ax.legend(loc=3) # 2 means left top

plt.ylim(0.5e5,1e7)
plt.gca().set_yscale('log')
plt.gca().set_xlim(Tmin, Tmax)
plt.ylabel('P [Pa]')
plt.xlabel('T [K]')
# plt.title('Contour of Z and $\Gamma$ for siloxane MM')
plt.tight_layout()
fig.savefig("mm_z_Contour_PT.eps")
print("plotcontour.py called")