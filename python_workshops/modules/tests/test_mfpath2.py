#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Tests for mpath, axial flow

This file tests mpath with flows that axially diverges from a well or towards
a well. The well is fully penetrating.

There are 6 tests. In each one a fully penetrating well is placed in the
central axis of the model. This given three direction: along the z axis, the
y axis and the x axis. To let the flow be axially, the cells along the 4walls
of the model parallel to the place screen obrain prescribed head equal to 0.
The other two model faces, perpendicular to the screen are kept closed. Because
we run the test with outward and inward flow direction, we have 6 tests in
total.

The model is symmetric along all axis, that is the number of rows, columns
and layers are equal, and so are the cell sizes in each three directions.
Hence, both the entire model and the invidivual cells are cubes.

The rsults are compared againts the analytical solution.

Created on Sun Nov  6 16:21:07 2016

@author: Theo
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


def set_up_and_run_fdm(gridpar, k, Q, well_axis):

    Lx, wx, Ly, wy, D, d = gridpar

    x = np.linspace(-Lx, Lx, int(2 * Lx / wx) + 1)
    y = np.linspace(-Ly, Ly, int(2 * Ly / wy) + 1)
    z = np.linspace(-D , D,  int(2 *  D /  d) + 1)
    gr = mfgrid.Grid(x, y, z)

    K = gr.const(k) # * np.random.rand(gr.Nod).reshape(gr.shape)
    FH = gr.const(0.)
    FQ = gr.const(0.)

    # Cell indices of center of model: hard wired here
    x0, y0, z0 = 0., 0., 0.
    icx, icy, icz = gr.ixyz(x0, y0, z0)
     # Covner to int to prevent shape errors with FQ below
    icx = int(icx); icy=int(icy); icz=int(icz)

    if well_axis == 2: # i.e. z
        # screen in z direction, flow in xy plane
        IBOUND = gr.const(1)
        IBOUND[[0,-1], :, :] = -1
        IBOUND[:, [0,-1], :] = -1
        FQ[icy, icx, :] = Q * gr.dz / np.sum(gr.dz)
    elif well_axis == 0:  # i.e. y
        # screen in x direction, flow in zx plane
        IBOUND = gr.const(1)
        IBOUND[:, [0,-1], :] = -1
        IBOUND[:, :, [0,-1]] = -1
        FQ[:, icx, icz] = Q * gr.dy / np.sum(gr.dy)
    elif well_axis == 1: # i.e. x
        # screen in y direction, flow in yz plane
        IBOUND = gr.const(1)
        IBOUND[[0,-1], :, :] = -1
        IBOUND[:, :, [0,-1]] = -1
        FQ[icy, :, icz] = Q * gr.dx / np.sum(gr.dx)
    else:
        print("well_axis must be 0, 1, or 2, not {}".format(well_axis))

    # Solve for the heads:
    Out = fdm.fdm3(gr, (K, K, K), FQ, FH, IBOUND)

    return Out, gr, IBOUND

def radius_at_t(gr, Np, Q, r0, t, H, peff, R=1.):
    """Returns travel time between first and further radii

    $$ Q t = \pi \left(r^2 - r_0^2 \right) H n  R $$

    $$ r =  \sqrt { r0^2 +  \frac {Q t} {\pi  H  n R } } $$

    Parmeters:
    ----------
    gr : mfgrid.Grid object
    Np : the number of coordinate pairs to generate
    Q : flow into fully penetrating well
    r : futher distance from well (vector)
    r0 : location of starting particles (scalar)
    H : aquifer thickness (computed from gr)
    n : effective porosity (used peff in code)
    R : retardation

    @TO161115
    """

    r = np.sqrt( r0**2 + Q * t / (np.pi * H * peff * R))
    return r

def xyz_points(r, N, well_axis=None, x0=0., y0=0., z0=0.):
    """Returns points around afully penetrating well along zaxis

    The well is in the center of the model.
    Make sure the number of cells is uneven so that the center cell
    is exactly in the center of the model

    Parameters:
    -----------
    N  : number of particles to generate
    r  : radius at which to place the particles
    well_axis : axis along which the well is oriented, must be 0, 1 ,or 2
    x0 : well x-coordinate (default = 0.)
    y0 : well y-coordinate (default = 0.)
    z0 : well z-coordinate (default = 0.)

    @TO161115
    """
    if well_axis==2: # vertical, along z
        x = r * np.cos(np.arange(N, dtype=float) / N * 2. * np.pi)
        y = r * np.sin(np.arange(N, dtype=float) / N * 2. * np.pi)
        z = np.random.randn(N)
    elif well_axis==0: # along y
        x = r * np.sin(np.arange(N, dtype=float) / N * 2. * np.pi)
        y = np.random.randn(N)
        z = r * np.cos(np.arange(N, dtype=float) / N * 2. * np.pi)
    elif well_axis==1: # along x
        x = np.random.randn(N)
        y = r * np.sin(np.arange(N, dtype=float) / N * 2. * np.pi)
        z = r * np.cos(np.arange(N, dtype=float) / N * 2. * np.pi)
    else:
        print("well_axis must be 0, 1 or 2, not {}".format(well_axis))
        raise ValueError()
    return x, y, z

def r_analytic(r0, Q, H, peff, t):
    """Resturns analytically calculated particle distance from well.

    The flow is radial and starts at r0.
    Values are computed for all times t.
    """
    return np.sqrt(r0**2 + Q/(np.pi * peff * H) * t)


def simulate(case):
    """
    Test example:
        Tesing particle tracking with varable velocity but only in one
        direction. Like it is the case for a fully penetrating well in a
        confined aquifer.
        We take a cubic model with cubic cells and install a linear
        screen in its center like pencel, fully penetrating.
        The heads on the opposite sites are kept constant at zero.
        The flow should be axial and can be computed analytically.
        Constant velocity between opposite cell faces in x, y and z

        There are 3 directions to compare both for an infiltrating and
        an exfiltrating well.

        @ TO161115
    """

        # Parameters to set up a grid for the model
    #          Lx    wx     Ly     wy    D     d
    gridpar= (1050., 100., 1050., 100., 1050., 100.) # odd number of cells

    crit = 0.05
    Np = 25
    k = 10.
    peff = 0.35
    T = np.arange(0., 750., 30)

    # the six test cases:
    Q = 1.5e6 * np.array([1, -1, 1, -1, 1, -1], dtype=float)
    well_axis =          [2,  2, 0,  0, 1,  1]

    # run fdm model
    out, gr, IBOUND = set_up_and_run_fdm(gridpar, k, Q[case], well_axis[case])

    Peff = gr.const(0.35)

    # initial distance for each case
    # starting at 200 will bring the particles at 726 after 750 days if Q>0
    # starting at 726 will bring the particles at 200 after 750 days if Q<0
    r = [200, 726, 200, 726, 200, 726] # initial distances

    # The x,y and z of the particles are computed vorm u, v and w norm.coords.
    xyz = xyz_points(r[case], Np, well_axis[case])

    # Track particles
    pcl = mfpath.particle_tracker(gr, out, Peff, T, xyz)
    #mfpath.visualize(gr, pcl, ugrid=False, phi=out.Phi[:,:,0])
    #mfpath.visualize(gr, pcl, ugrid=True)

    if well_axis[case] == 2:  # i.e. z
        R_sim =  np.sqrt(pcl.x**2 + pcl.y**2)
        H = sum(gr.dz)
    elif well_axis[case] == 0: # i.e. y
        R_sim = np.sqrt(pcl.z**2 + pcl.x**2)
        H = sum(gr.dy)
    elif well_axis[case] == 1: # i.e. x
        R_sim = np.sqrt(pcl.y**2 + pcl.z**2)
        H = sum(gr.dx)


    Ra = r_analytic(r[case], Q[case], H, peff, T)

    return Ra, np.mean(R_sim, axis=0), crit, pcl, out


class MfpathAxialFlowTests(unittest.TestCase):
    """Tests axial flow from and to a fully penetrating well

    The well is oriented alternatively in all 3 grid directions.
    """


    def test_distance_outward_xy(self):
        """Compare distance traveld radially outward in xy plane"""
        #pdb.set_trace()
        case = 0
        Ra, Rn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Ra-Rn)/(Ra+Rn)) < crit)
        self.assertTrue(ok)
    def test_distance_inward_xy(self):
        """Compare distance traveled radially inward in xy plane"""
        #pdb.set_trace()
        case = 1
        Ra, Rn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Ra-Rn)/(Ra+Rn)) < crit)
        self.assertTrue(ok)
    def test_distance_outward_yz(self):
        """Compare distance travelled radially outward in yz plane"""
        #pdb.set_trace()
        case = 2
        Ra, Rn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Ra-Rn)/(Ra+Rn)) < crit)
        self.assertTrue(ok)
    def test_distance_inward_yz(self):
        """Compare distance travelled radially inward in yz plane"""
        #pdb.set_trace()
        case = 3
        Ra, Rn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Ra-Rn)/(Ra+Rn)) < crit)
        self.assertTrue(ok)
    def test_distance_outward_zx(self):
        """Compare distance travelled radiall outward in zx plane"""
        #pdb.set_trace()
        case = 4
        Ra, Rn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Ra-Rn)/(Ra+Rn)) < crit)
        self.assertTrue(ok)
    def test_distance_inward_zx(self):
        """Compare distance travelled radially inward in zx plane"""
        #pdb.set_trace()
        case = 5
        Ra, Rn, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Ra-Rn)/(Ra+Rn)) < crit)
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
