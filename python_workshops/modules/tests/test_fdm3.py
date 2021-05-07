# -*- coding: utf-8 -*-
"""
This script tets fdm3, the steady state 3D Finite Difference Model
implemented as a function in python (module fdm)

The teste here are just two examples. The model is implicitly and intensively
tested in the tests related to mfpath, the 3D particle tracker. For each test
of mfpath, the fdm3 model is run in a different configuration. mfpath uses
the outcomes of fmd3 and is verified against anlatical solutions for linear
constant and non-constant flow, for axial flow in with a well alternatively
in each of the three grid directions and for spherical flow. As mfpath
successes with all its tests, this also holds true for fdm3.

Created on Fri Sep 30 04:26:57 2016

@author: TO 161117

"""
import sys

myModules = '/Users/Theo/GRWMODELS/Python_projects/mfpy/modules'

if not myModules in sys.path:
    sys.path.insert(0, myModules)

import unittest
import numpy as np
import scipy.special
import matplotlib.pylab as plt
import mfgrid
import fdm
import pdb

crit = 0.01

def vanMarzure(s0, kD,c, x):
    """Analytical solution of Van Mazure: for 1-d semi-inf. semi conf. aquifer.

    The head above the confining unit on top of the aquifer is mainained at 0.
    The head at x=0 is fixed to s0. S0 can be considered as a `drawdown`.
    The flow is steady.

    Parameters:
    -----------
    s0  : [L] head maintained at x=0
    kD  : [L2/T] transmissivity of the aquifer
    c   : [1/T] vertical hydraulic resistance of confining unit
    x   : [L] distance to locaton with fixed head
    Returns:
    s : [L] the head relative to that above the confing unit as function of x.
    """
    lam = np.sqrt(kD * c)
    s = s0 * np.exp(-x / lam)
    return s


def de_glee(Q, kD, c, r0, r):
    """Returns analytical solution of steady well in semi-confined aquifer.

    Solution after De Glee (1930), makes use of Bessel functions K0 and K1.
    """
    K0 = lambda x: scipy.special.kn(0, x) # Bessel function second kind, order 0
    K1 = lambda x: scipy.special.kn(1, x) # Bessel function second kind, order 1

    lam= np.sqrt(kD * c)
    dd = Q / (2 * np.pi * kD) * K0( r / lam) / (r0/ lam * K1(r0/ lam))
    return dd


# Examples that take the function of tests
def example_mazure():
    """1D flow in semi-confined aquifer example
    Mazure was Dutch professor in the 1930s, concerned with leakage from
    polders that were pumped dry. His situation is a cross section perpendicular
    to the dike of a regional aquifer covered by a semi-confining layer with
    a maintained head in it. The head in the regional aquifer at the dike was
    given as well. The head obeys the following analytical expression
    phi(x) - hp = (phi(0)-hp) * exp(-x/lam), lam = sqrt(kDc)
    To compute we use 2 model layers and define the values such that we obtain
    the Mazure result.
    """
    x = np.hstack((0.001, np.linspace(0., 2000., 101))) # column coordinates
    y = np.array([-0.5, 0.5]) # m, model is 1 m thick
    d = 10. # m, thickness of confining top layer
    D = 50. # m, thickness of regional aquifer
    z = np.array([0, -d, -d-D]) # tops and bottoms of layers
    gr = mfgrid.Grid(x, y, z, axial=False)
    c = 250 # d, vertical resistance of semi-confining layer
    k1 = d/c # m/d conductivity of the top layer
    k2 = 10. # m/d conductivity of the regional aquifer
    kD = k2 * D # m2/d, transmissivity of regional aquifer
    K = gr.const([k1/2., k2]) # k1 = 0.5 d/c because conductance from layer center
    FQ = gr.const(0) # prescribed flows
    s0 = 2.0 # head in aquifer at x=0
    IH = gr.const(0); IH[:,0,-1] = s0 # prescribed heads
    IBOUND = gr.const(1); IBOUND[:,:,0] = -1; IBOUND[:,0,-1]=-1
    out = fdm.fdm3(gr, K, FQ, IH, IBOUND) # compute heads, run model

    numerical = out.Phi[0,:,-1]
    analytic  = vanMarzure(s0, kD,c, gr.xm)

#==============================================================================
#     plt.figure()
#     plt.setp(plt.gca(), 'xlabel','x [m]', 'ylabel', 'head [m]', 'title', 'Mazure 1D flow')
#     plt.plot(gr.xm, numerical, 'ro-', label='fdm3') # numeric solution
#     plt.plot(gr.xm, analytic  ,'bx-', label='analytic') # analytic solution
#     plt.legend()
#
#==============================================================================
    return numerical, analytic, out



def example_de_glee():
    """Axial symmetric example, well in semi-confined aquifer (De Glee case)
    De Glee was a Dutch engineer/groundwater hydrologist and later the
    first director of the water company of the province of Groningen.
    His PhD (1930) solved the axial symmetric steady state flow to a well
    in a semi confined aquifer using the Besselfunctions of the second kind,
    known as K0 and K1.
    The example computes the heads in the regional aquifer below a semi confining
    layer with a fixed head above. It uses two model layers a confining one in
    which the heads are fixed and a semi-confined aquifer with a prescribed
    extraction at r=r0. If r0>>0, both K0 and K1 Bessel functions are needed.
    The grid is signaled to use inteprete the grid as axially symmetric.
    """
    Q  = -1200.0 # m3/d, well extraction
    r0 = 100.  # m, well radius
    R  = 2500. # m, outer radius of model
    d = 10. # m, thickness of confining top layer
    D = 50. # m, thickness of regional aquifer
    c = 250 # d, vertical resistance of confining top layer
    k1 = d/c # m/d conductivity of confining top layer
    k2 = 10.  # m/d conductivity of regional aquifer
    kD = k2 * D # m2/d, transmissivity of regional aquifer
    r  = np.hstack((r0+0.001, np.logspace(np.log10(r0), np.log10(R), 41))) # distance to well center
    y = None # dummy, ignored because problem is axially symmetric
    z = np.array([0, -d, -d-D]) # m, elevation of tops and bottoms of model layers
    gr = mfgrid.Grid(r, y, z, axial=True) # generate grid
    FQ = gr.const(0.)
    FQ[0,0,-1] = Q # m3/d fixed flows
    IH = gr.const(0.) # m, initial heads
    IBOUND = gr.const(1)
    IBOUND[:,:,0] = -1 # modflow like boundary array
    K = gr.const([k1/2., k2]) # full 3D array of conductivities
    out = fdm.fdm3(gr, K, FQ, IH, IBOUND) # run model

    numerical  = out.Phi[0,:,-1]
    analytic   = de_glee(Q, kD, c, r0, gr.xm)

#==============================================================================
#     plt.figure()
#     plt.setp(plt.gca(), 'xlabel', 'r [m]', 'ylabel', 'head [m]',\
#              'title', 'De Glee, well extraction, axially symmetric', 'xscale', 'log', 'xlim', [1.0, R])
#     plt.plot(gr.xm, numerical, 'ro-', label='fdm3')
#     plt.plot(gr.xm, analytic , 'bx-',label='analytic')
#     plt.legend()
#
#==============================================================================
    return numerical,analytic, out

class Fdm3Tests(unittest.TestCase):

    def setUp(self):
        pass

    def test_mazure(self):
        """Tests fmd3 in linear flow mode. """
        #pdb.set_trace()
        num, anal, out = example_mazure()
        # integral over num and anal data should be almost equal
        ok1 = (np.sum(num) - np.sum(anal))/(np.sum(num) + np.sum(anal)) < crit
        ok2 = np.round(np.sum(out.Q), 10) == 0. # water balance
        self.assertTrue(ok1)
        self.assertTrue(ok2)

    def test_deGlee(self):
        """Tests fdmr in axial flow mode."""
        #pdb.set_trace()
        num, anal, out = example_de_glee()
        # integral over num and anal data should be almost equal
        ok1 = (np.sum(num) - np.sum(anal))/(np.sum(num) + np.sum(anal)) < crit
        ok2 = np.round(np.sum(out.Q), 10) == 0. # water balance
        self.assertTrue(ok1)  # heads
        self.assertTrue(ok2)  # water balancee

if __name__ == "__main__":
    unittest.main()

