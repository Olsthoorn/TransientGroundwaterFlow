#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Tests for mpath, radial flow

This file tests mpath with flows that radially diverges from a well or towards
an extraction or injection point. The flow is spherical from or to the center
cell of the model.

There are 2 tests. In one the flow diverges from and in the secod it converges
to the cell in the center of the mode which injects or extracts.

All outer boundaries of the model have prescribed head equal to zero to
make the flow radial, at least near the "well".

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


def setup_and_run_fdm(gridpar, k, Q):

    Lx, wx, Ly, wy, D, d = gridpar

    x = np.linspace(-Lx, Lx, int(2 * Lx / wx) + 1)
    y = np.linspace(-Ly, Ly, int(2 * Ly / wy) + 1)
    z = np.linspace(-D , D,  int(2 *  D /  d) + 1)
    gr = mfgrid.Grid(x, y, z)

    K = gr.const(k) # * np.random.rand(gr.Nod).reshape(gr.shape)
    FH = gr.const(0.)
    FQ = gr.const(0.)

    IBOUND = gr.const(1)
    IBOUND[[0,-1], :, :] = -1
    IBOUND[:, [0,-1], :] = -1
    IBOUND[:, :, [0,-1]] = -1

    icx, icy, icz = gr.ixyz(0., 0., 0.)

    FQ[icy,icx,icz] = Q

    # Solve for the heads:
    Out = fdm.fdm3(gr, (K, K, K), FQ, FH, IBOUND)

    return Out, gr, IBOUND

def xyz_radial(r, x0=0., y0=0., z0=0.):
    """Returns points around afully penetrating well along zaxis

    The well is the center cell of the model or at least at
    coordinates x0, y0 z0, which happens to be the center of the test model.
    Make sure the number of cells is uneven so that the center cell
    is exactly in the center of the model

    Parameters:
    -----------
    N   : number of particles to generate
    r : radius at which to place the particles
    x0 : well x-coordinate (default = 0.)
    y0 : well y-coordinate (default = 0.)
    z0 : well z-coordinate (default = 0.)

    @TO161115
    """
    # polar coordinates are r, theta (from vertical donwward) and phi (from
    # x axis anti-clockwise)
    theta = np.pi / 180 * np.array([
                   30,  45,  60,  90, 120, 135, 150], dtype=float)
    phi = np.pi / 180 * np.array([
               0,  30,  45,  60,  90, 120,  135, 150,
             180, 210, 225, 240, 270, 300,  315, 330], dtype=float)

    x = r * (np.sin(theta[:, np.newaxis]) * np.cos(phi[np.newaxis, :])).ravel()
    y = r * (np.sin(theta[:, np.newaxis]) * np.sin(phi[np.newaxis, :])).ravel()
    z = r * (np.cos(theta[:, np.newaxis]) * np.ones((1, len(phi)))).ravel()

    x = np.round(np.hstack(([0., 0.], x)), 10)
    y = np.round(np.hstack(([0., 0.], y)), 10)
    z = np.round(np.hstack(([r,  -r], z)), 10)

    return (x,y,z)

def rad(r0, Q, t, peff):
    """Returns distance reached starting ar r0 by Q in time t"""
    r = (r0**3 + Q * t/ (4./3. * np.pi * peff)) ** (1./3.)
    return r

def simulate(case):
    """
    Radial flow by well injection into or extracting from the central cell
    of the model.
    The model is cubic, with cubic cells and the number of cells are teh same
    in each direction.
    All walls of the cubic model obtain prescribed head equal to zero.

    The finite difference model is run to get the flows across the cell faces.
    Together with the effecive porosity (and an implicit retardation of 1),
    the particles are tracked.

    The particles are initially on a sphere with given radius.
    Their track should be radial and there location expressed in
    terms of distance form the center of the model is easily verified
    by the analytically computed distance as a function of the times given.

    The two cases use the same flow but with opposite signs.
    The starting radius of the second case is equal to the analytically
    computed end radius of the first case and vice versa, to ease comparison
    of the analytical with the numerical solutions.

    @ TO161116
    """
    # Parameters to set up a grid for the model
    #          Lx    wx     Ly     wy    D     d
    gridpar= (1050., 100., 1050., 100., 1050., 100.)

    crit = 0.05
    k    = 10.
    peff = 0.35

    T = np.linspace(0., 720., 21)

    Q = [0.5e6, -0.5e6] # two cases

        # run fdm model
    out, gr, IBOUND = setup_and_run_fdm(gridpar, k, Q[case])

    #### Particle tracking

    r = [217., # with Q = -0.5e6 rechage in 720 d from r1
         634.]  # with Q =  0.5e6 reached in 720 d from r0

    # The x,y and z ditributd regularly over a sphere of given radius
    xyz = xyz_radial(r[case])

    Peff = gr.const(0.35)

    pcl = mfpath.particle_tracker(gr, out, Peff, T, xyz)
    #mfpath.visualize(gr, pcl, ugrid=False, phi=out.Phi[:,:,0])
    #mfpath.visualize(gr, pcl, ugrid=True)

    R_sim = np.sqrt(pcl.x**2 + pcl.y**2 + pcl.z**2)
    R_analytic = rad(r[case], Q[case], T, peff)

    return np.mean(R_sim, axis=0), R_analytic, crit, pcl, out


class MfpathRadialFlowTests(unittest.TestCase):
    """Tests radial flow from and to the cell in center of grid"""

    def test_distance_radial_outward_xy(self):
        """Compare distance traveld radially outward in xy plane"""
        case = 0
        Rs, Ra, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Rs-Ra)/(Rs+Ra)) < crit)
        self.assertTrue(ok)
    def test_distance_radial_inward_xy(self):
        """Compare distance traveled radially inward in xy plane"""
        case = 1
        Rs, Ra, crit, pcl, out = simulate(case)
        ok = np.all(np.abs((Rs-Ra)/(Rs+Ra)) < crit)
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
