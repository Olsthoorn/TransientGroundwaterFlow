#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Test set for mfpath, variavel velocity along each of the axes.

This file tests mfpath.particle_tracker.

The tests consists of setting of 6 3D models in which the flow in each test
is parallel to one of the three axes. But the flow varies along the axis
because we add recharge. The particles are placed at the inner cell faces
of the boundary cells opposite to the flow direction. We fixe both sides
of the model heads oppoosite to te flow direction, so that the particles will
stagnage towards the water divide in the center of the model. The tests are
run with forward and backward flow by specifying positive and negative
recharge.

The computed travel times are verified againts the analytical solution.

The model has the same extent, number of cells and cell size in each
direction, to that the model itself and its cells are cubes.

To easily verify the results, the recharge will be in every cell of the model.
This keeps the flow perfectly in line with the axis direction.

Created on Sun Nov  6 16:21:07 2016

@author: TO
"""
import sys

myModules = '/Users/Theo/GRWMODELS/Python_projects/mfpy/modules/'

if not myModules in sys.path:
    sys.path.insert(0, myModules)

import matplotlib.pylab as plt
import numpy as np
import mfgrid
import mfpath
import fdm
from mfetc import display, prarr
import unittest
import pdb

def AND(*args):
    L = args[0]
    for arg in args:
        L = np.logical_and(L, arg)
    return L

NOT = np.logical_not

def setup_and_run_fdm(gridpar, k, rch, axis=1):

    Lx, wx, Ly, wy, D, d = gridpar

    x = np.linspace(-Lx, Lx, int(2 * Lx / wx) + 1)
    y = np.linspace(-Ly, Ly, int(2 * Ly / wy) + 1)
    z = np.linspace(-D , D,  int(2 *  D /  d) + 1)
    gr = mfgrid.Grid(x, y, z)

    K  = gr.const( k )
    FH = gr.const( 0.)
    FQ = gr.Volume * rch

    IBOUND = gr.const(1)

    if axis == 0:
        IBOUND[[0,-1], :, :] = -1
    elif axis == 1:
        IBOUND[:, [0,-1], :] = -1
    elif axis == 2:
        IBOUND[:, :, [0,-1]] = -1
    else:
        print("axis must be 0, 1, or 2, not {}".format(axis))

    # Solve for the heads:
    Out = fdm.fdm3(gr, (K, K, K), FQ, FH, IBOUND)

    return Out, gr, IBOUND

def analytic_travel_pos(rch, T, x0, peff):
    """Travel distance towards or from water divide.

    x0 is distance to the water divide. In our case, this corresponds with
    grid coordinates zero, i.e. the model center.

    This works for all directions because the model is symmetric in all three
    axis directions.
    """
    x = x0 * np.exp(rch/peff * T)
    return x

def get_particles(gr, Np, s0, axis=None):
    """Returns placed particles (particle coordinate in tupple Xp, Yp, Zp)

    The particls are place at the center of the second cell-plane
    of the boundary when, flow is towards the center of the model and on
    the analytical solution for that flow as starting points whenthe flow
    is reversed.
    """
    if axis is None or not (axis in [0, 1, 2]):
        print("axis must be 0, 1 or 3, not {}".format(axis))
        raise ValueError()
    pass

    # at the positive side of the water divide
    aR = s0 * np.ones(Np)  # constant
    bR = s0 * np.random.rand(Np) # random
    cR = s0 * np.random.rand(Np) # random
    # opposite the water divide
    aL = -aR[:]
    bL = -bR[:]
    cL = -cR[:]
    # join
    a = np.hstack((aL, aR))
    b = np.hstack((bL, bR))
    c = np.hstack((cL, cR))

    if axis==0:
        x, y, z = c, a, b   # here the y is constant
    elif axis==1:
        x, y, z = a, b, c   # here the x is constant
    elif axis==2:
        x, y, z = b, c, a   # here the z is constant

    return x, y, z

def pos(s0, rch, peff, t):
    """Returns the postion of particle starting at s0

    Notice the velocity must fulfill: v = n x / peff
    So x is relative to the water divide.

    Parameters:
    -----------
    s0 : [L] starting position along the axis of the current flow.
    rch : [1/T] specific recharge that is n/D with n recharge and D aquifer thickness
    peff: [-] effective porosity
    t : time

    Returns
    s(t) : postion for all given times

    """
    return s0 * np.exp(rch/peff * t)

def simulate(case):
    """
    Simulates particle tracking with variable velocity.

    The particles move parelle to each of the axes in turn.
    The variable velocity is obtained by means of recharge.

    The model has cobic shape and so has all its cells. It is symmetric
    in all three axis directions.

    The recharge is divided uniformly over all cells of the model

    The flow along one axis is created by setting the head fixed at two
    of the opposite model faces in turn.

    Flow inward and outward is created by using positive and negative
    specific recharge.

    The displacement results are compared with the analytical solution.

    @ TO161115
    """

    global t_hand, t_sim

    print("I'm Testing the code.")
    print("Setting up the test.")

    Np = 25
    crit = 0.05

    # Parameters to set up a grid for the model
    #          Lx    wx     Ly     wy    D     d
    gridpar= (1050., 100., 1050., 100., 1050., 100.)  # odd number of cells

    k = 10.
    peff = 0.35

    T = np.arange(0., 750., 30.)

    rch = 0.0005 # [1/d] specific rechare i.e recharge/aqufier thickness
    spec_rech = np.array([0, -1, 0, -1, 0, -1]) * rch  # spec. recharge for all 6 cases
    axis      =          [0,  0, 1,  1,  2, 2] # for each case

    # run fdm model
    out, gr, IBOUND = setup_and_run_fdm(gridpar, k, spec_rech[case], axis=axis[case])

    #### particle tracking
    Peff = gr.const(0.35)

    s1 = 200. # with this rch particles starting at 200 m end at 723 m after 720d
    s2 = 720. # with this rch particles starting at 723 m end at 200 m after 720 d
    s0   = [ s1, s2, s1, s2, s1, s2] # for each case

    xyz = get_particles(gr, Np, s0[case], axis=axis[case])

    pcl = mfpath.particle_tracker(gr, out, Peff, T, xyz)
    #mfpath.visualize(gr, pcl, ugrid=False, phi=out.Phi[:,:,0])
    #mfpath.visualize(gr, pcl, ugrid=True)

    print('Finished')
    #
    # expected distances, sa is the analytically computed particle position
    sa = analytic_travel_pos(spec_rech[case], T, s0[case], peff)

    # sn is the simulated particle position along the axis of the flow
    if axis[case] == 0:
        sn = pcl.y
    elif axis[case] == 1:
        sn = pcl.x
    elif axis[case] == 2:
        sn = pcl.z
    else:
        print("axis must be 0, 1, or 2, not{}".format(axis[case]))

    return sa, np.mean(np.abs(sn), axis=0), crit, pcl, out


class Mfpath1dVariableVelocityTests(unittest.TestCase):

    def test_variable_v_x_pos(self):
        """Compare variable v outward in x-direction"""
        case = 0
        sa, sn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((sa - sn)/(sa + sn)) < crit)
        #pdb.set_trace()
        self.assertTrue(ok)
    def test_variable_v_x_neg(self):
        """Compare variable v inward in x-direction"""
        case = 1
        sa, sn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)
    def test_variable_v_y_pos(self):
        """Compare variable v outward in y-direction"""
        case = 2
        sa, sn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((sa - sn)/(sa + sn)) < crit)
        #pdb.set_trace()
        self.assertTrue(ok)
    def test_variable_v_y_neg(self):
        """Compare variable v inward neg y-direction"""
        case = 3
        sa, sn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((sa - sn)/(sa + sn)) < crit)
        #pdb.set_trace()
        self.assertTrue(ok)
    def test_variable_v_z_pos(self):
        """Compare variable v outward in z-direction"""
        case  = 4
        sa, sn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((sa - sn)/(sa + sn)) < crit)
        #pdb.set_trace()
        self.assertTrue(ok)
    def test_variable_v_z_neg(self):
        """Compare variable v inward in z-direction"""
        case = 5
        sa, sn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((sa - sn)/(sa + sn)) < crit)
        #pdb.set_trace()
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
