#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 20:01:33 2018

@author: Theo
"""

import numpy as np
from scipy.special import exp1
import matplotlib.pyplot as plt

Q = 1200
kD = 600
S = 0.15
r = 100
t = np.arange(10, 10 * 24 * 60 + 10, 10) / (24 * 60)

u = r**2 * S / (4 * kD * t)
s = Q/ (4 * np.pi * kD) * exp1(u)

sigma = 0.002
s = s + sigma * np.random.randn(len(t))

plt.title('Pumping test drawdown, Q = {:.0f} m3/d'.format(Q))
plt.xlabel('t --> [d]')
plt.ylabel('<-- drawdown [m]')
plt.grid(True)
plt.xscale('log')
plt.ylim((np.max(s), np.min(s)))
plt.plot(t, s, '.')
plt.show()

