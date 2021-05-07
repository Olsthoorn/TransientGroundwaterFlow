#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Test set for mfpath

This file tests mfpath.particle_tracker.

The tests consists of setting of 6 3D models in which the flow is each time
in one of the axis directions with constand heads at the opposite model
boundary cells. In each axis direction the flow is the two opposite directions.
This gives 6 cases in total.

The computed travel times are verified againts the analytical solution.

Notice that this test does not invoke the formula that is implemented for
the situation in which the velocity with cells varies. This is tested in other
files with the names that start with `test_mpath`

Created on Sun Nov  6 16:21:07 2016

@author: TO
"""
import sys

myModules = '/Users/Theo/GRWMODELS/Python_projects/mfpy/modules/'

if not myModules in sys.path:
    sys.path.insert(0, myModules)  #prepending

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


def set_up_and_run_fdm(gridpar, k, hbound, axis=None):

    Lx, wx, Ly, wy, D, d = gridpar

    x = np.linspace(-Lx, Lx, int(2 * Lx / wx) + 1)
    y = np.linspace(-Ly, Ly, int(2 * Ly / wy) + 1)
    z = np.linspace(-D , D,  int(2 *  D /  d) + 1)
    gr = mfgrid.Grid(x, y, z)

    K = gr.const(k) # * np.random.rand(gr.Nod).reshape(gr.shape)
    FH = gr.const(0.)
    FQ = gr.const(0.)

    IBOUND = gr.const(1)

    if axis == 0:
        IBOUND[[0, -1], :, :] = -1
        FH[0, :, :] = hbound[0]
        FH[-1, :,:] = hbound[1]
    elif axis == 1:
        IBOUND[:,[0, -1], :] = -1
        FH[:,  0, :] = hbound[0]
        FH[:, -1, :] = hbound[1]
    elif axis == 2:
        IBOUND[:, :, [0, -1]] = -1
        FH[:, :,  0] = hbound[0]
        FH[:, :, -1] = hbound[1]
    else:
        print("axis must be 0, 1, or to, not {}".format(axis))
        raise ValueError()

    # Solve for the heads:
    Out = fdm.fdm3(gr, (K, K, K), FQ, FH, IBOUND)

    return Out, gr, IBOUND

def get_points(gr, Np, s0, flow_axis):


    rp = np.random.rand(Np) # start corodinates in other directions

    # starting points in normalized coordinates
    if flow_axis==0: # flow in y/v direction
        u = rp * gr.Nx
        v = gr.vp(s0) * np.ones(Np)
        w = rp * gr.Nz
    elif flow_axis==1: # flow in x/u direction
        u = gr.up(s0) * np.ones(Np)
        v = rp * gr.Ny
        w = rp * gr.Nz
    elif flow_axis==2: # flow in z/w direction
        u = rp * gr.Nx
        v = rp * gr.Ny
        foo = 0.
        w = gr.wp(foo, foo, s0) * np.ones(Np) # foo is a ummys
    else:
        print("flow_axis must be 0, 1 or 2, not {}".format(flow_axis))
        raise ValueError()

    x, y, z = gr.uvw2xyz(u, v, w)
    return x, y, z

def pos(s0, dh, L, k, peff, t):
    """returns the position along flow_axis startin at s0 for all times
    """
    return s0 - k * dh/(L * peff) * t


def simulate(case):
    """
    Test example:
        Constant velocity between opposite cell faces in x, y and z
        directions.
        Altnernatively the fixed heads are set at two opposite planes, one
        direction at a time. Once to let the flow be along the positive axis
        direction, once to let the flow be in the opposite direction.
        To make sure that the particle velocities are constant, we start
        them at the second cell face. The particles are automatically captured
        when the reach the last-but-one cell face at the opposite side of the
        grid.
        Hence, we have 6 cases that are captured by the hound array, which
        specifies the heads in all outer planes for each case, where None means
        that no head is prescribed.

        With the boundary heads and the correcponding IBOUND set, the heads
        and the flows are computed by fdm.fdm3.

        With thes flows, the particles are tracked in each of the cases.

        The results are collected and comapared with the hand-calculated
        travel time for each case.

        While the staring position of the particles in the researched direction
        is set as described above, the positions in the other directions are
        chosen randomly within that plane. All these particles should have the
        the same travel time.

        We make the grid a pure cube, so that both times and positions can eas-
        ily be compared betweeen the directions. The must all match exactly.

        @ TO161115
    """

    global t_hand, t_sim

    print("I'm Testing the code.")
    print("Setting up the test.")

    crit = 0.01
    Np = 25

        # Parameters to set up a grid for the model
    #          Lx    wx     Ly     wy    D     d
    gridpar= (1050., 100., 1050., 100., 1050., 100.)

    k = 10.
    peff = 0.35
    T = np.arange(0., 16000., 2000.)

    #  FH  @   N     S    W   E    T     B
    hbound= np.array([[ 9, 0],
                      [ 0, 9],
                      [ 0, 9],
                      [ 9, 0],
                      [ 0, 9],
                      [ 9, 0]], dtype=float)

    flow_axis = [1, 1, 0, 0, 2, 2]
        # run fdm model
    out, gr, IBOUND = set_up_and_run_fdm(gridpar, k, hbound[case], axis=flow_axis[case])

    Peff = gr.const(0.35)

    # The x,y and z of the particles are computed vorm u, v and w norm.coords.

    # starting at -900 will bring particles to +900 in 14000 d when dh = -9 m
    # sarting  at +900 will bring particles to -900 in 14000 d when dh = +9 m
    s0 = 900 * np.array([-1, 1, -1, 1, -1, 1], dtype=float)

    xyz = get_points(gr, Np, s0[case], flow_axis[case])

    # Track particles
    pcl = mfpath.particle_tracker(gr, out, Peff, T, xyz)
    #mfpath.visualize(gr, pcl, ugrid=False, phi=out.Phi[:,:,0])
    #mfpath.visualize(gr, pcl, ugrid=True)

    print('Finished')
    #

    # sa is the analytically computed position at all t
    # sn is the numerically computed position at all t
    if case == 0:
        L = np.abs(np.diff(gr.xm[[0,-1]]))
        sa = pos(s0[case], np.diff(hbound[case]), L, k, peff, T)
        sn = pcl.x
    elif case == 1:
        L = np.abs(np.diff(gr.xm[[0,-1]]))
        sa = pos(s0[case], np.diff(hbound[case]), L, k, peff, T)
        sn = pcl.x
    elif case == 2:
        L = np.abs(np.diff(gr.ym[[0,-1]]))
        sa = pos(s0[case], -np.diff(hbound[case]), L, k, peff, T)
        sn = pcl.y
    elif case == 3:
        L = np.abs(np.diff(gr.ym[[0,-1]]))
        sa = pos(s0[case], -np.diff(hbound[case]), L, k, peff, T)
        sn = pcl.y
    elif case == 4:
        L = np.abs(np.diff(gr.zm[[0,-1]]))
        sa = pos(s0[case], -np.diff(hbound[case]), L, k, peff, T)
        sn = pcl.z
    elif case == 5:
        L = np.abs(np.diff(gr.zm[[0,-1]]))
        sa = pos(s0[case], -np.diff(hbound[case]), L, k, peff, T)
        sn = pcl.z

    return sa, np.mean(sn, axis=0), crit, pcl, out


class Mfpath1dConstantVelocityTests(unittest.TestCase):


    def test_const_v_x_pos(self):
        """Compare const velocity in pos x-direction"""
        #pdb.set_trace()
        case = 0
        sa, sn, crit, pcl, out =simulate(case)
        ok = np.all(abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)
    def test_const_v_x_neg(self):
        """Compare const velocity in neg x-direction"""
        #pdb.set_trace()
        case = 1
        sa, sn, crit, pcl, out =simulate(case)
        ok = np.all(abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)
    def test_const_v_y_pos(self):
        """Compare const velocity in pos y-direction"""
        #pdb.set_trace()
        case = 2
        sa, sn, crit, pcl, out =simulate(case)
        ok = np.all(abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)
    def test_const_v_y_neg(self):
        """Compare const velocity in neg y-direction"""
        #pdb.set_trace()
        case = 3
        sa, sn, crit, pcl, out =simulate(case)
        ok = np.all(abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)
    def test_const_v_z_pos(self):
        """Compare const velocity in pos z-direction"""
        #pdb.set_trace()
        case = 4
        sa, sn, crit, pcl, out =simulate(case)
        ok = np.all(abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)
    def test_const_v_z_neg(self):
        """Compare const velocity in neg z-direction"""
        #pdb.set_trace()
        case = 5
        sa, sn, crit, pcl, out =simulate(case)
        ok = np.all(abs((sa - sn)/(sa + sn)) < crit)
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
