#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:03:45 2016

@author: Theo
"""

#from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import mfgrid

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')


Np = 11
x = np.arange(Np, dtype=float)
y = np.arange(Np, dtype=float)
z = np.arange(Np, dtype=float)

gr = mfgrid.Grid(x, y, z)

gr.plot_grid3d('gbr', alpha=0.5)

plt.show()