
# coding: utf-8

# # Suction and capillary fringe thickness (p 20)

# How much capillary rise can we expect depending on pore radius?
# 
# (see exercise 14 on page 27 of the syllabus.
# 
# 
# T.N. Olsthoorn (2018-12-30)

# In[1]:


import nbconvert


# Let a straw with radius $r$ represent the porous medium with the same effective pore size. Then the equlibrium at elevation where presssure is equal to atmospheric pressure, i.e. bij definition, this is the water table, we have
# 
# $$ \rho g h \pi r^2 = 2 \pi r \gamma \cos{\alpha} $$
# 
# and so
# 
# $$ h = \frac {2 \gamma \cos \alpha} {\rho g r} $$
# 
# If the direction of the cohesion is virtually in the direction of the water surface in the straw, meaning its tension equals the surface tension of the water in the straw, $\tau = 75 \times 10^-3 $ N/m.
# 
# Assuming that the angle $\gamma$ is quite small, we may say $\cos \alpha \approx 1$, which yields
# 
# $$h \approx \frac {2 \gamma} {\rho g r}$$

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
rho = 1e3 # kg/m3
g = 9.81 # N/kg
gam = 75e-3 # N/m
r = np.logspace(-5, -3, 31)
h = 2 * gam / (rho * g * r)


# In[10]:


plt.title('Capillary rise in straw of given radius')
plt.xlabel('pore radius [m]')
plt.ylabel('capillary rise [m]')
plt.xscale('log')
plt.grid()
plt.plot(r, h)


# Note that the effective grain diameter is about 10 times the effective pore radius. How to derive this, is another matter. It can be one by comparing Poisseuille flow in a tube with a porous medium by using the hydraulic radius instead of pore radius for both.
# 
# A sand of a grain diameter of say 0.2 mm will have a conductivity of around 10 m/d and a capillary rise of about 20 cm. This should correspond with a pore radius of 0.02 mm
# 
# 
# 
