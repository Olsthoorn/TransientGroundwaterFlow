#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:41:21 2016

@author: Theo
"""

import matplotlib.pyplot as plt
#plt.switch_backend('QT4Agg')

# a little hack to get screen size; from here [1]
mgr = plt.get_current_fig_manager()
mgr.full_screen_toggle()
py = mgr.canvas.height()
px = mgr.canvas.width()
mgr.window.close()
# hack end

x = [i for i in range(0,10)]
plt.figure()
plt.plot(x)

figManager = plt.get_current_fig_manager()
# if px=0, plot will display on 1st screen
figManager.window.move(px, -500)
figManager.window.showMaximized()
figManager.window.setFocus()

plt.show()
